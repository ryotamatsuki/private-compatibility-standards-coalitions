"""R12 independent non-monotone incidence certification for the ORIGINAL R9 witness.

This is a research-stage validation. It does not alter the original R9
theorems, numerical witness, Appendix proofs, or submitted manuscript.

The a-path interpolates *only for accounting*, between existing no-adoption
and full-compatibility/residual-cost configurations; a is not a firm action.
All symbolic identities, inequalities, and certificates are exact rational.
"""
from math import comb
import sympy as s

a,x,y=s.symbols("a x y",real=True)
v=s.Rational(6,25)
c=s.Rational(1,10)
d=s.Rational(1,20)
Q=2*x+y
pH=1-Q+v*(2*x+a*y)
pO=1-Q+v*a*(2*x+y)
costO=c+(d-c)*a
# Cournot FOCs; home marginal price derivative = -1+v.
# Outsider's own derivative = -1+av.
sln=s.solve((pH-(1-v)*x,pO-costO-(1-v*a)*y),(x,y),dict=True)[0]
xh=s.factor(sln[x]);yo=s.factor(sln[y])
W=s.factor((Q**2/2+2*pH*x).subs(sln))
KI=9/(32*(1-v)**2)
P=1/(16*(1-v))
C=(1-v)*(1-2*c)**2/(4*(2-3*v)**2)
KM=(3-c-3*v+3*c*v)**2/(8*(2-3*v)**2)
AH=(1-v)*(1+c)**2/(4*(2-3*v)**2)
KR=(3-d)**2/(32*(1-v)**2)
AR=(1+d)**2/(16*(1-v))
assert s.factor(W.subs(a,0)-(KM+2*AH))==0
assert s.factor(W.subs(a,1)-(KR+2*AR))==0
G0=s.factor(W.subs(a,0)+C-KI-3*P)
G1=s.factor(W.subs(a,1)+C-KI-3*P)
assert G0==s.Rational(2408509,295731200)>0
assert G1==-s.Rational(1341,184832)<0
assert s.factor(W.subs(a,1)-W.subs(a,0))==-s.Rational(4554109,295731200)
assert s.factor(s.diff(xh,a))==-205/(8*(3*a+16)**2)
assert s.factor(s.diff(yo,a)-15*(891*a*a+156*a+19891)/(8*(3*a+16)**2*(6*a-25)**2))==0
# W'(a) changes sign: the uniform pointwise welfare-loss condition
# is NOT necessary and cannot be certified for this original witness.
Wprime=s.factor(s.diff(W,a))
assert Wprime.subs(a,0)<0 and Wprime.subs(a,1)>0
Wsecond=s.factor(s.diff(W,a,2))
num,den=s.fraction(Wsecond)
assert s.factor(den-64*(3*a+16)**4*(6*a-25)**4)==0
poly=s.Poly(num,a)
n=poly.degree()
bern=[s.factor(sum(poly.nth(k)*s.Rational(comb(j,k),comb(n,k))
                    for k in range(j+1))) for j in range(n+1)]
assert all(b>0 for b in bern),bern
# Positive Bernstein coefficients and positive denominator imply
# W''>0 for the entire [0,1] interval, hence W' increasing.
N=16
right_upper=s.factor(sum(Wprime.subs(a,s.Rational(j,N))/N
                         for j in range(1,N+1)))
assert right_upper < -G0  # Exact, not a floating-point comparison.
assert (W.subs(a,1)-W.subs(a,0)) <= right_upper
print("R9 numerical witness endpoints EXACT: PASS")
print("Original no-adoption and after-adoption market block mapping: PASS")
print("Domestic diversion and outsider expansion on entire path: PASS")
print("Wprime changes sign, so R12 uniform pointwise loss: FAIL (as expected)")
print("Wsecond strictly positive on entire path (Bernstein): PASS")
print("Wprime right Riemann N=16 upper bound:",s.N(right_upper,15))
print("Threshold -G0:",s.N(-G0,15))
print("Actual government gap pre:",s.N(G0,15),"post:",s.N(G1,15))
print("Non-monotone conduct-neutral integrated sufficient test: PASS")
