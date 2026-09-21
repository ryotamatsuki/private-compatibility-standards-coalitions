# Revision Track R0–R9 — Post-IJIO Theory Redevelopment

## Status

- Repository: `ryotamatsuki/private-compatibility-standards-coalitions`
- Paper: *Private Compatibility and the Stability of Standards Coalitions*
- Trigger: desk rejection before external review, IJIO-D-26-00585
- Integration branch: `revision/research-track`
- Base commit candidate for submitted source: `28bed286bd03b43bce8294b9eaebfcc7ceb6ca2a`
- Current status: **R0 COMPLETE WITH ARTIFACT-PROVENANCE LIMITATION; R1 COMPLETE; R2 DESIGN FROZEN; R2 THEORY NOT YET EXECUTED**
- IJIO resubmission: **not an objective**
- Production-manuscript rewrite before theory re-certification: **prohibited**
- Governing reusable workflow: **research-paper-workflow v2.2 @ 42574d6c5931275ccff3ef7e8b4acc188077332a**
- Workflow lock: `docs/revision/00_workflow_lock.md`

## Research objective

This revision is not a routine manuscript revision. It reopens research development under a paper-specific Revision Track R0–R9.

The central research question is:

> Under what conditions does private standards adaptation promote formal international coordination, and under what conditions does it not, in a way that can be explained beyond the current three-country linear Cournot model?

The purpose is not to make the existing result appear broader. If genuine generalization fails, that limitation is itself to be recorded as a research result, and restructuring the existing model into a concise specialist paper remains an admissible route.

The existing Stage-8 theory freeze remains valid for the old version. New claims developed on this revision branch must not overwrite the old theorem ledger or be treated as certified until the relevant revision stages are closed.

---

## 0. Governing workflow and inherited obligations

At execution start, identify and freeze the actually adopted version of `research-paper-workflow`, its complete commit SHA, and the exact governing documents. Do not infer v2.1 merely from past prose.

The paper-specific R0–R9 track is not a substitute for the standard workflow's certification duties. At minimum it inherits:

- independent adversarial mathematical audit;
- distinction between validity of a candidate equilibrium and exhaustiveness of the equilibrium set;
- audit of generality, quantification, and locality;
- structural-isomorphism checks and checks against existing theorems;
- explicit decision on formal verification and execution where appropriate;
- reproducibility checks and journal-requirement checks.

The old frozen theory remains frozen as a historical version. The revision branch must state explicitly which assumptions and results are reopened. Unproved new claims must not overwrite the old theory ledger.

Full production-manuscript rewriting is deferred until the research-route decision and theory re-certification are complete. Research notes, candidate propositions, proof drafts, counterexamples, and exploratory code are allowed.

---

## 1. Revision Track overview

| Stage | Purpose | Main outputs | Completion criterion |
|---|---|---|---|
| R0 | Freeze IJIO submission outcome | submission manifest, decision record, reproducibility record | verified and unverified submission facts are traceable |
| R1 | Audit claims and mechanism | claim ledger, assumption-dependence table, preliminary literature audit | hypotheses and stop conditions are explicit |
| R2 | General conditions for one-way adoption | adoption model, candidate G1, proof, counterexamples | adoption asymmetry is explained from underlying conditions |
| R3 | Partial erosion analysis | candidate G2, partial-erosion model, boundaries | local robustness is separated from genuine general insight |
| R4 | Role of network effects | analytic proof, parameter region, specification audit | general logic is separated from model-specific requirements |
| R5 | Alternative competition test | comparison model, proofs/failure results | portability and non-portability are identified |
| R6 | Coalition-stability robustness | deviation rules, blocking table, robustness results | preference effects are separated from institution-dependent stability |
| R7 | Novelty reassessment and theory re-certification | literature comparison, independent audit, generality audit, formal-verification decision | admissible claim scope is frozen |
| R8 | Manuscript reconstruction | manuscript v2, appendices, figures, code | text and certified results agree |
| R9 | Final audit and journal repositioning | final audit, journal comparison, submission package | mathematics, claims, reproducibility, and journal rules are closed |

R4 baseline checks and preliminary literature work begin during R1. Stages are not mandatory merely because they have numbers: a stage may be declared out of scope with a recorded reason.

---

## 2. R0 — Freeze IJIO submission and editorial decision

