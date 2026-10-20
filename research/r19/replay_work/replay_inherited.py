"""R19 read-only replay of inherited mathematical checks.

Only research/r19/replay_work is written. Output is evidence of executing
the named checks, not an upgrade of numerical examples into general proofs.
"""
from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import platform
import subprocess
import sys
import time
import sympy
import numpy
import scipy

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
BASE = "6cd349daec244def5cb4ed475cc448ed091b9c22"
CHECKS = [
    ("r9_final", "code/revision/check_r9_final_audit.py", "exact symbolic and source scope"),
    ("r9_zero_network_failure", "code/revision/check_network_zero.py", "analytic counterexample"),
    ("r2_adoption", "code/revision/check_r2_adoption.py", "exact symbolic"),
    ("r3_partial_erosion", "code/revision/check_r3_partial_erosion.py", "exact symbolic residual boundary"),
    ("r5_portability_failure", "code/revision/check_r5_competition_portability.py", "historical failure under its own declared surplus convention"),
    ("r6_coalition", "code/revision/check_r6_coalition_stability.py", "exact limited original coalition concept"),
    ("r7_cleanroom", "code/revision/check_r7_cleanroom.py", "exact independent original primitives"),
    ("r10_welfare_correction", "research/r15/audit_r10_welfare_convention.py", "exact CS correction and withdrawal"),
    ("r13_consumers", "research/r13/verify_consumer_microfoundation.py", "exact symbolic consumer identities"),
    ("r12_cournot_investment", "research/r12/verify_r9_generic_adoption_dominance.py", "exact 8 SU / 64 SW; all unilateral investment deviations"),
    ("r12_cournot_incidence", "research/r12/verify_r9_nonmonotone_incidence.py", "exact interval Bernstein/Riemann certificate"),
    ("r15_nonlinear_cournot", "research/r15/verify_infinite_dimensional_neighborhood.py", "numerical nonlinear FOCs/adoption; exact baseline Jacobians"),
    ("r16_bertrand_investment", "research/r16/verify_bertrand_r13_full_game.py", "exact interior FOCs and all investment deviations"),
    ("r16_global_price", "research/r16/verify_global_bertrand_price_deviations.py", "exact all active-set unilateral price deviations from positive candidate"),
    ("r16_boundary_entry", "research/r16/verify_bertrand_no_boundary_equilibria.py", "exact entry at restricted-active-set stationary candidates; see diagnostic caveat"),
    ("r16_integrated_incidence", "research/r16/verify_integrated_bertrand_incidence.py", "exact interval Bernstein/Riemann"),
    ("r16_nonlinear_bertrand", "research/r16/verify_nonlinear_bertrand_consumer.py", "numerical interior FOCs/adoption, not global nonlinear price proof"),
    ("r18", "research/r18/verify_r18.py", "exact full investment games and R18 response bounds"),
]

def inherited_hashes():
    paths = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", BASE], cwd=ROOT, text=True).splitlines()
    return {path: hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
            for path in paths if (ROOT/path).is_file()}

def run(spec):
    name, path, status = spec
    start = time.monotonic()
    result = subprocess.run([sys.executable, path], cwd=ROOT, capture_output=True, text=True)
    elapsed = time.monotonic()-start
    (OUT/f"{name}.stdout.txt").write_text(result.stdout)
    (OUT/f"{name}.stderr.txt").write_text(result.stderr)
    record = {"name":name,"command":["python",path],"exit_code":result.returncode,
              "seconds":round(elapsed,3),"proof_status":status,
              "stdout":f"{name}.stdout.txt","stderr":f"{name}.stderr.txt"}
    print(json.dumps(record),flush=True)
    return record

def main():
    before = inherited_hashes()
    (OUT/"inherited_sha256.json").write_text(json.dumps(before,indent=2)+"\n")
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(run,CHECKS))
    after = inherited_hashes()
    assert before == after, "An inherited source changed during replay"
    report={"baseline":BASE,"python":platform.python_version(),
            "versions":{"sympy":sympy.__version__,"numpy":numpy.__version__,"scipy":scipy.__version__},
            "inherited_files_hashed":len(before),"inherited_sources_unchanged":True,
            "results":results,"all_pass":all(x["exit_code"]==0 for x in results)}
    (OUT/"replay_results.json").write_text(json.dumps(report,indent=2)+"\n")
    assert report["all_pass"], "At least one inherited script failed; inspect saved output"
    print("R19 inherited read-only replay PASS",flush=True)

if __name__=="__main__":
    main()
