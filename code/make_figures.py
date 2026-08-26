"""Generate reproducible manuscript figures from the frozen canonical model.

The figures are infrastructure / illustrations only. They are not proofs.
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
    """Conceptual illustration: the five-stage game timing."""
    fig, ax = plt.subplots(figsize=(10.5, 2.2))
    ax.set_axis_off()

    xs = [0.08, 0.29, 0.50, 0.71, 0.92]
    labels = [
        "Formal coalition\n$\\rho$",
        "Private adoption\n$a^*(\\rho,F)$",
        "Cournot competition\n$q^*$",
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
    ax.text(0.5, 0.08, "Conceptual timing diagram", transform=ax.transAxes, ha="center", fontsize=9)
    save(fig, "figure_01_timing.pdf")


def selective_erosion_figure() -> None:
    """Conceptual illustration of E-D -> -D; not a numerical proof."""
    fig, ax = plt.subplots(figsize=(10.5, 3.2))
    ax.set_axis_off()

    ax.text(
        0.22,
        0.65,
        r"Before bypass" + "\n" + r"$+\mathscr{E}_i-\mathscr{D}_i>0$",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=14,
        bbox={"boxstyle": "round,pad=0.6"},
    )
    ax.text(
        0.22,
        0.27,
        r"$+\mathscr{E}_i$: member-market exclusion surplus" + "\n" + r"$-\mathscr{D}_i$: reciprocal outsider-market disadvantage",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=9.5,
    )

    ax.text(
        0.78,
        0.65,
        r"After outsider-only bypass" + "\n" + r"$-\mathscr{D}_i<0$",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=14,
        bbox={"boxstyle": "round,pad=0.6"},
    )
    ax.text(
        0.78,
        0.27,
        r"$\mathscr{E}_i$ is removed" + "\n" + r"$\mathscr{D}_i$ remains",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=10,
    )

    ax.annotate(
        "",
        xy=(0.60, 0.65),
        xytext=(0.40, 0.65),
        xycoords=ax.transAxes,
        textcoords=ax.transAxes,
        arrowprops={"arrowstyle": "->", "linewidth": 1.4},
    )
    ax.text(
        0.50,
        0.79,
        "Private compatibility bypass",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=10,
    )
    ax.text(
        0.5,
        0.05,
        "Conceptual illustration only; the ranking reversal is proved analytically.",
        transform=ax.transAxes,
        ha="center",
        fontsize=9,
    )
    save(fig, "figure_02_selective_erosion.pdf")


def f_region_figure() -> None:
    """Numerical illustration of the headline Theorem-2 F regions at the frozen witness."""
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
        (0.0, f_l, "Outside headline theorem\n(boundaries / lower-$F$ cases\nnot characterized here)"),
        (f_l, f_star, "Intermediate region\nOutsider-only SU bypass\nIS uniquely stable"),
        (f_star, x_max, "High-$F$ region\nNo SU/SW adoption\nThree regional SUs stable"),
    ]
    for left, right, label in segments:
        ax.text((left + right) / 2, 0.36, label, ha="center", va="center", fontsize=9)

    ax.text(
        x_max / 2,
        -0.27,
        r"Verified witness: $(c,v)=(0.10,0.24)$. Numerical illustration of Theorem 2; not a proof.",
        ha="center",
        va="center",
        fontsize=9,
    )
    save(fig, "figure_03_f_regions.pdf")


def main() -> None:
    print("Figure 1 purpose: conceptual game timing (conceptual illustration).")
    timing_figure()
    print("Figure 2 purpose: selective-erosion mechanism (conceptual illustration).")
    selective_erosion_figure()
    print("Figure 3 purpose: headline stability regions at the verified witness (numerical illustration).")
    f_region_figure()
    print("FIGURE GENERATION: PASS")


if __name__ == "__main__":
    main()