Preserve:

- initial submission date, revised-submission date, decision date, manuscript number;
- actual submitted manuscript PDF and source bundle;
- Editorial Manager generated PDF, if available;
- editorial decision letter;
- submitted author information and declarations;
- code, figures, build instructions;
- hashes and provenance for preserved artifacts.

Treat `28bed286bd03b43bce8294b9eaebfcc7ceb6ca2a` as a **candidate** submission-source commit until checked against actual submission files and history. Do not label it the submitted version before verification.

Editorial correspondence stored in a public repository must exclude unnecessary account-operation links, authentication material, and other private metadata. Full correspondence and public research records may require different sharing scopes.

After identifying the submitted version, create a fixed tag if useful, e.g. `ijio-submission-final-2026-09`. Do not move existing tags.

Distinguish preservation of the actual submitted PDF from reproducibility of its substantive content from source. Binary differences caused only by generation timestamps do not by themselves imply non-reproducibility.

If artifacts remain incomplete, record:

`SUBMITTED ARTIFACT NOT FULLY VERIFIED`

This blocks a claim of complete submission reconstruction, but does not automatically block R1 analysis based on verified source.

Planned outputs:

- `docs/revision/00_ijio_outcome.md`
- `docs/revision/submission_manifest.json`

---

## 3. R1 — Preliminary audit of claims, assumptions, and literature

Inventory every existing Lemma, Proposition, Theorem, Corollary, and welfare claim.

For each claim record:

- exact claim and quantified domain;
- assumptions and theorem dependencies;
- whether it is an identity, conditional proposition, existence result, or characterization;
- dependence on the current Cournot structure;
- dependence on symmetry, interiority, and coalition rules;
- equilibrium-selection dependence;
- location of proof, computation, and counterexample search;
- strongest wording currently justified.

Classifications are non-exclusive. For example, a result may be both an identity and dependent on a particular market configuration.

Track separately:

1. outsider-only adoption exists as an equilibrium;
2. outsider-only adoption is the unique equilibrium;
3. private adoption strengthens government incentives toward IS;
4. private adoption reverses the government's ranking.

Result 3 does not imply 4. Result 4 does not imply a change in coalition stability.

Map the editor's criticism to individual claims and distinguish mathematical, generality, economic-significance, and exposition issues.

Begin preliminary literature work before R7. Search beyond standards-specific papers to fixed-cost adoption, common costs across markets, erosion of exclusion rents, and institutional participation incentives.

Do not treat absence of the same institutional label as evidence of novelty. Translate candidate results into institution-free mathematical form and check whether they are special cases of known results.

Planned outputs:

- `docs/revision/01_claim_mechanism_audit.md`
- `docs/revision/theorem_ledger_v2.md`
- `docs/revision/preliminary_literature_audit.md`

---

## 4. R2 — General conditions for one-way adoption

The purpose is not to replace the current condition `F < 2 T_A` by abstract symbols.

Define adoption gain with rivals' adoption actions explicit:

\[
\Delta_j(a_{-j};C)
=
B_j(a_{-j};C)-K_j(a_{-j};C),
\]

where \(B_j\) is the change in operating profit derived from market equilibrium and \(K_j\) is the incremental adoption cost. If market equilibrium is multiple, state an equilibrium-selection rule or payoff correspondence.

For a proposed outsider-only profile, first verify equilibrium existence. If uniqueness is claimed, inspect all other pure equilibria and mixed equilibria separately.

Candidate selection-independent sufficient conditions include:

\[
\inf_{a_{-o}} \Delta_o(a_{-o};C)>0,
\]

\[
\sup_{a_{-i}} \Delta_i(a_{-i};C)<0
\qquad(i\in C).
\]

If these hold over the relevant action sets, outsider adoption and member non-adoption are strict dominant actions. Treat these as sufficient conditions unless necessity is separately proved.

Where a common fixed cost can be separated, investigate a representation such as:

\[
\max_{i\in C}\overline B_i<F<\underline B_o.
\]

Do not create a nonempty interval merely by defining payoff differences. Derive non-emptiness from underlying conditions.

Candidate cost structure:

\[
K_o(C)=F_s+\sum_{k\in C}f_{ok}.
\]

If market-specific costs can be avoided by abandoning a market, solve market participation or establish conditions under which serving all relevant markets is optimal.

