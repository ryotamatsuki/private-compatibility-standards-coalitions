"""R12 model-independent incidence identity, including *original* R9 welfare.

Unlike earlier R11, this check DOES NOT impose CS=U-p.q or p=grad(U).
That would fail to nest the R9 demand/consumer surplus convention.
No journal model, theorem statement, or frozen R9 source is modified.
"""
import sympy as sp

for n_home in (2,3,4):
    n=n_home+1
    q=sp.symbols(f"q0:{n}",real=True)
    speed=sp.symbols(f"z0:{n}",real=True)
    a=sp.symbols("a",real=True)
    S=sp.Function("S")(*q,a)
    p=[sp.Function(f"p{i}")(*q,a) for i in range(n)]
    C=[sp.Function(f"C{i}")(q[i]) for i in range(n_home)]
    W=S+sum(p[i]*q[i]-C[i] for i in range(n_home))
    dt=lambda x: sp.diff(x,a)+sum(sp.diff(x,q[j])*speed[j] for j in range(n))
    A=sp.diff(S,a)+sum(q[i]*sp.diff(p[i],a) for i in range(n_home))
    H=[sp.diff(S,q[j])+sum(q[i]*sp.diff(p[i],q[j]) for i in range(n_home))+
       (p[j]-sp.diff(C[j],q[j]) if j<n_home else 0) for j in range(n)]
    assert sp.simplify(dt(W)-A-sum(H[j]*speed[j] for j in range(n)))==0
    print(f"generic n_home={n_home}: non-integrable welfare identity PASS")

q0,q1,qo,v,a=sp.symbols("q0 q1 qo v a",real=True)
Q=q0+q1+qo
# R9: p_i = 1-Q+network, while the paper defines CS=Q^2/2.
ph=1-Q+v*(q0+q1+a*qo)
S=Q**2/2
W=S+ph*(q0+q1)
qs=(q0,q1,qo)
p=(ph,ph,1-Q+v*a*Q)
C=(sp.Integer(0),sp.Integer(0))
Am=sp.diff(S,a)+sum(qs[h]*sp.diff(p[h],a) for h in (0,1))
Hm=[sp.diff(S,qs[j])+sum(qs[h]*sp.diff(p[h],qs[j]) for h in (0,1))+
    (p[j] if j<2 else 0) for j in range(3)]
assert sp.simplify(Am-v*(q0+q1)*qo)==0
assert all(sp.simplify(Hm[j]-(qo+v*(q0+q1)+ph))==0 for j in (0,1))
assert sp.simplify(Hm[2]-(qo+v*a*(q0+q1)))==0
vel=sp.symbols("vel0:3",real=True)
dtW=sp.diff(W,a)+sum(sp.diff(W,qs[j])*vel[j] for j in range(3))
assert sp.simplify(dtW-Am-sum(Hm[j]*vel[j] for j in range(3)))==0
print("R9 canonical p_i with CS=Q^2/2: EXACT NESTING PASS")
print("R12 generality identity VERIFIED; dominance and global bounds remain conditional")
