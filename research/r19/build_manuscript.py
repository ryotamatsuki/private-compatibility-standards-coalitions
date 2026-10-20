"""Build a research proposal from immutable R9 sources, never inherited edits."""
from pathlib import Path
import hashlib,json,re,runpy,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
OUT=ROOT/'build'/'r19-manuscript'
R9='08d6e6adb1a90bdf03fa223c0961ac04620f0fa2'

def blob(path):
 return subprocess.check_output(['git','show',f'{R9}:{path}'],cwd=ROOT)

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 sources={}
 paths=[x for x in subprocess.check_output(['git','ls-tree','-r','--name-only',R9,'paper/jict_short'],cwd=ROOT,text=True).splitlines() if x.endswith('.tex') and 'supplement' not in x]
 paths += ['paper/preamble.tex','paper/notation.tex','paper/references.bib']
 for path in paths:
  if path=='paper/jict_short/main.tex':continue
  raw=blob(path);(OUT/Path(path).name).write_bytes(raw)
  sources[path]=hashlib.sha256(raw).hexdigest()
 for name in ('R19_PROPOSED_MANUSCRIPT.tex','R19_AUDITED_EXTENSION.tex','R19_ADDITIONAL_REFERENCES.bib'):
  shutil.copy2(HERE/name,OUT/name)
 # Regenerate original illustration from its immutable code with ONLY its
 # output variable redirected into this research build. Source is unchanged.
 env={'__file__':str(ROOT/'code/revision/make_jict_short_figure.py'),'__name__':'r19_figure_snapshot'}
 exec(compile(blob('code/revision/make_jict_short_figure.py'),'r9_figure','exec'),env)
 env['OUT']=OUT;env['main']()
 shutil.copy2(OUT/'figure_02_selective_erosion.pdf',OUT/'Fig1.pdf')
 sys.path.insert(0,str(ROOT/'code'))
 tables=runpy.run_path(str(ROOT/'code/make_tables.py'))
 table=tables['residual_rent_table']()
 table=table.replace(r'\begin{table}[htbp]',r'\begin{table}[H]')
 old=r'$R(d,v)=\mathscr D$ or $R(d,v)=\mathscr E$ & Boundary case & Indifference in the corresponding comparison \\'
 new=r'$R(d,v)=\mathscr D$ & SU and IS indifferent & Strengthens; no strict ranking \\'+'\n'+r'$R(d,v)=\mathscr E$ & SU strictly preferred & Unchanged \\'
 assert old in table
 (OUT/'table_residual_rent_regions.tex').write_text(table.replace(old,new))
 logs=[]
 for cmd in ([ 'pdflatex','-interaction=nonstopmode','-halt-on-error','R19_PROPOSED_MANUSCRIPT.tex'],['bibtex','R19_PROPOSED_MANUSCRIPT'],['pdflatex','-interaction=nonstopmode','-halt-on-error','R19_PROPOSED_MANUSCRIPT.tex'],['pdflatex','-interaction=nonstopmode','-halt-on-error','R19_PROPOSED_MANUSCRIPT.tex']):
  r=subprocess.run(cmd,cwd=OUT,text=True,capture_output=True)
  logs.append({'command':cmd,'exit_code':r.returncode,'output':r.stdout+r.stderr})
  if r.returncode:
   (OUT/'build_log.json').write_text(json.dumps(logs,indent=2));print(r.stdout[-4000:]);raise SystemExit(r.returncode)
 log=(OUT/'R19_PROPOSED_MANUSCRIPT.log').read_text()
 assert not re.search(r'(undefined references|undefined citations|multiply defined|LaTeX Warning: (Reference|Citation).*undefined)',log,re.I)
 if 'Overfull \\hbox' in log:
  print('\n'.join(log[max(0,m.start()-120):m.start()+500] for m in re.finditer('Overfull',log)))
  raise AssertionError('Overfull box; inspect saved TeX log')
 (OUT/'build_log.json').write_text(json.dumps(logs,indent=2))
 (OUT/'immutable_sources.json').write_text(json.dumps({'R9':R9,'sources':sources},indent=2))
 print('R19 proposal compile PASS; original sources snapshotted unchanged; output',OUT/'R19_PROPOSED_MANUSCRIPT.pdf')

if __name__=='__main__':main()
