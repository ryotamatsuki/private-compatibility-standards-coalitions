"""Generate reproducible manuscript figures.

The figures illustrate certified analytical results. They are not proofs.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

import canonical as can

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "paper" / "figures" / "generated"
PDF_METADATA = {"Creator": "make_figures.py", "CreationDate": None, "ModDate": None}


def save(fig: plt.Figure, filename: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / filename
    fig.savefig(path, format="pdf", bbox_inches="tight", metadata=PDF_METADATA)
    plt.close(fig)
    print(f"generated {path.relative_to(ROOT)}")


def timing_figure() -> None:
    fig, ax = plt.subplots(figsize=(10.5, 2.2))
    ax.set_axis_off()

    xs = [0.08, 0.29, 0.50, 0.71, 0.92]
    labels = [
        "Formal coalition\n$\\rho$",
        "Private adoption\n$a^*(\\rho,F)$",
        "Product-market\ncompetition",
        "Government welfare\n$W_i$",
        "Coalition stability\n$\\mathcal{S}(F)$",
    ]
    for x, label in zip(xs, labels, strict=True):
        ax.text(
            x,
            0.5,
            label,
            transform=ax.transAxes,
            ha="center",
            va="center",
            fontsize=10,
            bbox={"boxstyle": "round,pad=0.45"},
        )
    for left, right in zip(xs[:-1], xs[1:], strict=True):
        ax.annotate(
            "",
            xy=(right - 0.075, 0.5),
            xytext=(left + 0.075, 0.5),
            xycoords=ax.transAxes,
            textcoords=ax.transAxes,
            arrowprops={"arrowstyle": "->", "linewidth": 1.2},
        )
    ax.text(
        0.5,
        0.08,
        "Formal membership is fixed before firms choose private adaptation.",
        transform=ax.transAxes,
        ha="center",
        fontsize=9,
    )
    save(fig, "figure_01_timing.pdf")


def residual_rent_figure() -> None:
    """Illustrate all three R(d,v) regions with one admissible parameterization."""
    c = 0.073
    v = 0.225

    P = 1.0 / (16.0 * (1.0 - v))
    A = (1.0 - v) * (1.0 + c) ** 2 / (4.0 * (2.0 - 3.0 * v) ** 2)
    C = (1.0 - v) * (1.0 - 2.0 * c) ** 2 / (4.0 * (2.0 - 3.0 * v) ** 2)
    KI = 9.0 / (32.0 * (1.0 - v) ** 2)
    KM = (3.0 - c - 3.0 * v + 3.0 * c * v) ** 2 / (8.0 * (2.0 - 3.0 * v) ** 2)
    E = (KM - KI) + 2.0 * (A - P)
    D = P - C

    def residual(d: float) -> float:
        return d * ((5.0 - 4.0 * v) * d + 2.0 * (1.0 - 4.0 * v)) / (
            32.0 * (1.0 - v) ** 2
        )

    def root_for(z: float) -> float:
        return (
            -(1.0 - 4.0 * v)
            + (
                (1.0 - 4.0 * v) ** 2
                + 32.0 * (5.0 - 4.0 * v) * (1.0 - v) ** 2 * z
            )
            ** 0.5
        ) / (5.0 - 4.0 * v)

    d_d = root_for(D)
    d_e = root_for(E)
    xs = [c * i / 250.0 for i in range(251)]
    ys = [residual(x) for x in xs]

    fig, ax = plt.subplots(figsize=(10.5, 4.2))
    ax.plot(xs, ys, linewidth=1.6, label=r"$R(d,v)$")
    ax.axhline(D, linewidth=1.0, linestyle="--", label=r"$\mathcal{D}$")
    ax.axhline(E, linewidth=1.0, linestyle=":", label=r"$\mathcal{E}$")
    ax.axvline(d_d, linewidth=0.9)
    ax.axvline(d_e, linewidth=0.9)

    ax.text(d_d / 2, E * 1.10, "ranking\nreversal", ha="center", va="bottom", fontsize=9)
    ax.text((d_d + d_e) / 2, E * 1.10, "IS incentive strengthens\nwithout reversal", ha="center", va="bottom", fontsize=9)
    ax.text((d_e + c) / 2, E * 1.10, "IS incentive\nweakens", ha="center", va="bottom", fontsize=9)

    ax.set_xlim(0.0, c)
    ax.set_ylim(0.0, max(ys[-1], E) * 1.38)
    ax.set_xlabel(r"Residual marginal adaptation cost $d$")
    ax.set_ylabel("Residual member-market rent")
    ax.legend(loc="upper left", fontsize=9)
    ax.text(
        c / 2,
        -0.00030,
        r"Illustration: $(c,v)=(0.073,0.225)$. Analytical boundaries are $R=\mathcal{D}$ and $R=\mathcal{E}$.",
        ha="center",
        va="top",
        fontsize=8.8,
    )
    save(fig, "figure_02_selective_erosion.pdf")


def f_region_figure() -> None:
    w = can.witness_values()
    f_l = w["F_L"]
    f_star = w["F_star"]
    x_max = 1.24 * f_star

    fig, ax = plt.subplots(figsize=(11.2, 3.6))
    ax.set_xlim(0.0, x_max)
    ax.set_ylim(-0.36, 1.08)
    ax.set_yticks([])
    ax.spines[["left", "right", "top"]].set_visible(False)
    ax.spines["bottom"].set_position(("data", 0.0))
    ax.set_xlabel(r"Private compatibility fixed cost $F$")

    for x, symbol, numeric in [
        (f_l, r"$F_L=\max\{T_W,T_A\}$", f_l),
        (f_star, r"$F^*=2T_A$", f_star),
    ]:
        ax.axvline(x, ymin=0.22, ymax=0.80, linewidth=1.0)
        ax.text(x, 0.88, symbol + f"\n{numeric:.4f}", ha="center", va="bottom", fontsize=9)

    segments = [
        (0.0, f_l, "Lower-$F$ cases\noutside application"),
        (f_l, f_star, "Outsider-only SU adoption\nIS uniquely stable"),
        (f_star, x_max, "No SU/SW adoption\nthree SUs stable under\nstrict blocking"),
    ]
    for left, right, label in segments:
        ax.text((left + right) / 2, 0.36, label, ha="center", va="center", fontsize=9)

    ax.text(
        x_max / 2,
        -0.27,
        r"Full-bypass application at $(c,v)=(0.10,0.24)$; numerical illustration only.",
        ha="center",
        va="center",
        fontsize=9,
    )
    save(fig, "figure_03_f_regions.pdf")


def assumption_dependence_figure() -> None:
    """Conceptual hierarchy of which results survive which checks."""
    fig, ax = plt.subplots(figsize=(10.8, 4.8))
    ax.set_axis_off()

    rows = [
        ("One-way private adoption", "survives $v=0$, S1 witness, and R5 witnesses"),
        ("Initial SU advantage / political effect", "fails at $v=0$, under S1, and in frozen R5 demand"),
        ("Intermediate unique-IS application", "survives strict/weak blocking and certified small asymmetry"),
        ("Symmetric high-$F$ SU multiplicity", "fails under weak blocking; symmetry sensitive"),
    ]
    ys = [0.82, 0.62, 0.39, 0.18]

    for (title, detail), y in zip(rows, ys, strict=True):
        ax.text(
            0.18,
            y,
            title,
            transform=ax.transAxes,
            ha="center",
            va="center",
            fontsize=10,
            bbox={"boxstyle": "round,pad=0.45"},
        )
        ax.annotate(
            "",
            xy=(0.41, y),
            xytext=(0.31, y),
            xycoords=ax.transAxes,
            textcoords=ax.transAxes,
            arrowprops={"arrowstyle": "->", "linewidth": 1.1},
        )
        ax.text(
            0.44,
            y,
            detail,
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=9.5,
        )

    ax.text(
        0.5,
        0.96,
        "Robustness hierarchy",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=12,
    )
    ax.text(
        0.5,
        0.04,
        "Each statement is scoped to the pre-specified check reported in the paper; no universal robustness claim is implied.",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=8.8,
    )
    save(fig, "figure_04_assumption_dependence.pdf")


def main() -> None:
    print("Figure 1: timing.")
    timing_figure()
    print("Figure 2: residual-rent government-incentive regions.")
    residual_rent_figure()
    print("Figure 3: full-bypass fixed-cost application.")
    f_region_figure()
    print("Figure 4: assumption-dependence hierarchy.")
    assumption_dependence_figure()
    print("FIGURE GENERATION: PASS")


if __name__ == "__main__":
    main()
