# R19 independent replay, missing lemmas, and boundary-price audit

Baseline: `6cd349daec244def5cb4ed475cc448ed091b9c22` (R18).
This audit is independent execution and an adversarial mathematical reread
of inherited code; it is not external academic peer review. No inherited
source is changed. The user's R19 instruction explicitly authorizes this
separate research extension despite the older repository freeze language.

## Executed checks

Run `python research/r19/replay_work/replay_inherited.py` from repository root.
All eighteen commands recorded in `replay_results.json` returned exit 0.
Each command's complete stdout/stderr, duration, and epistemic status is
saved beside the report. Runtime: Python 3.12, SymPy 1.13.3, NumPy 2.1.3,
SciPy 1.14.1. SHA256 for all 191 baseline tracked files is unchanged before
and after execution (`inherited_sha256.json`). This is a local execution
record, not a statement about the new GitHub Actions result.

| Check | Result and precise scope |
|---|---|
| R9 success / residual cost | Exact original pre gap `2408509/295731200`, post `-1341/184832`; original residual formula and witness line checks pass. |
| R9 zero-network failure | Exact `c(13c-6)/32`, hence negative on `0<c<1/3`; at `c=1/10`, `-47/3200`. |
| R5 differentiation failure | Historical gamma=1/2 negative results reproduce under the script's declared welfare convention; no restoration of a common-conduct positive example. |
| R9 investment | All 8 SU and 64 SW profiles and unilateral investment deviations checked exactly. |
| R9 coalition / cleanroom | Original restricted strict-blocking results reproduce; no generalized treaty-transition claim. |
| R10 welfare correction | Original common-parameter Cournot/Bertrand reversal remains withdrawn; correct fulfilled-expectations Cournot pre gap is negative at the former witness. |
| R13 consumers | Exact envelope, inverse-quantile CS, and homogeneous R9 demand/CS matching. |
| R15 nonlinear Cournot | All profiles numerically re-solved; exact baseline 27-pattern SPD checks. Nonlinear gap `+0.008337180701925129` to `-0.0072301474902085605`. This executable does not certify an explicit whole function-space ball or an interval enclosure of every nonlinear root. |
| R16 rational Bertrand | All profiles, exact profits and correct CS; pre `+0.0027740073314801`, post `-0.00090743388933369`. |
| R16 global price deviations | All 19 relevant market configurations; 211 feasible stationary/boundary price candidates, plus zero sales, checked exactly. This establishes that each displayed positive candidate is a global pure Nash equilibrium. |
| R16 inherited entry | 171 exact entry inequalities for restricted-active-set stationary candidates reproduce; see the stronger new audit below for arbitrary kinks. |
| R16 integrated incidence | Exact positive Bernstein and 64-bin rational Riemann bound reproduce. |
| R16 nonlinear Bertrand | All 8/64/1 profiles and 19 numerical interior FOC solutions; gap `+0.0027294670474107274` to `-0.0009097766726917644`. This remains a numerical example, not global nonlinear price-game uniqueness or a certified C3 radius. |
| R18 | Full rational investment games, affine derivative bounds, strict pre lower/post upper bounds and zero-network counterexample reproduce. |

The Cournot and Bertrand positive witnesses have different primitives,
including different differentiation assumptions. No identical-parameter
joint result is asserted.

## A gap in the inherited boundary-equilibrium argument, now closed at the rational witness

The inherited `verify_bertrand_no_boundary_equilibria.py` solves the
interior stationary price equations of every proper positive-sales set
and checks excluded-brand entry at those points. This alone does not
exhaust possible price kinks: an inactive brand may sit exactly at its
choke price, and changing an active firm's price may change the demand
slope on one side. This observation is a proof-coverage gap, not a
counterexample to R16 or a contradiction in canonical R9 theory.

The following stronger finite-dimensional certificate covers those
kinks. It is new R19 mathematical verification, without modifying R16.

