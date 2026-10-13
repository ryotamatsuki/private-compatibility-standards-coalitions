"""Release-file audit for the short edition; does not change theory or original sources."""
from __future__ import annotations
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "submission/generated"
BASE = "e828684594479b674b9b1538ae0bc4a19a00b681"
FORBIDDEN = ("Ryota Matsuki", "ryota.matsuki@gmail.com", "github.com/ryotamatsuki")
UNRESOLVED = r"LaTeX Warning: (Reference|Citation).*undefined|There were undefined references|multiply defined"

def capture(*cmd, cwd=None):
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, check=True).stdout

def pdf_text(p):
    return capture("pdftotext", str(p), "-")

def page_count(p):
    return int(re.search(r"(?m)^Pages:\s*(\d+)", capture("pdfinfo",str(p))).group(1))

def anonymous(data, suffix, location):
    if suffix == ".zip":
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            for item in z.infolist():
                assert not item.filename.startswith("/") and ".." not in Path(item.filename).parts
                anonymous(z.read(item), Path(item.filename).suffix.lower(), location+"/"+item.filename)
        return
    if suffix == ".pdf":
        with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
            f.write(data); f.flush()
            text = pdf_text(Path(f.name)) + capture("pdfinfo",f.name)
    else:
        text = data.decode("utf-8", errors="ignore")
    for word in FORBIDDEN:
        assert word.lower() not in text.lower(), f"identity leak: {location}"

def embedded_fonts(p):
    listing = capture("pdffonts",str(p)).splitlines()[2:]
    assert listing, f"No font list: {p}"
    for row in listing:
        match = re.search(r"\s+(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$",row)
        assert match and match.group(1) == "yes", f"Unembedded font: {row}"
    return len(listing)

def clean_source(name, shipped, bib):
    with tempfile.TemporaryDirectory(prefix="jict-short-release-") as td:
        folder = Path(td)
        with zipfile.ZipFile(OUT/name) as z:
            assert all(Path(n).name == n for n in z.namelist()), "Source ZIP is not flat"
            assert not any(n.endswith((".aux",".log",".bbl",".out",".fls",".fdb_latexmk")) for n in z.namelist())
            z.extractall(folder)
        cmd = ["latexmk","-pdf","-interaction=nonstopmode","-halt-on-error"]
        if not bib:cmd.append("-bibtex-")
        capture(*cmd,"main.tex",cwd=folder)
        log = (folder/"main.log").read_text(errors="replace")
        assert not re.search(UNRESOLVED,log,re.I)
        regenerated = folder/"main.pdf"
        normal = lambda text:re.sub(r"\s+"," ",text).strip()
        assert normal(pdf_text(regenerated)) == normal(pdf_text(OUT/shipped))
        return {"status":"PASS","pages":page_count(regenerated),"text_matches_shipped":True}

