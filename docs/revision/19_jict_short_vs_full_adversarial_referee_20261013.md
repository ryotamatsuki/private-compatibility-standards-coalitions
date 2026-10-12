# 39-page R9 JICT manuscript vs 16-page short manuscript: adversarial economic/mathematical readability pre-review

Review date 2026-10-13 JST. **Verdict: CONDITIONAL GO for the 16-page version as preferred submission architecture; NOT READY TO REPLACE 39-page version without two MAJOR exposition repairs.** This is an AI-assisted critical pre-review, not independent human journal refereeing.

## Material and verification

1. Actual 39-page anonymous reviewer PDF: Paper CI run 38271682894, archive `jict_submission_ci.zip` / `generated/jict_manuscript.pdf` (39 US-letter pages, original certified R9 with JICT packaging).
2. Actual 16-page anonymous reviewer PDF and flat source: `R9_JICT_short_preview_16pp.pdf` / `R9_JICT_short_source.zip`, uploaded in same conversation and rebuilt by the branch's dedicated JICT Short Preview CI run 38276888557.
3. Anonymous Online Supplement, **15 pages**. Read through full text, especially Appendices B (national-welfare sign certificates), C/D (firm deviations) and E.4 (blocking), not simply rely on its summary.
4. The full certified source `paper/sections/{03_model,05_private_compatibility,06_selective_erosion,07_coalition_stability,08_secondary_results}.tex`; short source `paper/jict_short/short_{02_model,03_adoption,04_incentives,05_stability_scope}.tex`; independently checked Stage R6 code `code/revision/check_r6_coalition_stability.py`.
5. GitHub workflows on PR #33: dedicated short version **PASS** and historical complete Paper CI incl. R2–R9, Lean, original JICT and replication clean-room **PASS**. Technical PASS does NOT certify the economic completeness of a revised short exposition.

## Side-by-side comparison

| Criterion | 39 pp | 16 pp | Critical decision |
| --- | --- | --- | --- |
| Journal typical under-20 format | Does not meet usual target, barely meets 40-p maximum | Meets typical target (16 pp), exactly same elsarticle review class and 612x792 pt paper size; original/short fonts render differently at named font level but document class is identical; no margin-hiding detected | **SHORT BETTER** |
| Economic research question and causal channel | Well explained but duplicated in Intro, literature, Discussion | Clear one-way outsider bypass vs formal country standards, CS vs home incumbent profits; conditional policy takeaway | **SHORT BETTER/COMPARABLE** |
| Position relative to prior literature | Full Related Literature ~3–4 pp, closest comparators identified | Intro consolidates standards unions, partial compatibility and regulatory agreements in ~1 page; no firstness overclaim | **SHORT ACCEPTABLE**, retain source-specific comparator description |
| Primitives (demand, cost, timing, national welfare) | Redundantly elaborated ~7 pp | Short §2, pp.3–5 defines all market/technology ingredients, game timing, objective, Cournot market quantities, eight payoff blocks | **SHORT PASS** for headline theorem |
| Supporting complete-relief adoption | Exact blocks and adoption lemma, more narrative | Short §3, pp.5–6 gives full sufficient F interval and refers to SI C | **SHORT PASS** provided deviation appendix supplied |
| Incomplete-relief adoption and sign theorem | Full proof of R3 in main pp.17–22 | **Exact same core source** in `short_04_incentives.tex`, pp.6–11 | **SHORT PASS** |
| Strict joint `(c,v,lambda,F)=(1/10,6/25,1/2,9/100)` open-set witness | Present exact rational proof | Same exact fractions and inequalities (p.11) | **SHORT PASS** |
| Formal coalition stability | ~4 pp, theorem, blocking sensitivity, asymmetry and more payoff comparisons | ~2 pp, theorem and a proof sketch (p.12), with reference to SI B/E/F | **SHORT MAJOR REPAIR**: ambiguous deviation mapping and inadequate visible five-partition proof bridge |
| Failure boundaries and robustness | ~4 pp, important quantified R4 fixed-c root and R5 sign comparison plus figures | ~1 page, preserves v=0 formula, singleton and pre-specified differentiated Cournot/Bertrand scope and caveats | **SHORT ACCEPTABLE for secondary results**, exact root theorem now SI/code only |
| Empirical/policy implications | Detailed caveats about observables and institution mapping | Concise Discussion p.13 retains F vs d, unilateral vs reciprocal, politically relevant observables and lack of identification | **SHORT ACCEPTABLE** |
| Visual integrity and citations | Text readable, some redundancy and figure/table density | Pages rendered and sampled; no obvious clipping/overprint; residual-rent figure and threshold table retained; reference and labels validated by CI | **SHORT PASS** |
| Formal reproducibility | Old R9 package includes replication suite | Dedicated short build + complete original R9 CI both pass | **PASS, BUT NOT A SUBSTITUTE FOR EXPLAINING COALITION DEVIATIONS IN PAPER** |

