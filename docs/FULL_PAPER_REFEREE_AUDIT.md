# Full-Paper Referee Audit and IJIO Submission Readiness

Final literature/framing audit: 2026-08-27

Target journal: *International Journal of Industrial Organization* (IJIO)

This document records the final pre-submission referee audit after the 2026 compatibility/interoperability literature closure. Earlier detailed audit versions remain available in Git history. This revision does not modify the Stage-8 frozen theory.

## Executive verdict

- Desk-reject risk: **MODERATE, reduced by the final framing revision but not eliminated**.
- Novelty classification: **B — DISTINCT BUT NARROW**.
- Theory-hold status: **NO HOLD**.
- Novelty blocker: **NONE IDENTIFIED**.
- IJIO scientific readiness: **GO**.
- Overall submission readiness: **CONDITIONAL GO / submit after administrative metadata and author certifications are completed**.
- New theory before first submission: **NOT RECOMMENDED**.

The final literature closure strengthens rather than weakens the claim discipline. Private compatibility, endogenous interoperability, fixed compatibility costs, unilateral/one-way compatibility, multihoming, firm standard adoption, standards coalitions, and coalition formation all have clear antecedents. The defensible contribution remains the particular continuation-payoff feedback generated when private compatibility is chosen after a formal government standards coalition has been fixed and the resulting directional bypass changes the rents that governments use to evaluate formal coalition deviations.

The source audit did not identify a prior paper containing the full sequence

`formal government coalition -> post-coalition strategic private compatibility -> directional outsider-only bypass -> selective erosion of members' exclusion payoff -> government preference reversal -> formal coalition stability reversal`.

## 1. Latest-theory status

The Stage-8 canonical theory remains unchanged. The final framing PR makes no change to:

- countries, firms, markets, or formal partitions;
- demand, compatibility, `c`, or `F`;
- timing or the used-standard rule;
- Cournot blocks or consumer-surplus formulas;
- private-adoption thresholds;
- `Omega_0` or any parameter condition;
- theorem, proposition, lemma, or corollary statements;
- strict blocking or the stable-set results;
- welfare conclusions, comparative statics, or technical appendices.

The verified Main chain remains:

- `T_A = P-B`, `T_U = A-C`, `T_W = A-S`;
- `F_L = max{T_W,T_A}`, `F* = 2T_A`;
- before outsider bypass, `W_i^{SU,N}-W_i^{IS} = E_i-D_i`;
- after outsider-only bypass, `W_i^{SU,O}-W_i^{IS} = -D_i`;
- hence `E_i-D_i -> -D_i`;
- for `(c,v) in Omega_0` and `F>2T_A`, precisely the three symmetric regional SUs are stable;
- for `(c,v) in Omega_0` and `F_L<F<2T_A`, IS is uniquely stable.

No global monotonicity in `F` or general robustness to alternative oligopoly/coalition structures is inferred.

## 2. Final literature kill test

### 2.1 Takarada et al. (2020)

**Overlap risk: HIGH. Kill-test result: PASS.**

Takarada et al. remain the closest published standards-coalition benchmark: three-country Cournot competition, national/regional/multilateral standards, coalition/core stability, and a fixed-cost extension. Their multi-standard setup cost follows from the government standards regime. It is not a separate post-formation private adoption game. The same formal regional SU therefore does not switch endogenously between no-bypass and outsider-only effective-compatibility states in their model, and the selective-erosion/stable-set feedback is not reproduced.

### 2.2 Gandal and Shy (2001)

**Overlap risk: HIGH. Mechanism not absorbed.**

They combine three countries, network effects, conversion costs, government recognition, and standardization unions. The conversion burden is determined by the recognition environment rather than a separate standard-specific fixed-cost private-adoption stage after coalition formation. The paper must therefore continue to avoid claiming novelty for conversion/private workaround technology itself.

### 2.3 Buccella, Fanti & Gori (2023)

**Overlap risk: HIGH on compatibility technology; selective-erosion contribution not absorbed.**

They study a Cournot network industry in which firms strategically choose compatibility, including quasi-fixed compatibility costs and one-way compatibility outcomes. This removes any plausible priority claim for endogenous compatibility, a compatibility fixed cost, or unilateral compatibility. Their model has no government formal standards partition and no coalition-stability feedback from a post-government private support decision.