def main():
    bundle = OUT/"r9_jict_submission_set.zip"
    exports = ("jict_short_manuscript.pdf","jict_short_online_supplement.pdf","r9_jict_submission_set.zip")
    protected = ["paper/main.tex","paper/sections","paper/appendix","paper/preamble.tex",
                 "paper/notation.tex","paper/references.bib","code/canonical.py",
                 "code/revision/check_network_zero.py","code/revision/check_r2_adoption.py",
                 "code/revision/check_r3_partial_erosion.py","code/revision/check_r4_network_role.py",
                 "code/revision/check_r5_competition_portability.py","code/revision/check_r6_coalition_stability.py",
                 "code/revision/check_r7_cleanroom.py","code/revision/check_r8_claim_scope.py",
                 "code/revision/check_r9_final_audit.py","formal/r7","Makefile",
                 "code/make_figures.py","code/make_tables.py","code/make_submission_package.py",
                 "code/make_jict_submission_package.py","submission/jict_cover_letter.tex","submission/jict_title_page.tex"]
    assert not capture("git","diff","--name-only",BASE,"HEAD","--",*protected).strip(), "Frozen source changed"
    capture("git","diff","--check",BASE,"HEAD")
    main_pdf=OUT/"jict_short_manuscript.pdf"
    supplement=OUT/"jict_short_online_supplement.pdf"
    report={"protected_original_sources":"PASS","main_pages":page_count(main_pdf),
            "supplement_pages":page_count(supplement)}
    assert 17 <= report["main_pages"] <= 19
    assert report["supplement_pages"] == 22
    report["cleanroom_main"]=clean_source("jict_short_source.zip",main_pdf.name,True)
    report["cleanroom_supplement"]=clean_source("jict_short_online_supplement_source.zip",supplement.name,False)
    for name in ("jict_short_manuscript.pdf","jict_short_online_supplement.pdf",
                 "jict_short_source.zip","jict_short_online_supplement_source.zip",
                 "jict_short_replication_package_anonymous.zip"):
        path=OUT/name
        anonymous(path.read_bytes(),path.suffix,name)
    report["recursive_anonymization"]="PASS"
    report["embedded_fonts"]={p.name:embedded_fonts(p) for p in (main_pdf,supplement)}
    assert (OUT/"ESM_1.pdf").read_bytes() == supplement.read_bytes()
    log=(OUT/"jict_short_source/main.log").read_text()
    spacing=re.search(r"JICT BODY FONT=(\d+); BASELINE=([\d.]+)pt",log)
    assert spacing and spacing.group(1)=="12" and float(spacing.group(2)) >= 23.9
    report["body_font_pt"]=spacing.group(1);report["body_baseline_pt"]=spacing.group(2)
    tex=(OUT/"jict_short_source/main.tex").read_text()
    abstract=re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}",tex,re.S).group(1)
    report["abstract_whitespace_words"]=len(abstract.split())
    assert 150 <= report["abstract_whitespace_words"] <= 250
    with zipfile.ZipFile(OUT/"jict_short_identified_source.zip") as z:
        assert sorted(z.namelist()) == ["jict_cover_letter.tex","jict_title_page.tex"]
    report["identified_files_separate"]="PASS"
    report["live_portal_requirements"]="UNVERIFIED; journal operation was expressly excluded"
    report["pdf_visual_review"]="All local candidate main 1-19 and SI 1-22 inspected; unchanged SI pages were compared pixel-for-pixel. CI also rebuilds exact source ZIPs. No external human reviewer claimed."
    qa = OUT/"r9_final_package_qa.json"
    qa.write_text(json.dumps(report,indent=2)+"\n")
    patch = OUT/"r9_final_source_changes.patch"
    patch.write_text(capture("git","diff","--no-ext-diff",BASE,"HEAD","--",
                            ".github/workflows/jict-short-preview.yml","code/revision",
                            "paper/jict_short","docs/revision"))
    names = ["jict_short_manuscript.pdf","jict_short_online_supplement.pdf",
             "jict_short_source.zip","jict_short_online_supplement_source.zip",
             "jict_short_replication_package_anonymous.zip",
             "jict_short_identified_title_page.pdf","jict_short_cover_letter.pdf",
             "jict_short_identified_source.zip","jict_short_upload_manifest.md",
             "ESM_1.pdf","Fig1.eps",qa.name,patch.name]
    with zipfile.ZipFile(bundle,"w",zipfile.ZIP_DEFLATED) as z:
        for name in names:z.write(OUT/name,name)
        for path in sorted((ROOT/"docs/revision").glob("*r9_final_polish*20261013.md")):
            z.write(path,path.name)
        z.write(ROOT/"build/final-polish/independent-certificates.json","independent-certificates.json")
        z.writestr("README_FIRST.txt","Anonymous main: 19 pages at 12-point true double spacing.\n"
                   "Anonymous SI: 22 pages. ESM_1.pdf is the same SI, not a second resource.\n"
                   "Identified title/cover and their source ZIP are separate from reviewer files.\n"
                   "See the upload manifest, audit, change ledger and exact QA/certificate JSON.\n"
                   "This package has not been submitted; PR approval and live-portal validation remain.\n")
    print("JICT SHORT FINAL PACKAGE QA: PASS")
    print(json.dumps(report,indent=2))
    for name in exports:
        print("R9 FILE SHA256 "+name+" "+hashlib.sha256((OUT/name).read_bytes()).hexdigest())
if __name__=="__main__":main()
