"""R15 independent R10-versus-R13 consumer-welfare consistency audit.

Old R10 used CS=1/2 q'(M0-vC)q, which corresponds to
internalized-network quadratic gross utility. R9/R13 buyers take the
network as given and have baseline gross utility 1'q-1/2 q'M0q,
so CS=1/2 q'M0q even when prices reflect vCq.
The latter is the welfare concept used in this audit.
All comparisons and demand matrices are exact rationals.
"""
import sympy as s
Q=s.Rational
gamma,c,v,d=Q(23,25),Q(2,125),Q(33,500),Q(1,500)
M0=(1-gamma)*s.eye(3)+gamma*s.ones(3)
ones=s.ones(3,1)

def market(used,cost,mode):
    C=s.zeros(3)
    for i in range(3):
        for j in range(3):
            if used[i]==used[j] and used.count(used[i])>=2:
                C[i,j]=1
    M=M0-v*C
    assert all(M[:i,:i].det()>0 for i in (1,2,3))
    costs=s.Matrix(cost)
    if mode=="Cournot":
        qt=(M+s.diag(*[M[i,i] for i in range(3)])).inv()*(ones-costs)
        pt=ones-M*qt
    else:
        iv=M.inv()
        own=s.diag(*[iv[i,i] for i in range(3)])
        pt=(iv+own).inv()*(iv*ones+own*costs)
        qt=iv*(ones-pt)
    assert all(x>0 for x in qt)
    prof=tuple(s.cancel((pt[i]-costs[i])*qt[i]) for i in range(3))
    cs_external=s.cancel((qt.T*M0*qt)[0]/2)
    cs_old=s.cancel((qt.T*M*qt)[0]/2)
    return prof,cs_external,cs_old

for mode in ("Cournot","Bertrand"):
    isv=market((0,0,0),(0,0,0),mode)
    pre=market((0,0,1),(0,0,c),mode)
    post=market((0,0,0),(0,0,d),mode)
    outsider=market((0,0,1),(c,c,0),mode)
    def gap(state,csidx):
        return s.factor(state[csidx]+2*state[0][0]+outsider[0][0]
                        -isv[csidx]-3*isv[0][0])
    oldpre,oldpost=gap(pre,2),gap(post,2)
    newpre,newpost=gap(pre,1),gap(post,1)
    assert oldpre>0 and oldpost<0,(mode,oldpre,oldpost)
    if mode=="Cournot":
        assert newpre<0 and newpost<0
    else:
        assert newpre>0 and newpost<0
    print(mode,"R10_old_quadratic_network_surplus",s.N(oldpre,12),
          s.N(oldpost,12))
    print(mode,"R13_fulfilled_expectations_surplus",s.N(newpre,12),
          s.N(newpost,12))
print("R15 R10 CORRECTION EXACT: old common-conduct witness INVALID for R9/R13 welfare")