### Lemma K (a necessary polytope for every boundary pure-price Nash)

Consider a linear fulfilled-expectations quantity demand defined by the
LCP `q>=0, p-1+Mq>=0, q_i(p_i-1+(Mq)_i)=0`, where `M` is symmetric
positive definite. Firms have constant costs `c_i>=0` and may charge
nonnegative prices. Write `h_i=1/(M^{-1})_ii>0`.
If a pure-price Nash has nonempty positive-sales set `B`, its active
quantity vector must belong to

`P_B = {q_B>=0: [M_BB+diag(h_B)]q_B <= 1-c_B}`.

For every omitted brand `j`, a necessary no-entry condition is
`M_jB q_B >= 1-c_j`.

**Proof.** Positive definiteness gives a unique LCP solution for every
price vector, continuously and piecewise affinely in prices. For active
`i`, all currently positive brands stay positive under a sufficiently
small increase in its own price. On a sufficiently small right interval,
let `A` be the positive-sales set, so `A` contains `B` and
`dq_i/dp_i=-(M_AA^{-1})_ii`. Schur complements of an SPD matrix give
`(M_AA^{-1})_ii <= (M^{-1})_ii`. The right derivative of profit at a
Nash must be nonpositive:

`q_i-(p_i-c_i)(M_AA^{-1})_ii <= 0`.

In particular an active firm cannot have nonpositive markup. Therefore
`p_i-c_i >= q_i/(M_AA^{-1})_ii >= h_i q_i`.
Active demand clearing is `p_B=1-M_BB q_B`; combining yields the stated
componentwise inequalities. This argument does not require interior
price differentiability at the candidate itself.

For inactive `j`, let `t_j=1-M_jB q_B` be its choke price. If
`t_j>c_j`, it can set any price strictly between `c_j` and `t_j`,
sufficiently close to `t_j`. Its new quantity is strictly positive:
otherwise the remaining quantities would equal the unique restricted
LCP allocation at unchanged rival prices, which violates brand `j`'s
complementarity inequality. Its positive sales at positive markup yield
a profitable deviation from zero. Thus no entry requires `t_j<=c_j`.
QED.

### Corollary K (primitive-data certificate of no boundary pure Nash)

Suppose `P_B` is compact for each nonempty proper `B` and, for every
omitted `j`,

`max_{q_B in P_B} M_jB q_B < 1-c_j`.

Then there is no boundary pure-price Nash. If all-brand-zero sales is
also ruled out by a positive choke-price-minus-cost, every pure Nash has
all brands active. An all-active price Nash must satisfy the unique
linear interior FOC system. Together with an independent global
best-reply verification of that candidate, the pure-price Nash is unique.

This is a sufficient certificate, not a necessity characterization or a
new economics mechanism. It does not rule out mixed price equilibria.

### Exact R16 witness certificate

`verify_bertrand_boundary_kinks.py` independently regenerates the 19
markets from standard portfolios and builds `M`, costs and `h` from the
original rational consumer/technology primitives. Every relevant
`P_B` has dimension one or two and is bounded because its constraints
have strictly positive coefficients. Its linear objective maximum is
attained at a vertex; all feasible vertices are enumerated exactly by
intersections of active constraints, including zero coordinates.

All 171 proper-active-set/omitted-brand inequalities are strict. Minimum
entry slack is exactly `33819/12831625>0`. The full rational certificate
is `bertrand_kink_certificate.json`. Empty sales is impossible because
every cost is below the standalone choke price 1. Hence there are no
boundary pure-price Nash equilibria, including inactive-at-choke kinks.
Combined with the inherited global 211-candidate check and unique
all-positive FOC solution, each of the 19 original R16 market games has
a unique pure-price Nash continuation.

**Limits.** This does not prove uniqueness of arbitrary mixed price Nash,
does not apply unchanged to nonlinear demand, and is not itself the
requested Level 3 private-investment/policy theorem. It repairs a
technical nonvacuity verification at a fixed rational witness.

