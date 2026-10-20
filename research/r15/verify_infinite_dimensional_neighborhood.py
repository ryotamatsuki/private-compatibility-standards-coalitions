"""R15 nonlinear consumer-demand witness; research-only reproducibility QA.

D_e(Q)=1-Q+e Q^2/[4(1+Q^2)], an optimizing-buyer inverse quantile.
For every adoption profile and destination, solve the firm's true
Cournot FOCs with fulfilled network expectations, using the ORIGINAL
group rule and cost levels; consumer surplus comes from the same D_e.
Recompute all weak Nash profiles, not only the expected equilibrium.
A separate analytical argument establishes uniqueness in a small C2
function-space neighborhood; this numerical script is NOT itself a
computer-assisted interval proof of every nonzero perturbation.
"""
import itertools
from functools import lru_cache
import numpy as np
import scipy.optimize as opt
import sympy as s

v,c,d,F=.24,.10,.05,.09
EPS=.01

def h(Q):
    return Q*Q/(4*(1+Q*Q))

def hp(Q):
    return Q/(2*(1+Q*Q)**2)

def cs(Q):
    return Q*Q/2+EPS*((Q-np.arctan(Q))/4-Q*h(Q))

def groups(used):
    return np.array([[float(used[i]==used[j] and used.count(used[i])>=2)
                      for j in range(3)] for i in range(3)])
@lru_cache(None)
def market(used,cost):
    G=groups(used)
    costs=np.array(cost)
    def foc(q):
        Q=float(np.sum(q))
        p=1-Q+EPS*h(Q)+v*(G@q)
        own=-1+EPS*hp(Q)+v*np.diag(G)
        return p-costs+q*own
    sol=opt.root(foc,[.3,.3,.3],tol=1e-12)
    q=sol.x
    assert np.max(np.abs(foc(q)))<1e-10 and np.min(q)>0
    Q=q.sum()
    p=1-Q+EPS*h(Q)+v*(G@q)
    return tuple((p-costs)*q),float(cs(Q)),tuple(q)

def stage(base):
    actions=[]
    for i in range(3):
        others=sorted(set(base)-{base[i]})
        actions.append([frozenset((base[i],)+t)
                        for n in range(len(others)+1)
                        for t in itertools.combinations(others,n)])
    profiles=list(itertools.product(*actions))
    payoffs={}
    consumers={}
    for prof in profiles:
        profits=np.zeros(3)
        sv=[]
        for k,dstd in enumerate(base):
            used=tuple(dstd if dstd in prof[i] else base[i] for i in range(3))
            costs=tuple(0 if base[i]==dstd else
                        (d if dstd in prof[i] else c) for i in range(3))
            pi,csval,_=market(used,costs)
            profits+=np.array(pi)
            sv.append(csval)
        payoffs[prof]=tuple(profits-F*np.array([len(x)-1 for x in prof]))
        consumers[prof]=tuple(sv)
    nash=[]
    for prof in profiles:
        improvements=[]
        for i in range(3):
            for act in actions[i]:
                if act==prof[i]:continue
                dev=prof[:i]+(act,)+prof[i+1:]
                improvements.append(payoffs[prof][i]-payoffs[dev][i])
        if all(z>=-1e-9 for z in improvements):
            nash.append((prof,min(improvements)))
    return payoffs,consumers,nash

def proof_of_stability():
    # At epsilon=0, canonical firm Cournot FOCs have symmetric
    # Jacobian -J and J is SPD for EVERY relevant compatibility group.
    # Use exact Sylvester principal minors, with v fixed at 6/25.
    vr=s.Rational(6,25)
    for pattern in itertools.product(range(3),repeat=3):
        G=s.zeros(3)
        for i in range(3):
            for j in range(3):
                G[i,j]=int(pattern[i]==pattern[j] and pattern.count(pattern[i])>=2)
        M=s.ones(3)-vr*G
        J=M+s.diag(*[M[i,i] for i in range(3)])
        assert all(J[:k,:k].det()>0 for k in range(1,4))
    # In the perturbed FOC Jacobian, each entry deviates from
    # the baseline by at most |epsilon|*(2|h'|+2|h''|).
    # The chosen h has global |h'|,|h''| <=1.
    print("ALL 27 COMPATIBILITY-MATRIX COURNOT JACOBIANS SPD: EXACT PASS")

proof_of_stability()
su=stage((0,0,1))
sw=stage((0,1,2))
is_=stage((0,0,0))
su0=(frozenset({0}),frozenset({0}),frozenset({1}))
su1=(frozenset({0}),frozenset({0}),frozenset({0,1}))
sw0=(frozenset({0}),frozenset({1}),frozenset({2}))
is0=(frozenset({0}),)*3
assert len(su[2])==len(sw[2])==1
assert su[2][0][0]==su1 and sw[2][0][0]==sw0
assert su[2][0][1]>.02 and sw[2][0][1]>.02
before=su[0][su0][0]+su[1][su0][0]-(is_[0][is0][0]+is_[1][is0][0])
after=su[0][su1][0]+su[1][su1][0]-(is_[0][is0][0]+is_[1][is0][0])
assert before>.008 and after<-.007,(before,after)
print("EPS:",EPS)
print("Nonlinear original-R9-compliant SU government gaps:",before,after)
print("SU and SW unique pure equilibria + strict unilateral margins:",su[2],sw[2])
print("COMPLETE 8 SU, 64 SW, 1 IS PROFILES RE-EQUILIBRATED: PASS")
print("R15 NONLINEAR DEMAND EXEMPLAR: PASS")
