"""R16 exact R13-consistent Bertrand witness with endogenous standard investment.

Demand derives from a consumer optimization problem with a quadratic
*baseline* valuation, fulfilled expectations g=v*C*q, and products
priced by oligopolists. R13 welfare: CS=1/2*q.T*M0*q.
Unlike former R10, NEVER use 1/2*q.T*(M0-v*C)*q as R9 welfare.

All relevant product subgames are solved exactly over Q.  All 8 SU,
64 SW, and 1 IS adoption profiles, and every unilateral deviation are
re-solved.  The inequality certificate implies nonempty parameter-open
local persistence *within this specified differentiated Bertrand game*.
The check proves interior Nash FOCs and global *investment stage* Nash,
but does not on its own certify global off-interior Bertrand deviations.
"""
from functools import lru_cache
from itertools import combinations, product
import sympy as S

Q=S.Rational
GAMMA=Q(23,25)
V=Q(33,500)
COST=Q(2,125)
RESIDUAL=Q(1,500)
FEE=Q(1,40)
M0=(1-GAMMA)*S.eye(3)+GAMMA*S.ones(3,3)
ONE=S.ones(3,1)

@lru_cache(None)
def market(used, costs):
    comp=S.zeros(3,3)
    for i in range(3):
        for j in range(3):
            if used[i]==used[j] and used.count(used[i])>=2:
                comp[i,j]=1
    M=M0-V*comp
    assert all(M[:k,:k].det()>0 for k in (1,2,3)),(used,M)
    inv=M.inv()
    own=S.diag(*[inv[i,i] for i in range(3)])
    r=S.Matrix(costs)
    price=(inv+own).inv()*(inv*ONE+own*r)
    q=inv*(ONE-price)
    assert all(x>0 for x in q),(used,costs,q)
    assert all(price[i]>r[i] for i in range(3))
    profit=tuple(S.cancel((price[i]-r[i])*q[i]) for i in range(3))
    cs=S.cancel((q.T*M0*q)[0]/2)
    # Consumer's baseline U0(q) has symmetric PD M0, while network
    # benefit g=V*comp*q is *external* to each atomistic consumer.
    for i in range(3):
        assert S.factor(price[i] - (1-(M0*q)[i]+(V*comp*q)[i]))==0
        assert S.factor(q[i]-(inv*(ONE-price))[i])==0
        assert S.factor(q[i]-inv[i,i]*(price[i]-r[i]))==0
    return profit,cs,price,q

def stage(partition):
    bases=list(partition)
    actions=[]
    for i in range(3):
        other=sorted(set(bases)-{bases[i]})
        actions.append([frozenset((bases[i],)+t)
                        for n in range(len(other)+1)
                        for t in combinations(other,n)])
    profs=list(product(*actions))
    operating={}
    consumer={}
    for prof in profs:
        totals=[S.Integer(0)]*3
        surplus=[]
        for std in bases:
            used=tuple(std if std in prof[i] else bases[i] for i in range(3))
            cost=tuple(Q(0) if bases[i]==std else
                       (RESIDUAL if std in prof[i] else COST)
                       for i in range(3))
            pi,cs,_,_=market(used,cost)
            totals=[totals[i]+pi[i] for i in range(3)]
            surplus.append(cs)
        operating[prof]=tuple(totals)
        consumer[prof]=tuple(surplus)
    net={p:tuple(operating[p][i]-FEE*(len(p[i])-1) for i in range(3))
         for p in profs}
    Nash=[]
    for p in profs:
        margins=[]
        for i in range(3):
            for a in actions[i]:
                if a==p[i]: continue
                dev=p[:i]+(a,)+p[i+1:]
                margins.append(net[p][i]-net[dev][i])
        if all(z>=0 for z in margins):
            Nash.append((p,min(margins) if margins else S.oo))
    return actions,profs,operating,consumer,net,Nash

su=stage((0,0,1))
sw=stage((0,1,2))
is_=stage((0,0,0))
N=(frozenset({0}),frozenset({0}),frozenset({1}))
A=(frozenset({0}),frozenset({0}),frozenset({0,1}))
SWN=(frozenset({0}),frozenset({1}),frozenset({2}))
ISN=(frozenset({0}),)*3
assert (len(su[1]),len(sw[1]),len(is_[1]))==(8,64,1)
assert len(su[5])==len(sw[5])==len(is_[5])==1
assert su[5][0][0]==A and sw[5][0][0]==SWN and is_[5][0][0]==ISN
assert su[5][0][1]>0 and sw[5][0][1]>0
def home_welfare(game,profile):
    # Only one member owns one home firm, but symmetric destinations
    # imply two domestic-owned member-market profit blocks.
    own=game[2][profile][0]
    cs_member=game[3][profile][0]
    return cs_member+own

# For any partition there are three destination markets. Member firms
# have one representative local consumer welfare + ONE firm's global
# operating profits, net of its fixed standard-support fees.
def W(game,prof):
    return game[3][prof][0]+game[4][prof][0]

before=S.factor(W(su,N)-W(is_,ISN))
after=S.factor(W(su,A)-W(is_,ISN))
assert before>0 and after<0, (before,after)

gH=[]
for p in su[1]:
    for i in (0,1):
        if len(p[i])==1:
            t=p[:i]+(frozenset({0,1}),)+p[i+1:]
            gH.append(su[2][t][i]-su[2][p][i])
gSW=[]
for p in sw[1]:
    for i in range(3):
        for other in (set((0,1,2))-p[i]):
            t=p[:i]+(p[i]|{other},)+p[i+1:]
            gSW.append(sw[2][t][i]-sw[2][p][i])
gO=S.factor(su[2][A][2]-su[2][N][2])
mH=max(gH);mSW=max(gSW)
assert gO>FEE
# G1 is a *stronger* sufficient test than the original unique Nash
# evidence. If it fails, note the correct restricted result; do not
# misreport the global investment-dominance assumption as passing.
strong_G1=(max(mH,mSW,Q(0))<FEE<gO)
print("PRIVATE INVESTMENT profiles SU/SW/IS:",len(su[1]),len(sw[1]),len(is_[1]))
print("G1 global max member",S.N(mH,13),"max SW",S.N(mSW,13),
      "outsider gain",S.N(gO,13),"fee",FEE,"PASS:",strong_G1)
print("Bertrand SU uniqueness margin",S.N(su[5][0][1],13))
print("Bertrand SW uniqueness margin",S.N(sw[5][0][1],13))
print("Bertrand R13 SU-IS before exact:",before,"float:",S.N(before,14))
print("Bertrand R13 SU-IS after exact:",after,"float:",S.N(after,14))
print("Unique interior Bertrand solutions for distinct operating subgames:",market.cache_info())
print("R13-CONSISTENT BERTRAND ADOPTION + PUBLIC REVERSAL: EXACT PASS")
