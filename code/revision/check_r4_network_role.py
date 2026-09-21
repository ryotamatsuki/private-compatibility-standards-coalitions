"""R4 symbolic verification: network effects and baseline specification.

Independent verification for Revision Track R4. This script reconstructs the
Stage-8 symmetric Cournot objects rather than modifying code/canonical.py.
It proves the fixed-c feasibility map, the exact root structure of the
pre-adoption SU-IS welfare gap, the reciprocal-disadvantage intersection,
the v=0 adoption logic, the R3 residual-rent boundary, and one deliberately
minimal singleton-network sensitivity model.
"""

from __future__ import annotations
import sympy as sp

c, v, F, d, x = sp.symbols("c v F d x", real=True)

def eq(a, b=0):
    return sp.simplify(sp.together(a-b)) == 0

# Canonical blocks.
P = 1 / (16 * (1 - v))
A = (1 - v) * (1 + c) ** 2 / (4 * (2 - 3 * v) ** 2)
B = (1 - 3 * c - 3 * (1 - c) * v) ** 2 / (4 * (2 - 3 * v) ** 2)
C = (1 - v) * (1 - 2 * c) ** 2 / (4 * (2 - 3 * v) ** 2)
S = (1 - 2 * c) ** 2 / 16
K_I = 9 / (32 * (1 - v) ** 2)
K_M = (3 - c - 3 * v + 3 * c * v) ** 2 / (8 * (2 - 3 * v) ** 2)

W_IS = sp.simplify(K_I + 3 * P)
W_SU = sp.simplify(K_M + 2 * A + C)
Phi = sp.factor(sp.together(W_SU - W_IS))
E = sp.factor((K_M - K_I) + 2 * (A - P))
Drec = sp.factor(P - C)

T_A = sp.factor(P - B)
T_U = sp.factor(A - C)
T_W = sp.factor(A - S)

N = (
    36*c**2*v**4 - 144*c**2*v**3 + 232*c**2*v**2 - 176*c**2*v + 52*c**2
    - 72*c*v**4 + 240*c*v**3 - 288*c*v**2 + 144*c*v - 24*c
    + 36*v**4 - 114*v**3 + 81*v**2 - 12*v
)
num, den = sp.fraction(Phi)
assert eq(num, N)
assert eq(den, 32*(1-v)**2*(2-3*v)**2)
assert eq(Phi.subs(v, 0), c*(13*c-6)/32)

# Fixed-c feasibility:
# 3c(1-v)<1-3v iff 3v(1-c)<1-3c.
assert sp.expand((1-3*v)-3*c*(1-v)-((1-3*c)-3*v*(1-c))) == 0
vbar = (1-3*c)/(3*(1-c))
assert eq(vbar.subs(c, sp.Rational(1,9)), sp.Rational(1,4))
assert eq(vbar-sp.Rational(1,4), (9*c-1)/(12*(c-1)))

# Boundary values.
assert eq(N.subs(v, sp.Rational(1,4)),
          sp.Rational(9,64)*(145*c**2-18*c+3))
Q = 17*c**3 + 109*c**2 - 89*c + 11
assert eq(N.subs(v, vbar), Q/(9*(1-c)**3))

# c* exact root isolation.
cstar_lo = sp.Rational(1529167, 10_000_000)
cstar_hi = sp.Rational(1529168, 10_000_000)
assert Q.subs(c, cstar_lo) > 0 > Q.subs(c, cstar_hi)
assert sp.count_roots(Q, cstar_lo, cstar_hi) == 1
assert sp.count_roots(Q, sp.Rational(0), sp.Rational(1,3)) == 1

# Root count, case I: 0<c<=1/9, U=1/4.
U1 = sp.Rational(1,4)
p1 = sp.Poly(sp.cancel(N.subs(v, U1*x/(1+x))*(1+x)**4), x)
a = [sp.factor(z) for z in p1.all_coeffs()]
assert eq(a[0], sp.Rational(9,64)*(145*c**2-18*c+3))
assert eq(a[-1], 4*c*(13*c-6))
assert sp.discriminant(145*c**2-18*c+3, c) < 0
for z in a[1:-1]:
    assert sp.count_roots(z, sp.Rational(0), sp.Rational(1,9)) == 0
    assert z.subs(c, sp.Rational(1,18)) < 0
assert a[-1].subs(c, sp.Rational(1,18)) < 0
# Signs: +----, hence exactly one positive x root by Descartes.

