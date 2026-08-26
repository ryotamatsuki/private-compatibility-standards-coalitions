"""Symbolic verification of the Stage-8 frozen canonical theory.

The script deliberately re-derives the four Cournot subgames from their FOCs
rather than merely comparing copied closed forms. Any failed identity exits
non-zero and must trigger the repository's theory-hold procedure.
"""

from __future__ import annotations

import sys

import sympy as sp

import canonical as can


def assert_zero(label: str, expr: sp.Expr) -> None:
    value = sp.factor(sp.cancel(sp.simplify(expr)))
    if value != 0:
        raise AssertionError(f"{label}: nonzero symbolic difference = {value}")


def solve_focs() -> None:
    q1, q2, q3 = sp.symbols("q1 q2 q3", real=True)
    c, v = can.c, can.v

    # 1. Complete compatibility: all three firms are compatible and zero-cost.
    Q = q1 + q2 + q3
    foc_complete = [
        sp.Eq(1 - (1 - v) * (Q + q1), 0),
        sp.Eq(1 - (1 - v) * (Q + q2), 0),
        sp.Eq(1 - (1 - v) * (Q + q3), 0),
    ]
    sol = sp.solve(foc_complete, (q1, q2, q3), dict=True)[0]
    for idx, q in enumerate((q1, q2, q3), start=1):
        assert_zero(f"complete q{idx}", sol[q] - can.q_I)

    # 2. SU member market: two compatible zero-cost bloc firms; outsider cost c.
    foc_member = [
        sp.Eq(1 - (1 - v) * (2 * q1 + q2) - q3, 0),
        sp.Eq(1 - (1 - v) * (q1 + 2 * q2) - q3, 0),
        sp.Eq(1 - q1 - q2 - 2 * q3 - c, 0),
    ]
    sol = sp.solve(foc_member, (q1, q2, q3), dict=True)[0]
    assert_zero("SU member q1", sol[q1] - can.q_M)
    assert_zero("SU member q2", sol[q2] - can.q_M)
    assert_zero("SU member outsider q3", sol[q3] - can.q_B)

    # 3. SU outsider market: two compatible bloc firms each cost c; native zero-cost singleton.
    foc_outsider = [
        sp.Eq(1 - c - (1 - v) * (2 * q1 + q2) - q3, 0),
        sp.Eq(1 - c - (1 - v) * (q1 + 2 * q2) - q3, 0),
        sp.Eq(1 - q1 - q2 - 2 * q3, 0),
    ]
    sol = sp.solve(foc_outsider, (q1, q2, q3), dict=True)[0]
    assert_zero("SU outsider bloc q1", sol[q1] - can.q_C)
    assert_zero("SU outsider bloc q2", sol[q2] - can.q_C)
    assert_zero("SU outsider native q3", sol[q3] - can.q_D)

    # 4. Separate national standards: native zero-cost; two foreign firms cost c.
    foc_sw = [
        sp.Eq(1 - 2 * q1 - q2 - q3, 0),
        sp.Eq(1 - q1 - 2 * q2 - q3 - c, 0),
        sp.Eq(1 - q1 - q2 - 2 * q3 - c, 0),
    ]
    sol = sp.solve(foc_sw, (q1, q2, q3), dict=True)[0]
    assert_zero("SW native q1", sol[q1] - can.q_H)
    assert_zero("SW foreign q2", sol[q2] - can.q_S)
    assert_zero("SW foreign q3", sol[q3] - can.q_S)


