"""Exact global one-firm Bertrand deviation audit with buyer quantity corners.

This addresses the subtle weakness of checking only interior price FOCs.
Consumer (fulfilled-expectations) quantity Q is the unique nonnegative
solution of LCP(M, p-1), where M=M0-vC is symmetric positive definite.
Thus when firms deviate in price, any rival product may exit, and each
active-set region is a rational interval of unilateral prices.

Enumerate every active set containing the deviating firm and optimize
its concave quadratic profit on that interval; also allow zero sales.
If no such deviation strictly improves on the interior Nash vector,
its interior FOC is a GLOBAL price best reply, not merely local.
"""
import sympy as s
from itertools import combinations
from functools import lru_cache

Q=s.Rational
gamma,v,c,d=Q(23,25),Q(33,500),Q(2,125),Q(1,500)
M0=(1-gamma)*s.eye(3)+gamma*s.ones(3,3)
ONE=s.ones(3,1)
TOTAL_CHECKS=0

def linear_conditions_feasible(cond,x,cost):
    # Candidate x must be >= cost and satisfy all affine inequalities.
    return all(s.factor(expr.subs(x,candidate))>=0 for expr in cond
               for candidate in [])  # Unused: explicit candidate below.

@lru_cache(None)
def verify_market(used,costs):
    global TOTAL_CHECKS
    C=s.zeros(3,3)
    for i in range(3):
        for j in range(3):
            C[i,j]=int(used[i]==used[j] and used.count(used[i])>=2)
    M=M0-v*C
    assert all(M[:k,:k].det()>0 for k in (1,2,3))
    r=s.Matrix(costs)
    A=M.inv()
    diag=s.diag(*[A[i,i] for i in range(3)])
    p=(A+diag).inv()*(A*ONE+diag*r)
    qt=A*(ONE-p)
    assert all(z>0 for z in qt)
    NashProf=[s.factor((p[i]-r[i])*qt[i]) for i in range(3)]
    for i in range(3):
        x=s.symbols("x")
        for others in [(),*(tuple(j for j in cset)
                           for n in (1,2)
                           for cset in combinations([j for j in range(3) if j!=i],n))]:
            active=tuple(sorted((i,)+others))
            inactive=tuple(j for j in range(3) if j not in active)
            Ma=M.extract(active,active)
            assert all(Ma[:k,:k].det()>0 for k in range(1,len(active)+1))
            px=[x if j==i else p[j] for j in active]
            qa=Ma.inv()*(s.ones(len(active),1)-s.Matrix(px))
            q=s.zeros(3,1)
            for j,idx in enumerate(active):
                q[idx]=s.factor(qa[j])
            feasible=[x-r[i]]
            feasible += [q[j] for j in active] # q_j >=0
            feasible += [s.factor(p[j]-1+(M*q)[j]) for j in inactive]  # inactive gradient <=0
            q_i=s.factor(q[i])
            margin=s.factor((x-r[i])*q_i)
            deriv=s.factor(s.diff(margin,x))
            assert s.degree(s.together(margin).as_numer_denom()[0],x)<=2
            # A piecewise quadratic's constrained maximum is at
            # a stationary point or a feasible boundary of its interval.
            candidates={r[i],p[i]}
            stationary=s.solve(deriv,x)
            for z in stationary:
                if z.is_real is True: candidates.add(s.factor(z))
            for expr in feasible:
                f=s.factor(expr)
                if f!=0 and f.has(x):
                    zeros=s.solve(f,x)
                    for z in zeros:
                        if z.is_real is True:candidates.add(s.factor(z))
            for cand in candidates:
                if not all(s.factor(e.subs(x,cand))>=0 for e in feasible):
                    continue
                TOTAL_CHECKS+=1
                gap=s.factor(NashProf[i]-margin.subs(x,cand))
                assert gap>=0,("PROFITABLE DEVIATION",used,costs,i,active,cand,gap,p)
        assert NashProf[i]>0
        # Every firm has an interior stationary best reply; exactly
        # NashProf[i] is attained at the equilibrium price.
        assert s.factor(qt[i]-A[i,i]*(p[i]-r[i]))==0
    return True

# Each possible market composition and marginal-cost tuple found in the
# R9 three-country region under SU, SW and IS for any adopted profile.
def gather_markets():
    out=set()
    for partition in [(0,0,1),(0,1,2),(0,0,0)]:
        actions=[]
        for i in range(3):
            others=sorted(set(partition)-{partition[i]})
            actions.append([frozenset((partition[i],)+t)
                            for n in range(len(others)+1)
                            for t in combinations(others,n)])
        from itertools import product
        for prof in product(*actions):
            for dest in partition:
                used=tuple(dest if dest in prof[i] else partition[i] for i in range(3))
                costs=tuple(Q(0) if dest==partition[i] else
                            (d if dest in prof[i] else c) for i in range(3))
                out.add((used,costs))
    return sorted(out,key=str)

markets=gather_markets()
assert len(markets)==19,len(markets)
for k,(used,costs) in enumerate(markets,1):
    assert verify_market(used,costs)
print("R16 VERIFIED GLOBAL PRICE BEST REPLIES:",len(markets),"distinct market games")
print("Feasible rational candidate prices evaluated:",TOTAL_CHECKS)
print("All rival-exit active sets, all stationary points and boundaries PASS")
print("Consumer LCP demand uniqueness: M positive definite for all games")
print("R16 GLOBAL UNILATERAL BERTRAND DEVIATION AUDIT: PASS")