### 2.4 Bourreau, Raizonville & Thébaudin (2026)

**Overlap risk: MEDIUM-HIGH on interoperability strategy; contribution not absorbed.**

They endogenize platform interoperability with network effects and consumer multihoming. The paper is a direct modern IO antecedent for interoperability as a strategic firm choice, but it contains no government standards partition and no formal coalition blocking/stability comparison generated by post-coalition private compatibility.

### 2.5 Motta & Peitz (2025)

**Overlap risk: MEDIUM on strategic interoperability/exclusion; contribution not absorbed.**

They analyze strategic denial of vertical interoperability and future first-party entry in a dynamic foreclosure environment. This is important IJIO-facing evidence that interoperability is a live industrial-organization margin. It does not reproduce the present government-standards-coalition/private-support/continuation-rent/stability sequence.

### 2.6 Economides & Skrzypacz (2003, working paper)

**Overlap risk: MEDIUM-HIGH on standards coalitions and endogenous firm compatibility; institutional distinction survives.**

Firms choose affiliation to technical standards coalitions before oligopoly competition, so firm-side standards-coalition formation is an important antecedent that must not be ignored. In the present paper, governments determine formal coalition membership first and firms may later support additional standards without joining or leaving that formal coalition. The key formal-membership/effective-compatibility separation is therefore not absorbed.

### Final blocking question

No verified source in the final search contains the complete causal sequence required to absorb the current contribution. `BLOCKING_NOVELTY_ISSUE` is therefore **NO**.

Novelty classification remains:

**B — DISTINCT BUT NARROW.**

## 3. What is and is not new

Established antecedents include:

- compatibility and network effects;
- converters, interoperability, and multihoming;
- endogenous compatibility choice;
- fixed or quasi-fixed compatibility/adaptation costs;
- one-way compatibility;
- firm standard adoption;
- firm standards-coalition affiliation;
- government standardization unions;
- regional versus multilateral harmonization;
- coalition/core stability;
- regulatory blocs and costly regulatory diversity.

The incremental object is:

`formal government standards coalition -> strategic post-formation private standard support -> asymmetric effective compatibility under the same formal partition -> changed product-market continuation rents -> changed government blocking incentives -> changed formal stable set`.

The manuscript should therefore continue to sell a mechanism, not a collection of ingredients.

## 4. Final Introduction / front-end audit

The final Introduction was revised to expose the contribution earlier without changing the result sequence. The revision now establishes, before the model description, that strategic private compatibility is an established IO margin and that the contribution is the post-coalition continuation-payoff feedback. The recent interoperability literature is acknowledged in a short bridge rather than a survey paragraph.

The editor-facing order is now:

1. problem and economic tension;
2. formal versus effective compatibility;
3. selective-erosion mechanism;
4. explicit statement that private compatibility itself is an antecedent;
5. model and continuation-payoff decomposition;
6. headline stable-set reversal;
7. contribution and closest literature.

The Introduction was edited with approximately length-neutral source changes rather than expanded to accommodate citations. The objective was lower cognitive load, not a broader literature review.

## 5. Related Literature audit

The three-part literature architecture is retained:

1. standards/harmonization and strategic government choice;
2. private compatibility and firm adaptation;
3. regionalism/standards coalitions and coalition formation.

The final revision adds the missing current IO comparisons without citation padding. In particular:

- Buccella et al. closes the endogenous-compatibility/fixed-cost gap;
- Bourreau et al. closes the recent endogenous-interoperability/multihoming gap;
- Motta & Peitz closes the recent IJIO interoperability/exclusion gap;
- Economides & Skrzypacz closes an older but highly relevant firm standards-coalition gap.

The Takarada distinction is now stated as `same formal SU, different endogenous continuation state`, rather than “another fixed cost.” The Gandal--Shy distinction remains the separate post-formation private-choice margin.

## 6. Claim-control audit

The final manuscript framing does not rely on the following priority claims:

- first model of compatibility;
- first endogenous compatibility choice;
- first fixed compatibility cost;
- first one-way compatibility;
- first private standards adoption;
- first standards-coalition model;
- first regional-versus-multilateral standards model;
- first use of coalition stability in standards;
- first link between interoperability and public policy.

