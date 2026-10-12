"""Reproducible, uncluttered figure for the JICT short manuscript only.

Never overwrite the certified R9 full-manuscript figure. This is an
illustration of previously certified analytic thresholds, not a proof.
"""
from __future__ import annotations

from pathlib import Path
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "paper" / "jict_short" / "generated"
C, V = 0.073, 0.225


def main() -> None:
    c, v = C, V
    P = 1 / (16 * (1 - v))
    A = (1 - v) * (1 + c) ** 2 / (4 * (2 - 3 * v) ** 2)
    Cprofit = (1 - v) * (1 - 2 * c) ** 2 / (4 * (2 - 3 * v) ** 2)
    KI = 9 / (32 * (1 - v) ** 2)
    KM = (3 - c - 3 * v + 3 * c * v) ** 2 / (8 * (2 - 3 * v) ** 2)
    E = KM - KI + 2 * (A - P)
    D = P - Cprofit

    def residual(d: float) -> float:
        return d * ((5 - 4 * v) * d + 2 * (1 - 4 * v)) / (32 * (1 - v) ** 2)

    def root(level: float) -> float:
        return (-(1 - 4 * v) + math.sqrt(
            (1 - 4 * v) ** 2 + 32 * (5 - 4 * v) * (1 - v) ** 2 * level
        )) / (5 - 4 * v)

    dD, dE = root(D), root(E)
    if not 0 < dD < dE < c:
        raise ValueError("Figure illustration does not exhibit the certified three regimes")

    xs = [i * c / 500 for i in range(501)]
    fig, ax = plt.subplots(figsize=(8.0, 3.35))
    ax.plot(xs, [residual(x) for x in xs], linewidth=1.9, label=r"$R(d,v)$")
    ax.axhline(D, linestyle="--", color="0.35", linewidth=1.15, label=r"$\mathcal{D}$")
    ax.axhline(E, linestyle=":", color="0.45", linewidth=1.15, label=r"$\mathcal{E}$")
    ax.axvline(dD, linewidth=0.85, linestyle="-.", color="0.45")
    ax.axvline(dE, linewidth=0.85, linestyle="-.", color="0.45")
    ax.set_xlim(0, c)
    ax.set_ylim(0, max(residual(c), E) * 1.18)
    ax.set_xlabel(r"Residual adaptation cost $d$", labelpad=8)
    ax.set_ylabel(r"Residual rent $R(d,v)$", labelpad=7)
    ax.set_xticks([0, dD, dE, c],
                  [r"$0$", r"$d_{\mathcal{D}}$", r"$d_{\mathcal{E}}$", r"$c$"])
    ax.legend(loc="upper left", fontsize=9, frameon=False, ncol=3)
    # Caption (rather than chart annotations) names the three regimes:
    # the high-d regime is very narrow at this numerical illustration.
    ax.grid(alpha=0.12)
    fig.subplots_adjust(left=0.13, right=0.98, top=0.95, bottom=0.20)
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "figure_02_selective_erosion.pdf"
    fig.savefig(path, bbox_inches="tight", metadata={
        "Creator": "JICT analytical illustration", "CreationDate": None, "ModDate": None
    })
    plt.close(fig)
    print(f"JICT SHORT FIGURE: PASS ({path.relative_to(ROOT)})")


if __name__ == "__main__":
    main()