# Root count, case II: 1/9<c<1/3, U=vbar.
raw2 = sp.cancel(N.subs(v, vbar*x/(1+x))*(1+x)**4)
raw2_num, raw2_den = sp.fraction(raw2)
assert eq(raw2_den, 9*(c-1)**3)
# raw2 = (-raw2_num)/(9(1-c)^3), denominator positive on c<1.
p2 = sp.Poly(-sp.expand(raw2_num), x)
b = [sp.factor(z) for z in p2.all_coeffs()]
assert eq(b[0], Q)
for z in b[1:]:
    assert sp.count_roots(z, sp.Rational(1,9), sp.Rational(1,3)) == 0
    assert z.subs(c, sp.Rational(1,8)) < 0
assert Q.subs(c, sp.Rational(1,8)) > 0
assert Q.subs(c, sp.Rational(1,6)) < 0

# Rational witnesses on both sides.
assert Phi.subs({c:sp.Rational(1,10), v:sp.Rational(1,5)}) < 0
assert Phi.subs({c:sp.Rational(1,10), v:sp.Rational(6,25)}) > 0
assert N.subs({c:sp.Rational(3,20), v:vbar.subs(c,sp.Rational(3,20))}) > 0
assert N.subs({c:sp.Rational(4,25), v:vbar.subs(c,sp.Rational(4,25))}) < 0

# Reciprocal disadvantage.
linear_D = sp.expand((2-3*v) - 2*(1-v)*(1-2*c))
assert eq(linear_D, 4*c*(1-v)-v)
vD = 4*c/(1+4*c)
assert eq(linear_D.subs(v, vD), 0)
assert eq(vD-sp.Rational(1,4), (12*c-1)/(4*(4*c+1)))
assert eq(vD-vbar, -(11*c-1)/(3*(c-1)*(4*c+1)))

H = 512*c**3 - 224*c**2 - 241*c + 18
assert eq(N.subs(v, vD), -4*c*H/(1+4*c)**4)
cdag_lo = sp.Rational(7078518, 100_000_000)
cdag_hi = sp.Rational(7078520, 100_000_000)
assert H.subs(c, cdag_lo) > 0 > H.subs(c, cdag_hi)
assert sp.count_roots(H, cdag_lo, cdag_hi) == 1
assert sp.count_roots(H, sp.Rational(0), sp.Rational(1,3)) == 1
assert cdag_hi < sp.Rational(1,12) < sp.Rational(1,9) < cstar_lo
assert N.subs({c:sp.Rational(7,100), v:vD.subs(c,sp.Rational(7,100))}) < 0
assert N.subs({c:sp.Rational(9,125), v:vD.subs(c,sp.Rational(9,125))}) > 0
assert Phi.subs({c:sp.Rational(3,40), v:sp.Rational(9,40)}) > 0
assert Drec.subs({c:sp.Rational(3,40), v:sp.Rational(9,40)}) > 0

# v=0 private adoption.
TA0, TU0, TW0 = [sp.factor(z.subs(v,0)) for z in (T_A,T_U,T_W)]
assert eq(TA0, 3*c*(2-3*c)/16)
assert eq(TU0, 3*c*(2-c)/16)
assert eq(TW0, TU0)
assert eq(TU0-TA0, 3*c**2/8)
assert eq(2*TA0-TW0, 3*c*(2-5*c)/16)
cw, Fw = sp.Rational(1,10), sp.Rational(1,20)
assert TW0.subs(c,cw) < Fw < (2*TA0).subs(c,cw)

# R3 residual rent.
R = d*((5-4*v)*d + 2*(1-4*v))/(32*(1-v)**2)
assert eq(R.subs(v,0), d*(5*d+2)/32)
assert eq(E.subs(v,0), c*(5*c+2)/32)
assert eq(Drec.subs(v,0), c*(1-c)/4)
assert eq((E-Drec).subs(v,0), c*(13*c-6)/32)
dRdv = sp.factor(sp.diff(R,v))
assert eq(dRdv, d*(2*d*v-3*d+4*v+2)/(16*(v-1)**3))

# Singleton sensitivity S1: remove only the |G|>=2 exception.
K = 3*v**2 - 6*v + 2
qM1 = (1+c-2*v)/(2*K)
qB1 = (1-3*v-3*c*(1-v))/(2*K)
qC1 = (1-2*v-2*c*(1-v))/(2*K)
qD1 = (1+2*c-3*v)/(2*K)
A1 = (1-v)*qM1**2
B1 = (1-v)*qB1**2
C1 = (1-v)*qC1**2
KM1 = (2*qM1+qB1)**2/2

