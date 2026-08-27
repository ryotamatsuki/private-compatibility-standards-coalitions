"""Symbolic sign-support certificates for canonical welfare inequalities.

The paper proves the signs by concavity in c plus endpoint arguments.  This
script independently verifies every polynomial representation, curvature, and
endpoint identity used by that proof.  It does not replace the analytical sign
argument in the appendix.
"""

from __future__ import annotations

import sys

import sympy as sp

import canonical as can


def assert_zero(label: str, expr: sp.Expr) -> None:
    value = sp.factor(sp.cancel(sp.simplify(expr)))
    if value != 0:
        raise AssertionError(f"{label}: nonzero symbolic difference = {value}")


def main() -> int:
    c, v = can.c, can.v
    cmax = can.c_upper

    try:
        # 1. SU member versus separate national standards.
        n_ms = sp.expand(32 * (2 - 3 * v) ** 2 * (can.W_SU_member_no - can.W_SW))
        target_ms = (
            -216 * c**2 * v**2
            + 264 * c**2 * v
            - 60 * c**2
            + 108 * c * v**2
            - 144 * c * v
            + 56 * c
            - 99 * v**2
            + 84 * v
        )
        assert_zero("SU-member/SW scaled numerator", n_ms - target_ms)
        assert_zero(
            "SU-member/SW curvature",
            sp.diff(n_ms, c, 2) + 24 * (18 * v**2 - 22 * v + 5),
        )
        assert_zero("SU-member/SW c=0 endpoint", n_ms.subs(c, 0) - 3 * v * (28 - 33 * v))
        p_ms = 621 * v**4 - 1206 * v**3 + 729 * v**2 - 92 * v - 36
        assert_zero(
            "SU-member/SW cmax endpoint",
            sp.simplify(n_ms.subs(c, cmax)) + p_ms / (3 * (1 - v) ** 2),
        )
        q_ms = sp.Rational(12285, 16) * v**2 - 92 * v - 36
        assert_zero("SU-member/SW bound endpoint v=1/4", q_ms.subs(v, sp.Rational(1, 4)) + sp.Rational(2819, 256))

        # 2. International standardization versus separate national standards.
        n_is = sp.expand(32 * (1 - v) ** 2 * (can.W_IS - can.W_SW))
        target_is = (
            -28 * c**2 * v**2
            + 56 * c**2 * v
            - 28 * c**2
            + 20 * c * v**2
            - 40 * c * v
            + 20 * c
            - 15 * v**2
            + 24 * v
        )
        assert_zero("IS/SW scaled numerator", n_is - target_is)
        assert_zero("IS/SW curvature", sp.diff(n_is, c, 2) + 56 * (1 - v) ** 2)
        assert_zero("IS/SW c=0 endpoint", n_is.subs(c, 0) - 3 * v * (8 - 5 * v))
        assert_zero(
            "IS/SW cmax endpoint",
            sp.simplify(n_is.subs(c, cmax)) - (32 + 144 * v - 207 * v**2) / 9,
        )

        # 3. International standardization versus the SU outsider.
        n_io = sp.expand(
            32 * (1 - v) ** 2 * (2 - 3 * v) ** 2 * (can.W_IS - can.W_SU_outsider_no)
        )
        target_io = (
            -144 * c**2 * v**4
            + 576 * c**2 * v**3
            - 912 * c**2 * v**2
            + 672 * c**2 * v
            - 192 * c**2
            + 288 * c * v**4
            - 912 * c * v**3
            + 1072 * c * v**2
            - 560 * c * v
            + 112 * c
            - 252 * v**4
            + 666 * v**3
            - 537 * v**2
            + 132 * v
        )
        assert_zero("IS/SU-outsider scaled numerator", n_io - target_io)
        assert_zero(
            "IS/SU-outsider curvature",
            sp.diff(n_io, c, 2) + 96 * (1 - v) ** 2 * (3 * v**2 - 6 * v + 4),
        )
        p0 = 84 * v**3 - 222 * v**2 + 179 * v - 44
        assert_zero("IS/SU-outsider c=0 endpoint", n_io.subs(c, 0) + 3 * v * p0)
        assert_zero("p0 derivative at v=1/4", sp.diff(p0, v).subs(v, sp.Rational(1, 4)) - sp.Rational(335, 4))
        assert_zero("p0 endpoint v=1/4", p0.subs(v, sp.Rational(1, 4)) + sp.Rational(189, 16))
        p1 = 324 * v**4 - 990 * v**3 + 843 * v**2 - 92 * v - 48
        assert_zero("IS/SU-outsider cmax endpoint", sp.simplify(n_io.subs(c, cmax)) + p1 / 3)
        q1 = sp.Rational(3453, 4) * v**2 - 92 * v - 48
        assert_zero("IS/SU-outsider bound endpoint v=1/4", q1.subs(v, sp.Rational(1, 4)) + sp.Rational(1091, 64))

    except Exception as exc:
        print("WELFARE SIGN CERTIFICATES: FAIL")
        print(f"{type(exc).__name__}: {exc}")
        return 1

    print("SU-MEMBER > SW SIGN SUPPORT: PASS")
    print("IS > SW SIGN SUPPORT: PASS")
    print("IS > SU-OUTSIDER SIGN SUPPORT: PASS")
    print("WELFARE SIGN CERTIFICATES: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