def verify_blocks() -> None:
    # Profits implied by the FOCs / margins.
    assert_zero("P block", can.P - (1 - can.v) * can.q_I**2)
    assert_zero("A block", can.A - (1 - can.v) * can.q_M**2)
    assert_zero("B block", can.B - can.q_B**2)
    assert_zero("C block", can.C - (1 - can.v) * can.q_C**2)
    assert_zero("D block", can.D - can.q_D**2)
    assert_zero("H block", can.H - can.q_H**2)
    assert_zero("S block", can.S - can.q_S**2)

    totals = can.total_quantities()
    assert_zero("K_I from total quantity", can.K_I - totals["complete"] ** 2 / 2)
    assert_zero("K_M from total quantity", can.K_M - totals["su_member"] ** 2 / 2)
    assert_zero("K_O from total quantity", can.K_O - totals["su_outsider"] ** 2 / 2)
    assert_zero("K_W from total quantity", can.K_W - totals["sw"] ** 2 / 2)


def verify_canonical_identities() -> None:
    c, v, F, delta = can.c, can.v, can.F, can.delta

    # A. Corrected welfare identity.
    expected_w_is = 3 * (5 - 2 * v) / (32 * (1 - v) ** 2)
    assert_zero("corrected W_IS", can.W_IS - expected_w_is)

    # Historical error audit: the old expression overstates corrected welfare by this amount.
    old_w_is = 3 * (5 - v) / (32 * (1 - v) ** 2)
    assert_zero("historical W_IS error size", old_w_is - can.W_IS - 3 * v / (32 * (1 - v) ** 2))

    # B. T_U closed form.
    expected_tu = 3 * c * (2 - c) * (1 - v) / (4 * (2 - 3 * v) ** 2)
    assert_zero("T_U closed form", can.T_U - expected_tu)

    # C. T_W - T_U factorization.
    expected_tw_minus_tu = v * (1 - 2 * c) ** 2 * (8 - 9 * v) / (16 * (2 - 3 * v) ** 2)
    assert_zero("T_W-T_U factorization", can.T_W - can.T_U - expected_tw_minus_tu)

    # D. Selective erosion in the symmetric main model.
    assert_zero(
        "selective erosion before bypass",
        can.W_SU_member_no - can.W_IS - (can.E - can.Drec),
    )
    assert_zero(
        "selective erosion after outsider-only bypass",
        can.W_SU_member_outsider_only - can.W_IS + can.Drec,
    )

    # E. Exact factorization governing reciprocal disadvantage.
    first_factor = 4 * c * (1 - v) - v
    second_factor = 4 * (1 - c) - v * (5 - 4 * c)
    expected_pc = first_factor * second_factor / (16 * (1 - v) * (2 - 3 * v) ** 2)
    assert_zero("P-C factorization", can.P - can.C - expected_pc)

    # Under c < c_upper, second_factor is strictly above its value at c_upper.
    # The boundary value is 8/3 - v > 0 for v < 1/4, so the sign of P-C
    # is exactly the sign of first_factor on the canonical domain.
    boundary_second = sp.simplify(second_factor.subs(c, can.c_upper))
    assert_zero("P-C second factor boundary", boundary_second - (sp.Rational(8, 3) - v))
    assert_zero(
        "reciprocal disadvantage threshold algebra",
        sp.solve(sp.Eq(first_factor, 0), c)[0] - v / (4 * (1 - v)),
    )

    # F. Secondary partner-selection identity.
    assert_zero("partner selection", can.W1_SU12_no - can.W1_SU13_no - delta * (can.A - can.C))

    # G. Low-F accounting under universal effective compatibility.
    constructed_su = can.K_I + 3 * can.P - F
    constructed_sw = can.K_I + 3 * can.P - 2 * F
    assert_zero("low-F SU accounting", constructed_su - (can.W_IS - F))
    assert_zero("low-F SW accounting", constructed_sw - (can.W_IS - 2 * F))


def main() -> int:
    try:
        solve_focs()
        verify_blocks()
        verify_canonical_identities()
    except Exception as exc:  # hard gate: any mismatch is a non-zero exit.
        print("SYMBOLIC VERIFICATION: FAIL")
        print(f"{type(exc).__name__}: {exc}")
        return 1

    print("P-C factorization:")
    print(sp.factor(can.P - can.C))
    print("SYMBOLIC VERIFICATION: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
