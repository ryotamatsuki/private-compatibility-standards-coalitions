#!/usr/bin/env python3
"""R9 final mathematical and manuscript-facing audit."""

from pathlib import Path
import re
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
PAPER = ROOT / "paper"

c, v, d = sp.symbols("c v d", positive=True)
P = 1 / (16 * (1 - v))
A = (1 - v) * (1 + c) ** 2 / (4 * (2 - 3 * v) ** 2)
B = (1 - 3*c - 3*(1-c)*v) ** 2 / (4 * (2 - 3 * v) ** 2)
C = (1 - v) * (1 - 2*c) ** 2 / (4 * (2 - 3 * v) ** 2)
S = (1 - 2*c) ** 2 / 16
KI = sp.Rational(9, 32) / (1-v) ** 2
KM = (3-c-3*v+3*c*v) ** 2 / (8*(2-3*v) ** 2)
E = sp.simplify((KM-KI) + 2*(A-P))
D = sp.simplify(P-C)

AR = (1+d) ** 2 / (16*(1-v))
BR = (1-3*d) ** 2 / (16*(1-v))
KR = (3-d) ** 2 / (32*(1-v) ** 2)
WIS = KI + 3*P
WPRE = KM + 2*A + C
WPOST = KR + 2*AR + C
R = d*((5-4*v)*d + 2*(1-4*v)) / (32*(1-v) ** 2)

assert sp.simplify((WPRE-WIS) - (E-D)) == 0
assert sp.simplify((WPOST-WIS) - (-D+R)) == 0
assert sp.simplify(sp.diff(R,d) - (2*(5-4*v)*d + 2*(1-4*v))/(32*(1-v)**2)) == 0
assert sp.factor((WPRE-WIS).subs(v,0)) == c*(13*c-6)/32

# Exact joint witness from R3/R7.
vals = {c: sp.Rational(1,10), v: sp.Rational(6,25), d: sp.Rational(1,20)}
pre = sp.factor((WPRE-WIS).subs(vals))
post = sp.factor((WPOST-WIS).subs(vals))
assert pre == sp.Rational(2408509,295731200)
assert post == -sp.Rational(1341,184832)

qA = ((1-v)*(1+c) - d*(3-4*v))/(2*(1-v)*(2-3*v))
qS = (1-3*v-3*c*(1-v)+d)/(2*(2-3*v))
AA = (1-v)*qA**2
AAA = (1-2*d)**2/(16*(1-v))
TO = sp.simplify(BR-B)
TU = sp.simplify(AA-C)
TW = sp.simplify(AA-S)
TAR = sp.simplify(AAA-qS**2)
Fstar = sp.simplify(2*TO)
F = sp.Rational(9,100)
tw = sp.factor(TW.subs(vals))
tar = sp.factor(TAR.subs(vals))
fstar = sp.factor(Fstar.subs(vals))
assert tw == sp.Rational(2122041,31129600)
assert tar == sp.Rational(2024181,31129600)
assert fstar == sp.Rational(459189,3891200)
assert tw < F < fstar and tar < F < fstar

# Manuscript-facing claim audit.
files = [PAPER/"main.tex", *sorted((PAPER/"sections").glob("*.tex"))]
text = "\n".join(p.read_text(encoding="utf-8") for p in files)
low = text.lower()

required = [
    r"-\mathscr D+R(d,v)",
    r"R(d,v)<\mathscr D",
    r"\mathscr D<R(d,v)<\mathscr E",
    r"R(d,v)>\mathscr E",
    r"nonempty open set",
    r"not generally portable",
    r"full-bypass",
    r"weak/Pareto blocking",
]
for token in required:
    if token not in text:
        raise AssertionError(f"R9 required manuscript claim missing: {token}")

forbidden = [
    "first paper to show",
    "first to show",
    "generally promotes international standardization",
    "competition-form independent",
    "demand-system independent",
    "network effects are irrelevant",
    "globally first best",
    "global first best",
]
for token in forbidden:
    if token in low:
        raise AssertionError(f"R9 prohibited overclaim: {token}")

# Check abstract word count against the selected JICT rule.
main = (PAPER/"main.tex").read_text(encoding="utf-8")
abstract = main.split(r"\begin{abstract}",1)[1].split(r"\end{abstract}",1)[0]
plain = re.sub(r"\\[A-Za-z]+(?:\[[^]]*\])?\{([^}]*)\}", r"\1", abstract)
plain = re.sub(r"[$\\{}]", " ", plain)
words = re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", plain)
if not 150 <= len(words) <= 250:
    raise AssertionError(f"JICT abstract length outside 150-250: {len(words)}")

keyword_block = main.split(r"\begin{keyword}",1)[1].split(r"\end{keyword}",1)[0]
keywords = [x.strip() for x in keyword_block.split(r"\sep") if x.strip() and not x.strip().startswith(r"\JEL")]
# The final split element before JEL is handled by splitting at JEL.
kw_text = keyword_block.split(r"\JEL",1)[0]
keywords = [x.strip() for x in kw_text.split(r"\sep") if x.strip()]
if not 4 <= len(keywords) <= 6:
    raise AssertionError(f"JICT keyword count outside 4-6: {len(keywords)}")

print(f"R9 FINAL MATHEMATICAL / CLAIM AUDIT: PASS (abstract words={len(words)}, keywords={len(keywords)})")
