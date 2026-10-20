"""Exact symbolic partial comparative statics, NOT the full R19 target theorem."""
import json
from pathlib import Path
import sympy as s
L,T,t,h,k,g,z=s.symbols('L T t h k gamma z', real=True)
K=L*T-2*t*t
x=(T-t+t*z)/K
y=(L-2*t-L*z)/K
P=1+g+2*h
m=P*x*x+2*g*x*y+y*y/2
pi=k*y*y
eta=(P*t-g*L)/(k*L)*x/y+(2*g*t-L)/(2*k*L)
assert s.factor(s.diff(m,z)/(-s.diff(pi,z))-eta)==0
assert s.factor(s.diff(eta,z)-(P*t-g*L)*K/(k*L*(L-2*t-L*z)**2))==0
assert s.factor(s.diff(x/y,z)-K/(L-2*t-L*z)**2)==0
# Primitive quadratic Cournot counterexample; inverse-demand substitution != gross substitutes.
M=s.Matrix([[s.Rational(3,2),1,s.Rational(1,10)], [1,s.Rational(3,2),1],[s.Rational(1,10),1,s.Rational(3,2)]])
A=M+s.diag(*M.diagonal())
q=A.inv()*s.ones(3,1)
v=-A.inv()[:,2]
assert all(M[:i,:i].det()>0 for i in (1,2,3))
assert all(A[i,i]>sum(abs(A[i,j]) for j in range(3) if j!=i) for i in range(3))
assert all(a>0 for a in q)
assert v[0]<0 and v[1]>0 and v[2]<0
# For all-positive off-diagonal A no sign signature turns it into a Z matrix:
# s1*s2<0,s1*s3<0 force s2*s3>0; symbolic sign case enumeration.
import itertools
assert not any(all(a[i]*a[j]<0 for i in range(3) for j in range(i)) for a in itertools.product((-1,1),repeat=3))
result={
 'status':'complete symbolic partial lemma; not full primitive joint theorem',
 'ratio_formula':str(eta),
 'ratio_derivative':str((P*t-g*L)*K/(k*L*(L-2*t-L*z)**2)),
 'counterexample':{'M':str(M),'M_leading_principal_minors':[str(M[:i,:i].det()) for i in (1,2,3)],'A':str(A),'q':list(map(str,q)),'dq_dcost3':list(map(str,v))},
 'scope':'inverse-demand substitutability and SPD/diagonal dominance alone do not force all rivals to lose; this example is not Marshallian gross substitutes'
}
print(json.dumps(result,indent=2))
