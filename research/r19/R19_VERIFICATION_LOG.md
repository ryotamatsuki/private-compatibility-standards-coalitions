# R19 verification and epistemic log — 2026-10-20

Input R18 SHA `6cd349daec244def5cb4ed475cc448ed091b9c22`; original PR34
head `08d6e6adb1a90bdf03fa223c0961ac04620f0fa2`. R18 Actions run
39409427371 actually completed SUCCESS on the input SHA, with both the
rational and inherited replay jobs. This historical result was retrieved,
not inferred from documentation. Full API input evidence is retained.

## Local execution actually performed

- `python research/r19/replay_work/replay_inherited.py`: 18/18 inherited
  commands exit0; all191 tracked baseline source files unchanged. Exact
  commands, versions, wall times, complete stdout/stderr and classifications
  are in replay_results.json and adjacent logs.
- `python research/r19/verify_r19.py`: exact symbolic/rational partial
  theorem, independent referee expansion, incidence counterexample,
  arbitrary-kink price entry polytope and additional counterfactuals pass.
  The driver verifies original Git blob SHA1 identities, not just current
  file-before/file-after equality.
- Rational R16 full price certificate:19 markets,211 feasible deviation
  candidates,171 new arbitrary-kink entry bounds; minimum slack
  `33819/12831625`. At d=0:15 labeled market configurations,171 global
  candidates,135 kink-entry bounds. Distinct counting conventions are
  explained by the saved scripts; do not equate stage-cache and global
  audit configuration counts.
- R9/R16 full8SU/64SW investment comparisons, original negative tests,
  R10 CS withdrawal and R13 consumer optimization replayed. Mixed
  investment uniqueness follows from all-profile dominance, not merely
  enumerating pure Nash. No mixed-price uniqueness is claimed.
- R15/R16 nonlinear outputs re-executed numerically. They remain numerical,
  not exact interval root certificates or a new C3 global price theorem.

The theorem and independent audit use SymPy1.13.3, NumPy2.1.3,
SciPy1.14.1, Python3.12. Plotting uses Matplotlib3.10.8. The new CI pins
the same stack. Symbolic assertions support the written proofs; test
success is not independent proof of priority or the whole R19 target.

## Manuscript build

`python research/r19/build_manuscript.py` snapshots the immutable PR34
body and then compiles the single new audited section. Existing files
are untouched. The local environment initially lacked elsarticle.cls;
system-package installation was unavailable, so the official
STM-Document-Engineering elsarticle Git repository at
`04aee43a9049051128c5d58b617dcd05e34df8b4` supplies local TEXINPUTS and
BSTINPUTS, without changes to this project's inherited source. CI uses
its separately installed TeX publisher package. A first layout pass found
one overfull new paragraph; its wording was shortened and rebuilt.

Final compile and render evidence is recorded in build/r19-manuscript,
with undefined-reference/citation/duplicate and overfull checks failing
closed in the builder. Generated build files are CI artifacts, not
production manuscript replacements. Pagination is reported only; no
journal-length or journal-readiness assertion is made.

## Independent review

Separate theory, replay, literature and hostile-audit roles were used.
The hostile agent wrote five disciplinary referee positions, received an
explicit author response and reassessed it independently. Full reports
and its independently derived verifier are retained. These are internal
independent-agent audits, not external journal referee reports.

## GitHub Actions distinction

New R19 Actions status must be read from the actual resulting branch
commit/run. This local log makes no prospective success claim. The PR
body and final user report identify the actual remote commit and runs.
No merge or submission occurs. Highest joint grade remains2; both full
Level3 and cumulative Level4 remain unmet regardless of CI success.
