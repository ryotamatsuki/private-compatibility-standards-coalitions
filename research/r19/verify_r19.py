"""Fail-closed R19 mathematical replay entry point.

The proof remains the written derivation. This command checks symbolic
identities, exact rational certificates, immutable inputs and claim labels.
"""
from pathlib import Path
import hashlib,json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
BASE='6cd349daec244def5cb4ed475cc448ed091b9c22'
NEW='.github/workflows/r19-primitive-theorem-audit.yml'
CHECKS=[
 'theory_work/verify_residual_incidence.py',
 'incidence_work/verify_incidence.py',
 'referee_work/verify_independent_referee.py',
 'replay_work/verify_bertrand_boundary_kinks.py',
 'replay_work/extra_counterfactuals.py',
]

def preserve():
 raw=subprocess.check_output(['git','ls-tree','-r',BASE],cwd=ROOT,text=True)
 count=0
 for line in raw.splitlines():
  meta,path=line.split('\t',1)
  mode,typ,expected=meta.split()
  if typ!='blob':continue
  p=ROOT/path
  assert p.is_file(),f'Missing protected source {path}'
  data=p.read_bytes()
  actual=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
  assert actual==expected,f'Protected source changed: {path}'
  count+=1
 changed=subprocess.check_output(['git','diff','--name-only',BASE,'HEAD'],cwd=ROOT,text=True).splitlines()
 for path in changed:
  assert path.startswith('research/r19/') or path==NEW,f'Unexpected committed change: {path}'
 print(f'Protected R18 Git blobs unchanged: {count}',flush=True)
 return count

def labels():
 ledger=json.loads((HERE/'R19_CLAIMS.json').read_text())
 assert ledger['overall_level']==2 and not ledger['level3_attained'] and not ledger['level4_attained']
 assert ledger['requested_main_theorem']=='NOT_PROVED'
 assert ledger['claims']['R16_nonlinear_example']=='NUMERICAL'
 assert ledger['claims']['all_C3_price_global_uniqueness']=='UNPROVED'
 doc=(HERE/'R19_LEVEL_3_4_FINAL_VERDICT.md').read_text()
 assert 'Level 3 NOT ATTAINED' in doc and 'Level 4 NOT ATTAINED' in doc
 assert r'\newcommand{\RnineteenLevel}{2}' in (HERE/'R19_PROPOSED_MANUSCRIPT.tex').read_text()
 required=['R19_PRIMITIVE_MODEL.md','R19_R18_GAP_DIAGNOSIS.md','R19_EQUILIBRIUM_COMPARATIVE_STATICS.md','R19_ENDOGENOUS_ADOPTION_THEOREM.md','R19_MAIN_THEOREM_AND_PROOFS.md','R19_NOVEL_THEOREM_DISCOVERY.md','R19_PRIOR_ART_ABSORPTION.md','R19_ORIGINAL_NESTING_AND_PRESERVATION.md','R19_ADVERSARIAL_REFEREES.md','R19_LEVEL_3_4_FINAL_VERDICT.md','R19_PROPOSED_MANUSCRIPT.tex']
 assert all((HERE/f).is_file() for f in required)
 # This label check prevents known claim mismatches; it is not semantic
 # certification of novelty, the entire proof, or arbitrary prose.
 print('Required evidence files and proof/numerical/unknown labels consistent',flush=True)

def main():
 n=preserve();labels()
 out=HERE/'verification'
 out.mkdir(exist_ok=True)
 results=[]
 for f in CHECKS:
  r=subprocess.run([sys.executable,str(HERE/f)],cwd=ROOT,text=True,capture_output=True)
  (out/(Path(f).stem+'.stdout.txt')).write_text(r.stdout)
  (out/(Path(f).stem+'.stderr.txt')).write_text(r.stderr)
  results.append({'script':f,'exit_code':r.returncode})
  print(json.dumps(results[-1]),flush=True)
  if r.returncode:
   print(r.stdout[-3000:]);print(r.stderr[-3000:]);raise SystemExit(r.returncode)
 preserve()
 (out/'r19_results.json').write_text(json.dumps({'all_pass':True,'protected_blobs':n,'overall_level':2,'checks':results,'proof_scope':'partial theorem; complete target unproved'},indent=2)+'\n')
 print('R19 exact partial theorem and counterexample certificates PASS; full Level3/4 NOT established',flush=True)

if __name__=='__main__':main()