qm, qb = sp.symbols("qm qb", real=True)
sol = sp.solve([
    sp.Eq(1 - 2*(1-v)*qm - qb, (1-v)*qm),
    sp.Eq(1 - 2*qm - 2*(1-v)*qb - c, 0),
], [qm,qb], dict=True)[0]
assert eq(sol[qm], qM1)
assert eq(sol[qb], qB1)

Phi1 = sp.factor(sp.together(KM1+2*A1+C1-W_IS))
M1, den1 = sp.fraction(Phi1)
assert eq(den1, 32*(1-v)**2*K**2)

# Phi1<0 over the original canonical domain.
s1p1 = sp.Poly(sp.cancel(M1.subs(v,U1*x/(1+x))*(1+x)**5), x)
s1a = [sp.factor(z) for z in s1p1.all_coeffs()]
for z in s1a[:-1]:
    assert sp.count_roots(z, sp.Rational(0), sp.Rational(1,9)) == 0
    assert z.subs(c, sp.Rational(1,18)) < 0
assert eq(s1a[-1], 4*c*(13*c-6))
assert s1a[-1].subs(c, sp.Rational(1,18)) < 0

s1raw2 = sp.cancel(M1.subs(v,vbar*x/(1+x))*(1+x)**5)
s1n2, s1d2 = sp.fraction(s1raw2)
assert eq(s1d2, 243*(c-1)**5)
s1p2 = sp.Poly(-sp.expand(s1n2), x)
for z in s1p2.all_coeffs():
    assert sp.count_roots(z, sp.Rational(1,9), sp.Rational(1,3)) == 0
    assert z.subs(c,sp.Rational(1,5)) < 0

# S1 reciprocal disadvantage.
D1 = sp.factor(P-C1)
f1 = 4*c*(1-v)**2-v**2
f2 = 4*c*(1-v)**2-(7*v**2-12*v+4)
nd1, dd1 = sp.fraction(D1)
assert eq(nd1, f1*f2)
assert eq(f2.subs(c,(1-3*v)/(3*(1-v))),
          -(9*v**2-20*v+8)/3)
# On 0<v<1/4, 9v^2-20v+8 is decreasing and remains positive
# at v=1/4. Since f2 increases in c, canonical feasibility implies f2<0.
assert (18*sp.Rational(1,4)-20) < 0
assert 9*sp.Rational(1,4)**2-20*sp.Rational(1,4)+8 > 0
# K(v)>0 on the same interval, so all cleared denominators used above
# have the asserted fixed signs.
assert (6*sp.Rational(1,4)-6) < 0
assert K.subs(v,sp.Rational(1,4)) > 0

# S1 adoption thresholds.
qS1 = (1-2*v-2*c*(1-v))/(2*(2-v)*(1-2*v))
S1 = (1-v)*qS1**2

# Independent SW FOC reconstruction (one zero-cost native, two cost-c foreign
# singleton firms under S1).
qh, qs = sp.symbols("qh qs", real=True)
sol_sw = sp.solve([
    sp.Eq(1-2*(1-v)*qh-2*qs, 0),
    sp.Eq(1-qh-(3-2*v)*qs-c, 0),
], [qh, qs], dict=True)[0]
assert eq(sol_sw[qs], qS1)

TA1 = sp.factor(P-B1)
TU1 = sp.factor(A1-C1)
TW1 = sp.factor(A1-S1)
# In the one-adopter state the remaining singleton earns B1; after it adopts,
# all three are compatible and it earns P. Hence the post-rival threshold is TA1.
w = {c:sp.Rational(1,10), v:sp.Rational(6,25)}
assert sp.factor(Phi1.subs(w)) == -sp.Rational(60921623,2423193728)
assert sp.factor(D1.subs(w)) == sp.Rational(547149,15942064)
assert sp.factor(TA1.subs(w)) == sp.Rational(5183091,63768256)
assert sp.factor(TU1.subs(w)) == sp.Rational(295659,3356224)
assert sp.factor(TW1.subs(w)) == sp.Rational(7226119311,68631424576)
assert max(TU1.subs(w), TA1.subs(w), TW1.subs(w)) < 2*TA1.subs(w)

print("R4 canonical Phi reconstruction: PASS")
print("R4 fixed-c feasibility and c=1/9 switch: PASS")
print("R4 unique-root certification: PASS")
print("R4 c* and c_dagger exact isolation: PASS")
print("R4 joint Phi>0 and D>0 region: PASS")
print("R4 zero-network private-adoption interval: PASS")
print("R4 residual-rent boundary/comparative static: PASS")
print("R4 singleton-network S1 sensitivity: PASS")