## Clean textual identity of the primary mathematical result

A complete line-by-line unified diff of `full/06_selective_erosion.tex` vs `short_04_incentives.tex` finds **exactly three changed lines**, all cross-reference labels or section references:
- section label `sec:selective-erosion` -> `sec:short-incentives`;
- one Cournot blocks section reference;
- last sentence's robustness-section reference.

Every displayed R(d,v) formula, derivative, government-payoff identity, proposition statement, proof, d_Z boundary, and exact incomplete-cost-relief witness is **unchanged**. This is stronger than claiming thematic equivalence.

Independent rational-arithmetic smoke check of the R3 witness (not an independent complete proof):
`c=1/10, v=6/25, lambda=1/2, d=1/20, F=9/100`:
`E-D=2408509/295731200>0`, `R-D=-1341/184832<0`. Verified directly from SU Cournot market blocks and own consumer surplus + domestic producer payoff formulas. Existing R3 clean-room CI independently certifies adoption thresholds. The main result is not accidentally lost.

## MAJOR-1: Underspecified exact coalition-deviation technology, destroying standalone institutional clarity

Short §5 says “the admissible deviating set and exclusivity rule are the same as in the full canonical partition game”, but the **full version is not a formally submitted second main text**. A reader of the 16-page main paper plus SI cannot reconstruct `rho -> rho'` from the short model alone. This is a strategy-set ambiguity, not merely prose editing.

The actual R6 program defines **exactly**:
```
rho'(rho,D) = {D} ∪ { B\D : B in rho, B\D nonempty },
```
for nonempty `D ⊆ {1,2,3}`, with current-block residual members remaining together. Deviations that recreate rho do not block. E.g., from SU_12 a new {1,3} coalition induces SU_13, and from IS a single defector induces SU among the remaining pair.

**REQUIRED before short version submission:** add that mapping and explicitly state strict and weak/Pareto blocking payoff inequalities in short §5. The added material is 5–8 lines, likely <=0.5 page. Never rely on a nonexistent “full canonical partition game” provided to referees.

## MAJOR-2: Inadequate standalone supporting bridge for full-bypass stability theorem

Short §5 asserts high-F stability of *three* SU partitions and intermediate-F uniqueness of IS, but omits `SW`'s explicit payoff even though the sketch says `IS` or `SU` blocks `SW`. The SI B.1–B.4 has correct welfare sign polynomials, and SI E.4 covers weak blocking; however **no complete five-partition/blocking case table appears in the 15-page SI**. SI E.4 invokes a named R6 computational enumeration without actually reproducing it.

**REQUIRED:**
1. Add to short §2 or §5 the immediately checkable SW benchmark
```
H=(1+2c)^2/16,  S=(1-2c)^2/16,
K_W=(3-2c)^2/32,
W^{SW}=K_W+H+2S.
```
2. Add a concise symmetric-coalition blocking ledger, either in main (preferable ~0.5 page) or as a table with precise SI reference: high-F `SW -> SU` via {i,j}; `IS -> SU` via {i,j}; `SU -> another SU` has common-member indifference; intermediate-F `SW -> IS` via N; `SU -> IS` via N; `IS` has no profitable unilateral/pair/grand deviation. Support each with at least one national-payoff difference or rigorous pointer to SI B.1/B.2/B.3/B.4.
3. If leaving R6 asymmetric claims in main, give the **exact witness restrictions** for the small-`delta` range or explicitly refer to reproducible exhaustive enumeration as a *computational audit*, distinguishing the exact all-domain statement from witness-only perturbation. The short text currently says “sufficiently small” and does not overclaim, but proof trace can be improved.
4. Amend SI E.4 to describe how `deviate(partition,coalition)` creates the new partition and reproduce enough of the finite payoff comparison to make its proof human-auditable without obtaining the private code repository.

