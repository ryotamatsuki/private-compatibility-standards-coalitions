from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EN = ROOT / "paper"
JA = ROOT / "paper-ja"

FILES = [
    "sections/01_introduction.tex",
    "sections/02_related_literature.tex",
    "sections/03_model.tex",
    "sections/04_product_market_equilibrium.tex",
    "sections/05_private_compatibility.tex",
    "sections/06_selective_erosion.tex",
    "sections/07_coalition_stability.tex",
    "sections/08_secondary_results.tex",
    "sections/09_discussion.tex",
    "sections/10_conclusion.tex",
    "sections/11_submission_declarations.tex",
]
APPS = [
    "appendix/app_a_cournot_derivations.tex",
    "appendix/app_b_welfare_algebra.tex",
    "appendix/app_c_adoption_equilibria.tex",
    "appendix/app_f_low_f.tex",
]
PAIRS = [(EN / p, JA / p) for p in FILES + APPS]

TABLES = [
    "table_cournot_blocks.tex",
    "table_thresholds.tex",
    "table_stability_regions.tex",
]
TABLE_PAIRS = [
    (EN / "tables" / "generated" / p, JA / "tables" / "generated" / p)
    for p in TABLES
]

CMD_PATTERNS = {
    "label": re.compile(r"\\label\{([^{}]+)\}"),
    "ref": re.compile(r"\\ref\{([^{}]+)\}"),
    "eqref": re.compile(r"\\eqref\{([^{}]+)\}"),
    "cite": re.compile(r"\\cite(?:t|p)?\*?\{([^{}]+)\}"),
}

DISPLAY_ENVS = ["equation", "align", "align*", "gather", "multline"]
ENV_NAMES = ["theorem", "lemma", "proposition", "corollary", "assumption"]


def read(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8")


def strip_comments(s: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", s)


def norm_math(s: str) -> str:
    return re.sub(r"\s+", "", strip_comments(s))


def display_math_stream(text: str) -> list[str]:
    hits: list[tuple[int, str]] = []
    for env in DISPLAY_ENVS:
        pattern = re.compile(
            rf"\\begin\{{{re.escape(env)}\}}(.*?)\\end\{{{re.escape(env)}\}}",
            re.DOTALL,
        )
        for m in pattern.finditer(text):
            hits.append((m.start(), norm_math(m.group(1))))
    for m in re.finditer(r"\\\[(.*?)\\\]", text, re.DOTALL):
        hits.append((m.start(), norm_math(m.group(1))))
    hits.sort(key=lambda x: x[0])
    return [content for _, content in hits]


def strip_display_math(text: str) -> str:
    out = text
    for env in DISPLAY_ENVS:
        out = re.sub(
            rf"\\begin\{{{re.escape(env)}\}}.*?\\end\{{{re.escape(env)}\}}",
            "",
            out,
            flags=re.DOTALL,
        )
    out = re.sub(r"\\\[.*?\\\]", "", out, flags=re.DOTALL)
    return out


def inline_math_multiset(text: str) -> Counter[str]:
    stripped = strip_display_math(text)
    vals = re.findall(r"(?<!\\)\$(?!\$)(.*?)(?<!\\)\$", stripped, flags=re.DOTALL)
    return Counter(norm_math(v) for v in vals)


def sections(text: str) -> list[str]:
    return re.findall(r"\\(section\*?|subsection\*?|subsubsection\*?)\{", text)


def env_counts(text: str) -> Counter[str]:
    return Counter(
        env
        for env in ENV_NAMES
        for _ in re.finditer(rf"\\begin\{{{env}\}}", text)
    )


def command_values(kind: str, text: str) -> list[str]:
    vals = CMD_PATTERNS[kind].findall(text)
    if kind == "cite":
        return [key.strip() for group in vals for key in group.split(",")]
    return vals


def fail(path: Path, check: str, left, right) -> None:
    print(f"AUDIT FAIL: {path.relative_to(ROOT)}: {check}")
    print(f"  EN: {left}")
    print(f"  JA: {right}")
    raise SystemExit(1)


def check_pair(en_path: Path, ja_path: Path) -> None:
    en = read(en_path)
    ja = read(ja_path)

    for kind in ("label", "cite"):
        ev = command_values(kind, en)
        jv = command_values(kind, ja)
        if ev != jv:
            fail(en_path, f"ordered {kind}s", ev, jv)

    for kind in ("ref", "eqref"):
        ev = Counter(command_values(kind, en))
        jv = Counter(command_values(kind, ja))
        if ev != jv:
            fail(en_path, f"{kind} multiplicity", ev, jv)

    if sections(en) != sections(ja):
        fail(en_path, "section hierarchy", sections(en), sections(ja))

    if env_counts(en) != env_counts(ja):
        fail(en_path, "theorem-like environment counts", env_counts(en), env_counts(ja))

    em = display_math_stream(en)
    jm = display_math_stream(ja)
    if em != jm:
        for i, (a, b) in enumerate(zip(em, jm, strict=False)):
            if a != b:
                fail(en_path, f"display mathematics item {i + 1}", a, b)
        fail(en_path, "display mathematics count", len(em), len(jm))

    ei = inline_math_multiset(en)
    ji = inline_math_multiset(ja)
    if ei != ji:
        fail(en_path, "inline mathematics exact-token multiplicity", ei - ji, ji - ei)


def main_inputs(path: Path) -> list[str]:
    text = read(path)
    return re.findall(r"\\input\{([^{}]+)\}", text)


def main() -> None:
    try:
        for en_path, ja_path in PAIRS:
            check_pair(en_path, ja_path)

        for en_path, ja_path in TABLE_PAIRS:
            en = read(en_path)
            ja = read(ja_path)
            if command_values("label", en) != command_values("label", ja):
                fail(en_path, "generated-table labels", command_values("label", en), command_values("label", ja))
            if inline_math_multiset(en) != inline_math_multiset(ja):
                fail(en_path, "generated-table math tokens", inline_math_multiset(en), inline_math_multiset(ja))
            en_tab = (en.count(r"\begin{tabular}"), en.count(r"\end{tabular}"))
            ja_tab = (ja.count(r"\begin{tabular}"), ja.count(r"\end{tabular}"))
            if en_tab != ja_tab:
                fail(en_path, "generated-table tabular structure", en_tab, ja_tab)

        en_inputs = [x for x in main_inputs(EN / "main.tex") if x.startswith("sections/") or x.startswith("appendix/")]
        ja_inputs = [x for x in main_inputs(JA / "main-ja.tex") if x.startswith("sections/") or x.startswith("appendix/")]
        if en_inputs != ja_inputs:
            fail(EN / "main.tex", "main input sequence", en_inputs, ja_inputs)

    except FileNotFoundError as exc:
        print(f"AUDIT FAIL: missing file: {exc}")
        raise SystemExit(1) from exc

    print("JAPANESE STRUCTURAL AUDIT: PASS (15 translated source files + 3 generated tables)")
    print("- ordered labels/citations: identical")
    print("- refs/eqrefs: identical multiplicity")
    print("- section hierarchy and theorem environments: identical")
    print("- display mathematics: identical after whitespace normalization")
    print("- inline mathematics: identical exact-token multiplicity")
    print("- generated tables: labels/mathematical tokens/tabular structure identical")


if __name__ == "__main__":
    main()
