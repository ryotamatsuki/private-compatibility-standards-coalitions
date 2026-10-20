"""R16 nonquadratic differentiated Bertrand microfoundation, full adoption audit.

U_e(q)=1'q-q'M0 q/2-eps*sum(q_i^4)/4 is strictly concave.
Fulfilled buyer expectations g=v*C*q yield inverse price
p=1-(M0-vC)q-eps*q_i^3; the *consumer-derived*
CS=U_e(q)-q.grad U_e(q)=q'M0q/2+3eps*sum(q_i^4)/4.

Each product-market Bertrand FOC uses the entire fulfilled-demand
Jacobian. Every one of the 8 SU, 64 SW, 1 IS investment profiles is
re-solved and all unilateral standard-support deviations evaluated.
Small epsilon numerical witness complements, but is not a substitute
for, the structural C^3 openness theorem.
"""
from itertools import combinations, product
from functools import lru_cache
import numpy as np
from scipy.optimize import root

GAMMA,V,C,D,F,EPS=.92,.066,.016,.002,.025,.0001
M0=(1-GAMMA)*np.eye(3)+GAMMA*np.ones((3,3))

@lru_cache(None)
def market(used,costs):
    comp=np.array([[int(used[i]==used[j] and used.count(used[i])>=2)
                    for j in range(3)] for i in range(3)])
    M=M0-V*comp
    costs=np.array(costs,dtype=float)
    def foc(q):
        p=1-M@q-EPS*q**3
        inv=np.linalg.inv(M+np.diag(3*EPS*q*q))
        return p-costs-q/np.diag(inv)
    initial=np.linalg.solve(M+np.diag(np.diag(M)),np.ones(3)-costs)
    solution=root(foc,initial,tol=1e-12)
    q=solution.x
    assert np.max(np.abs(foc(q)))<2e-11 and np.min(q)>0,(used,costs,solution)
    p=1-M@q-EPS*q**3
    assert np.min(p-costs)>0
    pi=(p-costs)*q
    cs=.5*q@M0@q+.75*EPS*np.sum(q**4)
    assert cs>0
    return tuple(pi),float(cs)

def stage(base):
    acts=[]
    for i in range(3):
        other=sorted(set(base)-{base[i]})
        acts.append([frozenset((base[i],)+extra)
                     for n in range(len(other)+1)
                     for extra in combinations(other,n)])
    profiles=list(product(*acts))
    net={};consumer={}
    for prof in profiles:
        pay=np.zeros(3)
        cs=[]
        for destination in base:
            used=tuple(destination if destination in prof[i]
                       else base[i] for i in range(3))
            costs=tuple(0. if destination==base[i] else
                        D if destination in prof[i] else C for i in range(3))
            pi,csval=market(used,costs)
            pay+=np.array(pi)
            cs.append(csval)
        net[prof]=pay-F*np.array([len(s)-1 for s in prof])
        consumer[prof]=tuple(cs)
    eq=[]
    for prof in profiles:
        margins=[]
        for i in range(3):
            for action in acts[i]:
                if action==prof[i]:continue
                dev=prof[:i]+(action,)+prof[i+1:]
                margins.append(net[prof][i]-net[dev][i])
        if all(z>=-1e-9 for z in margins):
            eq.append((prof,min(margins) if margins else float('inf')))
    return net,consumer,eq

su,sw,is_=(stage(regime) for regime in [(0,0,1),(0,1,2),(0,0,0)])
su0=(frozenset({0}),frozenset({0}),frozenset({1}))
su1=(frozenset({0}),frozenset({0}),frozenset({0,1}))
sw0=(frozenset({0}),frozenset({1}),frozenset({2}))
is0=(frozenset({0}),)*3
assert len(su[2])==len(sw[2])==len(is_[2])==1
assert su[2][0][0]==su1 and sw[2][0][0]==sw0
assert su[2][0][1]>.004 and sw[2][0][1]>.01
W=lambda stage,profile: stage[0][profile][0]+stage[1][profile][0]
pre=W(su,su0)-W(is_,is0)
post=W(su,su1)-W(is_,is0)
assert pre>.0027 and post<-.0009,(pre,post)
assert market.cache_info().currsize==19
print("EPSILON:",EPS)
print("Buyer-consistent differentiated nonlinear price demand: PASS")
print("Original government SU-IS preference prior:",pre,"after:",post)
print("SU and SW unique pure firm adoption, strict margin:",su[2][0][1],sw[2][0][1])
print("All 8 SU, 64 SW, 1 IS profiles and 19 nonlinear market equilibria: PASS")
print("NONLINEAR BERTRAND NUMERICAL EXEMPLAR: PASS, not interval proof")
