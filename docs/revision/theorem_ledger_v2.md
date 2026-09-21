# Revision Theorem Ledger v2

This ledger governs **new research status only**. It does not overwrite `docs/THEOREM_LEDGER.md`, which remains the historical Stage-8/IJIO-version record.

Status vocabulary used here:

- `LEGACY CERTIFIED`
- `LEGACY CERTIFIED / REOPENED FOR GENERALIZATION`
- `CANDIDATE — UNPROVED`
- `PROVED`
- `PROVED IN PRECHECK`
- `SECONDARY`
- `OUT OF SCOPE FOR CURRENT STAGE`
- `REFUTED`
- `UNRESOLVED`

| ID | Result | Status | Exact scope / dependency | Next certification requirement |
|---|---|---|---|---|
| V2-L1 | canonical Cournot product-market blocks | LEGACY CERTIFIED | old canonical domain only | retain as R2/R3 mapping benchmark |
| V2-L2 | canonical adoption correspondence | LEGACY CERTIFIED | binary standard support, segmented markets, old costs | compare with G1; do not infer generality |
| V2-I1 | exact selective-erosion identity | LEGACY CERTIFIED / REOPENED FOR GENERALIZATION | exact post-bypass member-market equality to IS; outsider market unchanged | R3 must relax exact erosion |
| V2-T1 | old ranking-reversal theorem | LEGACY CERTIFIED / REOPENED FOR GENERALIZATION | \(\mathscr E_i>\mathscr D_i>0\) plus V2-I1 | separate incentive increase from actual reversal |
| V2-P1 | three-country Cournot microfoundation | LEGACY CERTIFIED | \((c,v)\in\Omega_0\) | becomes microfoundation if G1/G2 survive |
| V2-T2 | strict-blocking stable-set reversal | SECONDARY | symmetry, strict blocking, old institutional menu | R6 alternative blocking/asymmetry audit |
| V2-N0 | zero-network baseline gap | PROVED IN PRECHECK | \(v=0,\;0<c<1/3\) in old symmetric Cournot model | preserve symbolic regression test |
| G1-E | outsider-only adoption is a strict Nash equilibrium under profile-specific net-gain inequalities | PROVED | segmented-market locality; Proposition R2.1 | retained as certification result, not standalone novelty |
| G1-U | outsider adoption/member non-adoption are strict dominant actions under robust gain bounds; outsider-only adoption is unique | PROVED — SUFFICIENT, NOT NECESSARY | finite binary action space; Theorem R2.2 | use as selection-free R3 continuation condition |
| G1-S | coalition expansion changes the one-way feasibility slack by \(\Delta U-\Delta L_+\); interval creation also requires positive final slack | PROVED — CONDITIONAL | R2 scope/competition decomposition | monotonic larger-bloc claim is rejected; carry condition to R3 |
| G1-C | asymmetric adopter costs preserve selection-free one-way adoption when outsider value is positive and member costs exceed robust reverse gains | PROVED | Proposition R2.4 | robustness only; not a novelty claim |
| G1-O | additive optional deployment has value \(\sum_k\max\{u_k,0\}\); pure option-set expansion is weakly nondecreasing | PROVED | R2 optional-deployment boundary test | H2.4 strong form refined; negative scope needs package or payoff feedback |
| G2-L | ranking reversal survives positive residual adaptation cost locally around full bypass | PROVED IN R3 — PENDING R7 RECERTIFICATION | canonical Cournot extension with d=lambda c and full compatibility | independent adversarial re-derivation at R7 |
| G2-S | residual-rent function R(d) separates reversal, incentive-strengthening-only, and incentive-weakening regions | PROVED IN R3 — PENDING R7 RECERTIFICATION | Proposition R3.1 and thresholds d_D,d_E | test parent-theorem absorption and independent proof at R7 |
| G2-J | incomplete adoption and government ranking reversal coexist with a selection-free firm equilibrium on a nonempty open set | PROVED IN R3 — PENDING R7 RECERTIFICATION | exact witness (c,v,lambda,F)=(1/10,6/25,1/2,9/100) plus continuity | retain as joint-region certificate |
| R5-B | portability to one differentiated-Bertrand model | AUTHORIZED AFTER R4 IF ROUTE A SURVIVES | R2/R3 provisional Route A | execute one pre-specified differentiated-Bertrand test |

## Quantifier discipline

For G1, four statements remain separate:

1. a proposed outsider-only profile is an equilibrium;
2. it is a strict equilibrium;
3. it is the unique equilibrium;
4. all equilibrium selections imply outsider-only adoption.

No evidence for (1) is evidence for (3) or (4).

For G2, three statements remain separate:

1. private adaptation raises the relative incentive for IS;
2. that change reverses the government's ranking;
3. the firm-adoption equilibrium that produces the change exists for the same primitives.

The R2 and R3 parameter sets must eventually have a verified nonempty intersection before a joint headline claim is certified.

## R2 closure

R2 verdict: **CONDITIONAL GO TO R3**. G1 is retained as a supporting structural lemma with high prior-art overlap. The common-cost scope-dominance condition and the scope-versus-reverse-threshold comparative static are mathematically certified for the stated R2 model, but no standalone theorem-novelty claim is authorized. See `02_r2_results.md` and `02_r2_literature_absorption.md`.


## R3 closure

R3 verdict: **GO**. The exact full-bypass identity has been replaced by an equilibrium-derived residual-rent function

[
R(d)=rac{d[(5-4v)d+2(1-4v)]}{32(1-v)^2}.
]

The new government effect is conditional: reversal iff (R(d)<mathscr D), incentive strengthening without reversal when (mathscr D<R(d)<mathscr E), and incentive weakening when (R(d)>mathscr E). The firm-adoption and ranking conditions have a verified nonempty open intersection with (0<lambda<1). These are R3 research results, not yet R7-certified final-paper theorems.
