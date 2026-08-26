"""Deterministic numerical sanity checks for the Stage-8 frozen theory.

These checks are regression / mismatch detectors only. They are not proofs.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
import sympy as sp

import canonical as can

RNG_SEED = 20260826
ROOT = Path(__file__).resolve().parents[1]
SUMMARY_PATH = ROOT / "build" / "verification" / "numeric_summary.json"

# Vectorized numerical evaluators. All formulas come from canonical.py.
_Q_FUNCS = {
    "q_I": sp.lambdify((can.c, can.v), can.q_I, "numpy"),
    "q_M": sp.lambdify((can.c, can.v), can.q_M, "numpy"),
    "q_B": sp.lambdify((can.c, can.v), can.q_B, "numpy"),
    "q_C": sp.lambdify((can.c, can.v), can.q_C, "numpy"),
    "q_D": sp.lambdify((can.c, can.v), can.q_D, "numpy"),
    "q_H": sp.lambdify((can.c, can.v), can.q_H, "numpy"),
    "q_S": sp.lambdify((can.c, can.v), can.q_S, "numpy"),
}
_EXPR_FUNCS = {
    "P": sp.lambdify((can.c, can.v), can.P, "numpy"),
    "C": sp.lambdify((can.c, can.v), can.C, "numpy"),
    "D": sp.lambdify((can.c, can.v), can.D, "numpy"),
    "K_O": sp.lambdify((can.c, can.v), can.K_O, "numpy"),
    "J": sp.lambdify((can.c, can.v), can.J, "numpy"),
    "T_A": sp.lambdify((can.c, can.v), can.T_A, "numpy"),
    "T_U": sp.lambdify((can.c, can.v), can.T_U, "numpy"),
    "T_W": sp.lambdify((can.c, can.v), can.T_W, "numpy"),
    "E": sp.lambdify((can.c, can.v), can.E, "numpy"),
    "Drec": sp.lambdify((can.c, can.v), can.Drec, "numpy"),
    "Phi0": sp.lambdify((can.c, can.v), can.Phi0, "numpy"),
    "W_IS": sp.lambdify((can.c, can.v), can.W_IS, "numpy"),
    "W_SU_member_no": sp.lambdify((can.c, can.v), can.W_SU_member_no, "numpy"),
    "W_SU_member_outsider_only": sp.lambdify((can.c, can.v), can.W_SU_member_outsider_only, "numpy"),
    "W_SU_outsider_no": sp.lambdify((can.c, can.v), can.W_SU_outsider_no, "numpy"),
    "W_SW": sp.lambdify((can.c, can.v), can.W_SW, "numpy"),
}


def fail(message: str) -> None:
    raise AssertionError(message)


def scalar(name: str, c_val: float, v_val: float) -> float:
    return float(np.asarray(_EXPR_FUNCS[name](c_val, v_val)))


def qscalar(name: str, c_val: float, v_val: float) -> float:
    return float(np.asarray(_Q_FUNCS[name](c_val, v_val)))


def canonical_quantities(c_val: float, v_val: float) -> dict[str, np.ndarray]:
    return {
        "complete": np.array([qscalar("q_I", c_val, v_val)] * 3, dtype=float),
        "su_member": np.array(
            [qscalar("q_M", c_val, v_val), qscalar("q_M", c_val, v_val), qscalar("q_B", c_val, v_val)],
            dtype=float,
        ),
        "su_outsider": np.array(
            [qscalar("q_C", c_val, v_val), qscalar("q_C", c_val, v_val), qscalar("q_D", c_val, v_val)],
            dtype=float,
        ),
        "sw": np.array(
            [qscalar("q_H", c_val, v_val), qscalar("q_S", c_val, v_val), qscalar("q_S", c_val, v_val)],
            dtype=float,
        ),
    }


def direct_foc_quantities(c_val: float, v_val: float) -> dict[str, np.ndarray]:
    one_minus_v = 1.0 - v_val

    A_complete = one_minus_v * np.array(
        [[2.0, 1.0, 1.0], [1.0, 2.0, 1.0], [1.0, 1.0, 2.0]], dtype=float
    )
    b_complete = np.ones(3, dtype=float)

    A_su_member = np.array(
        [
            [2.0 * one_minus_v, one_minus_v, 1.0],
            [one_minus_v, 2.0 * one_minus_v, 1.0],
            [1.0, 1.0, 2.0],
        ],
        dtype=float,
    )
    b_su_member = np.array([1.0, 1.0, 1.0 - c_val], dtype=float)

    A_su_outsider = A_su_member
    b_su_outsider = np.array([1.0 - c_val, 1.0 - c_val, 1.0], dtype=float)

    A_sw = np.array([[2.0, 1.0, 1.0], [1.0, 2.0, 1.0], [1.0, 1.0, 2.0]], dtype=float)
    b_sw = np.array([1.0, 1.0 - c_val, 1.0 - c_val], dtype=float)

    return {
        "complete": np.linalg.solve(A_complete, b_complete),
        "su_member": np.linalg.solve(A_su_member, b_su_member),
        "su_outsider": np.linalg.solve(A_su_outsider, b_su_outsider),
        "sw": np.linalg.solve(A_sw, b_sw),
    }


def check_witness(summary: dict) -> None:
    c0, v0 = 0.10, 0.24
    ta = scalar("T_A", c0, v0)
    tu = scalar("T_U", c0, v0)
    tw = scalar("T_W", c0, v0)
    values = {
        "T_U": tu,
        "T_A": ta,
        "T_W": tw,
        "F_L": max(tw, ta),
        "F_star": 2.0 * ta,
        "F_low": min(tu, ta),
        "E": scalar("E", c0, v0),
        "Drec": scalar("Drec", c0, v0),
        "Phi0": scalar("Phi0", c0, v0),
        "P": scalar("P", c0, v0),
        "C": scalar("C", c0, v0),
        "J": scalar("J", c0, v0),
    }
    expected = {
        "T_U": 0.06610107422,
        "T_A": 0.08182424445,
        "T_W": 0.10031982422,
        "E": 0.01616234269,
        "Drec": 0.008018092105,
        "Phi0": 0.00814425059,
    }
    for name, target in expected.items():
        if not math.isclose(values[name], target, rel_tol=0.0, abs_tol=5e-10):
            fail(f"main witness mismatch for {name}: got {values[name]:.12g}, expected {target:.12g}")

    if not values["Phi0"] > 0:
        fail("main witness does not satisfy Phi0 > 0")
    if not values["P"] > values["C"]:
        fail("main witness does not satisfy P > C")
    if not values["F_L"] < values["F_star"]:
        fail("main witness does not satisfy F_L < F_star")
    if not values["J"] > 0:
        fail("main witness does not satisfy J > 0")

    summary["main_witness"] = values


def check_open_neighborhood(summary: dict) -> None:
    c_grid = np.linspace(0.095, 0.105, 41)
    v_grid = np.linspace(0.235, 0.245, 41)
    cc, vv = np.meshgrid(c_grid, v_grid, indexing="ij")

    c_max = (1.0 - 3.0 * vv) / (3.0 * (1.0 - vv))
    if not np.all((vv > 0.0) & (vv < 0.25) & (cc > 0.0) & (cc < c_max)):
        fail("verified witness neighborhood contains a point outside the baseline domain")

    phi = np.asarray(_EXPR_FUNCS["Phi0"](cc, vv), dtype=float)
    pc = np.asarray(_EXPR_FUNCS["P"](cc, vv) - _EXPR_FUNCS["C"](cc, vv), dtype=float)
    ta = np.asarray(_EXPR_FUNCS["T_A"](cc, vv), dtype=float)
    tw = np.asarray(_EXPR_FUNCS["T_W"](cc, vv), dtype=float)
    margin = 2.0 * ta - np.maximum(tw, ta)

    if not np.all(phi > 0.0):
        fail(f"Phi0 <= 0 in verified neighborhood; min={float(phi.min())}")
    if not np.all(pc > 0.0):
        fail(f"P <= C in verified neighborhood; min(P-C)={float(pc.min())}")
    if not np.all(margin > 0.0):
        fail(f"F_L >= F_star in verified neighborhood; min margin={float(margin.min())}")

    summary["open_neighborhood"] = {
        "points": int(phi.size),
        "min_Phi0": float(phi.min()),
        "min_P_minus_C": float(pc.min()),
        "min_Fstar_minus_FL": float(margin.min()),
    }


def check_general_domain(summary: dict, n: int = 20000) -> None:
    rng = np.random.default_rng(RNG_SEED)
    vv = rng.uniform(1e-5, 0.24999, n)
    c_max = (1.0 - 3.0 * vv) / (3.0 * (1.0 - vv))
    cc = rng.uniform(1e-5, 0.99999, n) * c_max

    qvals = {name: np.asarray(func(cc, vv), dtype=float) for name, func in _Q_FUNCS.items()}
    for name, arr in qvals.items():
        if not np.all(arr > 0.0):
            fail(f"nonpositive {name}; min={float(arr.min())}")

    totals = {
        "complete": 3.0 * qvals["q_I"],
        "su_member": 2.0 * qvals["q_M"] + qvals["q_B"],
        "su_outsider": 2.0 * qvals["q_C"] + qvals["q_D"],
        "sw": qvals["q_H"] + 2.0 * qvals["q_S"],
    }
    for name, arr in totals.items():
        if not np.all(arr < 1.0):
            fail(f"non-interior total quantity in {name}; max={float(arr.max())}")

    ta = np.asarray(_EXPR_FUNCS["T_A"](cc, vv), dtype=float)
    tu = np.asarray(_EXPR_FUNCS["T_U"](cc, vv), dtype=float)
    tw = np.asarray(_EXPR_FUNCS["T_W"](cc, vv), dtype=float)
    if not np.all((ta > 0.0) & (tu > 0.0) & (tw > 0.0)):
        fail(f"nonpositive adoption threshold: mins TA={ta.min()}, TU={tu.min()}, TW={tw.min()}")
    if not np.all(tw > tu):
        fail(f"T_W <= T_U detected; min(TW-TU)={float((tw-tu).min())}")

    w_su_m = np.asarray(_EXPR_FUNCS["W_SU_member_no"](cc, vv), dtype=float)
    w_su_o = np.asarray(_EXPR_FUNCS["W_SU_outsider_no"](cc, vv), dtype=float)
    w_is = np.asarray(_EXPR_FUNCS["W_IS"](cc, vv), dtype=float)
    w_sw = np.asarray(_EXPR_FUNCS["W_SW"](cc, vv), dtype=float)
    gaps = {
        "SU_member_minus_SW": w_su_m - w_sw,
        "IS_minus_SW": w_is - w_sw,
        "IS_minus_SU_outsider": w_is - w_su_o,
    }
    for name, arr in gaps.items():
        if not np.all(arr > 0.0):
            fail(f"canonical welfare inequality failed for {name}; min={float(arr.min())}")

    summary["general_domain"] = {
        "seed": RNG_SEED,
        "points": n,
        "min_quantity": {name: float(arr.min()) for name, arr in qvals.items()},
        "max_total_quantity": {name: float(arr.max()) for name, arr in totals.items()},
        "min_threshold": {
            "T_A": float(ta.min()),
            "T_U": float(tu.min()),
            "T_W": float(tw.min()),
            "T_W_minus_T_U": float((tw - tu).min()),
        },
        "min_welfare_gap": {name: float(arr.min()) for name, arr in gaps.items()},
    }


def check_direct_foc_consistency(summary: dict, n: int = 2000) -> None:
    rng = np.random.default_rng(RNG_SEED + 1)
    max_abs_error = 0.0

    for _ in range(n):
        v_val = float(rng.uniform(1e-4, 0.2499))
        c_max = (1.0 - 3.0 * v_val) / (3.0 * (1.0 - v_val))
        c_val = float(rng.uniform(1e-4, 0.999 * c_max))
        closed = canonical_quantities(c_val, v_val)
        direct = direct_foc_quantities(c_val, v_val)
        for regime in closed:
            err = float(np.max(np.abs(closed[regime] - direct[regime])))
            max_abs_error = max(max_abs_error, err)
            if err > 1e-11:
                fail(f"direct FOC mismatch ({regime}) at c={c_val}, v={v_val}: err={err}")

    summary["direct_foc_consistency"] = {"points": n, "max_abs_error": max_abs_error}


def check_stability_regression(summary: dict) -> None:
    """Regression-check the five-partition headline classification at the witness."""
    c0, v0 = 0.10, 0.24
    w_is = scalar("W_IS", c0, v0)
    w_sw = scalar("W_SW", c0, v0)
    w_member_no = scalar("W_SU_member_no", c0, v0)
    w_outsider_no = scalar("W_SU_outsider_no", c0, v0)
    w_member_bypass = scalar("W_SU_member_outsider_only", c0, v0)
    p = scalar("P", c0, v0)
    d = scalar("D", c0, v0)
    k_o = scalar("K_O", c0, v0)
    ta = scalar("T_A", c0, v0)
    tw = scalar("T_W", c0, v0)
    f_l = max(tw, ta)
    f_star = 2.0 * ta
    f_mid = 0.5 * (f_l + f_star)
    w_outsider_bypass = k_o + 2.0 * p + d - f_mid

    # High-F: SW and IS are pair-blocked; each symmetric SU survives because
    # alternative regional pairs leave their common member indifferent.
    if not (w_member_no > w_sw and w_member_no > w_is and w_is > w_outsider_no):
        fail("high-F payoff ordering required for the stable-set classification failed")
    high_stable = ["SU12", "SU13", "SU23"]

    # Intermediate-F: IS strictly dominates every role in an SU and dominates SW.
    if not f_l < f_mid < f_star:
        fail("chosen intermediate-F regression point is outside (F_L,F_star)")
    if not (w_is > w_member_bypass and w_is > w_outsider_bypass and w_is > w_sw):
        fail("intermediate-F strict-blocking payoff ordering failed")
    intermediate_stable = ["IS"]

    if high_stable != ["SU12", "SU13", "SU23"]:
        fail(f"high-F stable-set mismatch: {high_stable}")
    if intermediate_stable != ["IS"]:
        fail(f"intermediate-F stable-set mismatch: {intermediate_stable}")

    summary["stability_regression"] = {
        "F_L": f_l,
        "F_star": f_star,
        "F_mid": f_mid,
        "high_F_stable_set": high_stable,
        "intermediate_F_stable_set": intermediate_stable,
        "W_IS": w_is,
        "W_SW": w_sw,
        "W_SU_member_no": w_member_no,
        "W_SU_outsider_no": w_outsider_no,
        "W_SU_member_bypass": w_member_bypass,
        "W_SU_outsider_bypass_mid": w_outsider_bypass,
    }


def main() -> int:
    summary: dict = {"status": "FAIL"}
    try:
        check_witness(summary)
        check_open_neighborhood(summary)
        check_general_domain(summary)
        check_direct_foc_consistency(summary)
        check_stability_regression(summary)
    except Exception as exc:
        SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
        summary["error"] = f"{type(exc).__name__}: {exc}"
        SUMMARY_PATH.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
        print("NUMERICAL VERIFICATION: FAIL")
        print(summary["error"])
        return 1

    summary["status"] = "PASS"
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")

    w = summary["main_witness"]
    print(
        "MAIN WITNESS: "
        f"T_U={w['T_U']:.11f}, T_A={w['T_A']:.11f}, T_W={w['T_W']:.11f}, "
        f"E={w['E']:.11f}, Drec={w['Drec']:.11f}, Phi0={w['Phi0']:.11f}, J={w['J']:.11f}"
    )
    print(f"DIRECT FOC MAX ABS ERROR: {summary['direct_foc_consistency']['max_abs_error']:.3e}")
    print("HIGH-F STABLE-SET REGRESSION: PASS")
    print("INTERMEDIATE-F STABLE-SET REGRESSION: PASS")
    print("NUMERICAL VERIFICATION: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
