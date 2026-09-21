"""R3 symbolic verification for residual adaptation cost.

This script independently verifies the algebra in
docs/revision/03_r3_results.md.

It does not alter the Stage-8 canonical module.
"""

from __future__ import annotations

import sympy as sp

c, v, lam, F, d = sp.symbols("c v lam F d", positive=True, real=True)
t = 1 - v

# Stage-8 baseline blocks
P = 1 / (16 * t)
A = t * (1 + c) ** 2 / (4 * (2 - 3 * v) ** 2)
B = (1 - 3 * c - 3 * (1 - c) * v) ** 2 / (4 * (2 - 3 * v) ** 2)
C = t * (1 - 2 * c) ** 2 / (4 * (2 - 3 * v) ** 2)
S = (1 - 2 * c) ** 2 / 16
K_I = 9 / (32 * t**2)
K_M = (3 - c - 3 * v + 3 * c * v) ** 2 / (8 * (2 - 3 * v) ** 2)

W_IS = sp.simplify(K_I + 3 * P)
W_no = sp.simplify(K_M + 2 * A + C)

E = sp.simplify((K_M - K_I) + 2 * (A - P))
Drec = sp.simplify(P - C)

assert sp.simplify(W_no - W_IS - (E - Drec)) == 0

# ---------------------------------------------------------------------------
# Member market after outsider adoption with residual cost d
# ---------------------------------------------------------------------------

q_member = (1 + d) / (4 * t)
q_outsider = (1 - 3 * d) / (4 * t)

A_R = sp.simplify(t * q_member**2)
B_R = sp.simplify(t * q_outsider**2)
K_R = sp.simplify((2 * q_member + q_outsider) ** 2 / 2)

W_partial = sp.simplify(K_R + 2 * A_R + C)

R = sp.simplify(
    d * ((5 - 4 * v) * d + 2 * (1 - 4 * v))
    / (32 * t**2)
)

assert sp.simplify(W_partial - W_IS - (-Drec + R)) == 0
assert sp.simplify(W_partial - W_no - (-E + R)) == 0

Rprime = sp.factor(sp.diff(R, d))
assert sp.simplify(
    Rprime
    - (2 * (5 - 4 * v) * d + 2 * (1 - 4 * v))
    / (32 * t**2)
) == 0

# ---------------------------------------------------------------------------
# One-adopter state in outsider/SW target market
# ---------------------------------------------------------------------------

q_native = sp.simplify(
    ((1 - v) * (1 + c) + d * (1 - 2 * v))
    / (2 * (1 - v) * (2 - 3 * v))
)
q_adopter = sp.simplify(
    ((1 - v) * (1 + c) - d * (3 - 4 * v))
    / (2 * (1 - v) * (2 - 3 * v))
)
q_single = sp.simplify(
    (1 - 3 * v - 3 * c * (1 - v) + d)
    / (2 * (2 - 3 * v))
)

profit_adopter = sp.simplify(t * q_adopter**2)

T_U_d = sp.simplify(profit_adopter - C)
T_W_d = sp.simplify(profit_adopter - S)

q_both_member = sp.simplify((1 - 2 * d) / (4 * t))
profit_both_member = sp.simplify(t * q_both_member**2)
T_A_R_d = sp.simplify(profit_both_member - q_single**2)

T_O_d = sp.simplify(B_R - B)

# Old thresholds recovered at d=0
T_A = sp.simplify(P - B)
T_U = sp.simplify(A - C)
T_W = sp.simplify(A - S)

assert sp.simplify(T_O_d.subs(d, 0) - T_A) == 0
assert sp.simplify(T_U_d.subs(d, 0) - T_U) == 0
assert sp.simplify(T_W_d.subs(d, 0) - T_W) == 0
assert sp.simplify(T_A_R_d.subs(d, 0) - T_A) == 0

# Difference between SW unilateral and SU reverse unilateral is invariant in d.
assert sp.simplify((T_W_d - T_U_d) - (C - S)) == 0


# Independent FOC reconstruction for the new partial-adoption blocks.
xm, yo = sp.symbols("xm yo", real=True)
sol_member = sp.solve(
    [
        sp.Eq(1 - t * (2 * xm + yo), t * xm),
        sp.Eq(1 - t * (2 * xm + yo) - d, t * yo),
    ],
    [xm, yo],
    dict=True,
)[0]
assert sp.simplify(sol_member[xm] - q_member) == 0
assert sp.simplify(sol_member[yo] - q_outsider) == 0

