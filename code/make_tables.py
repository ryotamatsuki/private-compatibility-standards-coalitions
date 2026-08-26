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
        r"\caption{Canonical Cournot building blocks}",
        r"\label{tab:cournot-blocks}",
        r"\resizebox{\textwidth}{!}{%",
        r"\begin{tabular}{lllll}",
        r"\toprule",
        r"Market regime & Firm type & Quantity & Profit & CS block \\",
        r"\midrule",
    ]
    for regime, firm, quantity, profit, cs in rows:
        cs_tex = f"${f(cs)}$" if cs is not None else r"---"
        lines.append(f"{regime} & {firm} & ${f(quantity)}$ & ${f(profit)}$ & {cs_tex}{ROW_END}")
    lines += [r"\bottomrule", r"\end{tabular}%", r"}", r"\end{table}"]
    return "\n".join(lines)


def threshold_table() -> str:
    rows = [
        (r"$T_A$", r"$P-B$", f("T_A")),
        (r"$T_U$", r"$A-C$", f("T_U")),
        (r"$T_W$", r"$A-S$", f("T_W")),
        (r"$F_{\mathrm{low}}$", r"$\min\{T_U,T_A\}$", f("F_low")),
        (r"$F_L$", r"$\max\{T_W,T_A\}$", f("F_L")),
        (r"$F^*$", r"$2T_A$", f("F_star")),
    ]
    lines = [
        r"\begin{table}[htbp]",
        r"\centering",
        r"\small",
        r"\caption{Canonical private-adoption thresholds}",
        r"\label{tab:thresholds}",
        r"\begin{tabular}{lll}",
        r"\toprule",
        r"Threshold & Definition & Canonical expression \\",
        r"\midrule",
    ]
    for name, definition, expression in rows:
        lines.append(f"{name} & {definition} & ${expression}${ROW_END}")
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{table}"]
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
