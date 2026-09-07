from __future__ import annotations

from collections import deque
from pathlib import Path
import re
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
OUT_ROOT = ROOT / "submission" / "generated"
OUT_DIR = OUT_ROOT / "ijio_em_source"
ZIP_PATH = OUT_ROOT / "ijio_em_source.zip"

AUTHOR_BLOCK = r"""\author[aff1]{Ryota Matsuki\corref{cor1}}
\ead{ryota.matsuki@gmail.com}
\cortext[cor1]{Corresponding author}
\address[aff1]{Independent Researcher, Matsuyama, Ehime, Japan}"""

INPUT_RE = re.compile(r"\\input\{([^}]+)\}")
GRAPHICS_RE = re.compile(r"(\\includegraphics(?:\[[^\]]*\])?\{)([^}]+)(\})")
BIB_RE = re.compile(r"\\bibliography\{([^}]+)\}")


def fail(message: str) -> None:
    raise SystemExit(f"IJIO EM SOURCE PACKAGE: FAIL — {message}")


def resolve_input(name: str) -> Path:
    candidate = PAPER / name
    if candidate.suffix == "":
        candidate = candidate.with_suffix(".tex")
    if not candidate.is_file():
        fail(f"missing input dependency: {name}")
    return candidate


def resolve_graphic(name: str) -> Path:
    candidate = PAPER / name
    if candidate.is_file():
        return candidate
    if candidate.suffix == "":
        for suffix in (".pdf", ".png", ".jpg", ".jpeg", ".eps"):
            test = candidate.with_suffix(suffix)
            if test.is_file():
                return test
    fail(f"missing figure dependency: {name}")


def register_basename(path: Path, seen: dict[str, Path]) -> None:
    previous = seen.get(path.name)
    if previous is not None and previous != path:
        fail(f"basename collision: {previous} and {path}")
    seen[path.name] = path


def rewrite_tex(path: Path, text: str, queue: deque[Path], seen: dict[str, Path]) -> str:
    if path == PAPER / "main.tex":
        if r"\author{Anonymous Author}" not in text:
            fail("canonical anonymous author marker not found in paper/main.tex")
        text = text.replace(r"\author{Anonymous Author}", AUTHOR_BLOCK, 1)

    def input_repl(match: re.Match[str]) -> str:
        dep = resolve_input(match.group(1))
        register_basename(dep, seen)
        queue.append(dep)
        return rf"\input{{{dep.stem}}}"

    text = INPUT_RE.sub(input_repl, text)

    def graphic_repl(match: re.Match[str]) -> str:
        dep = resolve_graphic(match.group(2))
        register_basename(dep, seen)
        shutil.copy2(dep, OUT_DIR / dep.name)
        return f"{match.group(1)}{dep.name}{match.group(3)}"

    text = GRAPHICS_RE.sub(graphic_repl, text)

    for match in BIB_RE.finditer(text):
        for bib_name in (part.strip() for part in match.group(1).split(",")):
            dep = PAPER / (bib_name if bib_name.endswith(".bib") else f"{bib_name}.bib")
            if not dep.is_file():
                fail(f"missing bibliography dependency: {bib_name}")
            register_basename(dep, seen)
            shutil.copy2(dep, OUT_DIR / dep.name)

    return text


def main() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)

    queue: deque[Path] = deque([PAPER / "main.tex"])
    processed: set[Path] = set()
    seen: dict[str, Path] = {}

    while queue:
        path = queue.popleft().resolve()
        if path in processed:
            continue
        if not path.is_file():
            fail(f"missing source file: {path}")
        register_basename(path, seen)
        text = path.read_text(encoding="utf-8")
        rewritten = rewrite_tex(path, text, queue, seen)
        (OUT_DIR / path.name).write_text(rewritten, encoding="utf-8")
        processed.add(path)

    main_tex = (OUT_DIR / "main.tex").read_text(encoding="utf-8")
    for required in (
        "Ryota Matsuki",
        "Independent Researcher, Matsuyama, Ehime, Japan",
        "ryota.matsuki@gmail.com",
        "Corresponding author",
    ):
        if required not in main_tex:
            fail(f"identified main.tex is missing {required!r}")
    if "Anonymous Author" in main_tex:
        fail("identified main.tex still contains Anonymous Author")

    for tex_path in OUT_DIR.glob("*.tex"):
        text = tex_path.read_text(encoding="utf-8")
        for match in INPUT_RE.finditer(text):
            if "/" in match.group(1) or "\\" in match.group(1):
                fail(f"subfolder input remains in {tex_path.name}: {match.group(1)}")
        for match in GRAPHICS_RE.finditer(text):
            if "/" in match.group(2) or "\\" in match.group(2):
                fail(f"subfolder graphic path remains in {tex_path.name}: {match.group(2)}")

    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(OUT_DIR.iterdir()):
            if path.is_file():
                zf.write(path, arcname=path.name)

    with zipfile.ZipFile(ZIP_PATH) as zf:
        names = zf.namelist()
        if not names or any("/" in name or "\\" in name for name in names):
            fail("archive is empty or contains a directory structure")

    print(f"IJIO EM SOURCE PACKAGE: PASS ({ZIP_PATH.relative_to(ROOT)})")
    print("Included files:")
    for name in sorted(path.name for path in OUT_DIR.iterdir() if path.is_file()):
        print(f"  {name}")


if __name__ == "__main__":
    main()