qn, qa, qs = sp.symbols("qn qa qs", real=True)
sol_pair = sp.solve(
    [
        sp.Eq(1 - t * (qn + qa) - qs, t * qn),
        sp.Eq(1 - t * (qn + qa) - qs - d, t * qa),
        sp.Eq(1 - c - qn - qa - 2 * qs, 0),
    ],
    [qn, qa, qs],
    dict=True,
)[0]
assert sp.simplify(sol_pair[qn] - q_native) == 0
assert sp.simplify(sol_pair[qa] - q_adopter) == 0
assert sp.simplify(sol_pair[qs] - q_single) == 0

qb, qn2 = sp.symbols("qb qn2", real=True)
sol_both = sp.solve(
    [
        sp.Eq(1 - t * (2 * qb + qn2) - d, t * qb),
        sp.Eq(1 - t * (2 * qb + qn2), t * qn2),
    ],
    [qb, qn2],
    dict=True,
)[0]
assert sp.simplify(sol_both[qb] - q_both_member) == 0

# ---------------------------------------------------------------------------
# Exact nonlocal witness
# ---------------------------------------------------------------------------

w = {
    c: sp.Rational(1, 10),
    v: sp.Rational(6, 25),
    lam: sp.Rational(1, 2),
}
d_w = sp.simplify((lam * c).subs(w))
subs_w = {c: w[c], v: w[v], d: d_w}

phi0_w = sp.factor((E - Drec).subs({c: w[c], v: w[v]}))
gap_w = sp.factor((W_partial - W_IS).subs(subs_w))

tu_w = sp.factor(T_U_d.subs(subs_w))
tw_w = sp.factor(T_W_d.subs(subs_w))
ta_r_w = sp.factor(T_A_R_d.subs(subs_w))
fstar_w = sp.factor((2 * T_O_d).subs(subs_w))

assert phi0_w == sp.Rational(2408509, 295731200)
assert gap_w == -sp.Rational(1341, 184832)
assert tu_w == sp.Rational(42273, 1245184)
assert tw_w == sp.Rational(2122041, 31129600)
assert ta_r_w == sp.Rational(2024181, 31129600)
assert fstar_w == sp.Rational(459189, 3891200)

F_w = sp.Rational(9, 100)
assert max(tw_w, ta_r_w, sp.Rational(0)) < F_w < fstar_w
assert gap_w < 0 < phi0_w

# ---------------------------------------------------------------------------
# Witness-line robustness for all lambda in [0,1]
# ---------------------------------------------------------------------------

d_line = lam * sp.Rational(1, 10)
line_subs = {c: sp.Rational(1, 10), v: sp.Rational(6, 25), d: d_line}

gap_line = sp.factor((W_partial - W_IS).subs(line_subs))
upper_line = sp.factor((2 * T_O_d).subs(line_subs))
tw_line = sp.factor(T_W_d.subs(line_subs))
ta_line = sp.factor(T_A_R_d.subs(line_subs))

assert sp.simplify(gap_line - (202 * lam**2 + 40 * lam - 741) / sp.Integer(92416)) == 0

diff_tw = sp.factor(upper_line - tw_line)
diff_ta = sp.factor(upper_line - ta_line)

assert sp.simplify(diff_tw - (
    3 * (16725 * lam**2 - 78350 * lam + 164283) / sp.Integer(7782400)
)) == 0
assert sp.simplify(diff_ta - (
    3 * (33825 * lam**2 - 166550 * lam + 212263) / sp.Integer(7782400)
)) == 0

# Analytic interval certificates:
# gap numerator is increasing on [0,1], with value -499 at lambda=1.
assert (202 + 40 - 741) < 0
# Each difference quadratic is decreasing on [0,1] because its derivative
# remains negative there; its minimum on the interval is therefore at 1.
assert 2 * 16725 - 78350 < 0
assert 16725 - 78350 + 164283 > 0
assert 2 * 33825 - 166550 < 0
assert 33825 - 166550 + 212263 > 0

print("R3 equilibrium identities: PASS")
print("R3 adoption-threshold recovery at d=0: PASS")
print("R3 exact witness: PASS")
print("R3 witness-line robustness certificates: PASS")
print("Witness:")
print(f"  d={float(d_w):.6f}")
print(f"  pre-adoption SU-IS gap={float(phi0_w):.9f}")
print(f"  post-adoption SU-IS gap={float(gap_w):.9f}")
print(f"  lower F={float(max(tw_w, ta_r_w)):.9f}")
print(f"  chosen F={float(F_w):.9f}")
print(f"  upper F={float(fstar_w):.9f}")
