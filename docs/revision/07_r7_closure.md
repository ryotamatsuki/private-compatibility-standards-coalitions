# R7 Closure Report — Novelty Reassessment and Theory Re-Certification

## Decision

[
oxed{	extbf{R7 COMPLETE — ROUTE B: LIMITED GENERALIZATION}}
]

R8 is authorized but not started.

Input integration commit:

`b45798f003db52a980f8f9b21186f054ebe62007`

Execution branch:

`revision/r7-execution`

Governing workflow:

`research-paper-workflow v2.2 @ 42574d6c5931275ccff3ef7e8b4acc188077332a`

## 1. Mathematical re-certification

R7 used a new clean-room evaluator:

`code/revision/check_r7_cleanroom.py`

It does not import `code/canonical.py` or the R2–R6 verification modules. It reconstructs the relevant Cournot first-order systems, welfare blocks, partial-adoption state, frozen R5 differentiated-demand witness calculations, and R6 deviation identities independently.

The clean-room route re-certified the surviving canonical mechanism and found no foundational mathematical contradiction.

## 2. Formal verification

Formal verification was judged applicable because claim scope depends on quantified inequalities, strict boundary logic, and exact logical implications.

Artifacts:

- `formal/r7/lean-toolchain`
- `formal/r7/lakefile.toml`
- `formal/r7/R7Formal.lean`

Lean 4 + mathlib verifies without `sorry` or `admit`:

1. `FV1_zeroNetworkGapNegative`;
2. `FV2_residualRentStrictlyIncreasing`;
3. `FV3_postGapNegative`;
4. `FV4_preferenceEffect`;
5. `FV5_indifferenceSeparatesBlockingRules`.

The formal layer certifies only the stated algebra/order/logical cores. It is not treated as evidence for economic novelty, exhaustive equilibrium enumeration, the R5 Bernstein certificate, or a general theorem beyond the mapped assumptions.

## 3. Novelty re-kill

See:

`docs/revision/07_novelty_reassessment.md`

The proposition-level comparison yields:

- G1 one-way private adoption: substantial overlap with converter/one-way-compatibility and fixed-cost-scope parent literatures; retained as supporting structure, not headline novelty.
- G2 residual-rent government-ranking partition: no direct absorption found in the closest located parent literature, but the result remains tied to the canonical microfoundation.
- R5: binding negative portability evidence. The political sign fails in the one pre-specified differentiated-demand environment under both Cournot and Bertrand while one-way adoption remains possible.
- R6: high-F symmetric stable-set multiplicity is blocking-rule/symmetry dependent; intermediate unique-IS preference gaps are comparatively more robust within the canonical model.

No priority or "first" claim is certified.

## 4. Final claim freeze

See:

`docs/revision/07_theory_recertification.md`

R8 may build around:

1. selection-free one-way adoption as supporting structure;
2. the canonical residual-rent partition separating actual reversal, incentive strengthening without reversal, and incentive weakening;
3. the nonempty open set with incomplete adaptation and actual reversal;
4. explicit zero-network, singleton-network, differentiated-demand, and blocking-rule boundaries;
5. the institutional contrast between robust intermediate unique-IS gaps and fragile symmetric high-F stable-set multiplicity.

R8 may not claim:

- that private compatibility generally promotes formal standardization;
- demand-system or competition-form independence;
- novelty of one-way compatibility/adoption itself;
- network-effect irrelevance for the initial political ranking;
- universal robustness of the three-SU high-F stable set;
- unrestricted first-best welfare;
- necessity of R2 sufficient conditions;
- a "first paper to show" priority statement.

## 5. Route decision

Route A is rejected because R5 demonstrates substantive non-portability of the political preference effect.

Route C is also rejected because R3 does more than local continuity or payoff relabeling: it supplies an equilibrium-derived residual-rent function, exact success/intermediate/failure thresholds, and a nonempty open incomplete-adaptation witness.

No foundational proof failure or complete prior-art absorption remains, so Route D is not warranted.

Therefore:

[
oxed{	extbf{Route B — LIMITED GENERALIZATION}}
]

The manuscript should be reconstructed in R8 as a conditional mechanism paper, not as a general-theory-first paper.

## 6. Reproducibility and merge gate

The R7 checks are integrated into `.github/workflows/paper-ci.yml`:

- R7 clean-room theory re-certification;
- Lean installation;
- targeted R7 formal verification;
- no-`sorry`/`admit` check.

Before integration, the execution branch must pass the complete repository CI, including all inherited R1–R6 checks, LaTeX compile, symbolic/numerical verification, figure/table generation, submission-package audit, source QA, replication-package QA, and artifact upload.

R7 is formally closed only after the R7 PR is merged into `revision/research-track` and the post-merge integration CI succeeds.
