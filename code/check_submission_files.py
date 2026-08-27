from __future__ import annotations

from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SUB = ROOT / "submission"
GEN = SUB / "generated"


def fail(message: str) -> None:
    raise SystemExit(f"SUBMISSION GATE: FAIL — {message}")


def read_pdf_text(path: Path) -> str:
    result = subprocess.run(["pdftotext", str(path), "-"], check=True, capture_output=True, text=True)
    return result.stdout


def pdfinfo(path: Path) -> str:
    return subprocess.run(["pdfinfo", str(path)], check=True, capture_output=True, text=True).stdout


def main() -> None:
    required = [
        GEN / "manuscript.pdf",
        GEN / "cover_letter.pdf",
        GEN / "title_page.pdf",
        GEN / "replication_package_anonymous.zip",
        SUB / "highlights.txt",
    ]
    for path in required:
        if not path.is_file() or path.stat().st_size == 0:
            fail(f"missing or empty {path}")

    highlights = [line.strip() for line in (SUB / "highlights.txt").read_text().splitlines() if line.strip()]
    if not 3 <= len(highlights) <= 5:
        fail("highlights must contain 3–5 nonempty lines")
    too_long = [(len(line), line) for line in highlights if len(line) > 85]
    if too_long:
        fail(f"highlight exceeds 85 characters: {too_long}")

    manuscript_text = read_pdf_text(GEN / "manuscript.pdf")
    if "Anonymous Author" not in manuscript_text:
        fail("reviewer manuscript is not visibly anonymous")
    for token in ("TBD -- USER", "ryotamatsuki", "github.com/ryotamatsuki", "/home/"):
        if token.lower() in manuscript_text.lower():
            fail(f"reviewer manuscript contains forbidden token {token!r}")
    for required_phrase in (
        "Data availability",
        "Code availability",
        "Declaration of generative AI",
    ):
        if required_phrase not in manuscript_text:
            fail(f"reviewer manuscript missing {required_phrase!r}")

    info = pdfinfo(GEN / "manuscript.pdf")
    author_lines = [line for line in info.splitlines() if line.startswith("Author:")]
    if author_lines and "Anonymous Author" not in author_lines[0] and author_lines[0].split(":", 1)[1].strip():
        fail(f"unexpected PDF author metadata: {author_lines[0]}")
    (GEN / "manuscript_pdfinfo.txt").write_text(info)

    with zipfile.ZipFile(GEN / "replication_package_anonymous.zip") as zf:
        names = zf.namelist()
        if any(name.startswith(".git") or "/.git" in name for name in names):
            fail("replication archive contains git history")
        for name in names:
            data = zf.read(name).decode("utf-8", errors="ignore").lower()
            for token in ("ryotamatsuki", "github.com/ryotamatsuki", "60263857", "@users.noreply.github.com", "/home/"):
                if token.lower() in data:
                    fail(f"replication archive identity leak {token!r} in {name}")

    source_text = "\n".join(
        p.read_text(errors="ignore")
        for p in [ROOT / "paper" / "main.tex", *sorted((ROOT / "paper" / "sections").glob("*.tex")), *sorted((ROOT / "paper" / "appendix").glob("*.tex"))]
    )
    residue = re.findall(r"\b(?:TODO|FIXME|XXX|placeholder)\b", source_text, flags=re.IGNORECASE)
    if residue:
        fail(f"manuscript source contains development residue: {residue}")

    print("SUBMISSION FILE GATE: PASS")


if __name__ == "__main__":
    main()