Valid uses of “unique” remain mathematical statements such as uniquely stable IS under the stated theorem conditions. `Omega_0` remains a nonempty open existence region, not a generic/global primitive characterization.

## 7. Editor-facing desk test

| Test | Result |
|---|---|
| 1. Research question is clear | YES |
| 2. Firm conduct is central | YES |
| 3. IO mechanism is clear | YES |
| 4. Private compatibility itself is not falsely claimed as novel | YES |
| 5. Takarada distinction is visible | YES |
| 6. Modern interoperability literature is acknowledged | YES |
| 7. Headline stability result is visible | YES |
| 8. Contribution does not read as “another fixed-cost model” | YES |
| 9. Scope limitations are credible | YES |
| 10. Editor has a reason to send to referees | YES |

Desk-test score: **10/10** on framing adequacy.

This does not imply a 10/10 contribution score or eliminate desk-reject risk. The residual editorial question is whether a distinct but narrow three-country mechanism clears IJIO's contribution threshold.

## 8. Independent referee passes

### Reviewer A — General IO editor

**MINOR.** The firm-conduct chain is now immediate and the interoperability literature bridge makes the IO positioning current. Residual concern: the final institutional object is government coalition stability in a stylized three-country model.

### Reviewer B — Compatibility / network IO expert

**PASS WITH MINOR SCOPE RESERVATION.** Buccella, Bourreau, Motta--Peitz, Farrell--Saloner, and Doğanoglu--Wright make technology novelty impossible, and the manuscript now says so. None of the verified sources absorbs the post-government coalition continuation-payoff mechanism.

### Reviewer C — Standards / international harmonization expert

**MINOR.** Takarada and Gandal--Shy remain close and must remain prominent. The current distinction is nevertheless identifiable: strategic post-formation support changes effective compatibility and the payoff of the same formal SU before blocking is evaluated.

### Reviewer D — Skeptical theorist

**MINOR.** The open-set/existence character of `Omega_0`, strict blocking, three countries, binary compatibility, and Cournot competition are correctly treated as scope restrictions rather than robustness claims. No additional theorem is required before first submission.

No reviewer pass produces a BLOCKER.

## 9. Residual referee attacks

The most likely serious objections remain:

1. the contribution is distinct but too narrow for IJIO;
2. `Omega_0` is an existence/microfoundation region rather than a sharp global primitive characterization;
3. the three-country environment and strict blocking may limit generality;
4. the outsider's two-market return creates a transparent geographic-scope component in the adoption threshold;
5. the manuscript remains long in review format.

These are publication-risk issues, not hidden correctness failures. Adding Bertrand competition, an `n`-country model, continuous interoperability, transfers, or endogenous `F` before first submission would materially change scope and is not recommended.

## 10. Reproducibility and build status

The pre-audit framing head `1da69adcd704f659c08fdd134e7f85c7054ae7a4` passed Paper CI run `33064528504` / run #115, including the repository's symbolic/numerical verification, manuscript build, submission-package gate, and clean-room replication QA.

Because this audit document is the final content update, the final PR head must also pass Paper CI before merge. The merge condition remains:

- source-verified citations;
- no theory change;
- no novelty blocker;
- no reviewer BLOCKER;
- final-head Paper CI PASS;
- final PDF visual QA PASS.

## 11. Journal recommendation

### Primary — International Journal of Industrial Organization

**FIT: GOOD / AMBITIOUS.**

The paper now presents a current IO margin---strategic compatibility/interoperability---as the firm-side input to an institutional-stability result, rather than claiming novelty for the technology itself. This is the strongest IJIO framing available without changing theory.

### Fallback — Review of Industrial Organization

**FIT: VERY GOOD.** If IJIO rejects primarily on contribution breadth rather than correctness, RIO remains the most natural second submission because the firm conduct, compatibility, competition, and policy mechanism can be retained with limited repositioning.

## 12. Final recommendation

Scientific/literature decision:

**GO FOR IJIO.**

Submission execution decision:

**B — SUBMIT AFTER ADMINISTRATIVE METADATA ONLY.**

No literature, framing, theory, or reproducibility blocker identified in this final audit. Remaining submission conditions are the author-only factual/administrative fields already tracked in the submission checklist and a final live portal check.
