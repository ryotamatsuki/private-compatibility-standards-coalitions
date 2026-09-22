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
| V2-T2 | strict-blocking stable-set reversal | SECONDARY / R6 AUDITED | symmetry, strict blocking, old institutional menu | R6 shows high-F multiplicity is rule/symmetry sensitive; intermediate unique-IS result is robust within canonical microfoundation |
| V2-N0 | zero-network baseline gap | PROVED IN PRECHECK | \(v=0,\;0<c<1/3\) in old symmetric Cournot model | preserve symbolic regression test |
| G1-E | outsider-only adoption is a strict Nash equilibrium under profile-specific net-gain inequalities | PROVED | segmented-market locality; Proposition R2.1 | retained as certification result, not standalone novelty |
| G1-U | outsider adoption/member non-adoption are strict dominant actions under robust gain bounds; outsider-only adoption is unique | PROVED — SUFFICIENT, NOT NECESSARY | finite binary action space; Theorem R2.2 | use as selection-free R3 continuation condition |
| G1-S | coalition expansion changes the one-way feasibility slack by \(\Delta U-\Delta L_+\); interval creation also requires positive final slack | PROVED — CONDITIONAL | R2 scope/competition decomposition | monotonic larger-bloc claim is rejected; carry condition to R3 |
| G1-C | asymmetric adopter costs preserve selection-free one-way adoption when outsider value is positive and member costs exceed robust reverse gains | PROVED | Proposition R2.4 | robustness only; not a novelty claim |
| G1-O | additive optional deployment has value \(\sum_k\max\{u_k,0\}\); pure option-set expansion is weakly nondecreasing | PROVED | R2 optional-deployment boundary test | H2.4 strong form refined; negative scope needs package or payoff feedback |
| G2-L | ranking reversal survives positive residual adaptation cost locally around full bypass | PROVED — R7 RECERTIFIED | canonical Cournot extension with d=lambda c and full compatibility | freeze for R8; do not generalize beyond the certified canonical microfoundation |
| G2-S | residual-rent function R(d) separates reversal, incentive-strengthening-only, and incentive-weakening regions | PROVED — R7 RECERTIFIED | canonical Cournot extension; exact residual-rent classification | principal surviving conditional mechanism result; no portability claim beyond certified scope |
| G2-J | incomplete adoption and government ranking reversal coexist with a selection-free firm equilibrium on a nonempty open set | PROVED — R7 RECERTIFIED | exact witness (c,v,lambda,F)=(1/10,6/25,1/2,9/100) plus strict inequalities and continuity | retain as existence/open-set certificate; not a global characterization |
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
| R6-S | legacy symmetric strict-blocking stable sets | PROVED | high F: three SUs; intermediate F: IS only | retain only as institution-specific canonical result |
| R6-WH | symmetric high-F stable set under weak/Pareto blocking | PROVED EMPTY | every SU is weakly blocked by an alternative SU; SW and IS also blocked | record exact institutional fragility; do not repair by changing rule |
| R6-WI | symmetric intermediate-F stable set under weak/Pareto blocking | PROVED | IS uniquely stable | strict payoff gaps, not indifference, drive result |
| R6-I | source of high-F strict-blocking stability | PROVED | common member is indifferent across symmetric SUs while former outsider strictly gains | label symmetry-induced indifference explicitly |
| R6-AH | small market-size asymmetry in high-F region | PROVED LOCALLY | m1=m2=1, m3=1-delta; SU12 uniquely stable under both blocking rules for sufficiently small delta>0 | exact witness line is stronger: all 0<delta<1 at c=1/10,v=6/25,F=1/5 |
| R6-AI | small market-size asymmetry in intermediate-F region | PROVED LOCALLY | outsider-only adoption remains selection free locally; IS uniquely stable under both rules | exact witness certifies 0<delta<=1/2 at c=1/10,v=6/25,F=3/25 |
| R6-WF | intermediate-region welfare ranking | PROVED / MENU-LOCAL | IS Pareto-dominates SW and all SU continuations within the five-partition menu on certified neighborhood | no unrestricted first-best claim |

