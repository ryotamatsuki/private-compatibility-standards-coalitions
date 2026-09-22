# R8 Closure Report — Manuscript Reconstruction

## Decision

**R8 COMPLETE — MANUSCRIPT RECONSTRUCTED UNDER ROUTE B; R9 AUTHORIZED, NOT STARTED**

Input integration commit:

`e7171387f002c4bddac5e7465b56a192fb778056`

Execution branch:

`revision/r8-execution`

Governing workflow:

`research-paper-workflow v2.2 @ 42574d6c5931275ccff3ef7e8b4acc188077332a`

## 1. Reconstruction outcome

The English production manuscript has been rebuilt around the R7-certified Route B claim scope.

The central result is now the conditional residual-rent mechanism

[
W_M^{SU,O}(d)-W^{IS}=-mathscr D+R(d,v),
]

with

[
R(d,v)
=
rac{d[(5-4v)d+2(1-4v)]}{32(1-v)^2}.
]

The main text distinguishes:

- actual SU-to-IS ranking reversal when (R<mathscr D);
- stronger IS incentives without reversal when (mathscr D<R<mathscr E);
- weaker IS incentives when (R>mathscr E).

The certified incomplete-adaptation open set is integrated into the main text. One-way adoption is presented as supporting continuation structure rather than as standalone novelty.

## 2. Scope and negative results

The manuscript now carries the R4–R6 boundaries visibly in the main text:

- the zero-network boundary removes the initial SU advantage while one-way adoption can survive;
- the pre-specified singleton-network alternative removes the initial SU advantage on the old canonical domain;
- the frozen differentiated-demand test removes the political effect in both Cournot and Bertrand while outsider-only adoption remains feasible;
- the symmetric high-F stable-set multiplicity is shown to depend on strict blocking and symmetry-induced indifference;
- the intermediate full-bypass unique-IS application is separated as the more robust institutional implication within the canonical microfoundation.

No priority claim, first-best claim, demand/competition portability claim, or general statement that private compatibility promotes formal harmonization is made.

## 3. Manuscript architecture

The English production paper now has:

1. Introduction centered on the conditional research question and success/failure regions;
2. Related Literature organized around parent-class absorption;
3. Model separating full bypass from residual-cost adaptation;
4. compact Cournot building blocks, with routine derivations in Appendix A;
5. Private Adoption as supporting structure;
6. Private Adaptation and Government Incentives as the central residual-rent section;
7. Coalition-Stability Application explicitly scoped to the full-bypass endpoint;
8. Scope and Robustness integrating R4/R5/R6;
9. Discussion focused on interpretation and limits;
10. a short conditional Conclusion.

Appendix D records the residual-cost equilibrium and adoption-threshold derivations. Appendix E records the robustness and institutional boundary calculations.

The Japanese translation in `paper-ja/` was intentionally not updated in R8. The English production manuscript is the canonical R8 artifact.

## 4. Reproducible presentation

The figure generator now produces:

- game timing;
- residual-rent success/intermediate/failure regions;
- the full-bypass fixed-cost institutional application;
- an assumption-dependence hierarchy.

The table generator now additionally produces:

- the residual-rent government-incentive classification;
- the scope/robustness matrix.

Figures are illustrations of certified analytical results, not proof substitutes.

## 5. Claim-scope audit

`code/revision/check_r8_claim_scope.py` enforces the R7 manuscript scope in CI.

It requires the residual-rent result, incomplete-adaptation statement, R5 non-portability, blocking-rule limitation, and Appendix D/E integration. It rejects prohibited overclaims and the old partner-selection-first architecture.

## 6. Verification status

Before this closure record, branch Paper CI #296 passed all substantive reconstruction gates:

- R1–R7 mathematical regression checks;
- R7 Lean verification;
- R8 manuscript claim-scope audit;
- symbolic and numerical verification;
- figure generation;
- table generation and syntax checks;
- canonical anonymous manuscript compilation;
- submission-package regression audit;
- clean-room source QA;
- clean-room replication-package QA;
- artifact uploads.

The final closure-record commit must pass the same full CI before PR integration. R8 is considered repository-closed only after its PR is merged to `revision/research-track` and post-merge integration CI succeeds.

## 7. Next stage

R9 is authorized only for final mathematical/claim/reproducibility audit and journal repositioning. No R9 work is performed in R8.
