# R8 — Manuscript Reconstruction: Design Freeze

## Status

- Stage: R8
- Branch: `revision/r8-execution`
- Input integration commit: `e7171387f002c4bddac5e7465b56a192fb778056`
- Governing workflow: `research-paper-workflow v2.2 @ 42574d6c5931275ccff3ef7e8b4acc188077332a`
- R7 route: **Route B — LIMITED GENERALIZATION**
- R9 journal reselection / submission audit: **out of scope**
- Target artifact: English production manuscript `paper/main.tex` and its included appendices/figures/tables
- Japanese translation: not canonical for R8 and not updated in this stage

R8 is a writing/integration stage. No new economic primitive, theorem, equilibrium selection rule, or robustness model may be introduced to rescue exposition.

## 1. Frozen paper thesis

The manuscript is reconstructed as a **conditional mechanism paper**.

Permitted central claim:

> In the canonical three-country Cournot microfoundation, a private outsider adaptation can change governments' relative incentives over regional versus international standardization. With residual adaptation cost (d), an equilibrium-derived rent (R(d,v)) determines whether the response reverses the ranking, strengthens the incentive for international standardization without reversal, or weakens that incentive. The result is non-knife-edge within the canonical model but not portable to the one pre-specified differentiated-demand environment.

Not permitted:

- private compatibility generally promotes formal harmonization;
- one-way compatibility/adoption is novel;
- competition-form or demand-system independence;
- network effects are irrelevant;
- the symmetric high-(F) three-SU stable set is institutionally robust;
- IS is unrestricted first best;
- any priority/"first" claim.

## 2. Main-text architecture

R8 keeps ten numbered sections but changes their function.

1. **Introduction** — conditional research question, answer, contribution, and limits.
2. **Related Literature** — parent-class absorption first; isolate the residual-rent government-incentive contribution.
3. **Model** — canonical institutional and product-market primitives; distinguish baseline adoption from the residual-cost extension.
4. **Cournot Building Blocks** — compact formulas only; routine first-order derivations moved to Appendix A.
5. **Private Adoption** — selection-free sufficient conditions plus canonical fixed-cost implementation; adoption is supporting structure.
6. **Private Adaptation and Government Incentives** — central R3 result:
   [
   W_M^{SU,O}(d)-W^{IS}=-mathscr D+R(d,v)
   ]
   with success/intermediate/failure regions, (d_D,d_E), and the joint open-set witness.
7. **Coalition-Stability Application** — strict-blocking application and the robust intermediate-(F) unique-IS result; high-(F) result explicitly labeled symmetry/rule sensitive.
8. **Scope and Robustness** — R4 zero-network and singleton checks; R5 differentiated-demand failure; R6 weak blocking and market-size asymmetry.
9. **Discussion** — interpretation, empirical relevance, limitations; no theorem restatement.
10. **Conclusion** — short conditional conclusion.

The old partner-selection proposition is removed from the main contribution. The market-size perturbation is retained only where it bears on institutional robustness.

## 3. Appendix architecture

- Appendix A: detailed Cournot derivations.
- Appendix B: welfare sign certificates.
- Appendix C: private-adoption equilibrium correspondence.
- Appendix D: residual-cost extension and threshold derivations.
- Appendix E: robustness and institutional-detail proofs (R4/R5/R6 facts used in the text).
- Appendix F: low-(F) continuation cases.

## 4. Figures and tables

R8 figures:

1. timing;
2. residual-rent mechanism with (R(d)), (mathscr D), and (mathscr E);
3. private fixed-cost continuation regions;
4. assumption-dependence summary for the political result.

Numerical figures illustrate certified analytical results and are never used as proof.

R8 tables:

- compact Cournot building blocks;
- adoption thresholds;
- residual-rent government-incentive classification;
- coalition-stability application under strict blocking;
- scope/robustness matrix.

## 5. Claim-to-proof mapping

Every theorem/proposition/corollary retained in the main text must map to an R7-certified ledger item or an inherited exact Stage-8 theorem that remains valid under the R7 scope freeze.

New labels may reorganize already certified material, but no candidate research statement may be promoted by prose alone.

Key mappings:

- private selection-free adoption: G1-U / R3 re-solved thresholds;
- residual-rent classification: G2-S;
- incomplete-adaptation open witness: G2-J;
- zero-network boundary: N1;
- singleton sensitivity: N7 (conditional, one alternative only);
- differentiated-demand non-portability: R5-C/B/E/R/X;
- strict/weak blocking distinction: R6-S/WH/WI/I;
- market-size asymmetry robustness: R6-AH/AI.

## 6. Completion gate

R8 closes only after:

- all English production sections are reconstructed;
- routine Cournot derivations are shortened in the main text and preserved in appendices;
- R3 residual-cost model and proofs are integrated;
- R4/R5/R6 limitations are visible in the main text, not buried only in appendices;
- figures/tables are regenerated reproducibly;
- no R7-prohibited overclaim appears in title, abstract, introduction, theorem statements, discussion, or conclusion;
- the manuscript compiles;
- symbolic/numerical/R1–R7/Lean checks remain green;
- source/submission/replication QA remain green;
- a claim-scope textual audit passes;
- PR to `revision/research-track` passes full CI;
- PR is squash merged;
- post-merge integration CI passes.

R8 closure authorizes R9 only. It does not select a journal and does not mark the manuscript submission-ready.