This repair protects mathematical readability without moving the core novel R3 theorem or adding substantive research.

## MINOR-1: Supporting fixed-cost sufficient condition is not locally auditable on positive residual d

Short §3 defines `T_W(d)`, `T_A^R(d)` only in words, with expressions in SI D; full core proof in short §4 also points to SI D. For an applied-theory short format this is acceptable, but make one explicit table note (“all bounds are sufficient, not necessary; proofs and deviation profiles in Online Supplement D”) or add a single direct threshold formula to support economic interpretation. Do not burden the main 16-page manuscript with full adoption best-response polynomials.

## MINOR-2: Literature positioning is compressed to the point that the editor's “increment” question survives

Short Intro gives proper sources and caveats, but compared with original dedicated Related Literature, the **theorem-level comparison** to Gandal–Shy (governments' coalition stage), Takarada et al. (government stable sets) and Innocenti–Menicucci/Ding (firm compatibility stage) is relatively implicit. Add 2–3 sentences identifying precisely which parent does *not* make a member government's formal SU-vs-IS payoff comparison endogenous to outsider-only firm adoption. Avoid unsupported “first to ...” claims. At 16 pages, adding 0.2–0.3 page is a good trade.

## MINOR-3: Marginal policy connection

The short discussion's `d` comparative static and its explicit no-causal-identification caveat are correct, but add one sentence distinguishing observable `F` (one-time standard-entry expense) and `d` (per-unit adaptation residual) from institutional “harmonization” in published cases. Do not invent an empirical case or a policy instrument.

## Publication-value assessment

**Skeptical-editor objection:** The 16-page version is far more readable, but the government ranking trichotomy follows almost mechanically after Cournot payoffs are defined and is highly dependent on a singleton-zero network and particular linear demand. The paper does not establish broad institutional policy or unique coalition stability for positive d. An editor can still doubt substantive importance. Compression does not solve this scientific reach risk; preserving accurate conditional claims and the same-primitives joint witness is essential.

**Best defensible affirmative case:** Firm compatibility selection and governments' *formal* union preferences are different institutional decisions. In the model, outsider-only adaptation can improve domestic consumers' surplus while eroding domestic incumbent rents and leaving the home firm's outsider-market disadvantage unchanged. The private equilibrium and government preference shift are simultaneously feasible at positive residual cost, with a nonknife-edge exact certificate, and the failures under alternative demand and network specifications show that private interoperability is neither sufficient nor uniformly signed for formal harmonization. The 16-page version communicates this more sharply than the 39-page draft. No novel general regulation theory or global planner efficiency is asserted.

## Verdict and gate

- **Economic/editorial readability: SHORT > FULL**, conditional on preserving close parent theorem differentiation and candid R5 failures.
- **Headline theorem mathematics: equivalent and traceable**, exact same R3 source; both CI systems green.
- **Institutional theorem mathematical readability: SHORT < FULL**, MAIN issue currently **MAJOR 1 + MAJOR 2**; not enough to simply point to code.
- **Overall: CONDITIONAL GO / MINOR-TO-MODERATE REVISION BEFORE REPLACING R9 PACKAGE**. A 17–19 page short paper after the two mandatory additions is likely a better JICT candidate than either the 16-page uncorrected draft or the 39-page legacy version.
- Do not assert that these fixes are new results; they're exposition and proof traceability. Do not merge PR #33 as-is and do not submit. Preserve R9 mathematical freeze and original 39-page version as a rollback.
- After amendments, repeat 20-page limit, source/BibTeX, clean-room SI, private adoption, full R2–R9+Lean, and a blind editorial reread. External human review is not performed by this internal audit.
