from __future__ import annotations

from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SUB = ROOT / "submission"
GEN = SUB / "generated"


def fail(message: str) -> None:
    raise SystemExit(f"JICT SUBMISSION GATE: FAIL — {message}")


def pdf_text(path: Path) -> str:
    return subprocess.run(
        ["pdftotext", str(path), "-"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout


def pdf_pages(path: Path) -> int:
    info = subprocess.run(
        ["pdfinfo", str(path)],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    match = re.search(r"^Pages:\s+(\d+)\s*$", info, flags=re.MULTILINE)
    if not match:
        fail(f"cannot read page count from {path.name}")
    return int(match.group(1))


def check_flat_zip(path: Path, require_bib: bool = False) -> None:
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        if not names:
            fail(f"empty source archive: {path.name}")
        if any("/" in name or "\\" in name for name in names):
            fail(f"source archive contains subfolders: {path.name}")
        if "main.tex" not in names:
            fail(f"source archive missing main.tex: {path.name}")
        if require_bib and "references.bib" not in names:
            fail(f"source archive missing references.bib: {path.name}")
        for name in names:
            if not name.endswith((".tex", ".bib", ".txt", ".md")):
                continue
            text = zf.read(name).decode("utf-8", errors="ignore")
            low = text.lower()
            for token in (
                "ryota matsuki",
                "ryota.matsuki@gmail.com",
                "github.com/ryotamatsuki",
                "60263857",
                "@users.noreply.github.com",
            ):
                if token in low:
                    fail(f"identity leak {token!r} in {path.name}:{name}")
            for match in re.finditer(r"\\input\{([^}]+)\}", text):
                if "/" in match.group(1) or "\\" in match.group(1):
                    fail(f"subfolder input in {path.name}:{name}")
            for match in re.finditer(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", text):
                if "/" in match.group(1) or "\\" in match.group(1):
                    fail(f"subfolder figure path in {path.name}:{name}")


def main() -> None:
    required = [
        GEN / "jict_manuscript.pdf",
        GEN / "jict_online_supplement.pdf",
        GEN / "jict_title_page.pdf",
        GEN / "jict_cover_letter.pdf",
        GEN / "jict_source.zip",
        GEN / "jict_online_supplement_source.zip",
        SUB / "jict_metadata.md",
    ]
    for path in required:
        if not path.is_file() or path.stat().st_size == 0:
            fail(f"missing or empty artifact: {path}")

    manuscript = pdf_text(GEN / "jict_manuscript.pdf")
    supplement = pdf_text(GEN / "jict_online_supplement.pdf")
    title_page = pdf_text(GEN / "jict_title_page.pdf")
    cover = pdf_text(GEN / "jict_cover_letter.pdf")

    for name, text in (("manuscript", manuscript), ("supplement", supplement)):
        low = text.lower()
        for token in (
            "ryota matsuki",
            "ryota.matsuki@gmail.com",
            "independent researcher",
            "github.com/ryotamatsuki",
        ):
            if token in low:
                fail(f"identity leak in anonymous {name}: {token}")
        if "international journal of industrial organization" in low:
            fail(f"stale IJIO journal name in anonymous {name}")

    for required_phrase in (
        "Ryota Matsuki",
        "Independent Researcher",
        "ryota.matsuki@gmail.com",
        "Generative AI / LLM use",
        "Competing interests",
        "Funding",
    ):
        if required_phrase.lower() not in title_page.lower():
            fail(f"JICT title page missing {required_phrase!r}")

    if "Journal of Industry, Competition and Trade" not in cover:
        fail("JICT cover letter has wrong journal")
    if "International Journal of Industrial Organization" in cover:
        fail("JICT cover letter contains stale IJIO journal name")

    pages = pdf_pages(GEN / "jict_manuscript.pdf")
    if pages > 40:
        fail(f"reviewer manuscript exceeds JICT 40-page maximum: {pages}")

    supplement_pages = pdf_pages(GEN / "jict_online_supplement.pdf")
    if supplement_pages < 1:
        fail("online supplement is empty")

    check_flat_zip(GEN / "jict_source.zip", require_bib=True)
    check_flat_zip(GEN / "jict_online_supplement_source.zip", require_bib=False)

    if "Online Supplement" not in manuscript:
        fail("reviewer manuscript does not signal separated technical supplement")
    if "technical derivations" not in supplement.lower():
        fail("supplement front matter missing scope statement")

    print(
        "JICT SUBMISSION GATE: PASS "
        f"(reviewer manuscript={pages} pages; supplement={supplement_pages} pages)"
    )


if __name__ == "__main__":
    main()
