"""R18: exact independent rational witness/game and economic response-envelope audit.
Witness checks are not a general proof; Bertrand global price deviations remain an R16 dependency.
"""
import itertools, json
import sympy as s
z=s.symbols("z",real=True)
one=s.ones(3,1)

def Cmatrix(groups):
    return s.Matrix(3,3,lambda i,j:int(groups[i]==groups[j] and groups.count(groups[i])>=2))

def market(groups,cost,v,mode,gamma=None):
    C=Cmatrix(groups)
    M=s.ones(3,3)-v*C if mode=="cournot" else (1-gamma)*s.eye(3)+gamma*s.ones(3,3)-v*C
    A=M.inv() if mode=="bertrand" else None
    own=[M[i,i] if mode=="cournot" else 1/A[i,i] for i in range(3)]
    q=(M+s.diag(*own)).inv()*(one-s.Matrix(cost))
    p=one-M*q
    pi=tuple(s.factor((p[i]-cost[i])*q[i]) for i in range(3))
    cs=s.factor(sum(q)**2/2) if mode=="cournot" else s.factor((q.T*((1-gamma)*s.eye(3)+gamma*s.ones(3,3))*q)[0]/2)
    if all(not x.free_symbols for x in list(q)+list(p)+list(cost)):
        assert all(x>0 for x in q) and all(p[i]>cost[i] for i in range(3))
    return pi,cs

def stage(mode,v,c,d,F,gamma=None):
    cache={}
    def solve(groups,cost):
        key=(tuple(groups),tuple(cost))
        if key not in cache: cache[key]=market(groups,cost,v,mode,gamma)
        return cache[key]
    stages={}
    for name,standards in [("SU",(0,0,2)),("SW",(0,1,2)),("IS",(0,0,0))]:
        opts=[]
        for i in range(3):
            foreign=sorted(set(standards)-{standards[i]})
            opts.append(tuple(tuple(a for j,a in enumerate(foreign) if mask>>j&1) for mask in range(2**len(foreign))))
        payoff={}
        for actions in itertools.product(*opts):
            firm=[s.S(0)]*3; cs=[None]*3
            for k,standard in enumerate(standards):
                groups=[];costs=[]
                for i in range(3):
                    if standards[i]==standard: groups.append(standard);costs.append(s.S(0))
                    elif standard in actions[i]: groups.append(standard);costs.append(d)
                    else: groups.append(standards[i]);costs.append(c)
                pi,cs[k]=solve(groups,costs)
                for i in range(3):firm[i]+=pi[i]
            p=tuple(s.factor(firm[i]-F*len(actions[i])) for i in range(3))
            w=tuple(s.factor(cs[i]+p[i]) for i in range(3))
            payoff[actions]=(p,w)
        ne=[]
        for actions,(p,w) in payoff.items():
            if all(p[i]>=payoff[actions[:i]+(alt,)+actions[i+1:]][0][i]
                   for i in range(3) for alt in opts[i] if alt!=actions[i]):
                ne.append(actions)
        stages[name]=(payoff,ne)
    zero=((),(),());outside=((),(),(0,))
    su=stages["SU"][0];sw=stages["SW"][0];isim=stages["IS"][0]
    gross=s.factor(su[outside][0][2]-su[zero][0][2]+F)
    member=[]
    for a,(p,_) in su.items():
        for i in (0,1):
            if not a[i]:
                alt=a[:i]+((2,),)+a[i+1:]
                member.append(s.factor(su[alt][0][i]-p[i]+F))
    sw_single=[]
    for a,(p,_) in sw.items():
        for i in range(3):
            for st in (set([0,1,2])-{i}-set(a[i])):
                alt=a[:i]+(tuple(sorted(a[i]+(st,))),)+a[i+1:]
                sw_single.append(s.factor(sw[alt][0][i]-p[i]+F))
    assert max([s.S(0)]+member+sw_single)<F<gross
    assert stages["SU"][1]==[outside] and stages["SW"][1]==[zero]
    pre=s.factor(su[zero][1][0]-isim[zero][1][0])
    post=s.factor(su[outside][1][0]-isim[zero][1][0])
    assert pre>0>post
    return {"mode":mode,"profiles":{"SU":len(su),"SW":len(sw),"IS":len(isim)},
            "NE":{key:str(v[1]) for key,v in stages.items()},"distinct_markets":len(cache),
            "outsider_gross":str(gross),"max_member_reverse":str(max(member)),
            "max_SW_increment":str(max(sw_single)),"F":str(F),
            "pre":str(pre),"post":str(post),"pre_decimal":float(pre),"post_decimal":float(post)}

