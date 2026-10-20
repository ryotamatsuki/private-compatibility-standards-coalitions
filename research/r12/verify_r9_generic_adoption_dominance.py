"""Independently check R12 G1 adoption-gain bound in the certified R9 case.

Re-solve each Cournot market and all 8 SU/64 SW full firm action profiles.
No use of previous game's cached certificate or conjectured Nash equilibrium.
All payoffs, comparisons and dominance margins are exact rationals.
"""
from functools import lru_cache
from itertools import combinations,product
import sympy as s

v=s.Rational(6,25)
c=s.Rational(1,10)
d=s.Rational(1,20)
F=s.Rational(9,100)

@lru_cache(None)
def market(used,costs):
    compatible=s.zeros(3)
    for code in set(used):
        group=[i for i in range(3) if used[i]==code]
        if len(group)>=2:
            for i in group:
                for j in group:
                    compatible[i,j]=1
    M=s.ones(3,3)-v*compatible
    J=M+s.diag(*[M[i,i] for i in range(3)])
    q=J.inv()*(s.ones(3,1)-s.Matrix(costs))
    assert all(z>0 for z in q),(used,costs,q)
    p=s.ones(3,1)-M*q
    return tuple(s.factor((p[i]-costs[i])*q[i]) for i in range(3))

def solve(base):
    actions=[]
    for i in range(3):
        other=sorted(set(base)-{base[i]})
        actions.append([frozenset((base[i],)+extra)
                        for n in range(len(other)+1)
                        for extra in combinations(other,n)])
    profiles=list(product(*actions))
    profits={}
    for prof in profiles:
        pay=[s.Integer(0)]*3
        for dest in base:
            used=tuple(dest if dest in prof[i] else base[i] for i in range(3))
            costs=tuple(s.Integer(0) if base[i]==dest else
                        (d if dest in prof[i] else c) for i in range(3))
            block=market(used,costs)
            pay=[pay[i]+block[i] for i in range(3)]
        profits[prof]=tuple(pay)
    nash=[]
    for prof in profiles:
        margins=[]
        for i in range(3):
            for action in actions[i]:
                if action==prof[i]:
                    continue
                alternative=prof[:i]+(action,)+prof[i+1:]
                margins.append(profits[prof][i]-F*(len(prof[i])-1)
                               -(profits[alternative][i]-F*(len(action)-1)))
        if all(g>=0 for g in margins):
            nash.append((prof,min(margins)))
    return profiles,profits,nash

su,su_pi,su_eq=solve((0,0,1))
sw,sw_pi,sw_eq=solve((0,1,2))
assert len(su)==8 and len(sw)==64
assert len(su_eq)==1 and len(sw_eq)==1
assert su_eq[0][0]==(frozenset({0}),frozenset({0}),frozenset({0,1}))
assert sw_eq[0][0]==(frozenset({0}),frozenset({1}),frozenset({2}))
assert su_eq[0][1]>0 and sw_eq[0][1]>0

g_h=[];g_o=[]
for p in su:
    for i in range(3):
        if len(p[i])==1:
            alt=p[:i]+(frozenset({0,1}),)+p[i+1:]
            benefit=su_pi[alt][i]-su_pi[p][i]
            (g_o if i==2 else g_h).append((p,benefit))
sw_g=[]
for p in sw:
    for i in range(3):
        for j in set((0,1,2))-p[i]:
            alt=p[:i]+(p[i]|{j},)+p[i+1:]
            sw_g.append(sw_pi[alt][i]-sw_pi[p][i])
g_o0=[gain for prof,gain in g_o if all(len(t)==1 for t in prof)]
assert len(g_o0)==1
max_h=max(g for _,g in g_h)
max_sw=max(sw_g)
assert max(0,max_h,max_sw)<F<g_o0[0]
assert min(g for _,g in g_o)>=g_o0[0] # Extra dominance at witness.
print("R9 SU profiles=8; SW profiles=64; all unilateral deviations checked")
print("G1 exact max_member_gain:",max_h,"~",s.N(max_h,10))
print("G1 exact max_SW_gain:",max_sw,"~",s.N(max_sw,10))
print("G1 exact outsider_gain_if_members_not_adopt:",g_o0[0],"~",s.N(g_o0[0],10))
print("G1 exact F:",F)
print("Unique SU outsider-only and SW no-adoption equilibria: PASS")
print("R12 GENERIC STRICT ADOPTION DOMINANCE: PASS in original R9")
