"""R4 precheck: zero-network-effect SU-vs-IS welfare gap.

This is a symbolic regression check for the submitted symmetric Cournot model.
It is not a proof of any result outside that model.
"""

import sympy as sp

c, v = sp.symbols("c v", real=True)

P = 1 / (16 * (1 - v))
A = (1 - v) * (1 + c) ** 2 / (4 * (2 - 3 * v) ** 2)
C = (1 - v) * (1 - 2 * c) ** 2 / (4 * (2 - 3 * v) ** 2)

K_I = 9 / (32 * (1 - v) ** 2)
K_M = (3 - c - 3 * v + 3 * c * v) ** 2 / (8 * (2 - 3 * v) ** 2)

W_IS = K_I + 3 * P
W_SU_member_no_bypass = K_M + 2 * A + C

gap = sp.factor(sp.together(W_SU_member_no_bypass - W_IS))
gap_v0 = sp.factor(gap.subs(v, 0))
target = c * (13 * c - 6) / 32

assert sp.simplify(gap_v0 - target) == 0

# Analytic sign certificate on 0 < c < 1/3:
# c > 0 and 13*c - 6 < 13/3 - 6 = -5/3 < 0.
# Therefore target < 0 throughout the open interval.

print("W_SU_member_no_bypass - W_IS =", gap)
print("At v=0 =", gap_v0)
print("Identity check: PASS")
print("Sign on 0<c<1/3: NEGATIVE (analytic bound 13c-6 < -5/3)")