## R18 classification and minimum missing lemmas

| R18 assumption/object | Classification | What it does / what disappears if weakened |
|---|---|---|
| Atomistic quasilinear preferences, original inverse quantile, or specified `U` | Consumer primitive | Fixes CS; dropping it permits an arbitrary welfare accounting convention and invalidates the claimed government result. |
| Compatibility groups, singleton-zero rule, `c,d,F`, one standard covering two destinations | Network/cost/access primitives | Gives asymmetric destination coverage; without separate destination-specific recognition, outsider adoption need not leave member export conditions unchanged. |
| Segmented markets and symmetric member destinations | Structural restrictions | Permits two member-market profit blocks in a single country's world profit; without symmetry use actual destination sums, not foreign-owned profit. |
| Unique regular continuation or bounds uniform over all selections | Equilibrium existence/selection condition | Not guaranteed by consumer concavity. Without it an investment payoff table may not be well-defined, and favorable branch selection can drive a result. |
| `b_L,r_U,e_L,e_U` | Endogenous derivative-response bounds | `r_U` can be negative; there is no universally positive protection response. Removing a needed bound destroys its corresponding integral certificate, not necessarily the actual ranking. |
| `H,J` | Endogenous cross-network equilibrium contrasts | Neither has a primitive fixed sign; `J<0` in both witnesses. |
| `alpha,beta,sigma` | Endogenous adoption-profit bounds | A per-market positive outsider gain alone does not force its aggregated gain above reverse/SW gains; all rival/own-portfolio edge gains must be covered. |
| `max(0,beta,sigma)<F<2alpha` | Condition combining primitive F and endogenous thresholds | Ensures dominance/selection. At/beyond boundaries one-way selection may fail or become weak/multiple. Merely renaming these bounds primitive does not reach Level 3. |
| `c(b_L-e_U)>H+J` | Endogenous sufficient initial ranking certificate | Does not explicitly assume `D0>0`, but is quantitatively tailored to imply it. A Level 3 theorem must derive it from preferences/technology rather than posit response bounds. |
| `d*r_U<J+c*e_L` | Endogenous sufficient post ranking certificate | Same issue. Removing it allows either post ranking; failure of this sufficient bound is not a counterexample to reversal. |

Minimal additional proof obligations can be compressed to four linked
lemmas; decomposing them into more symbols cannot eliminate them:

1. **Primitive continuation lemma:** buyer-optimal fulfilled networks and
   global market pure Nash exist, are unique or selection-independent,
   over all market configurations and any comparison path used; include
   corners and parameter boundaries. Cournot/price conduct can have
   different sufficient conditions and must be proved separately.
2. **Primitive adoption-order lemma:** primitive demand/cost/network
   restrictions imply a strict aggregated outsider gain above *every*
   reverse/SW relevant incremental gain, with all strategic responses.
   It must prove threshold order, not merely define alpha and beta.
3. **Primitive incidence-order lemma:** the same restrictions imply a
   positive initial SU advantage and negative post advantage through
   actual consumers' CS and owned worldwide profits. Quantitative
   competition/CS comparison and persistent export handicap are both
   required; their signs alone are insufficient.
4. **Common-cause/nonvacuity lemma:** these primitive domains overlap in
   the exact homogeneous R9 and a genuine price-competition model;
   exhibit nonempty domains and show adoption and policy results share
   a structural source, rather than intersecting unrelated endpoint
   inequality tests.

These are the R19 Level 3 blockers. The classical implicit-function,
Rosen, matrix-sign and envelope tools are tools for these lemmas, not
independently new economic theorems.

## Investment equilibrium: pure uniqueness versus all mixed equilibria