Coalition size is discrete. Prefer:

\[
\Delta_k B_o(C)
=
B_o(C\cup\{k\})-B_o(C)
\]

and compare this with incremental cost. Use \(\partial B_o/\partial |C|\) only after defining an appropriate continuous scope or market-size variable.

Adding a market may alter competition and profit in existing markets. Include that effect and do not assume in advance that larger blocs are always more attractive adoption targets.

R2 outcome classifications:

- general sufficient conditions established;
- nonempty region derived from primitives for a defined model family;
- direct application of existing fixed-cost adoption theory;
- no region found within the pre-specified search space;
- nonexistence proved for the defined model family.

Required outputs:

- general adoption model;
- candidate Proposition G1;
- proof;
- counterexamples;
- mapping back to the baseline model.

---

## 5. R3 — Partial erosion and preference reversal

Use the diagnostic decomposition:

\[
(1-\alpha_i)\mathscr E_i
-
(1-\beta_i)\mathscr D_i.
\]

Do not treat a sign comparison imposed on \(\alpha_i,\beta_i\) as a new general theorem. Do not assume automatically that these parameters belong to \([0,1]\); derive their economic interpretation and admissible range from equilibrium where used.

First minimal extension candidate:

\[
c\longrightarrow \lambda c,
\qquad 0\leq\lambda\leq1.
\]

Here \(\lambda=0\) means complete removal of the residual adaptation cost. Compatibility and marginal cost are distinct objects, so the extended model must state:

- whether adoption changes compatibility groups;
- whether full network benefit is obtained;
- which firms and markets bear residual costs;
- whether IS eliminates the residual cost;
- whether reverse-direction markets are affected.

Full compatibility with residual cost means \(\lambda=1\) need not reproduce the no-adoption state. Endpoint interpretation must be checked, not assumed.

Re-solve quantities, prices, profits, consumer surplus, and adoption conditions consistently. Do not reuse old fixed-cost thresholds without derivation.

Separate three statements:

1. private adoption raises the relative incentive toward IS;
2. the increase is large enough to reverse the government's ranking;
3. the adoption state causing the reversal is itself an equilibrium of the firm game.

It is insufficient that the R2 adoption region and the R3 preference-reversal region are separately nonempty. Establish a nonempty intersection for the same primitives and the same adoption equilibrium.

### R3-L — Local robustness

Where strict inequalities, equilibrium regularity, and continuity hold, determine whether the baseline result survives in a neighborhood of \(\lambda=0\). This weakens dependence on exact equality but is not by itself a strong generalization result.

### R3-S — Economic characterization

Characterize, where possible:

- how large residual cost can be before reversal fails;
- which primitives determine the boundary;
- the distinction between the adoption boundary and preference-reversal boundary;
- cases in which reversal does not occur.

If one minimal extension leaves the reverse-direction market unchanged, \(\beta_i=0\) may remain. Do not add extensions merely to make both \(\alpha_i\) and \(\beta_i\) move.

Required outputs:

- candidate Proposition G2;
- joint adoption/preference region;
- local robustness proof;
- economic boundaries;
- counterexample or scoped non-result.

---

## 6. R4 — Role of network effects and baseline specification

Re-derive from primitives:

\[
\left.
\bigl(W_M^{SU,N}-W^{IS}\bigr)
\right|_{v=0}
=
\frac{c(13c-6)}{32}.
\]

Treat \(v=0\) as a boundary extension of the current \(v>0\) domain. Prove the sign on the corresponding interior interval \(0<c<1/3\).

Permitted conclusion:

> In the current symmetric Cournot model, on the stated interior domain, the pre-adoption SU advantage does not hold when the network effect is zero.

This is not evidence that network effects are necessary in every model. Conversely, before constructing a concrete no-network-effect example, do not broadly assert that the mechanism requires no network effects.

Characterize:

\[
\mathcal V_{SU}(c)
=
\left\{
v:
\text{feasibility conditions hold and }
W_M^{SU,N}>W^{IS}
\right\}.
\]

Do not introduce a unique \(v_{\min}(c)\) until it is proved that this set is a single upper interval. Check for emptiness, multiple intervals, and non-monotonicity.

Audit the specification assigning zero network benefit to a singleton and its role in the main results. Alternative specifications, if explored, are separate model changes rather than verification of the old result.

