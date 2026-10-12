# Post-R9 Stage 2 frontier addendum (v2.9 + unreleased result-boundary refinement)

Date checked: 2026-10-12
Status: PROVISIONAL — Stage 2 NOT CERTIFIED; no Stage 3/4 or manuscript change authorized.
Branch: research/v29-frontier-addendum-20261012 (based on revision/research-track).
Scope: source-based missing-literature audit, not a replacement for the R0–R9 re-certification.
Governing workflow reference: research-paper-workflow v2.9 (stable), plus unreleased main checklist RESULT_REVERSAL_BOUNDARY_CHECKLIST.md. Existing R0–R9 was certified under v2.2 and remains historically valid at its certified scope.

## Existing results that MUST NOT be rediscovered as novel

- R7 certified **Route B: LIMITED GENERALIZATION**, not a portable general theorem.
- R3: for incomplete outsider adaptation with residual cost d=lambda*c, the member-government difference is `W_M(SU,O;d)-W(IS) = -D + R(d,v)`, with `R(d,v)=d*((5-4v)*d+2*(1-4v))/(32*(1-v)^2)`. Reversal / strengthening-only / weakening are separated by existing thresholds.
- R3 joint open-set result: incomplete adaptation, selection-free outsider-only adoption, and government preference reversal can coexist. Do not claim mere incomplete adoption as new.
- R4: zero-network and singleton-specification boundaries.
- R5: in the pre-specified differentiated-demand environments, outsider-only adoption survives, but the proposed political sign/reversal fails under **both** Cournot and Bertrand. Do not assert that only Bertrand breaks the result.
- R6: symmetric high-F strict-blocking three-SU stability is sensitive to weak/Pareto blocking; intermediate unique-IS is more robust within the canonical menu.
- R9: revised paper title **Private Compatibility and Government Incentives for Standards Harmonization**; JICT reviewer package technically ready (as of 2026-09-22), actual submission not performed by R9; preexisting R9 track formally closed. The legacy main README is stale; use revision/research-track documents for the revised paper.

Primary internal evidence: docs/revision/{07_novelty_reassessment.md,05_r5_results.md,09_r9_closure.md,09_novelty_recheck.md,theorem_ledger_v2.md}.

## Newly inspected external closest-paper checks (as of 2026-10-12)

Reading-depth legend: FULL/SECTION = accessible preprint proposition and/or conclusion inspected; ABSTRACT/PUBLISHER = original publisher or institutional abstract plus metadata only. Later-paper coverage is incomplete. Absence of a paper in the current references.bib is a bibliography gap, not proof earlier authors never read it.

1. **Innocenti & Menicucci (2021), _Partial compatibility in oligopoly_**, JEBO 188:351–378, DOI 10.1016/j.jebo.2021.05.005. Accessible 2021 working-paper PDF: https://www.crctr224.de/research/discussion-papers/archive/dp278/@@download/file/CRCTR224_2021_278.pdf . FULL/SECTION: Proposition 1 (paper PDF p. 11) gives compatibility weakly dominant among symmetric firms in a two-stage compatibility–**price competition** game, subject to a trivial equilibrium distinction. Proposition 3 (PDF p. 20) gives quality-asymmetry regimes: all C, large firm NC only, all NC. AUTHOR-STATED future direction (PDF p. 23): alternative forms of firm asymmetry and **multiple standards allowing clusters of more than three firms**. Publication vs working-paper version differences still to check. Implication: endogenous/partial compatibility and asymmetry are not novel ingredients. Government standards-coalition feedback remains distinct only if it generates an unabsorbed theorem.

2. **Ding, Ko & Shen (2022), _Partial compatibility in two-sided markets: Equilibrium and welfare analysis_**, Economic Modelling 116:105989, DOI 10.1016/j.econmod.2022.105989. Publisher abstract: https://www.sciencedirect.com/science/article/pii/S0264999322002322 . ABSTRACT/PUBLISHER ONLY. Shows **partial compatibility can be a unique coalition-proof outcome**, compatibility costs can induce a direct move from full compatibility to incompatibility, and partial compatibility can maximize consumer/total surplus. Crucial additional parent-theorem threat for any "private compatibility + coalition-proofness + welfare" claim. The coalitions belong to platforms/compatibility choices, whereas the target paper concerns governments and formal agreements. Exact solution concept and theorem absorption UNRESOLVED until full source/proofs obtained.

3. **Stadler, Tobler Trexler & Unsorg (2022), _The Perpetual Trouble with Network Products Why IT Firms Choose Partial Compatibility_**, Networks and Spatial Economics 22:903–913, DOI 10.1007/s11067-022-09572-x, full open text: https://link.springer.com/article/10.1007/s11067-022-09572-x . FULL/SECTION. Explicit two-stage endogenous **continuous** compatibility choice and pricing; symmetric equilibrium compatibility can be interior when standardization coordination costs are high / installed base small; also studies common compatibility decisions. Strong antecedent to any continuous-compatibility extension. No government-region institutional coalition stage identified in inspected sections. Further full proposition/appendix cross-check pending.

4. **Chou (2026), _Asymmetric Compatibility Between Open-Source Software and Proprietary Software_**, Review of Industrial Organization 68(2):217–242, DOI 10.1007/s11151-025-10034-0. Publisher/RePEc abstract: https://ideas.repec.org/a/kap/revind/v68y2026i2d10.1007_s11151-025-10034-0.html . ABSTRACT/PUBLISHER ONLY. Studies continuous unilateral compatibility with asymmetric quality, installed base, and objective functions, including partial/full incompatibility choices. Another antecedent blocking novelty based solely on continuous unilateral bypass.

