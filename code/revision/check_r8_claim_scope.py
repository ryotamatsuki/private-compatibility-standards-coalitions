#!/usr/bin/env python3
"""R8 manuscript claim-scope and reconstruction audit."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PAPER = ROOT / "paper"

FILES = [
    PAPER / "main.tex",
    *sorted((PAPER / "sections").glob("*.tex")),
    *sorted((PAPER / "appendix").glob("*.tex")),
]
text = "\n".join(p.read_text(encoding="utf-8") for p in FILES)
lower = text.lower()

required = {
    "residual-rent identity": r"W_M\^\{SU,O\}\(d\)-W\^\{IS\}",
    "residual-rent function": r"R\(d,v\)",
    "incomplete adaptation": r"0<\\lambda<1",
    "R5 non-portability": r"differentiated-demand",
    "weak blocking": r"weak/Pareto blocking",
    "Route-B scope language": r"conditional mechanism",
    "partial appendix": r"appendix/app_d_partial_erosion",
    "robustness appendix": r"appendix/app_e_robustness",
}
for label, pattern in required.items():
    if not re.search(pattern, text):
        raise AssertionError(f"Missing R8 required element: {label}")

forbidden = [
    r"first paper to show",
    r"first to show",
    r"private compatibility generally promotes",
    r"private compatibility always promotes",
    r"competition-form independent",
    r"demand-system independent",
    r"network effects are irrelevant",
    r"international standardization is socially first-best",
    r"international standardization is globally first-best",
    r"universal robustness of the three",
]
for phrase in forbidden:
    if re.search(phrase, lower):
        raise AssertionError(f"R7-prohibited overclaim found: {phrase}")

# Old main-text architecture should no longer carry partner selection as a
# standalone proposition.
secondary = (PAPER / "sections" / "08_secondary_results.tex").read_text(encoding="utf-8")
if "Market-Size Partner Selection" in secondary:
    raise AssertionError("Old partner-selection proposition remains in R8 main text")

# The main result must distinguish government incentives from institutional
# stability and scope the latter to full bypass.
coalition = (PAPER / "sections" / "07_coalition_stability.tex").read_text(encoding="utf-8")
if "full-bypass" not in coalition.lower():
    raise AssertionError("Coalition-stability application is not scoped to full bypass")

# The abstract must visibly report both the positive mechanism and its
# portability limitation.
main = (PAPER / "main.tex").read_text(encoding="utf-8")
abstract = main.split(r"\begin{abstract}", 1)[1].split(r"\end{abstract}", 1)[0]
for term in ["residual", "not generally portable", "blocking rule"]:
    if term.lower() not in abstract.lower():
        raise AssertionError(f"Abstract missing R8 scope signal: {term}")

print("R8 CLAIM-SCOPE AND RECONSTRUCTION AUDIT: PASS")