Planned output:

- `docs/revision/04_network_role.md`
- analytic sign proof;
- feasible region;
- specification-dependence table;
- verification code.

---

## 7. R5 — Limited test under an alternative competition form

Execute only if R2–R3 justify further portability testing. Default candidate: differentiated-product Bertrand competition.

Before analysis, freeze demand, compatibility technology, costs, government objective, and comparison regimes. Where possible, use a common demand environment that isolates the competition-mode difference. If demand also changes, do not attribute resulting differences solely to Cournot versus Bertrand.

Check separately:

1. pre-adoption SU advantage;
2. outsider-only adoption equilibrium existence and, where relevant, uniqueness;
3. stronger incentive toward IS;
4. actual preference reversal.

Use a demand system with a coherent consumer-surplus measure. Check boundary cases needed for the claim, including zero demand, exit, and corner solutions where relevant.

Do not repeatedly redesign the model until a successful example appears. Corrections of mistakes and minimal economically motivated changes are allowed only with recorded reasons.

If the selected model fails, scope the conclusion to that model.

Permitted:

> In the specified differentiated-Bertrand model, the pre-adoption SU advantage fails, so this route to preference reversal does not arise.

Not permitted:

> Preference reversal requires quantity competition.

A finite numerical search without success is:

`UNRESOLVED WITHIN SEARCH BUDGET`

not a proof of nonexistence.

---

## 8. R6 — Preference effects versus coalition stability

Revised hierarchy:

**Primary result:** how private standards adaptation changes government incentives and preferences for broader standardization.

**Secondary institutional result:** how those preference changes affect the stable set under an explicitly stated coalition-formation rule.

For each coalition concept specify:

- who may deviate with whom;
- whose consent is required for accession or partnership;
- what happens to residual coalitions after deviation;
- whether firm adoption is re-solved after deviation;
- what comparison is used when adoption equilibrium is multiple.

Test:

- baseline strict blocking;
- blocking with weak improvement for all and strict improvement for at least one;
- small market-size asymmetry.

Separate stability driven by symmetry-induced indifference from preference results supported by strict payoff differences. Allow the stable set to be empty under an alternative rule.

The model is a static institutional comparison in which firm behavior is re-solved under each regime. Do not describe it as a dynamic renegotiation model with sunk adoption expenditure unless such dynamics are explicitly introduced.

Recheck welfare language. If every country strictly prefers IS to every alternative in the specified institutional set, world-welfare ranking within that set may follow; do not extend this to unrestricted first-best policy claims.

---

## 9. R7 — Novelty reassessment and theory re-certification

Update the R1 literature audit against the propositions that actually survive.

Compare:

- conclusions;
- sufficient and necessary conditions;
- failure conditions;
- comparative statics;

not merely differences in institutional labels.

For each main result answer:

- does prior literature imply the same sign?
- does this paper identify conditions under which the sign changes?
- is the condition only a restatement of an existing theorem?
- is the novelty mathematical, economic/application-level, integrative, or absent?

Before R8, independently re-derive new main propositions and search for counterexamples. Re-running production code is not a clean-room audit. Use a separate derivation route or independently implemented evaluator where feasible.

Audit separately:

- existence;
- uniqueness;
- all-equilibrium versus selected-equilibrium validity;
- locality;
- parameter range.

Confirm that R2 and R3 conclusions hold simultaneously under the same primitives.

Close the formal-verification applicability decision under the adopted standard workflow. If formal verification is used, map proved statements to assumptions explicitly. Do not treat formal verification as evidence of economic significance or novelty.

Only after these gates pass may the new theory be frozen. Preserve the old freeze record.

---

## 10. R8 — Manuscript reconstruction

Rewrite the manuscript only after R7 fixes the admissible claim scope.

If substantive generalization succeeds, organize around:

- research question and conditional answer;
- conditions for one-way private adoption;
- conditions for stronger IS incentives and preference reversal;
- the current Cournot model as a concrete microfoundation;
- boundaries and alternative-model tests;
- coalition-stability application;
- institutional interpretation and limitations.

Move most routine Cournot derivations to appendices while retaining equations and tables needed for understanding. Keep partner-selection results in the main text only if they materially support the new central results. Remove repeated explanations of the same mechanism.

