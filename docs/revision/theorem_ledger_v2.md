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
- `CONDITIONAL`

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
| N1 | zero-network initial SU advantage is impossible on the boundary extension | PROVED | \(v=0,\ 0<c<1/3\): \(\Phi=c(13c-6)/32<0\) | retain as R4 baseline certificate |
| N2 | complete fixed-c characterization of \(\mathcal V_{SU}(c)\) | PROVED | unique feasible root \(v_{SU}(c)\) for \(0<c<c^\ast\); upper interval above it | R7 independent re-derivation |
| N3 | initial SU advantage exists for some feasible \(v\) iff \(0<c<c^\ast\) | PROVED | \(c^\ast\) is the unique root of \(17c^3+109c^2-89c+11\) in \((0,1/3)\) | preserve exact root isolation |
| N4 | joint initial-SU and reciprocal-disadvantage region | PROVED | nonempty iff \(c_\dagger<c<c^\ast\), with piecewise \(v\)-interval | preserve exact root isolation and joint quantifier |
| N5 | one-way private adoption remains possible at \(v=0\) | PROVED | \(3c(2-c)/16<F<3c(2-3c)/8\) for \(0<c<1/3\) | do not conflate with government reversal |
| N6 | R3 partial-erosion identity survives the zero-network boundary | PROVED | \(R(d,0)=d(5d+2)/32\); incentive change can survive even though initial SU preference does not | R7 re-certify jointly with G2 |
| N7 | singleton-network assumption materially affects the initial SU ranking | CONDITIONAL | minimal S1 alternative is fully certified and gives \(\Phi_{S1}<0\) on the old canonical domain; no universal theorem over all alternatives | carry specification warning into R5/R7 |
| R5-D | frozen differentiated-demand environment is regular and interior on the audit box | PROVED | gamma=1/2; 0<c<1/3, 0<=v<1/4; exact positive-definite and quantity checks | retain as scope condition; do not generalize beyond frozen demand |
| R5-C | pre-adoption SU advantage under the differentiated Cournot comparator | REFUTED ON FROZEN R5 BOX | exact proof gives Phi^C<0 throughout the audit box | use to prevent attribution of R5 failure solely to Bertrand |
| R5-B | portability to the pre-specified differentiated-Bertrand model | REFUTED ON FROZEN R5 BOX | exact Bernstein certificate gives Phi^B<0 throughout the audit box | model-specific non-portability result; no universal Bertrand claim |
| R5-A | one-way outsider-only adoption under the frozen differentiated demand | PROVED | positive selection-free fixed-cost interval exists for both R5-C and R5-B | carry firm/political separation to R7 |
| R5-E | private adoption strengthens the relative IS incentive under R5 | REFUTED ON FROZEN R5 BOX | E^C<0 and E^B<0 exactly; adoption weakens relative IS incentive | surface sign of member-market term as portability condition |
| R5-R | SU-to-IS ranking reversal under R5-C or R5-B | REFUTED ON FROZEN R5 BOX | initial SU preference fails in both modes; post-adoption IS preference remains | do not infer that all differentiated or Bertrand models fail |
| R5-X | R5 political failure is a competition-mode effect | REFUTED | same failure occurs under R5-C and R5-B with identical demand primitives | attribute failure to frozen demand/welfare microfoundation, not price competition alone |

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


## R4 closure

R4 verdict: **COMPLETE — GO TO R5**. The canonical pre-adoption welfare gap has exactly one feasible \(v\)-root whenever an SU-advantage region exists. Writing \(c^\ast\) for the unique root of \(17c^3+109c^2-89c+11\) in \((0,1/3)\), the SU-advantage set is \((v_{SU}(c),\bar v(c))\) for \(0<c<c^\ast\) and empty otherwise. The reciprocal-disadvantage intersection is nonempty exactly for \(c_\dagger<c<c^\ast\), where \(c_\dagger\) is the unique root of \(512c^3-224c^2-241c+18\) in \((0,1/3)\).

At \(v=0\), selection-free one-way adoption remains possible, but the member government never initially prefers SU to IS. The R3 residual-rent identity also survives at \(v=0\), so firm circumvention, erosion of the relative IS incentive, and actual SU-to-IS ranking reversal are distinct objects.

The singleton-network S1 sensitivity is a certified specification warning: giving singleton firms the same own-group network formula eliminates the initial SU advantage throughout the old canonical feasible domain while leaving a one-way-adoption interval at an exact witness. This does not refute R2/R3, but it narrows the interpretation of the current Cournot microfoundation. Route A remains provisional; R5 is authorized and R7 remains the certification gate. Production-manuscript rewriting remains prohibited.


## R5 closure

R5 verdict: **COMPLETE — NON-PORTABILITY IDENTIFIED; R6 AUTHORIZED, NOT STARTED**.

The one pre-specified differentiated-demand environment uses gamma=1/2 and solves Cournot and Bertrand from the same inverse-demand, compatibility, cost, and welfare primitives. Exact analysis shows that the selection-free outsider-only adoption interval remains nonempty in both strategic-variable versions. However, the pre-adoption SU advantage fails everywhere on the frozen audit box in both R5-C and R5-B, and the member-market term satisfies E^C<0 and E^B<0. Thus private adoption weakens rather than strengthens the relative incentive for IS in this environment.

Because the same political failure already occurs under R5-C, R5 does not support a claim that Bertrand competition itself destroys the mechanism. The result is a model-specific demand/welfare portability failure. Route A is materially weakened but the final route decision remains reserved for R7. R6 may proceed only as an institutional robustness audit of the still-valid canonical preference results; production-manuscript rewriting remains prohibited.
