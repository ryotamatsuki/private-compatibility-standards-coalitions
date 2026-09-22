from __future__ import annotations

from collections import deque
from pathlib import Path
import re
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
OUT = ROOT / "submission" / "generated"
MAIN_DIR = OUT / "jict_source"
SUPP_DIR = OUT / "jict_online_supplement_source"
MAIN_ZIP = OUT / "jict_source.zip"
SUPP_ZIP = OUT / "jict_online_supplement_source.zip"

INPUT_RE = re.compile(r"\\input\{([^}]+)\}")
GRAPHICS_RE = re.compile(r"(\\includegraphics(?:\[[^\]]*\])?\{)([^}]+)(\})")
BIB_RE = re.compile(r"\\bibliography\{([^}]+)\}")

MAIN_APPENDIX_REFS = {
    r"Appendix~\ref{app:cournot}": "Online Supplement, Appendix A",
    r"Appendix~\ref{app:welfare}": "Online Supplement, Appendix B",
    r"Appendix~\ref{app:adoption-equilibria}": "Online Supplement, Appendix C",
    r"Appendix~\ref{app:partial-erosion}": "Online Supplement, Appendix D",
    r"Appendix~\ref{app:robustness}": "Online Supplement, Appendix E",
    r"Appendix~\ref{app:low-f}": "Online Supplement, Appendix F",
}

SUPPLEMENT_MAIN_REF_REPLACEMENTS = {
    r"Lemma~\ref{lem:cournot-blocks}": "the canonical Cournot-block lemma in the main article",
    r"Section~\ref{sec:product-market}": "the Cournot Building Blocks section of the main article",
    r"Section~\ref{subsec:model-domain}": "the model-domain subsection of the main article",
    r"Section~\ref{sec:coalition-stability}": "the Coalition-Stability Application section of the main article",
    r"Lemma~\ref{lem:private-adoption}": "the private-adoption lemma in the main article",
    r"equation~\eqref{eq:su-outsider-main-threshold}": "the SU outsider-adoption threshold in the main article",
    r"Theorem~\ref{thm:formal-coalition-stability}": "the coalition-stability theorem in the main article",
    r"Section~\ref{sec:selective-erosion}": "the Private Adaptation and Government Incentives section of the main article",
    r"equation~\eqref{eq:partial-erosion-identity}": "the residual-rent identity in the main article",
    r"Proposition~\ref{prop:incomplete-adaptation-open-set}": "the incomplete-adaptation open-set proposition in the main article",
    r"Section~\ref{sec:secondary}": "the Scope and Robustness section of the main article",
}


def fail(message: str) -> None:
    raise SystemExit(f"JICT PACKAGE: FAIL — {message}")


def resolve_input(name: str) -> Path:
    path = PAPER / name
    if path.suffix == "":
        path = path.with_suffix(".tex")
    if not path.is_file():
        fail(f"missing input dependency: {name}")
    return path.resolve()


def resolve_graphic(name: str) -> Path:
    path = PAPER / name
    if path.is_file():
        return path.resolve()
    if path.suffix == "":
        for suffix in (".pdf", ".png", ".jpg", ".jpeg", ".eps"):
            test = path.with_suffix(suffix)
            if test.is_file():
                return test.resolve()
    fail(f"missing graphic dependency: {name}")


def register(path: Path, seen: dict[str, Path]) -> None:
    old = seen.get(path.name)
    if old is not None and old != path:
        fail(f"basename collision: {old} and {path}")
    seen[path.name] = path


def transform_reviewer_main(text: str) -> str:
    start = text.find(r"\appendix")
    end_marker = r"\input{sections/11_submission_declarations}"
    end = text.find(end_marker)
    if start < 0 or end < 0 or end < start:
        fail("could not locate canonical appendix/declarations block")
    end += len(end_marker)
    replacement = (
        "\n\\section*{Online Supplement}\n"
        "Detailed derivations, equilibrium-correspondence calculations, "
        "robustness certificates, and lower-fixed-cost continuation cases are "
        "provided in the anonymous Online Supplement.\n"
    )
    text = text[:start] + replacement + text[end:]
    for old, new in MAIN_APPENDIX_REFS.items():
        text = text.replace(old, new)
    return text


def transform_reviewer_dependency(text: str) -> str:
    for old, new in MAIN_APPENDIX_REFS.items():
        text = text.replace(old, new)
    return text