def boundary(mode,v,c,d,gamma=None):
    pB,csB=market([0,0,2],[0,0,z],v,mode,gamma)
    pC,csC=market([0,0,0],[0,0,z],v,mode,gamma)
    pE,_=market([0,0,2],[z,z,0],v,mode,gamma)
    mB=s.factor(csB+pB[0]+pB[1])
    mC=s.factor(csC+pC[0]+pC[1])
    fB=s.factor(pE[0]);fC=pC[0].subs(z,0)
    b=s.factor(s.diff(mB,z))
    r=s.factor(s.diff(mC,z))
    e=s.factor(-s.diff(fB,z))
    assert all(s.diff(y,z,3)==0 for y in (mB,mC,fB))
    vals=lambda t,x:(t.subs(z,0),t.subs(z,x))
    bL=min(vals(b,c));rU=max(vals(r,d))
    eL=min(vals(e,c));eU=max(vals(e,c))
    H=s.factor(mC.subs(z,0)-mB.subs(z,0))
    J=s.factor(fC-fB.subs(z,0))
    beforeLB=s.factor(c*(bL-eU)-H-J)
    afterUB=s.factor(d*rU-J-c*eL)
    before=s.factor(mB.subs(z,c)+fB.subs(z,c)-mC.subs(z,0)-fC)
    after=s.factor(mC.subs(z,d)+fB.subs(z,c)-mC.subs(z,0)-fC)
    assert before>=beforeLB>0>afterUB>=after
    assert s.simplify(before-(s.integrate(b,(z,0,c))-H-J-s.integrate(e,(z,0,c))))==0
    assert s.simplify(after-(s.integrate(r,(z,0,d))-J-s.integrate(e,(z,0,c))))==0
    return {k:str(x) for k,x in dict(H=H,J=J,bL=bL,eL=eL,eU=eU,rU=rU,
                         pre_lower_bound=beforeLB,post_upper_bound=afterUB,
                         exact_pre=before,exact_post=after).items()}

def main():
    cases=[("cournot",s.Rational(6,25),s.Rational(1,10),s.Rational(1,20),s.Rational(9,100),None),
           ("bertrand",s.Rational(33,500),s.Rational(2,125),s.Rational(1,500),s.Rational(1,40),s.Rational(23,25))]
    result=[]
    for mode,v,c,d,F,gamma in cases:
        result.append({"stage":stage(mode,v,c,d,F,gamma),
                       "primitive_bounds":boundary(mode,v,c,d,gamma)})
    # Negative counterexample: no network externality, initial SU disadvantage.
    v=s.S(0); c=s.Rational(1,10)
    P=1/(16*(1-v));KI=s.Rational(9,1)/(32*(1-v)**2)
    A=(1-v)*(1+c)**2/(4*(2-3*v)**2)
    C=(1-v)*(1-2*c)**2/(4*(2-3*v)**2)
    KM=(3-c-3*v+3*c*v)**2/(8*(2-3*v)**2)
    no_network=s.factor(KM+2*A+C-KI-3*P)
    assert no_network == -s.Rational(47,3200)
    print(json.dumps({"cases":result,"negative_v0_gap":str(no_network),
                      "price_game_global_deviations":"NOT independently rerun; refer to R16",
                      "nonlinear_Bertrand_global_uniqueness":"UNPROVED"},indent=2))
if __name__=="__main__": main()
