# R7 — Novelty Reassessment and Theory Re-Certification: Design Freeze

## Status

- Stage: R7
- Branch: `revision/r7-execution`
- Input integration commit: `b45798f003db52a980f8f9b21186f054ebe62007`
- Governing workflow: `research-paper-workflow v2.2 @ 42574d6c5931275ccff3ef7e8b4acc188077332a`
- Production manuscript: **frozen; no edits in R7**
- R8 and later stages: **out of scope until R7 closes**

R7 is a certification stage. No new parameter, demand system, coalition concept, or rescue specification may be introduced.

## 1. Objects to re-certify

R7 reopens only the surviving R2–R6 research claims.

### Adoption structure

- G1-E: outsider-only adoption can be a strict equilibrium under profile-specific gain inequalities.
- G1-U: robust gain bounds give selection-free outsider adoption/member non-adoption.
- G1-S/G1-C/G1-O: scope, asymmetric-cost, and optional-deployment qualifications.

### Partial erosion and preference effects

- G2-L: ranking reversal survives positive residual marginal adaptation cost locally.
- G2-S: the residual-rent function separates reversal, incentive-strengthening-only, and incentive-weakening regions.
- G2-J: incomplete adoption and preference reversal coexist with a selection-free firm continuation on a nonempty open set.

### Baseline dependence

- N1–N7: zero-network boundary, exact initial-SU region, reciprocal-disadvantage intersection, and singleton-network specification dependence.

### Portability and institutional robustness

- R5-D/R5-C/R5-B/R5-A/R5-E/R5-R/R5-X.
- R6 strict-vs-weak blocking and market-size-asymmetry results.

## 2. Independent mathematical route

R7 must not certify the new theory by merely rerunning R2–R6 scripts.

A new clean-room evaluator must:

1. reconstruct the canonical Cournot first-order systems directly from inverse-demand primitives;
2. solve complete compatibility, SU member market, SU outsider market, SW, and partial-adoption market states independently;
3. reconstruct consumer surplus from total quantity rather than importing saved welfare blocks;
4. derive the R3 residual-rent identity and adoption thresholds from those independently solved states;
5. verify the exact R3 joint witness;
6. independently test the R4 zero-network sign and reciprocal-disadvantage condition;
7. reconstruct the R6 deviation graph and exact witnesses without importing the R6 stable-set output;
8. independently reconstruct the frozen R5 demand matrices and spot-check the certified negative portability signs and adoption witness.

The clean-room implementation must not import `code/canonical.py` or any R2–R6 verification module.

## 3. Counterexample / scope attack

For every surviving claim record:

- exact quantifiers;
- existence versus uniqueness;
- selected-equilibrium versus all-equilibrium scope;
- strict versus weak inequalities;
- local versus global parameter scope;
- functional-form dependence;
- network/singleton dependence;
- competition/demand dependence;
- coalition-rule dependence.

No robustness statement may be broader than the R4–R6 evidence.

## 4. Novelty re-kill

The literature search is proposition-centered rather than label-centered.

Mandatory parent classes:

1. fixed-cost economies of scope;
2. dependent multi-technology adoption;
3. converters and one-way compatibility;
4. endogenous compatibility with network effects;
5. standards unions / regional versus multilateral harmonization;
6. endogenous firm adoption of harmonized standards;
7. spontaneous harmonization and the role of international regulatory agreements;
8. coalition/core stability and blocking-concept dependence.

Strong comparison set includes at least:

- Gandal & Shy (2001), *Journal of International Economics*;
- Farrell & Saloner (1992), *Journal of Industrial Economics*;
- Farrell & Simcoe (2012), *Oxford Handbook of the Digital Economy*;
- Manenti & Somma (2008), *International Journal of the Economics of Business*;
- Gorman (1985), *RAND Journal of Economics*;
- Cho & McCardle (2009), *Operations Research*;
- Matutes & Régibeau (1989), *Journal of Industrial Economics*;
- Takarada et al. / Takarada standards-policy line;
- Kawabata et al. / deep-trade-agreement standards line;
- Schmidt & Steingress (2022), *Journal of International Economics*;
- Buccella, Fanti & Gori (2023), *Journal of Economics*;
- Maggi & Mrázová (2024), NBER Working Paper 33318.

For each result classify prior-art status as:

- `DIRECTLY ABSORBED`
- `PARTIALLY ABSORBED`
- `NOT ABSORBED BUT MODEL-SPECIFIC`
- `NOT ABSORBED AND STRUCTURALLY GENERAL`
- `UNRESOLVED`

Absence of identical institutional vocabulary is not evidence of novelty.

## 5. Formal-verification gate

Formal verification is **applicable**.

Reason: the surviving theory contains quantified polynomial/rational inequalities, threshold ordering, open-domain boundary logic, and welfare identities whose failure would alter the admissible claim scope.

R7 therefore uses targeted Lean 4 + mathlib formalization rather than full-model formalization.

### Formal targets

At minimum:

- FV1: zero-network canonical initial-SU gap is negative for (0<c<1/3);
- FV2: the R3 residual-rent function is nonnegative and strictly increasing in residual cost on the certified domain;
- FV3: (R(d)<D) implies the post-adoption SU–IS gap (-D+R(d)) is negative;
- FV4: if (E>D>0) and (R(d)<D), then adoption both raises the relative IS incentive and reverses the ranking;
- FV5: under weak blocking, one indifferent deviator plus one strict gainer satisfies the blocking predicate, whereas it does not satisfy strict blocking.

The formal layer certifies these algebra/order/logical cores only. It does **not** by itself certify:

- derivation of inverse demand;
- exhaustion of product-market equilibrium branches;
- the complete private-adoption equilibrium correspondence;
- the R5 Bernstein certificate;
- the complete R6 deviation enumeration;
- economic novelty.

Those remain clean-room/analytic responsibilities.

## 6. Route decision rule

R7 must choose exactly one of Routes A–D from the revision plan.

- Route A requires a preference-effect result with meaningful structural portability beyond the canonical microfoundation.
- Route B applies when adoption logic generalizes but preference reversal remains tied to a restricted market structure.
- Route C applies if the revision yields little beyond local robustness/payoff relabeling.
- Route D applies if a foundational proof or novelty problem remains unresolved.

R5's proved non-portability is binding evidence. R7 may not ignore it to preserve Route A.

## 7. R7 completion gate

R7 closes only when:

- clean-room re-derivation passes;
- theorem/quantifier/scope ledger is complete;
- novelty re-kill is recorded with source-level evidence;
- formal verification builds with no `sorry`/`admit` and a statement-fidelity certificate;
- final claim set and prohibited overclaims are frozen;
- Route A/B/C/D is fixed;
- theorem ledger and revision-track status are updated;
- R7 Python and Lean checks are in CI;
- PR to `revision/research-track` passes full CI;
- PR is squash-merged;
- post-merge integration CI passes.

Only then may R8 reconstruct the manuscript around the R7-certified claim scope.