An enumeration of pure investment profiles alone only finds pure Nash.
R18's **all-profile strict incremental upper bounds** give more: every
non-native member portfolio is strictly dominated by removing its
interfaces one at a time; the same applies to SW portfolios. Since the
bounds hold for every rival action and every own partial portfolio,
telescope to show native-only strictly dominates each nonempty
portfolio, also against mixed rivals. Thus those firms choose native
support with probability one in any mixed investment Nash. After
elimination, the outsider strictly adopts when its *total* gain exceeds
F; its action then also has probability one. Therefore the bound proves
the unique investment Nash even allowing mixed investment strategies,
conditional on the specified market pure-Nash continuations.

This proof needs only the outsider's lower gain after member actions
are eliminated. R18's stronger all-profile lower bound is sufficient
but needlessly strong. Nor is `F<2alpha` by itself sufficient if other
destinations are adversely affected by the new support: destination
separability, no capacity/global-cost spillovers, and local standard
recognition must be stated. The original segmented technology provides
these restrictions. Counting only destinations while allowing global
capacity or price linkages would invalidate the factor-two reasoning.

## CI recommendation

Use the same pinned three packages. Require a full checkout and fail if
any baseline tracked path differs from immutable R18 SHA; permit only
new `research/r19/**` and the new R19 workflow. Run the replay driver,
the kink proof, and new R19 theorem certificates in separate steps with
ordinary failing process exit codes (avoid a successful `tee` masking a
Python failure). Upload the JSON and text logs. Confirm paper-source
preservation separately from proof correctness. Require documentation
to label numerical nonlinear examples as numerical; do not make CI
output tokens a substitute for mathematical proof review.

## Additional exact counterfactuals (Stage 9)

`extra_counterfactuals.py` independently writes the finite-stage evaluator
from primitives; it does not remove R18's success-only policy assertions
in memory or modify inherited code. Its exact results are saved in
`extra_counterfactuals.json`.

**Private adoption without a government reversal.** At homogeneous
Cournot `(v,c,d,F)=(0,1/10,1/20,1/50)`, all 8 SU/64 SW/1 IS profiles
are re-solved. Every member/SW single-interface incremental gain is at
most `21/1280`, whereas outsider's two-market gross gain is `93/3200`.
Thus `21/1280 < 1/50 < 93/3200`; strict removal dominance and the
outsider's strict best reply imply unique outsider-only SU investment
and no SW investment, including mixed investment choices. Nevertheless
the member SU-minus-IS gaps are `-47/3200` before and `-243/12800` after
adoption. Private compatibility occurs but no initial SU advantage, so
there is no SU-to-IS policy reversal. Since all inequalities and regular
Cournot matrix minors are strict, continuity gives the same negative
policy/nontrivial investment pattern for sufficiently small positive
network strength as well. This is not solely a boundary degeneracy.

**A complete-compatibility Bertrand counterfactual.** Set residual cost
to `d=0`, retaining the other original R16 primitives. All investment
profiles re-solve exactly with strict one-way investment. The government
pre gap is unchanged, `+0.0027740073314800945`; its post gap is
`-12645019356141999684/18013487435825664407975` (approximately
`-0.0007019750840136195`). The inherited global-price algorithm, without
source edits, verifies 171 feasible candidate deviations over 15 distinct
labeled market configurations at `d=0`. The new polytope audit verifies
135 arbitrary-kink no-boundary inequalities, minimum strict slack again
`33819/12831625`. Together with the unique full-active FOCs, these prove
unique pure-price Nash in the complete-compatibility counterfactual.

The exact cost-only derivative of post SU-minus-IS member welfare at
`d=0` is `-17763659488800/168594391265507<0` in that Bertrand model.
For the original Cournot `v=6/25`, the original residual formula gives
the opposite derivative `25/5776>0`. Thus a universal assertion that
more incomplete adaptation necessarily restores members' SU preference
fails even at the zero-residual boundary, where both full endogenous
investment games and pure market continuations have been checked. This
is a pair of exact local comparative-static results, not a theorem that
all Bertrand/Cournot games must differ in this direction.