| R7-CR | independent clean-room reconstruction of the R3–R6 headline inputs and exact witnesses | PROVED | independent SymPy evaluator reconstructs Cournot states, welfare blocks, R3 residual-rent identity, R4 boundary identities, frozen R5 witness signs, and R6 deviation identities without importing R2–R6 verification modules | CI regression gate in R8/R9 |
| R7-FV1 | zero-network initial-SU gap is negative for 0<c<1/3 | FORMALLY VERIFIED | Lean 4 + mathlib; theorem `FV1_zeroNetworkGapNegative` | algebra/order core only; economic derivation remains clean-room responsibility |
| R7-FV2 | residual-rent function is strictly increasing in residual adaptation cost on the certified network domain | FORMALLY VERIFIED | Lean 4 + mathlib; theorem `FV2_residualRentStrictlyIncreasing` | canonical residual-rent expression only |
| R7-FV3 | R<D implies the post-adoption SU-minus-IS gap -D+R is negative | FORMALLY VERIFIED | Lean 4 + mathlib; theorem `FV3_postGapNegative` | logical/algebraic implication |
| R7-FV4 | E>D>0 and R<D imply both stronger relative IS incentive and preference reversal | FORMALLY VERIFIED | Lean 4 + mathlib; theorem `FV4_preferenceEffect` | logical/algebraic implication; no claim that antecedents are general |
| R7-FV5 | weak blocking admits one indifferent plus one strict gainer whereas strict blocking does not | FORMALLY VERIFIED | Lean 4 + mathlib; theorem `FV5_indifferenceSeparatesBlockingRules` | two-deviator predicate core only |
| R7-N | proposition-level novelty re-kill | COMPLETE — LIMITED NOVELTY SURVIVES | G1 substantially overlaps converter/one-way-compatibility and fixed-cost-scope parent classes; G2 exact government-ranking partition not directly absorbed in located closest literature but is model-specific | no priority/first claim; R8 must position as conditional mechanism |
| R7-R | final research route | ROUTE B — LIMITED GENERALIZATION | adoption logic broadens, but preference reversal is tied to the restricted canonical market structure and fails in the frozen R5 differentiated-demand test | R8 authorized as conditional-mechanism manuscript reconstruction |

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

The new government effect is conditional: reversal iff (R(d)<mathscr D), incentive strengthening without reversal when (mathscr D<R(d)<mathscr E), and incentive weakening when (R(d)>mathscr E). The firm-adoption and ranking conditions have a verified nonempty open intersection with (0<lambda<1). These R3 results were subsequently independently re-derived and re-certified at R7 within the explicitly frozen canonical scope.


## R4 closure

R4 verdict: **COMPLETE — GO TO R5**. The canonical pre-adoption welfare gap has exactly one feasible \(v\)-root whenever an SU-advantage region exists. Writing \(c^\ast\) for the unique root of \(17c^3+109c^2-89c+11\) in \((0,1/3)\), the SU-advantage set is \((v_{SU}(c),\bar v(c))\) for \(0<c<c^\ast\) and empty otherwise. The reciprocal-disadvantage intersection is nonempty exactly for \(c_\dagger<c<c^\ast\), where \(c_\dagger\) is the unique root of \(512c^3-224c^2-241c+18\) in \((0,1/3)\).

At \(v=0\), selection-free one-way adoption remains possible, but the member government never initially prefers SU to IS. The R3 residual-rent identity also survives at \(v=0\), so firm circumvention, erosion of the relative IS incentive, and actual SU-to-IS ranking reversal are distinct objects.

The singleton-network S1 sensitivity is a certified specification warning: giving singleton firms the same own-group network formula eliminates the initial SU advantage throughout the old canonical feasible domain while leaving a one-way-adoption interval at an exact witness. This does not refute R2/R3, but it narrows the interpretation of the current Cournot microfoundation. Route A remains provisional; R5 is authorized and R7 remains the certification gate. Production-manuscript rewriting remains prohibited.


## R5 closure

R5 verdict: **COMPLETE — NON-PORTABILITY IDENTIFIED; R6 AUTHORIZED, NOT STARTED**.

The one pre-specified differentiated-demand environment uses gamma=1/2 and solves Cournot and Bertrand from the same inverse-demand, compatibility, cost, and welfare primitives. Exact analysis shows that the selection-free outsider-only adoption interval remains nonempty in both strategic-variable versions. However, the pre-adoption SU advantage fails everywhere on the frozen audit box in both R5-C and R5-B, and the member-market term satisfies E^C<0 and E^B<0. Thus private adoption weakens rather than strengthens the relative incentive for IS in this environment.

