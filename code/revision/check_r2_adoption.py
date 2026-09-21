"""R2 verification: one-way private adoption conditions.

The script checks:
1. the common-cost threshold logic on finite examples;
2. scope-expansion success and failure cases;
3. the additive optional-deployment boundary formula;
4. the exact mapping to the submitted Cournot model at the canonical witness.

It is a verification aid, not a substitute for the analytical proofs in
docs/revision/02_r2_results.md.
"""

from __future__ import annotations

import math

import sympy as sp


def feasibility_slack(upper: float, lower: float) -> float:
    """Upper threshold minus the nonnegative lower threshold."""
    return upper - max(0.0, lower)


def interval_width(upper: float, lower: float) -> float:
    """Actual length of the positive common-F dominance interval."""
    return max(0.0, feasibility_slack(upper, lower))


def optional_value(net_market_values: list[float]) -> float:
    """Additive optional-deployment value before the common setup cost."""
    return sum(max(x, 0.0) for x in net_market_values)


# Generic finite examples

U0 = 1.50
L0 = 0.60
assert interval_width(U0, L0) > 0

# Scope expansion succeeds when the upper threshold grows more than the lower.
U1 = 1.90
L1 = 0.70
assert (U1 - U0) > (max(0.0, L1) - max(0.0, L0))
assert feasibility_slack(U1, L1) > feasibility_slack(U0, L0)
assert interval_width(U1, L1) > interval_width(U0, L0)

# A positive direct outsider gain is insufficient if the strongest reverse
# adoption threshold rises by more.
U2 = 1.90
L2 = 1.20
assert U2 > U0
assert feasibility_slack(U2, L2) < feasibility_slack(U0, L0)
assert interval_width(U2, L2) < interval_width(U0, L0)

# A slack improvement need not create a region if the starting slack is negative.
U_empty, L_empty = 0.40, 0.80
U_less_bad, L_less_bad = 0.60, 0.80
assert feasibility_slack(U_less_bad, L_less_bad) > feasibility_slack(U_empty, L_empty)
assert interval_width(U_empty, L_empty) == 0.0
assert interval_width(U_less_bad, L_less_bad) == 0.0

# Package adoption can be harmed by an added negative-net-value market.
package_before = sum([0.80, 0.70])
package_after = sum([0.80, 0.70, -1.00])
assert package_after < package_before

# Under additive optional deployment, that market is skipped.
opt_before = optional_value([0.80, 0.70])
opt_after = optional_value([0.80, 0.70, -1.00])
assert math.isclose(opt_before, opt_after)
assert optional_value([0.80, 0.70, 0.25]) > opt_before

# Adopter-specific costs can support strict dominant one-way adoption.
F_o = 1.00
member_costs = [0.80, 1.10]
member_thresholds = [0.50, 0.90]
assert F_o < U0
assert all(F_i > ell_i for F_i, ell_i in zip(member_costs, member_thresholds))


# Submitted Cournot-model mapping

c, v = sp.symbols("c v", real=True)

P = 1 / (16 * (1 - v))
B = (
    (1 - 3 * c - 3 * (1 - c) * v) ** 2
    / (4 * (2 - 3 * v) ** 2)
)
A = (1 - v) * (1 + c) ** 2 / (4 * (2 - 3 * v) ** 2)
C = (1 - v) * (1 - 2 * c) ** 2 / (4 * (2 - 3 * v) ** 2)
S = (1 - 2 * c) ** 2 / 16

T_A = sp.factor(P - B)
T_U = sp.factor(A - C)
T_W = sp.factor(A - S)

# Exact symbolic mapping in the symmetric two-member SU.
U_old = sp.factor(2 * T_A)
L_profile_old = sp.factor(T_U)

witness = {c: sp.Rational(1, 10), v: sp.Rational(6, 25)}

ta = float(sp.N(T_A.subs(witness), 15))
tu = float(sp.N(T_U.subs(witness), 15))
tw = float(sp.N(T_W.subs(witness), 15))
u = float(sp.N(U_old.subs(witness), 15))
l_profile = float(sp.N(L_profile_old.subs(witness), 15))
l_robust = max(tu, ta)
headline_lower = max(tw, ta)

expected = {
    "T_A": 0.0818242,
    "T_U": 0.0661011,
    "T_W": 0.1003198,
}
for key, value in [("T_A", ta), ("T_U", tu), ("T_W", tw)]:
    assert abs(value - expected[key]) < 1e-6, (key, value)

assert l_profile == tu
assert u > l_robust > 0
assert headline_lower > l_robust
assert u > headline_lower

# The submitted headline interval is a strict subset of the SU-only R2
# selection-free interval because it additionally suppresses SW adoption.
assert l_robust < headline_lower < u

print("R2 generic examples: PASS")
print("Optional-deployment boundary test: PASS")
print("Cournot mapping at (c,v)=(0.10,0.24):")
print(f"  T_U={tu:.7f}")
print(f"  T_A={ta:.7f}")
print(f"  T_W={tw:.7f}")
print(f"  R2 SU-only unique interval: ({l_robust:.7f}, {u:.7f})")
print(f"  Submitted headline interval: ({headline_lower:.7f}, {u:.7f})")
print("R2 verification: PASS")
