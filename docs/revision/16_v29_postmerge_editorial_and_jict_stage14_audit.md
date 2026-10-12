# R9 v2.9 post-merge Stage 11 referee audit & JICT Stage 14 preflight

Date: 2026-10-13 (JST). Reviewed baseline: merged PR #31, commit 35360048ce2e9f0ecab2427ac667d8f39ff70eac on revision/research-track. Proposed minor wording-only addition: revision/v29-final-editorial-qa-20261013. Earlier R9 (v2.2) math freeze remains intact.

## Separate decisions

**Stage 11 — ECONOMIC EDITORIAL VALUE: CONDITIONAL GO, no additional theorem is required at this stage.** The model answers the title's limited question: when endogenous outsider-only support for a bloc standard shifts a regional member government's *preference* for a formal international arrangement. It does NOT prove a general trend toward harmonization nor positive-d stable coalition formation. The product-market bridge is independently reconcilable with welfare components. The significance is a conditional institutional mechanism with verified joint adoption/ranking feasibility and identified failures, rather than novelty of the three sign inequalities. The proposition can be nontrivial but JICT desk rejection on restricted network microfoundations and small effect sizes is plausible.

**Stage 14 — EDITORIAL SOURCE & CURRENT POLICY PREFLIGHT: technically eligible / final CI PENDING FOR THE NEW BRANCH, author-only declarations PENDING.** Neither current audit nor CI constitutes an actual journal submission.

## Strongest skeptical referee rejection, answered at narrow claim level

Rejection: Three sign regions are algebraic rearrangements of welfare quantities in a restrictive segmented three-country Cournot demand model; the baseline singleton-network convention is pivotal and differentiated demand removes the initial regional preference. The static coalition-stability application uses full bypass, not the headline positive residual-cost extension. There is no fully modelled policy mechanism or empirical validation. Why is a 38-page applied-theory manuscript justified?

Answer: The stand-alone result is *not* the algebraic trichotomy or a universal harmonization recommendation. Outsider-only adaptation must arise in firm equilibrium under the SAME primitives as government preference reversal; the post-adoption member-market domestic CS gain versus incumbent producer-profit decline determines formal-regime continuation incentives, despite technological interoperability increasing. Explicit failures in v=0, singleton-network alternative and one differentiated-demand class prevent conflating private adoption with political harmonization. Under JICT aims, a conditional diagnostic with measurable setup costs, residual variable costs and unilateral vs reciprocal compliance may constitute an applied-theory contribution. Nevertheless, no existing test certifies the magnitude or cross-institution portability; the editor could still reject for insufficient scientific reach. This is **AI-assisted adversarial review, not independent human refereeing**.

## Current journal source check (2026-10-13)

Official scope: https://link.springer.com/journal/10842/aims-and-scope (applied theory manuscripts must highlight empirical and policy implications).
Official guidelines: https://link.springer.com/journal/10842/submission-guidelines .
Official editorial board: https://link.springer.com/journal/10842/editorial-board . Editor-in-Chief Justus Haucap, which matches jict_cover_letter.tex.
Springer Nature AI manuscript policy: https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation .

### Compliance matrix

