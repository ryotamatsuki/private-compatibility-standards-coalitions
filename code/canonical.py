"""Canonical machine-readable formulas for the Stage-8 frozen theory.

This module mirrors docs/CANONICAL_MODEL.md. It is the only Python-side source
for formulas used by verification, figure generation, and table generation.
Do not add extensions here without an explicit theory-repair stage.
"""

from __future__ import annotations

import sympy as sp

# Primitive symbols
c, v, F, delta = sp.symbols("c v F delta", positive=True, real=True)

# Canonical admissible upper bound for c in the symmetric main model.
c_upper = (1 - 3 * v) / (3 * (1 - v))

# ---------------------------------------------------------------------------
# Cournot quantities
# ---------------------------------------------------------------------------
q_I = 1 / (4 * (1 - v))

q_M = (1 + c) / (2 * (2 - 3 * v))
q_B = (1 - 3 * c - 3 * (1 - c) * v) / (2 * (2 - 3 * v))

q_C = (1 - 2 * c) / (2 * (2 - 3 * v))
q_D = (1 + 2 * c - 3 * v) / (2 * (2 - 3 * v))

q_H = (1 + 2 * c) / 4
q_S = (1 - 2 * c) / 4

# ---------------------------------------------------------------------------
# Profit blocks
# ---------------------------------------------------------------------------
P = 1 / (16 * (1 - v))

A = (1 - v) * (1 + c) ** 2 / (4 * (2 - 3 * v) ** 2)
B = (1 - 3 * c - 3 * (1 - c) * v) ** 2 / (4 * (2 - 3 * v) ** 2)

C = (1 - v) * (1 - 2 * c) ** 2 / (4 * (2 - 3 * v) ** 2)
D = (1 + 2 * c - 3 * v) ** 2 / (4 * (2 - 3 * v) ** 2)

H = (1 + 2 * c) ** 2 / 16
S = (1 - 2 * c) ** 2 / 16

# ---------------------------------------------------------------------------
# Consumer-surplus blocks
# ---------------------------------------------------------------------------
K_I = 9 / (32 * (1 - v) ** 2)
K_M = (3 - c - 3 * v + 3 * c * v) ** 2 / (8 * (2 - 3 * v) ** 2)
K_O = (3 - 2 * c - 3 * v) ** 2 / (8 * (2 - 3 * v) ** 2)
K_W = (3 - 2 * c) ** 2 / 32

# ---------------------------------------------------------------------------
# Government welfare: symmetric main model, no private bypass unless noted
# ---------------------------------------------------------------------------
W_IS = sp.simplify(K_I + 3 * P)
W_SU_member_no = sp.simplify(K_M + 2 * A + C)
W_SU_outsider_no = sp.simplify(K_O + 2 * B + D)
W_SW = sp.simplify(K_W + H + 2 * S)

# SU member welfare after outsider-only bypass in the symmetric main model.
W_SU_member_outsider_only = sp.simplify(K_I + 2 * P + C)

# ---------------------------------------------------------------------------
# Private-adoption thresholds
# ---------------------------------------------------------------------------
T_A = sp.simplify(P - B)
T_U = sp.simplify(A - C)
T_W = sp.simplify(A - S)
F_L = sp.Max(T_W, T_A)
F_star = sp.simplify(2 * T_A)
F_low = sp.Min(T_U, T_A)

# ---------------------------------------------------------------------------
# Selective-erosion decomposition: symmetric main model
# ---------------------------------------------------------------------------
E = sp.simplify((K_M - K_I) + 2 * (A - P))
Drec = sp.simplify(P - C)
Phi0 = sp.simplify(E - Drec)

# ---------------------------------------------------------------------------
# Secondary market-size branch: firm/country 1 as a coalition member
# ---------------------------------------------------------------------------
W1_SU12_no = sp.simplify(K_M + 2 * A + (1 - delta) * C)
W1_SU13_no = sp.simplify(K_M + (2 - delta) * A + C)

# ---------------------------------------------------------------------------
# Low-F universal-multistandarding accounting
# ---------------------------------------------------------------------------
W_SU_universal = sp.simplify(W_IS - F)
W_SW_universal = sp.simplify(W_IS - 2 * F)

# Useful derived object from Stage 8 (not a separate theorem here).
J = sp.simplify(K_I + P - K_O - D)

# Verified main witness used only for numerical verification / illustration.
MAIN_WITNESS = {c: sp.Rational(1, 10), v: sp.Rational(6, 25)}  # (0.10, 0.24)


def total_quantities() -> dict[str, sp.Expr]:
    """Total market quantity for each canonical product-market subgame."""
    return {
        "complete": sp.simplify(3 * q_I),
        "su_member": sp.simplify(2 * q_M + q_B),
        "su_outsider": sp.simplify(2 * q_C + q_D),
        "sw": sp.simplify(q_H + 2 * q_S),
    }


def witness_values() -> dict[str, float]:
    """Evaluate the key Stage-8 witness objects at (c,v)=(0.10,0.24)."""
    exprs = {
        "T_U": T_U,
        "T_A": T_A,
        "T_W": T_W,
        "F_L": F_L,
        "F_star": F_star,
        "F_low": F_low,
        "E": E,
        "Drec": Drec,
        "Phi0": Phi0,
        "P": P,
        "C": C,
    }
    return {name: float(sp.N(expr.subs(MAIN_WITNESS), 17)) for name, expr in exprs.items()}

# Controlled paper-facing LaTeX renderings. These strings preserve the frozen
# notation in docs/CANONICAL_MODEL.md and prevent SymPy from rewriting benign
# factors as (v-1) or (3v-2) in generated tables.
LATEX_FORMULAS = {
    "q_I": r"\frac{1}{4(1-v)}",
    "q_M": r"\frac{1+c}{2(2-3v)}",
    "q_B": r"\frac{1-3c-3(1-c)v}{2(2-3v)}",
    "q_C": r"\frac{1-2c}{2(2-3v)}",
    "q_D": r"\frac{1+2c-3v}{2(2-3v)}",
    "q_H": r"\frac{1+2c}{4}",
    "q_S": r"\frac{1-2c}{4}",
    "P": r"\frac{1}{16(1-v)}",
    "A": r"\frac{(1-v)(1+c)^2}{4(2-3v)^2}",
    "B": r"\frac{[1-3c-3(1-c)v]^2}{4(2-3v)^2}",
    "C": r"\frac{(1-v)(1-2c)^2}{4(2-3v)^2}",
    "D": r"\frac{(1+2c-3v)^2}{4(2-3v)^2}",
    "H": r"\frac{(1+2c)^2}{16}",
    "S": r"\frac{(1-2c)^2}{16}",
    "K_I": r"\frac{9}{32(1-v)^2}",
    "K_M": r"\frac{(3-c-3v+3cv)^2}{8(2-3v)^2}",
    "K_O": r"\frac{(3-2c-3v)^2}{8(2-3v)^2}",
    "K_W": r"\frac{(3-2c)^2}{32}",
    "T_A": r"P-B",
    "T_U": r"\frac{3c(2-c)(1-v)}{4(2-3v)^2}",
    "T_W": r"A-S",
    "F_low": r"\min\{T_U,T_A\}",
    "F_L": r"\max\{T_W,T_A\}",
    "F_star": r"2T_A",
}
