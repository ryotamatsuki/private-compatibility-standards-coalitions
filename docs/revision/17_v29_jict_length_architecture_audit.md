# JICT pre-submission structural-length audit of R9 manuscript

Date: 2026-10-13 JST.
Source: **actual generated JICT anonymous reviewer PDF** from Paper CI run 38271682894 (file `jict_manuscript.pdf`; 39 US-letter pages), independently extracted from workflow artifact ID 11757437684; anonymous online supplement 15 pages. Base: `revision/research-track` after PR #32 at commit `b36e7c8fa9e6358c1010dba8bc7c1f9524173ed4`.
Official journal instructions (checked 2026-10-13): https://link.springer.com/journal/10842/submission-guidelines , section “Manuscript Style, General”: papers **should typically be less than 20 double-spaced pages**; **must not exceed 40**. The 39-page package passes only the latter rule and is materially distant from typical length. Current package based on Elsevier `elsarticle[review,authoryear]` formatting; do not pretend 39 pages equals 20 pages by adjusting line spacing, type size or margins.
This file documents a **redesign opportunity**, not a re-certified new shorter manuscript or a waiver of scientific/technical verification. No theory statements or original frozen R9 materials changed.

## Actual page-level allocation (approximate inclusive pages because sections can share a page)

| Material | Actual reviewer PDF page region | Editorial observation |
| --- | --- | --- |
| Title, abstract and Introduction | pp.1–5 | Intro ~3–4 pages, much of it duplicating Secs.6–8. |
| Related Literature | pp.5–8 | ~3–4 pages. Retain nearest theorem comparator; cut broad background repetition. |
| Model | pp.9–15 | **~7 pages** and many exact definitions/equations; main structural compression target. |
| Cournot building blocks | p.16 | Detailed block table + lemma; send table and derivations to SI, retain one compact essentials display. |
| Private adoption | p.17–18 | fixed-cost conditions; keep selection-free existence and necessary definitions, send exhaustive deviations to SI. |
| Government preference and partial residual cost | pp.18–23 | **~6 pages; essential new contribution**. Retain R(d,v), two substantive propositions, same-primitives joint witness, and intuitive CS/producer mechanism. Eliminate repeated descriptions/one redundant diagram/table if necessary. |
| Coalition stability application | pp.24–27 | **~4 pages**, largely supporting *full-bypass* institutional application; keep one concise theorem/corollary and blocking sensitivity, move all subgroup/witness tables and extensive supporting discussion to SI. |
| Scope/robustness | pp.28–31 | **~4 pages**. Keep succinct zero-network, singleton counterexample and R5 differentiated-demand failure; move detailed root characterizations, graphical hierarchy and market-size proof calculations to SI. |
| Discussion and Conclusion | pp.32–35 | ~4 pages, several restatements of Introduction. Merge/reduce if appropriate, retain policy/empirical caveat and economic interpretation. |
| Bibliography | pp.36–39 | ~4 pages, cannot shrink by illegitimately dropping key sources; check working-paper references against publisher's rules. |

Counts are approximate per section, not an additive page decomposition. Literal PDF 39 pages; SI 15.

## Main scientific contribution to preserve VERBATIM IN SCOPE (not necessarily text)

1. Endogenous one-way outsider adoption with full selection-free sufficient conditions and exact admissible witness (supporting, not priority).
2. Initial govt payoff gap `E-D`; incomplete residual adaptation post-gap `-D+R(d,v)`, exact R(d,v), sign regions; *do not* claim political/firm-sign novelty from accounting alone.
3. Strict, nonknife-edge joint equilibrium and preference reversal for *same* `(c,v,lambda,F)` with `0<lambda<1`. This is the standalone paper's principal nontrivial certificate.
4. Negative portability: v=0, singleton-network specification, one prespecified differentiated-demand alternative in both Cournot and Bertrand. These qualifications must remain visible in the main text and abstract.
5. Coalition stability is under FULL bypass `d=0`, under specified blocking rule and small-asymmetry test: an **application**, not evidence of generality at positive residual cost.
6. Home CS gain versus domestic producer-profit loss; unilateral outsider support and lack of reciprocal member-market support; policy inference strictly conditional. No new model, numerical tables, or post hoc generalization.

## Proposed journal-facing page budget (EDITORIAL TARGET, NOT A GUARANTEE)

Target first a **self-contained 24–26-page prototype** and test readability and proof bridges. If that prototype retains essential science, try a second condensation approaching **19–21 double-spaced pages** so the journal's *typical under-20* standard is met as closely as possible. Do not sacrifice mathematical reviewer verifiability to hit an arbitrary page number. If 20 cannot be reached without serious loss, preserve a defensible 22–25-page main paper and document reason rather than fake pagination.