If generalization fails, do not preserve a "general theory first" structure merely for appearance. Reconstruct the paper as a concise, accurate, model-specific contribution.

Use figures for:

- regions of validity and failure;
- adoption thresholds versus preference-reversal thresholds;
- assumption dependence.

Numerical figures are not proofs.

Proceed section-by-section: save, integrate, compile, audit. Candidate research propositions must not silently become finalized manuscript theorems.

---

## 11. R9 — Final audit and journal reselection

Perform:

- mathematical audit;
- claim-scope audit;
- novelty recheck;
- reproducibility audit;
- abstract/introduction overclaim audit.

If a downstream failure is found, return to the earliest affected stage and mark dependent proofs, figures, manuscript text, and journal evaluation as `STALE`.

Build the journal candidate set from the surviving contribution, readership, article format, and length. Do not rely only on the old journal ladder or a few initially salient journals. Use publication venues of closest papers as a candidate-discovery device, not an automatic recommendation.

Passing R2–R3 is not sufficient for an upper-tier journal judgment. Evaluate novelty, generality, economic significance, and explanatory economy separately.

After selecting a target, recheck current official submission rules and prepare the package. Do not mark submission-ready while journal-rule questions remain open. Actual submission is separate from completion of this research track.

---

## 12. Research branches and stop conditions

At the end of R2 and R3 make a provisional route decision, finalized at R7.

| Route | Decision | Action |
|---|---|---|
| A — substantive generalization | one-way adoption and preference effects are derived from underlying conditions, with more than local continuity and with informative success/failure conditions | proceed to R5 as warranted; reassess journals after certification |
| B — limited generalization | adoption conditions broaden, but preference reversal remains tied to restricted market structure | present as a conditional mechanism paper |
| C — little additional generalization | work reduces mainly to payoff relabeling or local robustness, without new predictions | stop extending; shorten and reposition the existing model |
| D — unresolved or foundational problem | proof incomplete, equilibrium unresolved, old result fails, or literature subsumes result | record unresolved status and choose repair, hold, or abandonment |

Route C is not a proof that generalization is mathematically impossible. Route D must distinguish a genuine negative result from an unresolved research question.

During R1, pre-register the candidate specifications, search ranges, and stop conditions for later stages. A new specification requires a concrete problem it addresses and a reason existing attempts do not resolve that problem.

Do not continue adding parameters or extensions merely because prior attempts did not produce a publishable result.

---

## 13. Repository operations and stage records

The integration branch is:

`revision/research-track`

Stage work branches and PRs should target this integration branch rather than `main`.

From R0 through R7, uncertified research output must not be mixed into the production manuscript. Merge to `main` only when the scope and certification status of the merged material are explicit.

Distinguish stage completion from hypothesis success. A rigorously established non-result can close a stage successfully.

Every stage report must include:

- input commit;
- hypothesis and target model;
- derivations, audits, and searches performed;
- proved / refuted / unresolved classification;
- references to artifacts;
- judgment on the hypothesis;
- GO / CONDITIONAL GO / NO-GO;
- remaining limitations and allowed scope of next work.

Cross-check manual derivation, symbolic computation, and numerical computation. Use Python for computation. Numerical search is never a substitute for analytical proof.

Preserve counterexamples, additional equilibria, failed model variants, and discarded specifications. Do not remove inconvenient attempts from the research record.

---

## 14. Initial authorized execution scope

The first execution unit is:

1. complete R0;
2. complete R1;
3. fix the R2 model, hypotheses, literature position, and stop conditions;
4. within R1, perform the R4 baseline zero-network-effect check.

Before substantive R2 work, freeze the exact adoption game and whether the target claim is equilibrium existence, uniqueness, or both.

Proceed to the minimal residual-adaptation-cost extension in R3 only if R2 produces a valid reason to do so.

Passing R2 and R3 is necessary for the intended redevelopment route but is not sufficient for production-manuscript rewriting. Full manuscript reconstruction requires route selection and R7 theory re-certification.

---

## Governance principle

The success criterion for this revision is not "a longer paper" or "a more general-looking theorem."

The target contribution is a set of conditions that lets a reader determine, in a setting beyond the baseline configuration:

> when private compatibility promotes broader formal coordination, when it does not, and why.

If the project cannot deliver that without merely renaming model-specific payoff differences, the correct action is to stop generalization and reposition the certified baseline model.
