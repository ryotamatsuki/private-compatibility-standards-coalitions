"""Build an independent, fully anonymous JICT short reviewer package.

No edits to the canonical paper/sections/*.tex or original JICT package.
Requires existing generated figure/table files from `make figures tables`.
Can generate and compile the unchanged JICT Online Supplement automatically.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "paper" / "jict_short"
OUT = ROOT / "submission" / "generated"
FLAT = OUT / "jict_short_source"
REQUIRED = ["main.tex", *[f"short_{i:02d}_{n}.tex" for i, n in enumerate(
    ["introduction", "model", "adoption", "incentives", "stability_scope", "discussion"], start=1)]]


def run(*args: str, cwd: Path | None = None) -> None:
    subprocess.run(list(args), cwd=cwd, check=True)


def pages(path: Path) -> int:
    info = subprocess.run(["pdfinfo", str(path)], text=True, capture_output=True, check=True).stdout
    return int(re.search(r"(?m)^Pages:\s*(\d+)", info).group(1))


def build(require_supplement: bool = True) -> None:
    # The short edition has an independently regenerated, legible figure.
    run(sys.executable, str(ROOT / "code/revision/make_jict_short_figure.py"), cwd=ROOT)
    if FLAT.exists():
        shutil.rmtree(FLAT)
    FLAT.mkdir(parents=True, exist_ok=True)
    inputs = {name: SOURCE / name for name in REQUIRED}
    inputs.update({"preamble.tex": ROOT / "paper/preamble.tex",
                   "notation.tex": ROOT / "paper/notation.tex",
                   "references.bib": ROOT / "paper/references.bib",
                   "figure_02_selective_erosion.pdf": ROOT / "paper/jict_short/generated/figure_02_selective_erosion.pdf",
                   "table_residual_rent_regions.tex": ROOT / "paper/tables/generated/table_residual_rent_regions.tex"})
    for name, src in inputs.items():
        if not src.is_file():
            raise SystemExit(f"SHORT JICT FAIL: missing {src}; run 'make figures tables' first")
        shutil.copy2(src, FLAT / name)
    # Springer JICT permits bibliography entries for published/accepted work.
    # Preserve the canonical R9 bibliography untouched; omit unverified
    # unpublished techreports ONLY in this short-reviewer source.
    short_bib = FLAT / "references.bib"
    filtered = short_bib.read_text(encoding="utf-8")
    for key in ("maggiMrazova2024", "economidesSkrzypacz2003"):
        filtered, n = re.subn(
            rf"(?ms)^@techreport\{{{key},.*?^\}}\s*", "", filtered
        )
        if n != 1:
            raise SystemExit(f"SHORT JICT FAIL: missing unpublished bibliography entry {key}")
    short_bib.write_text(filtered, encoding="utf-8")
    # Treat this zip as a journal-compatible, single-directory TeX source bundle.
    with zipfile.ZipFile(OUT / "jict_short_source.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(FLAT.iterdir()):
            z.write(p, arcname=p.name)
    run("latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "main.tex", cwd=FLAT)
    log = (FLAT / "main.log").read_text(errors="replace")
    if re.search(r"LaTeX Warning: (Reference|Citation).*undefined|There were undefined references|multiply defined", log, re.I):
        raise SystemExit("SHORT JICT FAIL: unresolved LaTeX references, citations or duplicate labels")
    pdf = FLAT / "main.pdf"
    n = pages(pdf)
    if not 17 <= n <= 19:
        raise SystemExit(f"SHORT JICT FAIL: reviewer manuscript {n} pages, required 17--19")
    txt = subprocess.run(["pdftotext", str(pdf), "-"], text=True, capture_output=True, check=True).stdout
    for word in ("Ryota Matsuki", "ryota.matsuki@gmail.com", "github.com/ryotamatsuki"):
        if word.lower() in txt.lower():
            raise SystemExit(f"SHORT JICT FAIL: author information in anonymous manuscript: {word}")
    if "Preprint submitted to Elsevier" in txt:
        raise SystemExit("SHORT JICT FAIL: non-JICT publisher footer")
    if "ChatGPT (OpenAI)" not in txt or "AI-assisted methods" not in txt:
        raise SystemExit("SHORT JICT FAIL: substantive AI research methods disclosure missing")
    if "Maggi and Mr" not in txt or "Working Paper 33318" not in txt:
        raise SystemExit("SHORT JICT FAIL: working-paper discussion dropped")
    bbl = (FLAT / "main.bbl").read_text(encoding="utf-8")
    if "maggiMrazova2024" in bbl or "economidesSkrzypacz2003" in bbl:
        raise SystemExit("SHORT JICT FAIL: unpublished working paper retained in reference list")
    for key in ("Residual-rent government effect", "Incomplete adaptation with actual preference reversal", "Full-bypass stability application", "Differentiated-demand"):
        if key.lower() not in txt.lower():
            # Figure/proposition text may split at page or hyphenation; check source for precise presence.
            all_tex = "\n".join(p.read_text() for p in FLAT.glob("*.tex"))
            if key.lower() not in all_tex.lower():
                raise SystemExit(f"SHORT JICT FAIL: required scientific claim absent: {key}")
    shutil.copy2(pdf, OUT / "jict_short_manuscript.pdf")
    if require_supplement:
        # Preserve the six R9 mathematical appendices and append a human-readable
        # coalition blocking proof ledger (Appendix G), without changing the R9 proofs.
        # Prose-only cross-references are adapted to the short article's headings.
        canonical_si = OUT / "jict_online_supplement_source"
        if not (canonical_si / "main.tex").is_file():
            run(sys.executable, str(ROOT / "code/make_jict_submission_package.py"), cwd=ROOT)
        short_si = OUT / "jict_short_online_supplement_source"
        if short_si.exists():
            shutil.rmtree(short_si)
        shutil.copytree(canonical_si, short_si)
        ledger = SOURCE / "short_supplement_blocking.tex"
        if not ledger.is_file():
            raise SystemExit("SHORT JICT FAIL: missing five-partition blocking ledger")
        shutil.copy2(ledger, short_si / ledger.name)
        supplement_main = short_si / "main.tex"
        main_source = supplement_main.read_text(encoding="utf-8")
        if main_source.count(r"\end{document}") != 1:
            raise SystemExit("SHORT JICT FAIL: unexpected supplement document boundary")
        supplement_main.write_text(
            main_source.replace(
                r"\end{document}",
                "\\input{short_supplement_blocking}\n" + r"\end{document}",
            ),
            encoding="utf-8",
        )
        pointer_updates = {
            "the canonical Cournot-block lemma in the main article": "the Cournot payoff formulas in Section 2 of the short main article",
            "the Cournot Building Blocks section of the main article": "the Model and Product-Market Payoffs section of the short main article",
            "the model-domain subsection of the main article": "the model-domain restrictions in Section 2 of the short main article",
            "the Coalition-Stability Application section of the main article": "the Coalition Stability and Scope section of the short main article",
            "the private-adoption lemma in the main article": "the adoption inequalities in Section 3 of the short main article",
            "the SU outsider-adoption threshold in the main article": "the outsider-adoption threshold in Section 3 of the short main article",
            "the coalition-stability theorem in the main article": "the full-bypass stability theorem in Section 5 of the short main article",
            "the Private Adaptation and Government Incentives section of the main article": "the Private Adaptation and Government Incentives section of the short main article",
            "the residual-rent identity in the main article": "the residual-rent identity in Section 4 of the short main article",
            "the incomplete-adaptation open-set proposition in the main article": "the incomplete-adaptation open-set proposition in Section 4 of the short main article",
            "the Scope and Robustness section of the main article": "the scope discussion in Section 5 of the short main article",
            "the government-incentive and coalition-stability sections of the main article": "the government-incentive and stability sections of the short main article",
        }
        for tex in short_si.glob("*.tex"):
            body = tex.read_text(encoding="utf-8")
            for old, new in pointer_updates.items():
                body = body.replace(old, new)
            # Repair prose malformed by inherited full-to-short substitutions.
            body = body.replace(
                "Sections~the Private Adaptation and Government Incentives section of the main article and the Coalition-Stability Application section of the main article",
                "Sections 4 and 5 of the short main article",
            )
            # Only the short review supplement receives display repairs.
            # Single TeX control-space commands in the inherited R9 appendix
            # made multi-line align formulas render as one overfull line.
            if tex.name == "app_d_partial_erosion.tex":
                for symbol in ("q_A(d)", "q_S(d)", "T_W(d)", "T_A^R(d)", "F^*(d)"):
                    needle = ",\\\n" + symbol
                    if needle not in body:
                        raise SystemExit(f"SHORT JICT FAIL: expected appendix TeX alignment {symbol}")
                    body = body.replace(needle, ",\\\\\n" + symbol, 1)
            if tex.name == "app_e_robustness.tex":
                # Preserve exact code/Lean names, with line-breakable links.
                replacements = {
                    "code/revision/check\\_r4\\_network\\_role.py":
                        "code/revision/check_r4_network_role.py",
                    "FV5\\_indifferenceSeparatesBlockingRules":
                        "FV5_indifferenceSeparatesBlockingRules",
                }
                for escaped_name, natural_name in replacements.items():
                    for prefix in (r"\texttt{", "\texttt{"):
                        body = body.replace(prefix + escaped_name + "}",
                                            r"\path{" + natural_name + "}")
            tex.write_text(body, encoding="utf-8")
        run("latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "-bibtex-", "main.tex", cwd=short_si)
        supplement_pdf = short_si / "main.pdf"
        si_log = (short_si / "main.log").read_text(errors="replace")
        if re.search(r"LaTeX Warning: (Reference|Citation).*undefined|There were undefined references|multiply defined", si_log, re.I):
            raise SystemExit("SHORT JICT FAIL: supplement references or labels unresolved")
        supplement_text = subprocess.run(["pdftotext", str(supplement_pdf), "-"], capture_output=True, text=True, check=True).stdout
        if "Explicit Coalition-Deviation and Payoff Ledger" not in supplement_text:
            raise SystemExit("SHORT JICT FAIL: supplement coalition proof ledger absent")
        for word in ("Ryota Matsuki", "ryota.matsuki@gmail.com", "github.com/ryotamatsuki"):
            if word.lower() in supplement_text.lower():
                raise SystemExit("SHORT JICT FAIL: identity leak in anonymous supplement")
        shutil.copy2(supplement_pdf, OUT / "jict_short_online_supplement.pdf")
        if pages(supplement_pdf) < 1:
            raise SystemExit("SHORT JICT FAIL: supplement not compiled")
        with zipfile.ZipFile(OUT / "jict_short_online_supplement_source.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for tex in sorted(short_si.glob("*.tex")):
                z.write(tex, arcname=tex.name)
    # Build a complete, version-matched human-reviewed upload set.
    # Title page and cover letter are separate identified files, NOT reviewer inputs.
    for stem, dest in (
        ("jict_title_page", "jict_short_identified_title_page.pdf"),
        ("jict_cover_letter", "jict_short_cover_letter.pdf"),
    ):
        run("latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
            "-bibtex-", stem + ".tex", cwd=ROOT / "submission")
        shutil.copy2(ROOT / "submission" / (stem + ".pdf"), OUT / dest)
    run(sys.executable, str(ROOT / "code/make_submission_package.py"), cwd=ROOT)
    manifest = """# JICT short-manuscript upload checklist

