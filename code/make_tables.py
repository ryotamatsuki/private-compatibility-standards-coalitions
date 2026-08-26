"""Generate reproducible LaTeX table fragments from the frozen canonical model.

The tables are scaffold infrastructure and are not yet included in main.tex.
Paper-facing formula strings are controlled centrally by canonical.py.
"""

from __future__ import annotations

from pathlib import Path

import canonical as can

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "paper" / "tables" / "generated"
ROW_END = r" \\"  # two LaTeX backslashes


def f(name: str) -> str:
    return can.LATEX_FORMULAS[name]


def write(name: str, content: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    print(f"generated {path.relative_to(ROOT)}")


def cournot_table() -> str:
    rows = [
        ("Complete compatibility", "Compatible firm", "q_I", "P", "K_I"),
        ("SU member market", "Bloc firm", "q_M", "A", "K_M"),
        ("SU member market", "Excluded outsider", "q_B", "B", None),
        ("SU outsider market", "Bloc firm", "q_C", "C", "K_O"),
        ("SU outsider market", "Native outsider", "q_D", "D", None),
        ("Separate standards (SW)", "Native firm", "q_H", "H", "K_W"),
        ("Separate standards (SW)", "Foreign firm", "q_S", "S", None),
    ]
    lines = [
        r"\begin{table}[htbp]",
        r"\centering",
        r"\scriptsize",
        r"\caption{Cournot building blocks. The table reports the equilibrium quantities, firm-profit blocks, and consumer-surplus blocks for the four product-market configurations used throughout the analysis.}",
        r"\label{tab:cournot-blocks}",
        r"\resizebox{\textwidth}{!}{%",
        r"\begin{tabular}{lllll}",
        r"\toprule",
        r"Market configuration & Firm type & Quantity & Profit & CS block \\",
        r"\midrule",
    ]
    for regime, firm, quantity, profit, cs in rows:
        cs_tex = f"${f(cs)}$" if cs is not None else r"---"
        lines.append(f"{regime} & {firm} & ${f(quantity)}$ & ${f(profit)}$ & {cs_tex}{ROW_END}")
    lines += [r"\bottomrule", r"\end{tabular}%", r"}", r"\end{table}"]
    return "\n".join(lines)


def threshold_table() -> str:
    rows = [
        (
            "SU outsider: adopt bloc standard",
            "---",
            r"$2T_A=2(P-B)$",
            r"$F^\ast=2T_A$",
        ),
        (
            "SU member: adopt outsider standard",
            "Other member has not adopted",
            r"$T_U=A-C$",
            r"$T_U$",
        ),
        (
            "SU member: adopt outsider standard",
            "Other member has adopted",
            r"$T_A=P-B$",
            r"$T_A$",
        ),
        (
            "SW foreign firm: adopt target standard",
            "Rival foreign firm has not adopted",
            r"$T_W=A-S$",
            r"$T_W$",
        ),
        (
            "SW foreign firm: adopt target standard",
            "Rival foreign firm has adopted",
            r"$T_A=P-B$",
            r"$T_A$",
        ),
        (
            "Relevant no-adoption lower boundary",
            "SW unilateral or any post-rival adoption",
            r"$\max\{T_W,T_A\}$",
            r"$F_L=\max\{T_W,T_A\}$",
        ),
    ]
    lines = [
        r"\begin{table}[htbp]",
        r"\centering",
        r"\scriptsize",
        r"\caption{Private-adoption incentives and thresholds. The table reports the operating-profit gains associated with adopting an additional formal standard and the resulting fixed-cost thresholds in the symmetric Main Model.}",
        r"\label{tab:thresholds}",
        r"\resizebox{\textwidth}{!}{%",
        r"\begin{tabular}{llll}",
        r"\toprule",
        r"Decision & Rival adoption state & Operating-profit gain & Fixed-cost threshold \\",
        r"\midrule",
    ]
    for decision, state, gain, threshold in rows:
        lines.append(f"{decision} & {state} & {gain} & {threshold}{ROW_END}")
    lines += [r"\bottomrule", r"\end{tabular}%", r"}", r"\end{table}"]
    return "\n".join(lines)


def stability_table() -> str:
    return "\n".join(
        [
            r"\begin{table}[htbp]",
            r"\centering",
            r"\scriptsize",
            r"\caption{Canonical stability regions in the symmetric model}",
            r"\label{tab:stability-regions}",
            r"\resizebox{\textwidth}{!}{%",
            r"\begin{tabular}{lll}",
            r"\toprule",
            r"Fixed-cost region & Private compatibility pattern & Frozen stability statement \\",
            r"\midrule",
            r"$0<F<F_{\mathrm{low}}$ & Universal multistandarding & $\mathcal{S}(F)=\{\rho^{IS}\}$ (sufficient low-$F$ result) \\",
            r"$F_{\mathrm{low}}\le F\le F_L$ & Transition interval & Not characterized by the headline theorems \\",
            r"$F_L<F<2T_A$ & Outsider-only bypass in each SU & $\mathcal{S}(F)=\{\rho^{IS}\}$ \\",
            r"$F>2T_A$ & No private adoption & $\mathcal{S}(F)=\{\rho_{12}^{SU},\rho_{13}^{SU},\rho_{23}^{SU}\}$ \\",
            r"\bottomrule",
            r"\end{tabular}%",
            r"}",
            r"\end{table}",
        ]
    )


def main() -> None:
    write("table_cournot_blocks.tex", cournot_table())
    write("table_thresholds.tex", threshold_table())
    write("table_stability_regions.tex", stability_table())
    print("TABLE GENERATION: PASS")


if __name__ == "__main__":
    main()
