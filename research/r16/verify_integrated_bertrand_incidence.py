"""R16 exact R12-G3 theorem certificate for differentiated Bertrand.

At the fully microfounded price-competition witness, interpolate
OUTSIDER ONLY compatibility *as a mathematical welfare path*, not
as another investment action. The member-firm network group remains
compatible; outsider cross-network strength grows proportionally to a,
and its marginal cost declines from c to d.

For every a in [0,1], derive the unique interior differentiated
Bertrand equilibrium via symbolic symmetric 2x2 conditions. Prove
(i) demand/price regularity and positive output by Bernstein polynomial
certificates; (ii) W''(a)>0 using all-positive Bernstein coefficients of
numerator and denominator; (iii) exact 64-bin RIGHT upper Riemann sum
of W'(a) < -G0. This is the exact R12 non-monotone national-incidence
sufficient theorem, NOT a mere ex-post sign comparison.
"""
import sympy as S
from math import comb

a=S.symbols("a",real=True)
G=S.Rational(23,25)
V=S.Rational(33,500)
C=S.Rational(2,125)
D=S.Rational(1,500)
m=1-V
b=G-V
h=G-V*a
o=1-V*a
r=C+(D-C)*a
K=m+b
DET=S.factor((m-b)*(K*o-2*h*h))
Aii=S.factor((m*o-h*h)/DET)
Aoo=S.factor(K/(K*o-2*h*h))
LH=S.factor(K+1/Aii)
LO=S.factor(o+1/Aoo)
Dh=S.factor(LH*LO-2*h*h)
x=S.factor((LO-h*(1-r))/Dh)
y=S.factor((LH*(1-r)-2*h)/Dh)
# Quasilinear baseline U0=1'q-.5 q'M0 q, network utility
# v*C(a)*q taken as given by atomistic buyers. Hence
# CS=1/2 q'M0 q = (1+G)x^2+2Gxy+y^2/2.
# Two member firms' member-market profit equals 2*x^2/Aii.
W=S.factor((1+G+2/Aii)*x*x+2*G*x*y+y*y/2)

def bernstein(poly):
    pp=S.Poly(poly,a)
    n=pp.degree()
    assert n>=0
    return [S.factor(sum(pp.nth(k)*S.Rational(comb(j,k),comb(n,k))
                         for k in range(j+1))) for j in range(n+1)]

def strictly_positive_rational(expr,label):
    num,den=S.fraction(S.cancel(expr))
    ncoeff=bernstein(num)
    dcoeff=bernstein(den)
    # Rational expression was reduced. If either numerator/denominator
    # coefficients are all strictly negative, flip its signs together.
    if all(c<0 for c in ncoeff) and all(c<0 for c in dcoeff):
        ncoeff=[-c for c in ncoeff]
        dcoeff=[-c for c in dcoeff]
    assert all(c>0 for c in ncoeff),(label,"numerator",ncoeff)
    assert all(c>0 for c in dcoeff),(label,"denominator",dcoeff)
    print(label,"Bernstein degrees",len(ncoeff)-1,len(dcoeff)-1,"positive on [0,1]")

# Stability of the network feedback demand matrix for ALL a:
# principal minors m, m^2-b^2, determinant.
assert m>0 and m*m-b*b>0
strictly_positive_rational(DET,"M determinant")
strictly_positive_rational(m*o-h*h,"positive member inverse diagonal numerator")
strictly_positive_rational(x,"member q positive")
strictly_positive_rational(y,"outsider q positive")
assert all(z>0 for z in [W.subs(a,0),W.subs(a,1)])
print("All intermediate network-feedback and interior-price equilibria verified")

wp=S.factor(S.diff(W,a))
wpp=S.factor(S.diff(wp,a))
strictly_positive_rational(wpp,"W second derivative")
assert wp.subs(a,0)<0 and wp.subs(a,1)>0
G0=S.Rational(7855162695059566974763678509,
               2831702211424358619269262025000)
GA=S.Rational(-10594075757986722536572731513123,
               11674763178357541064558264771937500)
assert S.factor(W.subs(a,1)-W.subs(a,0)-(GA-G0))==0
N=64
upper=S.factor(sum(wp.subs(a,S.Rational(j,N))
                  for j in range(1,N+1))/N)
assert upper < -G0
print("R12 integrable incidence I(a)=dW(a)/da is strictly increasing")
print("Member government initial SU-IS advantage G0:",S.N(G0,16))
print("Bertrand 64-bin exact right-upper sum:",S.N(upper,16))
print("Required threshold -G0:",S.N(-G0,16))
print("Original exact Bertrand government gap after:",S.N(GA,16))
print("R16 SAME GENERIC R12-G1+G3 MECHANISM: EXACT BERTRAND PROOF PASS")