Candidate ~20-page budget (includes citation/reference pages):
- Title, abstract, Introduction: 2 pages
- Theorem-centric closest literature: 1.5 pages
- Model (primitives, timing, national welfare, private adoption strategy and blocking): 3 pages
- Product-market/adoption equilibrium core: 1.5 pages
- Headline residual-rent result + joint adoption/reversal witness + exact proof bridges: 4 pages
- Full-bypass coalition-stability application: 2 pages
- Failure/scope frontier: 1.5 pages
- Discussion/conclusion/limits: 1.5 pages
- References: 3.5 pages
Total ~20.5 pages before layout effects; aspirational, not certified. Each package rebuild, not estimates, determines actual pagination.

## Piecewise reduction strategy, highest marginal value first

**Pass 1 — Structural triage, no math deletion:** collapse Intro+Related Literature repetition, avoid repeating all E,D,R algebra in intro and conclusion, and make the literature compare closest prior theorem mechanisms rather than offer a second survey. Preserve existing citations whose relevance is material. ~2–3 pages potential.

**Pass 2 — Model 7→3–4 page architecture:** retain agents, coalition menu, consumer/network demand, firm costs, timing, national objective and permitted blocking. Move redundant verbal explanations, exhaustive notation, alternative cases and proof-adjacent parameter domain commentary into SI. Replace timing image with a compact sentence if no loss. Most important savings ~2–3 pages. Do not move any indispensable primitive out of main text.

**Pass 3 — Figures and five tables:** 4 figures and 5 generated tables occupy main article; preserve only 1 figure/1 table if they actually carry the economic effect. Candidates to move: timing chart, F-region chart, robustness-hierarchy chart; Cournot block table, adoption threshold table, stability-region table, scope-robustness table. Main could retain residual-rent plot and/or 3-outcome comparison; cross-references to renumbered Online Supplement mandatory. Every move requires edit to JICT packaging script, SI structure and QA, not just hiding `\input` or commenting figures.

**Pass 4 — Stability and portability core:** keep one restricted institutional theorem (d=0) and one paragraph per negative portability mechanism; move full fixed-cost payoff calculations, proof cases, root/Sturm details, alternative demand calculations and redundant graphical material to SI. ~3–5 pages potential, with explanatory bridge in main.

**Pass 5 — Publisher-specific DOI and references:** retain the decisive literature; review two working-paper bibliography entries (`maggiMrazova2024`, `economidesSkrzypacz2003`) against the guideline that reference list contains published/accepted sources and unpublished works normally appear in text. Do not assume the status of an NBER working paper equals a journal article; no silent deletions. Any switch must preserve accurate literature positioning.

## Must-pass short-paper QA

- Reader can reconstruct the causal/strategic mechanism and all key propositions from the MAIN PDF; SI supplies full detailed proofs and all exact deviations, not omitted conjectures.
- Equilibrium, national welfare and finite formal-partition blocking concept still defined unambiguously; R3, R4, R5 and R6 quantifiers unchanged, and negative results explicit.
- Narrative of 3 regions is supplemented by actual joint-feasibility evidence; if a new numerical common-base comparison is added, redo R3 formula and all firm deviations and certify its source.
- A skeptical referee must be able to trace one complete main welfare derivation/critical proof bridge without opening private production code.
- Word/page reductions must not be achieved by font size/margin/line-spacing changes, deleting closest parent works or moving the central economic theorem out of main.
- Build JICT reviewer PDF and anonymous SI, BibTeX/LaTeX source in both clean rooms, check every ref and `\input` or renamed Online Supplement appendix, 40-page absolute cap and preferably typical <20; JICT `make submission` check must pass.
- R2–R9 and Lean regression, all citation/anonymous-replication tests and an independent Stage 11 skeptical-editor review; no silent merge without green CI.
- Run full-original canonical manuscript regression and retain all frozen technical results.
- Journal submission still requires author confirmation of originality, funding/conflict/AI declarations, identity and final portal PDF.

## Decision

**YES: substantial structural compression is warranted BEFORE FINAL SUBMISSION**, even though 39 < 40. Source-grounded goal should be near the typical 20 double-spaced pages, with defensible scientific integrity and journal typography. Current technical QA PASS is not an editorial-length GO. This audit alone authorizes NO wholesale change to R9 theoretical primitives; implement as a separate editorial branch and fresh draft PR, never by overwriting already certified R9 main result.