Because the same political failure already occurs under R5-C, R5 does not support a claim that Bertrand competition itself destroys the mechanism. The result is a model-specific demand/welfare portability failure. Route A is materially weakened but the final route decision remains reserved for R7. R6 may proceed only as an institutional robustness audit of the still-valid canonical preference results; production-manuscript rewriting remains prohibited.


## R6 closure

R6 verdict: **COMPLETE — INSTITUTIONAL DEPENDENCE IDENTIFIED; GO TO R7**.

Under exact symmetry and high fixed cost, the legacy strict-blocking stable set of the three regional SUs is reproduced. Under weak/Pareto blocking, however, the high-F stable set is empty: an alternative SU gives the common member the same payoff and the former outsider a strict gain. Hence the exact symmetric high-F stability correspondence depends on both the strict-blocking rule and symmetry-induced indifference.

The specified market-size perturbation m1=m2=1, m3=1-delta breaks that equality. For sufficiently small delta>0, SU12 is uniquely stable under both blocking concepts. At the exact witness (c,v,F)=(1/10,6/25,1/5), this stronger conclusion holds for every 0<delta<1.

In the intermediate region, every SU country strictly prefers IS after outsider-only bypass, and IS remains uniquely stable under both blocking concepts and small asymmetry. At (c,v,F)=(1/10,6/25,3/25), the result is certified for 0<delta<=1/2 with the private-adoption continuation re-solved after every deviation.

R6 therefore separates a comparatively robust preference/unique-IS result from a fragile exact high-F symmetric stable-set correspondence. It does not repair the R5 portability failure. R7 is the next and only authorized stage; production-manuscript rewriting remains prohibited.


## R7 closure

R7 verdict: **COMPLETE — ROUTE B (LIMITED GENERALIZATION); R8 AUTHORIZED, NOT STARTED**.

R7 independently reconstructed the surviving R2–R6 theory using a clean-room evaluator rather than importing the stage-specific verification modules. The canonical R3 residual-rent identity, the incomplete-adaptation joint witness, the R4 zero-network and reciprocal-disadvantage identities, the frozen R5 negative-portability witness, and the R6 blocking/asymmetry identities were reproduced independently.

Targeted Lean 4 + mathlib verification was judged applicable and completed for five proof-critical algebra/order/logical cores: the zero-network sign, monotonicity of the residual-rent expression, the reversal implication, the incentive-strengthening/reversal implication, and the strict-versus-weak blocking distinction. The formal layer is deliberately narrower than the economic equilibrium derivation and does not certify novelty, exhaustive equilibrium enumeration, or the R5 Bernstein certificate.

The novelty re-kill finds heavy prior-art overlap for one-way compatibility/adoption and fixed-cost scope. The exact R3 government-ranking partition was not directly absorbed by the closest located parent literature, but R5 establishes that its sign is not portable to the pre-specified differentiated-demand comparator. Consequently Route A is rejected and the final route is **Route B**.

The R8 admissible claim set is frozen to a conditional mechanism paper: selection-free one-way adoption is supporting structure; the canonical residual-rent success/intermediate/failure partition is the central mechanism; incomplete adaptation is non-knife-edge within that microfoundation; and the R4/R5/R6 failures are explicit boundaries. Production-manuscript rewriting is authorized only under R8 and has not yet started.


## R8 closure

R8 verdict: **COMPLETE — MANUSCRIPT RECONSTRUCTED; R9 AUTHORIZED, NOT STARTED**.

R8 adds no new theorem. It maps the R7-certified claim set into the English production manuscript and makes the certification boundaries visible in the paper itself.

Manuscript mapping:

- G1-U / canonical adoption thresholds: supporting selection-free continuation structure;
- G2-S: central residual-rent success/intermediate/failure proposition;
- G2-J: incomplete-adaptation joint open-set proposition;
- N1/N2–N4/N7: zero-network, exact canonical network region, and singleton-specification boundaries;
- R5: explicit differentiated-demand non-portability boundary;
- R6: explicit strict/weak blocking and market-size-asymmetry institutional boundary.

R8 claim-scope status: **PASS**. The manuscript does not promote one-way adoption to headline novelty, does not claim competition- or demand-system independence, does not claim network-effect irrelevance, does not treat the high-F symmetric stable set as institutionally robust, does not claim unrestricted first-best welfare, and makes no priority/"first" claim.

The production manuscript, new residual-cost and robustness appendices, reproducible figures/tables, and R8 claim-scope audit pass the full repository build and verification gate. R9 is the only authorized next stage.
