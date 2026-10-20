"""Independent exact reproduction of R19 partial theorem; not a Level-3 certificate."""
import json
from pathlib import Path
import sympy as s

g,v,ell,d=s.symbols('gamma v ell d',real=True)
b=g-v
tau=1-g+ell
kappa=tau+3*b
x=(tau+b*d)/(tau*kappa)
y=(tau-(tau+2*b)*d)/(tau*kappa)
M0=(1-g)*s.eye(3)+g*s.ones(3)
M=M0-v*s.ones(3)
q=s.Matrix([x,x,y])
assert all(s.factor(z)==0 for z in (M+ell*s.eye(3))*q-s.Matrix([1,1,1-d]))
CS=(q.T*M0*q)[0]/2
m=CS+2*ell*x*x
rho=1+2*g-4*ell*b/tau
AA=tau*tau+4*(1-g)*tau*b+(6*(1-g)+4*ell)*b*b
residual=s.factor(m-m.subs(d,0))
expected=(-rho*d+AA*d*d/(2*tau*tau))/(kappa*kappa)
assert s.factor(residual-expected)==0
assert s.factor(s.diff(residual,d,2)-AA/(tau*tau*kappa*kappa))==0
ellB=(1-g)*(1+2*g-3*v)/(1+g-2*v)
Ainv=M.inv()
assert s.factor(ellB-1/Ainv[0,0])==0
rhoB=s.factor(rho.subs(ell,ellB))
num,den=s.fraction(rhoB)
assert s.factor(den-(-3*g+5*v-2))==0
assert s.factor(num.subs(v,0)-(g-2)*(2*g+1))==0
assert s.factor(num.subs(v,g)-2*(g-1)*(2*g+1))==0
assert s.diff(num,v,2)==24
r9=s.factor(residual.subs({g:1,ell:1-v}))
r9_expected=d*((5-4*v)*d+2*(1-4*v))/(32*(1-v)**2)
assert s.factor(r9-r9_expected)==0
assert s.factor(rho.subs({g:1,ell:1-v})-(4*v-1))==0
# The algebra does not certify incompatible markets: an exact counterexample.
G,V=s.Rational(9,10),s.Rational(4,5)
CB=s.Matrix([[1,1,0],[1,1,0],[0,0,0]])
M0bad=(1-G)*s.eye(3)+G*s.ones(3)
full=M0bad-V*s.ones(3)
partial=M0bad-V*CB
assert all(full[:i,:i].det()>0 for i in (1,2,3))
assert partial.det()<0
# Full-compatible demand slope magnitude rises at a rival-entry event.
n,t,bb=s.symbols('n t b',positive=True)
h=lambda n:(t+(n-1)*bb)/(t*(t+n*bb))
assert s.factor(h(n+1)-h(n)-bb*bb/(t*(t+n*bb)*(t+(n+1)*bb)))==0
r16={g:s.Rational(23,25),v:s.Rational(33,500)}
L=s.factor(ellB.subs(r16))
T=s.factor(tau.subs({**r16,ell:L}))
B=s.factor(b.subs(r16))
R=s.factor(rho.subs({**r16,ell:L}))
A=s.factor(AA.subs({**r16,ell:L}))
dmin=s.factor(R*T*T/A)
dbar=s.factor(T/(T+2*B))
assert s.Rational(2,125)<dmin<dbar
out={
    'status':'PASS; independent symbolic partial theorem and scope counterexample',
    'level3_joint_theorem':'NOT PROVED',
    'rho_bertrand':str(rhoB),
    'r9_exact_residual':str(r9),
    'r16_dmin':str(dmin),'r16_dbar':str(dbar),
    'partial_network_counterexample':{'gamma':str(G),'v':str(V),'full_det':str(full.det()),'partial_det':str(partial.det())},
    'proof_scope':'full-compatible residual family; pre-adoption and adoption game need separate certification'
}
print(json.dumps(out,indent=2))
Path(__file__).with_name('independent_referee_results.json').write_text(json.dumps(out,indent=2)+'\n')
