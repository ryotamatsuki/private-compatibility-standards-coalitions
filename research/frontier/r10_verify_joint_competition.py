"""Exploratory rational audit; NOT part of the JICT submitted manuscript.

Run: python research/frontier/r10_verify_joint_competition.py
Requires sympy.  Every firm adoption profile and each unilateral deviation
are checked, not just the proposed equilibrium.  All comparisons exact.
"""
from __future__ import annotations
from functools import lru_cache
from itertools import combinations, product
import sympy as S

Q = S.Rational
GAMMA, C, V, F, D = Q(23,25), Q(2,125), Q(33,500), Q(1,40), Q(1,500)

@lru_cache(None)
def market(mode, used, costs):
    network = S.zeros(3)
    for kind in set(used):
        group = [i for i, x in enumerate(used) if x == kind]
        if len(group) >= 2:
            for i in group:
                for j in group:
                    network[i,j] = 1
    M = (1-GAMMA)*S.eye(3)+GAMMA*S.ones(3)-V*network
    # Sylvester's criterion for this real symmetric demand matrix.
    assert all(M[:k,:k].det()>0 for k in (1,2,3))
    r = S.Matrix(costs)
    if mode == "Cournot":
        q = (M+S.diag(*[M[i,i] for i in range(3)])).inv()*(S.ones(3,1)-r)
        p = S.ones(3,1)-M*q
    else:
        inv = M.inv()
        own = S.diag(*[inv[i,i] for i in range(3)])
        p = (inv+own).inv()*(inv*S.ones(3,1)+own*r)
        q = inv*(S.ones(3,1)-p)
    assert all(z>0 for z in q), (mode,used,costs,q)
    profits = tuple(S.cancel((p[i]-r[i])*q[i]) for i in range(3))
    cs = S.cancel((q.T*M*q)[0]/2)
    return profits, cs

def game(mode, partition):
    base=list(partition)
    standards=sorted(set(base))
    acts=[]
    for i in range(3):
        other=[x for x in standards if x!=base[i]]
        acts.append([frozenset((base[i],)+xs)
                     for n in range(len(other)+1)
                     for xs in combinations(other,n)])
    profiles=list(product(*acts))
    ledger={}
    for prof in profiles:
        payoff=[Q(0)]*3
        cs=[]
        for dest_std in base:
            used=tuple(dest_std if dest_std in prof[i] else base[i] for i in range(3))
            costs=tuple(Q(0) if dest_std==base[i] else
                        (D if dest_std in prof[i] else C) for i in range(3))
            profits, surplus=market(mode,used,costs)
            payoff=[payoff[i]+profits[i] for i in range(3)]
            cs.append(surplus)
        ledger[prof]=(tuple(payoff[i]-F*(len(prof[i])-1) for i in range(3)),tuple(cs))
    nash=[]
    for prof in profiles:
        margins=[]
        for i in range(3):
            for act in acts[i]:
                if act == prof[i]:
                    continue
                deviation=prof[:i]+(act,)+prof[i+1:]
                margins.append(ledger[prof][0][i]-ledger[deviation][0][i])
        # Include weak equilibria: reject every non-target profile with any
        # strictly profitable deviation; the selected target is strict.
        if all(z>=0 for z in margins):
            nash.append((prof,min(margins) if margins else None))
    return ledger,nash

def welfare_for_home(g,profile):
    payoffs,consumer_surplus=g[profile]
    return payoffs[0]+consumer_surplus[0]

def check_mode(mode):
    su,eq_su=game(mode,(0,0,1))
    sw,eq_sw=game(mode,(0,1,2))
    is_,eq_is=game(mode,(0,0,0))
    none=(frozenset({0}),frozenset({0}),frozenset({1}))
    outsider_only=(frozenset({0}),frozenset({0}),frozenset({0,1}))
    sw_none=(frozenset({0}),frozenset({1}),frozenset({2}))
    all_same=(frozenset({0}),)*3
    assert len(eq_su)==len(eq_sw)==len(eq_is)==1
    assert eq_su[0][0]==outsider_only and eq_sw[0][0]==sw_none
    assert eq_su[0][1]>0 and eq_sw[0][1]>0
    before=welfare_for_home(su,none)-welfare_for_home(is_,all_same)
    after=welfare_for_home(su,outsider_only)-welfare_for_home(is_,all_same)
    assert before>0 and after<0
    print(mode, "pre_SUmIS", before, "=", S.N(before,12))
    print(mode, "post_SUmIS", after, "=", S.N(after,12))
    print(mode, "strict_SU_margin", S.N(eq_su[0][1],12),
          "strict_SW_margin", S.N(eq_sw[0][1],12))
    print(mode, "profiles_checked",len(su),len(sw),len(is_))

def symbolic_local_incidence():
    # Fully compatible member market, cost vector (0,0,d), national
    # market component W(d) = CS(d) + 2 * home-firm operating profit(d).
    m,b,d=S.symbols("m b d",positive=True)
    M=(m-b)*S.eye(3)+b*S.ones(3)
    cost=S.Matrix([0,0,d])
    expected_C=(2*b*b+b*m-2*m*m)/(4*(2*m-b)*(b+m)**2)
    expected_B=(b-2*m)*(b+m)**2/(4*m*m*(2*b+m)*(3*b+2*m))
    for mode,target in [("Cournot",expected_C),("Bertrand",expected_B)]:
        if mode=="Cournot":
            q=(M+S.diag(m,m,m)).inv()*(S.ones(3,1)-cost)
            price=S.ones(3,1)-M*q
        else:
            inv=M.inv()
            own=S.diag(*[inv[i,i] for i in range(3)])
            price=(inv+own).inv()*(inv*S.ones(3,1)+own*cost)
            q=inv*(S.ones(3,1)-price)
        welfare=(q.T*M*q)[0]/2+2*(price[0]*q[0])
        derivative=S.factor(S.diff(welfare,d).subs(d,0))
        assert S.factor(derivative-target)==0,(mode,derivative,target)
        print(mode,"exact_incidence_dW_dd_at_0",S.factor(derivative))
    assert S.factor(expected_C.subs({m:Q(467,500),b:Q(427,500)}))>0
    assert S.factor(expected_B.subs({m:Q(467,500),b:Q(427,500)}))<0

if __name__=="__main__":
    assert D/C==Q(1,8)  # Incomplete adaptation: 12.5% residual cost.
    symbolic_local_incidence()
    check_mode("Cournot")
    check_mode("Bertrand")
    print("EXPLORATORY JOINT EXACT WITNESS: PASS; NOT a novelty certificate")