| Requirement | Latest evidence | Status |
|---|---|---|
| Relevance to journal | industry, trade, interoperability, applied economic theory | PASS WITH SIGNIFICANCE RISK |
| Explicit empirical/policy implication | Discussion added **conditional** prediction: lower residual unit compliance cost d within the outsider-only equilibrium weakly strengthens government incentive for multilateral coordination because R'(d)>0; warned not an unconditional real-world prediction | EDITORIAL IMPROVEMENT ON NEW BRANCH; REBUILD PENDING |
| Page length | Springer normally <20 double-spaced pages, never >40; latest pre-change PR CI confirmed 38-page reviewer body and 15-page online supplement | **PASS absolute**, significant near-ceiling editorial risk. Reconfirm after new change |
| Double blind | reviewer manuscript and technical SI anonymous; separate identified title page; pre-change CI source and PDF anonymity tests passed | PASS IN INHERITED CI, repeat |
| Abstract & keywords | 150–250 words; 4–6 keywords; JEL | PASS IN INHERITED CI, repeat |
| Editor name | Editor-in-Chief **Justus Haucap** on live board; cover letter addressed to Professor Haucap | PASS |
| Mathematical LaTeX | explicitly allowed; flat source archive no subfolders; previous independent recompile passed | PASS IN INHERITED CI, repeat |
| References | Innocenti & Menicucci 2021 DOI 10.1016/j.jebo.2021.05.005; Ding, Ko & Shen 2022 DOI 10.1016/j.econmod.2022.105989; Maggi & Mrazova NBER w33318 2024 with 2026 revised working-paper version | VERIFIED FROM PUBLISHER; a strict reading of journal guidance says bibliography should include published/accepted works, therefore treatment of NBER and old NYU working papers to check at final portal; do NOT delete essential citations without author review |
| Declarations & substantive AI assistance | body `paper/sections/11_submission_declarations.tex` and `submission/jict_title_page.tex` disclose materially substantive assistance and human responsibility, code/data, funding and competing interests | EXIST / AUTHOR MUST VERIFY TRUTH |
| Supplement formatting vs anonymity | Springer generic SI advice requests author name; JICT-specific double-blind policy requires blind files; keep anonymized reviewer/SI copies and place name/contact only on separate identified Title Page; if live portal insists on named final SI, distinguish publication version from review version | PORTAL-DEPENDENT |
| Submission originality & affiliation | JICT metadata says IJIO desk rejected, no simultaneous submission assumed, single author independent researcher | **AUTHOR VERIFICATION REQUIRED** |
| Technical reproducibility | R2–R9, Lean, canonical latex, anonymous archive, clean-room source build and replication package PASS on PR #31 | PASS BASELINE; RECONFIRM NEW PR |
| Post-merge push run for 35360048 commit | available GitHub connector exposes PR-triggered runs only, and returned no run for merge commit | NOT OBSERVED, do NOT claim post-merge CI independently passed |

## Bounded economic implication and scope

The newly edited Discussion states a testable within-model comparative static: conditional on E>D>0 and **unchanged private adoption selection** with comparable c, v, lower residual marginal cost d lowers R(d,v), so Δ_SU−IS becomes smaller, i.e. international formal coordination more attractive. Across different firms, governments and sectors F and market structure jointly affect selection and E,D, so the statement is not an unconditional cross-sectional causal prediction. It does not introduce a new parameter or theorem; it is the signed derivative of an established R3 quantity.

At c=0.1, the canonical initial regional advantage requires sufficiently strong network parameter v under the model's narrow feasible interval (earlier v0≈0.2204586 at that c), hence the economically important macro-level portability risk remains. No new empirical effects/size calibration is asserted.

## Research-question completeness

- Title: *Private Compatibility and Government Incentives for Standards Harmonization* — answered within the frozen microfoundation.
- Positive residual-cost government ranking versus stable-coalition selection at full bypass — explicitly distinguished, **BOUNDED LIMITATION** rather than an omitted theorem essential to the title.
- No intervention or social planner globally optimal policy claimed. **Diagnostic-only** welfare channel defensible as applied theory with explicit within-model observable implication, though an editor may require a richer application.
- Restrictive singleton network/differentiated demand non-portability honestly disclosed and retained.
- No broader new dynamic private-government coalition theory warranted (post-R9 Stage 2 audits show substantial McLaren, Celik, Battaglini, Maggi parent art).

## Final decision tree

1. **Rerun full Paper CI** on small editorial change; require reviewer pages <=40; all source/anon/supplement/Lean/replication pass; if fail, correct without theory changes.
2. **Merge editorial-only PR only on full green CI**. Validate merged file and PR merged status. Do not claim post-merge CI if unavailable.
3. Treat Stage 11 economic editor-value as **CONDITIONAL GO**, given limited model-specific contribution and lack of independent external human evaluation; no new mathematics required by this AI reviewer.
4. **Stage 14/15 not fully certified** until author reads current final PDF and explicitly confirms originality, AI disclosures and own scholarly contribution, prior public dissemination, author/ORCID/email/affiliation, JICT online portal choices, and no simultaneous consideration. Live portal must approve uploaded LaTeX compilation. No tool-mediated journal submission performed here.
5. Editorial outcome is uncertain. R9 JICT fit does not guarantee peer review.

## Sources

Repository: revision/research-track/paper/main.tex; sections/01_introduction.tex,02_related_literature.tex,06_selective_erosion.tex,09_discussion.tex,10_conclusion.tex,11_submission_declarations.tex; submission/jict_title_page.tex, jict_cover_letter.tex, jict_metadata.md. PR #31 preceding build run 38269895237 (JICT reviewer 38 pp, 15 pp supplement; all verified).