def transform_supplement_dependency(text: str) -> str:
    for old, new in SUPPLEMENT_MAIN_REF_REPLACEMENTS.items():
        text = text.replace(old, new)
    return text


def flatten(entry_text: str, entry_origin: Path, out_dir: Path, transform_dependency) -> None:
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    seen: dict[str, Path] = {}
    queue: deque[tuple[Path, str | None]] = deque([(entry_origin.resolve(), entry_text)])
    processed: set[Path] = set()

    while queue:
        origin, supplied = queue.popleft()
        if origin in processed:
            continue
        register(origin, seen)
        text = supplied if supplied is not None else origin.read_text(encoding="utf-8")
        if origin != entry_origin.resolve():
            text = transform_dependency(text)

        def input_repl(match: re.Match[str]) -> str:
            dep = resolve_input(match.group(1))
            register(dep, seen)
            queue.append((dep, None))
            return rf"\input{{{dep.stem}}}"

        text = INPUT_RE.sub(input_repl, text)

        def graphic_repl(match: re.Match[str]) -> str:
            dep = resolve_graphic(match.group(2))
            register(dep, seen)
            shutil.copy2(dep, out_dir / dep.name)
            return f"{match.group(1)}{dep.name}{match.group(3)}"

        text = GRAPHICS_RE.sub(graphic_repl, text)

        for match in BIB_RE.finditer(text):
            for bib_name in (x.strip() for x in match.group(1).split(",")):
                dep = PAPER / (bib_name if bib_name.endswith(".bib") else bib_name + ".bib")
                if not dep.is_file():
                    fail(f"missing bibliography dependency: {bib_name}")
                dep = dep.resolve()
                register(dep, seen)
                shutil.copy2(dep, out_dir / dep.name)

        (out_dir / origin.name).write_text(text, encoding="utf-8")
        processed.add(origin)


def make_zip(source_dir: Path, zip_path: Path) -> None:
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(source_dir.iterdir()):
            if path.is_file():
                zf.write(path, arcname=path.name)
    with zipfile.ZipFile(zip_path) as zf:
        if not zf.namelist() or any("/" in x or "\\" in x for x in zf.namelist()):
            fail(f"invalid flat source zip: {zip_path.name}")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    canonical = (PAPER / "main.tex").read_text(encoding="utf-8")
    reviewer_main = transform_reviewer_main(canonical)
    flatten(reviewer_main, PAPER / "main.tex", MAIN_DIR, transform_reviewer_dependency)

    supplement_main = r"""\documentclass[11pt]{article}
\input{preamble}
\title{Online Supplement to Private Compatibility and the Stability of Standards Coalitions}
\author{}
\date{}
\begin{document}
\maketitle
\noindent This anonymous supplement contains technical derivations and robustness calculations referenced by the main article. It introduces no additional headline claim beyond the certified results stated in the main article.
\appendix
\input{appendix/app_a_cournot_derivations}
\input{appendix/app_b_welfare_algebra}
\input{appendix/app_c_adoption_equilibria}
\input{appendix/app_d_partial_erosion}
\input{appendix/app_e_robustness}
\input{appendix/app_f_low_f}
\end{document}
"""
    supplement_origin = PAPER / "main.tex"
    flatten(supplement_main, supplement_origin, SUPP_DIR, transform_supplement_dependency)

    make_zip(MAIN_DIR, MAIN_ZIP)
    make_zip(SUPP_DIR, SUPP_ZIP)

    for directory in (MAIN_DIR, SUPP_DIR):
        for path in directory.glob("*.tex"):
            text = path.read_text(encoding="utf-8")
            if "Ryota Matsuki" in text or "ryota.matsuki@gmail.com" in text or "ryotamatsuki" in text.lower():
                fail(f"identity leak in anonymous JICT source: {directory.name}/{path.name}")
            for match in INPUT_RE.finditer(text):
                if "/" in match.group(1) or "\\" in match.group(1):
                    fail(f"subfolder input remains in {directory.name}/{path.name}")
            for match in GRAPHICS_RE.finditer(text):
                if "/" in match.group(2) or "\\" in match.group(2):
                    fail(f"subfolder graphic remains in {directory.name}/{path.name}")

    print(f"JICT REVIEW SOURCE: PASS ({MAIN_ZIP.relative_to(ROOT)})")
    print(f"JICT SUPPLEMENT SOURCE: PASS ({SUPP_ZIP.relative_to(ROOT)})")


if __name__ == "__main__":
    main()
