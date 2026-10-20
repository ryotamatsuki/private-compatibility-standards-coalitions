"""R14: exact segmented-country-size and investment joint interval.

All equilibria for SU (8 adoption profiles), SW (64 profiles) and IS
are recomputed using original R9 Cournot demand and technology.
Only the per-capita demand-unmodified outsider market MASS t varies.
Firm fee F is per added standard; market payoffs scale by destination mass.
No original manuscript/source or R9 numerical result is altered.
"""
import sympy as s
from itertools import combinations,product
from functools import lru_cache
t=s.symbols("t",real=True)
v,c,d,F=s.Rational(6,25),s.Rational(1,10),s.Rational(1,20),s.Rational(9,100)

@lru_cache(None)
def market(used,costs):
    M=s.ones(3,3)
    for i in range(3):
        for j in range(3):
            if used[i]==used[j] and used.count(used[i])>=2:
                M[i,j]-=v
    J=M+s.diag(*[M[i,i] for i in range(3)])
    q=J.inv()*(s.ones(3,1)-s.Matrix(costs))
    assert all(z>0 for z in q), (used,costs,q)
    p=s.ones(3,1)-M*q
    return tuple(s.factor((p[i]-costs[i])*q[i]) for i in range(3)),s.factor(sum(q)**2/2)

def solve(base):
    actions=[]
    for i in range(3):
        standards=sorted(set(base)-{base[i]})
        actions.append([
            frozenset((base[i],)+add)
            for k in range(len(standards)+1)
            for add in combinations(standards,k)])
    profiles=list(product(*actions))
    profit,cs={},{ }
    for profile in profiles:
        pay=[s.Integer(0)]*3
        welfare=[]
        for dest,std in enumerate(base):
            used=tuple(std if std in profile[i] else base[i] for i in range(3))
            cost=tuple(s.Integer(0) if std==base[i] else
                       (d if std in profile[i] else c) for i in range(3))
            pi,consumer=market(used,cost)
            mass=t if dest==2 else s.Integer(1)
            pay=[pay[i]+mass*pi[i] for i in range(3)]
            welfare.append(mass*consumer)
        profit[profile]=tuple(s.factor(x) for x in pay)
        cs[profile]=tuple(welfare)
    return actions,profiles,profit,cs

su,sw,is_=solve((0,0,1)),solve((0,1,2)),solve((0,0,0))
assert len(su[1])==8 and len(sw[1])==64
su0=(frozenset({0}),frozenset({0}),frozenset({1}))
su1=(frozenset({0}),frozenset({0}),frozenset({0,1}))
sw0=(frozenset({0}),frozenset({1}),frozenset({2}))
is0=(frozenset({0}),)*3
assert su0 in su[1] and su1 in su[1] and sw0 in sw[1]

# Affine inequalities, always normalized to expr(t)>0.
ineqs=[]
def add(expr,label):
    expr=s.factor(expr)
    assert s.diff(expr,t,2)==0,(label,expr)
    ineqs.append((label,expr))
for profile in su[1]:
    for i in (0,1):
        if len(profile[i])==1:
            alt=profile[:i]+(frozenset({0,1}),)+profile[i+1:]
            add(F-(su[2][alt][i]-su[2][profile][i]),"SU member non-adoption")
for profile in sw[1]:
    for i in range(3):
        for std in set((0,1,2))-profile[i]:
            alt=profile[:i]+(profile[i]|{std},)+profile[i+1:]
            add(F-(sw[2][alt][i]-sw[2][profile][i]),"SW no-adoption")
outsider_gain=s.factor(su[2][su1][2]-su[2][su0][2])
add(outsider_gain-F,"SU outsider adoption")
assert s.diff(outsider_gain,t)==0

pre=s.factor(su[3][su0][0]+su[2][su0][0]-
             is_[3][is0][0]-is_[2][is0][0])
post=s.factor(su[3][su1][0]+su[2][su1][0]-
              is_[3][is0][0]-is_[2][is0][0])
E=s.factor(pre.subs(t,0))
R=s.factor(post.subs(t,0))
D=s.factor(-s.diff(pre,t))
assert s.factor(pre-(E-D*t))==0
assert s.factor(post-(R-D*t))==0
assert s.diff(post,t)==-D and E>R>0 and D>0
assert E==s.Rational(4779709,295731200),(E,R,D)
assert R==s.Rational(141,184832),(E,R,D)
assert D==s.Rational(39,4864),(E,R,D)
add(pre,"SU initially preferred")
add(-post,"IS after outsider adapts")
add(t,"positive outsider market size")

lo,hi=None,None
binding_lo,binding_hi=None,None
for label,expr in ineqs:
    intercept=s.factor(expr.subs(t,0))
    slope=s.factor(s.diff(expr,t))
    if slope>0:
        x=s.factor(-intercept/slope)
        if lo is None or x>lo:
            lo,binding_lo=x,label
    elif slope<0:
        x=s.factor(-intercept/slope)
        if hi is None or x<hi:
            hi,binding_hi=x,label
    else: assert intercept>0,(label,expr)
assert lo is not None and hi is not None and lo<hi
assert lo==s.Rational(47,494),(lo,hi,binding_lo,binding_hi)
assert hi==s.Rational(933888,707347),(lo,hi,binding_lo,binding_hi)
mid=s.factor((lo+hi)/2)
assert all(s.factor(expr.subs(t,mid))>0 for _,expr in ineqs)
assert all(s.factor(expr.subs(t,s.Integer(1)))>0 for _,expr in ineqs)

# Every affine inequality with positive values at BOTH endpoints must
# be positive throughout the whole open interval.
for label,expr in ineqs:
    assert s.factor(expr.subs(t,lo))>=0,(label,"lo",expr)
    assert s.factor(expr.subs(t,hi))>=0,(label,"hi",expr)

# Directly enumerate weak Nash equilibria at representative interior
# t, including every alternative action (rather than only strict ones).
def nash(game,T):
    actions,profiles,profits,_=game
    outcomes=[]
    for prof in profiles:
        diffs=[]
        for i in range(3):
            for act in actions[i]:
                if act==prof[i]:continue
                dev=prof[:i]+(act,)+prof[i+1:]
                this=s.factor((profits[prof][i]-F*(len(prof[i])-1)).subs(t,T))
                that=s.factor((profits[dev][i]-F*(len(act)-1)).subs(t,T))
                diffs.append(this-that)
        if all(z>=0 for z in diffs):outcomes.append(prof)
    return outcomes
assert nash(su,mid)==[su1]
assert nash(sw,mid)==[sw0]

print("SU 8 / SW 64 profiles, full affine inequalities:",len(ineqs))
print("Government region exact R/D < t < E/D:",s.factor(R/D),s.factor(E/D))
print("Joint exact country size interval: ",lo,"< t <",hi)
print("Binding lower",binding_lo,"upper",binding_hi)
print("At original t=1: government pre",pre.subs(t,1),
      "government post",post.subs(t,1))
print("Continuous original-R9-result-preserving joint t window EXACT PASS")
