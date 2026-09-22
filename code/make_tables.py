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
            r"\small",
            r"\caption{Headline formal-stability regions in the symmetric Main Model for $(c,v)\in\Omega_0$. The table reports the private-adoption continuation state and the strict-blocking stable set.}",
            r"\label{tab:stability-regions}",
            r"\resizebox{\textwidth}{!}{%",
            r"\begin{tabular}{lll}",
            r"\toprule",
            r"Fixed-cost region & Private-adoption continuation & Stable formal partitions \\",
            r"\midrule",
            r"$0<F\le F_L$ & Outside the headline theorem & Not characterized here \\",
            r"$F_L<F<2T_A$ & Outsider-only bypass in each SU; no SW adoption & $\{\rho^{IS}\}$ \\",
            r"$F>2T_A$ & No SU or SW private adoption & $\{\rho_{12}^{SU},\rho_{13}^{SU},\rho_{23}^{SU}\}$ \\",
            r"\bottomrule",
            r"\end{tabular}%",
            r"}",
            r"\end{table}",
        ]
    )



def residual_rent_table() -> str:
    return "\n".join(
        [
            r"\begin{table}[htbp]",
            r"\centering",
            r"\small",
            r"\caption{Government-incentive regions under incomplete private adaptation. The classification assumes the initial condition $\mathscr E>\mathscr D>0$ and the selection-free outsider-only continuation.}",
            r"\label{tab:residual-rent-regions}",
            r"\resizebox{\textwidth}{!}{%",
            r"\begin{tabular}{lll}",
            r"\toprule",
            r"Residual-rent condition & Post-adaptation ranking & Change in relative IS incentive \\",
            r"\midrule",
            r"$R(d,v)<\mathscr D$ & IS strictly preferred & Strengthens; ranking reverses \\",
            r"$\mathscr D<R(d,v)<\mathscr E$ & SU remains strictly preferred & Strengthens without reversal \\",
            r"$R(d,v)>\mathscr E$ & SU strictly preferred & Weakens \\",
            r"$R(d,v)=\mathscr D$ or $R(d,v)=\mathscr E$ & Boundary case & Indifference in the corresponding comparison \\",
            r"\bottomrule",
            r"\end{tabular}%",
            r"}",
            r"\end{table}",
        ]
    )


def scope_robustness_table() -> str:
    return "\n".join(
        [
            r"\begin{table}[htbp]",
            r"\centering",
            r"\scriptsize",
            r"\caption{Scope and robustness of the revision results. A check marked as surviving is only a result for the specified perturbation, not a universal theorem over the entire model class.}",
            r"\label{tab:scope-robustness}",
            r"\resizebox{\textwidth}{!}{%",
            r"\begin{tabular}{llll}",
            r"\toprule",
            r"Check & One-way private adoption & Initial SU advantage / political effect & Institutional implication \\",
            r"\midrule",
            r"Canonical baseline & Survives & Survives on certified parameter region & Intermediate full-bypass region gives unique IS under strict blocking \\",
            r"$v=0$ boundary & Survives & Fails: $W_M^{SU,N}<W^{IS}$ & Reversal route cannot start \\",
            r"Singleton-network alternative S1 & Survives at exact witness & Fails throughout old canonical domain & No political reversal route in S1 \\",
            r"Differentiated demand, Cournot & Survives at exact witness & Fails throughout frozen audit box & No certified reversal route \\",
            r"Differentiated demand, Bertrand & Survives at exact witness & Fails throughout frozen audit box & Failure is not attributable to price competition alone \\",
            r"Weak/Pareto blocking, symmetric high $F$ & Not the margin tested & Canonical payoffs unchanged & High-$F$ stable set becomes empty \\",
            r"Small market-size asymmetry & Re-solved and survives on certified ranges & Intermediate strict gaps survive & High-$F$ partner indifference is broken; intermediate unique IS survives \\",
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
    write("table_residual_rent_regions.tex", residual_rent_table())
    write("table_scope_robustness.tex", scope_robustness_table())
    print("TABLE GENERATION: PASS")


if __name__ == "__main__":
    main()