Generated from the 17--19-page short-edition branch. Upload ONLY these short
review files for manuscript and Online Supplement. The original 39-page
submission files remain archived for rollback.

1. ANONYMOUS REVIEWER PDF: jict_short_manuscript.pdf
2. ANONYMOUS REVIEWER SOURCE: jict_short_source.zip (flat LaTeX and bibliography)
3. ANONYMOUS ONLINE SUPPLEMENT PDF: jict_short_online_supplement.pdf
4. ANONYMOUS ONLINE SUPPLEMENT SOURCE: jict_short_online_supplement_source.zip
5. IDENTIFIED TITLE PAGE / DECLARATIONS: jict_short_identified_title_page.pdf
6. IDENTIFIED COVER LETTER: jict_short_cover_letter.pdf
7. ANONYMOUS CANONICAL PROOF REPLICATION: replication_package_anonymous.zip

Source identity, declarations, funding, conflicts, final portal categories,
author email, originality and simultaneous-submission statements REQUIRE the
author's explicit validation in the live journal portal. All main/SI files
must be reviewed as anonymous; author identity belongs only on named files.
"""
    (OUT / "jict_short_upload_manifest.md").write_text(manifest, encoding="utf-8")
    print(f"JICT SHORT PACKAGE: PASS (reviewer={n} pages, anonymous; original R9 proofs + Appendix G; complete identified/anonymous upload manifest)")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--preview-only", action="store_true", help="skip supplement generation")
    args = p.parse_args()
    build(require_supplement=not args.preview_only)
