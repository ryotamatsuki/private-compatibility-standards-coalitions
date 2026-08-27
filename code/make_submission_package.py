from __future__ import annotations

from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "submission" / "generated"
ZIP_PATH = OUT / "replication_package_anonymous.zip"

STATIC_FILES = [
    "Makefile",
    "requirements.txt",
    "code/README.md",
    "code/canonical.py",
    "code/make_figures.py",
    "code/make_tables.py",
    "code/verify_symbolic.py",
    "code/verify_welfare_inequalities.py",
    "code/verify_numeric.py",
    "docs/CANONICAL_MODEL.md",
    "docs/THEOREM_LEDGER.md",
    "paper/main.tex",
    "paper/preamble.tex",
    "paper/notation.tex",
    "paper/references.bib",
]

FORBIDDEN = [
    "ryotamatsuki",
    "github.com/ryotamatsuki",
    "60263857",
    "@users.noreply.github.com",
    "/home/",
    "\\Users\\",
]


def package_files() -> list[tuple[Path, str]]:
    files: list[tuple[Path, str]] = []
    for rel in STATIC_FILES:
        files.append((ROOT / rel, rel))
    for pattern in ("paper/sections/*.tex", "paper/appendix/*.tex"):
        for path in sorted(ROOT.glob(pattern)):
            files.append((path, path.relative_to(ROOT).as_posix()))
    files.append((ROOT / "submission" / "reproducibility_readme.md", "README.md"))
    return files


def assert_anonymous(path: Path, data: bytes) -> None:
    text = data.decode("utf-8", errors="ignore")
    lowered = text.lower()
    for token in FORBIDDEN:
        if token.lower() in lowered:
            raise SystemExit(f"ANONYMIZATION GATE: forbidden token {token!r} in {path}")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    files = package_files()
    for source, _ in files:
        if not source.is_file():
            raise SystemExit(f"Missing replication source: {source}")
        assert_anonymous(source, source.read_bytes())

    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for source, arcname in files:
            data = source.read_bytes()
            info = zipfile.ZipInfo(arcname, date_time=(2026, 8, 27, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, data)

    if ZIP_PATH.stat().st_size == 0:
        raise SystemExit("Replication archive is empty")
    print(f"ANONYMOUS REPLICATION PACKAGE: PASS ({ZIP_PATH})")


if __name__ == "__main__":
    main()
