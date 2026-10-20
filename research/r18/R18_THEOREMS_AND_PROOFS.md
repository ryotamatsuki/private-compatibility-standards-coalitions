# R18 — Theorems, proofs, counterexample, and falsifiable boundaries

**Status:** Main Proposition R18-P is proved **conditional on response envelopes and regular continuation**. It is a non-tautological *sufficient comparative-static condition*, but it does **not** prove that arbitrary consumer utility/technology/conduct primitives imply the required response bounds. Therefore it is not yet a fully primitive Level-3 theorem.

## Lemma 1 (microfoundation and national incidence)
On a regular fulfilled-expectations buyer-optimal branch, dCS = sum_i q_i(dG_i-dp_i). If home costs are C_h(q_h), fixed adoption states are held constant and the outsider-market export term is invariant along an outsider member-market counterfactual path, then

dW_member/da = sum_i q_i dG_i/da - q_o dp_o/da + sum_{h=1,2}(p_h-C'_h(q_h))dq_h/da.

**Proof.** Buyer maximization/envelope gives the first formula. Add operating-profit differentials of both symmetric member firms in the representative member market. The terms q_h dp_h cancel those consumer-price changes for home firms; foreign firm price remains -q_o dp_o; home cost derivatives produce domestic markups. For the homogeneous tied-buyer R9 case, direct CS(Q)=integral_0^Q D(t)dt-QD(Q) establishes the same equality. This is standard incidence accounting and NOT a new standalone theorem. QED.

## Lemma 2 (the two independent policy channels)
Let m_B,m_C,f_B be differentiable on [0,c], with m_C on [0,d], and all re-solved product games regular. Define b=m_B', r=m_C', e=-f_B', H=m_C(0)-m_B(0), J=f_C-f_B(0). Then exactly

D0 = integral_0^c b(z) dz - H - J - integral_0^c e(z) dz,
D1 = integral_0^d r(z) dz - J - integral_0^c e(z) dz.

**Proof.** Fundamental theorem of calculus applied to the three functions, with a compatible-institution reference m_C(0)+f_C. No use of a Cournot/Bertrand first-order condition. These equations are identities and are not themselves new economic results. QED.

## Proposition A (scope-induced firm selection)
Suppose under an SU an outsider buys one member standard, which is useful in two distinct member destinations. Along each compatible-support investment deviation path, computed by re-solving product-market equilibrium and differentiating the outsider's *operating* profit, its per-destination gain is at least alpha>0. Suppose for every rival adoption profile every member's whole reverse-interface gain is at most beta, and for every SW rival profile every one-standard addition has gain at most sigma; these bounds include the full reaction of all competitors and all destinations. If

max{0,beta,sigma} < F < 2 alpha,

then SU has the **unique** outsider-only adoption equilibrium and SW has unique non-adoption. These assumptions are to be checked from actual profit responses, NOT from sign of government welfare. The outsider gain bound can itself be checked by integrating pi_o'=q_o(p_o'-r_o')+(p_o-r_o)q_o' along each member-market cost/network switch; member and SW bounds use the analogous derivative formula in all relevant profiles.

**Proof.** Each member reverse interface is strictly dominated irrespective of other firms' adoption. Each separate-standard addition is strictly dominated in SW; any finite portfolio of added interfaces can be unpicked one at a time, so SW non-adoption is unique. With members' actions eliminated in SU, the outsider's single interface yields at least 2 alpha-F>0; hence it strictly adopts. Symmetric destinations give the factor 2; no FOC of Cournot or Bertrand is invoked. QED.

**Caveat:** Restricting upper gains to a single no-adoption profile would be insufficient for uniqueness. If support actions include strategic complementarity outside our all-profile bounds, the conclusion need not hold. The lower/upper gain envelopes are *equilibrium response restrictions*, not fundamental theorems about all possible demand systems.

## Proposition B (sign-identifiable national effects)
Suppose over [0,c] b(z)>=bL and eL<=e(z)<=eU, and over [0,d] r(z)<=rU, with finite real constants (rU need not be positive). Then

D0 >= c(bL-eU) - H - J =: L0,
D1 <= d rU - J - c eL =: U1.

**Proof.** Integrate the sign-preserving response inequalities in Lemma 2. QED.

These bounds are substantive because b, e and r can be calculated from demand curvature, costs, markups, network responsiveness, price pass-through and product-market equilibrium comparative statics **without computing the policy endpoints D0,D1**. E.g. b= sum q_i G_i,z - q_o p_o,z + sum_h mu_h q_h,z when the outsider's cost changes at fixed compatibility; e=-[(p_h-z)q_h,z+q_h p_h,z-q_h] in the outsider destination. They do not assert any universal sign; comparative-static restrictions must be demonstrated in applications.

## Main Proposition R18-P (scope–erosion–persistent-export-asymmetry)
Assume: (i) the microfounded, segmented two-member/one-outsider system defined in R18_GENERAL_MODEL; (ii) a unique regular continuation for the tested market states, or selection-independent versions of all the bounds; (iii) Proposition A's firm response envelope and fixed-cost interval; (iv) Proposition B's cost-wedge and network-contrast restrictions; (v) the **strict primitive-response inequalities**

c(bL-eU) > H+J, and d rU < J+c eL.

Then private outsider-only adaptation is the unique SU investment equilibrium, SW has no adoption, the representative member strictly prefers SU over IS **before** private investment, and strictly prefers IS over SU **after** investment. The comparison does not claim actual treaty renegotiation or generalized coalition stability.

**Proof.** Proposition A delivers endogenous investment profile. Lemma 2 and Proposition B imply D0>=L0>0 and D1<=U1<0. Domestic market protection can initially dominate the export disadvantage even though the private interface concentrates multiple destinations' gains on the outsider. Once the outsider buys the interface, m_B(c) becomes m_C(d), but the home firm's f_B(c) disadvantage in the outsider destination persists; since its export cost and compatible group are unchanged, the national comparison crosses zero. No ex-post sign is assumed. QED.

### Theorem limitations / necessary conditions
The strict conditions above are *sufficient*, not necessary. Exact necessary/sufficient ranking for a fixed regular branch remains D0>0>D1 (an endpoint identity, not independently novel). No universal comparative statics in c, d, market size or v follow unless the response envelopes can be held uniform as those primitives change. Market count scales outsider gross gain conditionally when per-market gain alpha is independent of scope; endogenous equilibrium feedback can invalidate simple monotonic scaling. A sign flip in marginal welfare along a continuous cost/compatibility path is admissible. Bertrand equilibrium existence/unicity for arbitrary C3 utilities is not supplied by this theorem.

### Failure and boundary
If c(bL-eU)<=H+J, no inference about the initial SU ranking is possible; if d rU>=J+c eL, the post-investment IS ranking is not certified. Either bound may fail even if an actual reversal occurs (sufficiency ≠ necessity). If F lies outside the interval the selected one-way investment can disappear. For original Cournot at v=0, c=1/10, D0=-47/3200, a genuine negative counterexample. R5 gamma=1/2 product differentiation failure is inherited unchanged. Under original R9, d* satisfying R(d*,v)=D is an exactly derived residual-cost boundary, not this general theorem's claimed universal cutoff. Under R16's Bertrand witness r(z)<0 on [0,d], showing that higher outsider residual cost need not *increase* member welfare in all models.