5. **Klimenko (2009), _Strategic interoperability standards and trade taxes_**, International Review of Economics & Finance 18(4):539–551, DOI 10.1016/j.iref.2008.09.015. Publisher original: https://www.sciencedirect.com/science/article/pii/S1059-0560%2808%2900124-X . ABSTRACT/PUBLISHER + accessible introduction. Explicitly analyzes the importing government's minimum compatibility standard and the exporting government's tax/subsidy for costly compatibility-enhancing investment. Therefore simply adding government compatibility policy/subsidy does NOT confer novelty. No government coalition-stability theorem established by inspected text.

6. **Llanes & Poblete (2020), _Technology Choice and Coalition Formation in Standards Wars_**, Journal of Industrial Economics 68:270–297, DOI 10.1111/joie.12207. 2014 working paper (must not automatically equate every theorem with final article): https://www.tse-fr.eu/sites/default/files/medias/doc/conf/sic/conf%202015/llanes.pdf . FULL/SECTION: WP Proposition 1 gives existence of stable allocation in standard-sponsor coalition game; WP Proposition 5: connected first-best allocation => stable allocations first-best under its transfer/connectivity premises. AUTHOR-STATED further research in WP §8: bargaining costs; technology replacement/reversibility; innovation incentives; etc. Strong dynamic/coalition parent-class threat for irreversible adoption / renegotiation. Sponsors and governments differ; cannot infer full absorption without a theorem map.

7. **Gandal & Shy (2001)**, Journal of International Economics 53:363–383, DOI 10.1016/S0022-1996(00)00067-2. Publisher abstract: https://www.sciencedirect.com/science/article/pii/S0022199600000672 . ABSTRACT/PUBLISHER on this pass, canonical old model within repo. Regional standardization unions can be privately attractive under high conversion costs; strength of network externalities changes mutual recognition incentives. Exact proposition numbering/conditions in original published text still to verify.

8. **Takarada, Kawabata, Yanase & Kurata (2020)**, Journal of Public Economic Theory 22, DOI 10.1111/jpet.12425. https://onlinelibrary.wiley.com/doi/10.1111/jpet.12425 . Publisher abstract: this is **negative consumption externality regulatory/product/process standards**, not simply a private technical-interoperability model. Has core stability of regional/multilateral agreements and fixed multi-standard costs. Its institutional solution concept is close, but welfare primitives differ materially. Exact theorem/author-limitations reading PENDING.

## References gap (confirmed against revision/research-track/paper/references.bib)

The reference file does **not** contain author-name entries for Innocenti, Ding, Stadler, Chou, or Llanes/Poblete as of the present reading. This is a reading/audit prioritization signal, not automatic grounds for citing all five. Klimenko and Guo do appear by author name. Do not edit bibliography before deciding relevance and validating bibliographic/version metadata.

## Candidate frontier after novelty-kill update

A: A generic **continuous/partial compatibility** extension is HIGH PRIOR-ART RISK. Existing R3 already gives incomplete **adaptation cost relief**, so do not duplicate it. A live question would need an independently determined new government equilibrium/stability or a sharp condition that is NOT merely an algebraic reexpression or inherited comparative static. Parent threats: Stadler 2022, Chou 2026, Ding 2022 and general coalition-theory reduction. STATUS: PROPOSED; NO GO.

B: **Irreversible private standards investments and ex-post renegotiable formal government coalitions** might change commitment incentives and coalition stability. Need specify a stateful game and an economic conclusion unavailable under existing sunk-cost/hold-up/dynamic-coalition parent theorems. Preserve exact nested R9 model; compare coalition continuation with sunk costs vs rebuilding standards. Parent threats: Llanes/Poblete and generic dynamic hold-up. STATUS: PROPOSED, first candidate for further literature-focused test, NOT mathematically tested, NO GO.

C: **Government compatiblity mandates/subsidies** by themselves are substantially anticipated by Klimenko 2009; reconsider only if a strictly new government's *coalition-dependent and incentive-compatible* policy theorem exists, not extra choice variables. STATUS: DOWNGRADE pending stronger justification.

D (cross-paper new-question candidate): **formal governmental coalition vs effective firm compatibility coalition with endogenous investment and blocking**. This is close to the current paper's subject, so it must state exactly what new government equilibrium/representation or impossibility could not be obtained from R9 residual-rent conditions, Ding 2022 private coalition-proof compatibility, or Llanes/Poblete firm sponsor coalition game. STATUS: PROPOSED, likely structural-absorption risk.

## Stage 2 next gate

1. Acquire/inspect full theorem statements and conclusions of Ding 2022, Klimenko 2009, Chou 2026, Takarada 2020 and published Llanes/Poblete 2020; report access limitations and do not paraphrase inaccessible theorem contents.
2. Build explicit `predecessor theorem -> agents/timing/actions/payoffs/equilibrium -> mapping -> ABSORBED/PARTIAL/NOT` for G2 and each NEW candidate. Distinguish private-firm coalition-proofness from governments' core/strict blocking.
3. Extract verified author-stated limitations versus auditor-inferred gaps with page/section; test forward citations, same-author later papers, general parent theorems. `NOT LOCATED` != `OPEN`.
4. Only if a candidate survives, prepare Stage 3 shortest kill test and explicit author selection; existing R9 certified scope and JICT package remain unchanged.

**Decision:** Stage 2 incremental frontier audit INCOMPLETE / UNRESOLVED; no recertified new substantive theorem; no new paper or journal switch authorized. All proposals explicitly NOT IMPLEMENTED.
