# R12 independent referee-style gate — IJIO generality criticism

Date: 2026-10-20. **No change to any original R9 theorem, model result, numerical witness, appendix or proof.**

## Controlling editorial evidence (exact relevance)

The 2026-09-21 IJIO desk-reject letter from editor Sandro Shelegia did **not** dismiss the question of whether private compatibility affects public standards agreements. It praised clarity and identified the narrowness of the existing **three-country linear Cournot modelling** as the central reason for declining external review. It criticized the reliance on comparing profits and welfare across specific Cournot subgame configurations and the lack of a portable economic mechanism. It also expressly said insufficient **innovation / scientific significance**, and doubted IJIO publication. Thus "fix portability" is directly responsive; "novelty automatically follows" is NOT a valid logical implication.

## Second independent numerical/theorem audit — results now verified

- Original R9/PR #34 head: `08d6e6adb1a90bdf03fa223c0961ac04620f0fa2`. Original Section 4 and 10 other scientific source files checked unchanged byte-for-byte in R12 CI.
- General strict investment bound (G1) computed **independently from all** eight SU and 64 SW pure action profiles under the original R9 Cournot demand and original fixed and residual variable costs at the certified witness:
  - (F=9/100=0.09).
  - (ar g_H=2024181/31129600 simeq0.065024318).
  - (ar g_{SW}=2122041/31129600 simeq0.068167949).
  - (g_O^0=459189/3891200 simeq0.118007042).
  - **Strict:** (max{0,ar g_H,ar g_{SW}}<F<g_O^0).
  - Exactly one weak-or-strict Nash continuation in SU (outsider-only) and SW (no adaptation), with strictly positive unilateral margins.
- R12's old uniform welfare-loss sufficient condition **fails even for the original R9 success witness** (though it is not mathematically wrong): the marginal national-welfare change (I(a)=W'(a)) switches from negative to positive during a smooth, expressly artificial compatibility/residual-cost interpolation.
- New general **integrated non-monotone incidence corollary**: if (I) is nondecreasing and (n^{-1}sum_{j=1}^n I(j/n)<-G_0), reversal is guaranteed by an upper Riemann bound. This is a market-response sufficient criterion, not an assumed ex-post ranking.
  - In the exact R9 witness, (G_0=2408509/295731200approx0.00814425059);
  - original post-compatibility SU-minus-IS gap (=-1341/184832approx-0.00725523719);
  - **16-cell certified upper bound** (-0.009698309537<-G_0=-0.008144250590).
  - (W''>0) on ([0,1]) by an exact positive-denominator / degree-five positive-Bernstein-coefficient certificate. Original pre/post R9 market-block output/profit/CS formula recovered exactly, with home output falling and outsider output increasing. **G1 and integrated G3 jointly pass at the same original witness**.
- `research/r12/verify_welfare_mapping.py`, `verify_r9_generic_adoption_dominance.py`, `verify_r9_nonmonotone_incidence.py`, and isolated R12 GitHub CI **PASS** for head `a499edbad74fccba05bb3802eba05ccf7ee5011d`.

## Reviewer-style score, distinguishing mathematical generality from originality

| Criterion | Finding | Editor-facing evidence |
|---|---|---|
| Original model preserved | PASS | Exact original Section 4 prefix and 10 other source files unmodified |
| Mathematically model-neutral decomposition | PASS / conditional | Works with specified independent price and consumer surplus mappings and any regular conduct equilibrium |
| Firm adoption not assumed | PASS, sufficient | Exact G1 dominance bound and full SU/SW deviation audit at R9 original witness |
| Endogenous policy reversal not assumed | PASS, conditional | General incidence response bounds, and integrated alternative verified under R9 even with locally positive welfare response |
| Economic primitive / microfoundation for unrestricted (S,p) | NOT FINISHED | Arbitrary independent price and CS functions are **algebraically possible but not necessarily representable by optimizing consumers**; restrict to economically justified families without losing the R9 nesting |
| Cross-market applicability beyond the original R9 | PARTIAL | R10 provides a same-primitives Cournot/Bertrand existence example; G1+G3 individually not yet certified on that R10 Bertrand path |
| Novelty relative to closest original theorems | NOT CERTIFIED | Standard finite-game dominance + welfare-incidence/response bounds may be absorbed by existing papers |
| Editorial usefulness | CONDITIONAL GO | This is a legitimate response to IJIO's **portability** criticism; it may still be judged a generic restatement without deeper primitive restrictions |
| Journal-ready manuscript | NO | R12 chapter additions exceed internal 17–19-page JICT short-manuscript builder; no approved new manuscript or portal preflight |

## Closest known overlaps from original publications/author sources

1. **Gandal & Shy (2001), JIE, doi 10.1016/S0022-1996(00)00067-2**: public recognition and regional versus international standardization unions, network effects and conversion costs. Original abstract: https://www.sciencedirect.com/science/article/pii/S0022199600000672 .
2. **Besen & Farrell (1994), JEP, doi 10.1257/jep.8.2.117**: strategic decisions to be compatible with rivals, economic benefits to private adoption, industry outcomes. https://www.aeaweb.org/articles?id=10.1257/jep.8.2.117 .
3. **Buccella, Fanti & Gori (2026), EINT 35(2), doi 10.1080/10438599.2025.2478583**: compatibility equilibria including asymmetric adoption under Cournot and Bertrand, network effects and variable costs. Published original abstract: https://www.tandfonline.com/doi/full/10.1080/10438599.2025.2478583 . Full theorem comparison remains open.
4. **Weyl & Fabinger (2013), JPE, doi 10.1086/670401**, especially integrating local market incidence to determine overall surplus; https://www.journals.uchicago.edu/doi/10.1086/670401 .
5. **Adachi & Fabinger (2022), JPubE 211:104589, doi 10.1016/j.jpubeco.2021.104589**: broad demand, firm heterogeneity, market competition, cost interventions and welfare sufficient statistics. Original is open-access (Kyoto University institutional repository): https://repository.kulib.kyoto-u.ac.jp/items/714a3cbe-6950-44b4-830f-f89c6431feaa . **It is improper to market G3 as a newly invented pass-through or local-to-global integration method.**

## Independent recommendation and stop/go

**GO to retain R12 as a generality-oriented substantive revision candidate; HOLD on declaring IJIO objection fully resolved or authorizing a journal submit.** The central claim has stronger *proof coverage* than at R9: original R9 result is not only symbolically nested but satisfies the model-neutral firm-adoption criterion AND a rigorous response-bound welfare reversal criterion. That is real progress. The third-stage assumption on empirically/microeconomically credible (S,p) remains essential, and the sufficient-statistics inequality is not inherently a new IO mechanism.

**Next precise gate**: specify a consumer-welfare-consistent subclass large enough to encompass the original canonical (p=1-Q+g_i,CS=Q^2/2) market; determine whether original R9's network-price adjustment makes this class incompatible with individually rational differentiated consumer choice. If not resolved, clearly label the R12 result a **reduced-form incidence generalization** rather than a fully microfounded conduct-neutral IO theorem. Then directly compare government-choice portion to Gandal–Shy 2001 and firm-compatibility portion to Buccella–Fanti–Gori 2026, before presenting generality as original standalone innovation.

Maintain original 19-page JICT PR #34 unchanged; R12 draft PR #37 unmerged and not submission-ready.
