# R18 — General model (research-only, base R17 786bbf434)

## Epistemic limits and frozen science
This note is a proposed overlay, **not** an amendment to R9, PR #34, the residual-rent R(d,v) theorem, or the original five-partition strict-blocking coalition result. No actual treaty renegotiation is claimed. R10's same-parameters Cournot/Bertrand welfare claim remains **RETRACTED** (R15): never use CS = q'(M0-vC)q/2 for the R13 fulfilled-expectations model.

## Timing and consumers
1. Governments' formal standards partition is fixed ex ante: SW, SU={1,2}|{o}, or IS. The experiment compares continuation national welfare across these counterfactual institutions.
2. Each firm can buy additional standards at real fixed setup cost F per *new standard*, giving access to every destination where it is in force; ownership/recognition of the formal institution is unaffected.
3. Given investments, in each segmented destination firms compete in a specified product-market game, possibly Cournot, Bertrand, or another strategic form. Buyers then maximize quasi-linear utility taking network benefits g^e fixed individually; producers anticipate *fulfilled* consumer expectations G(q,s) when selecting quantities or prices.
4. Government welfare W_i=CS_i+sum_k pi_i^k - F n_i, where pi_i^k is **home firm i**'s operating profit at destination k, not the sum of all producers' profit in i's market. Firms' own investment expenditures are charged to their own country's welfare; on outsider-only SU the member incurs none.

For heterogeneous atomistic unit-demand consumers, V(p,g)=integral max{0,max_i[taste_i+g_i-p_i]}dmu. On regular branches, dV=sum_i q_i(dg_i-dp_i), g=G(q,s). A differentiable representative-consumer alternative has strictly concave U(q), fulfilled expectations p=grad U(q)+G(q,s), and CS=U(q)-q'grad U(q) **only if** the maximizing allocation clears at those prices. For the canonical homogeneous R9 buyers with theta uniform on [0,1], active net prices p_i-G_i=1-Q and CS=Q²/2, retaining endogenous seller quantities and R9's singleton-zero network rule. There are buyer indifferences; use the direct quantile integral rather than a no-tie envelope. The original firm's Cournot commitment affects fulfilled expectations; imposing price-taking firm beliefs about G would be a different model.

## Equilibria
For institution rho and investments s, E(rho,s;theta) is the Nash equilibrium *correspondence* of the specified finite-player price/quantity product-market game together with a buyer-optimal fulfilled-expectations allocation. It may be empty or multi-valued: no general existence/uniqueness theorem is asserted. The R18 main proposition is conditional on a unique regular continuation or on branch-independent uniform bounds across all admissible equilibria. Firm investment equilibrium is the Nash equilibrium of the induced **finite** normal-form investment game. Positive Nash equilibrium in the two benchmark market games does not by itself imply global price Nash: the R16 active-set and re-entry audit is a separate necessary step.

## Three market primitives (conduct neutral)
For representative member i under SU, let z denote the outsider's marginal *member-market adaptation cost*, z=0 under IS and z=c before outsider adoption. B means outsider excluded from the compatible product group (while the two members remain compatible); C means all three share a compatible standard. Define

m_B(z)=CS_member(B,z)+pi_1^member(B,z)+pi_2^member(B,z),
m_C(z)=CS_member(C,z)+pi_1^member(C,z)+pi_2^member(C,z).

The two profit terms above are NOT foreign profit wrongly added to welfare: by symmetric member destinations, they exactly equal member i's operating profits over **both** member markets. Define f_B(z) as member i's export operating profit in outsider destination, where **both member firms** face the nonrecognized standard cost z while retaining their common member standard. Define f_C as that home firm's profit in the fully harmonized outsider market at zero mismatch cost.

The individual government's SU-IS gap, at no private adoption and after outsider-only adoption, respectively, is

D0 = m_B(c)+f_B(c)-m_C(0)-f_C;
D1 = m_C(d)+f_B(c)-m_C(0)-f_C.

In these market functions the *other* firms' actions, demand, prices, expectations, and profits are **re-solved** as z changes; m_B, m_C, and f_B are not exogenous payoffs. Fixed F falls on outsider, not member i.

At a regular path define b(z)=m_B'(z), r(z)=m_C'(z), e(z)=-f_B'(z), H=m_C(0)-m_B(0), and J=f_C-f_B(0). H and J can have **either** sign. In particular J is negative in both checked witnesses: calling it a necessarily positive network export penalty is incorrect. Firm-stage access benefit functions are derived from product-market operating profits under all competing adoption profiles (see proofs); no private investment decision is hard-coded.

## Minimum assumptions for theorem
Essential: a fixed/formal SU versus IS distinction, two member destinations to which one outsider interface applies, a cost/compatibility distinction before versus after adoption, microfounded fulfilled expectations, national (home ownership) welfare, regular market continuation, and a strict firm adoption interval. Symmetry and separability permit the scalar m/f representation but generalization to nonidentical markets is by sums. Neither linear G nor quadratic U nor quantity/price conduct is used in the algebra. However regularity/unique-selection of an unrestricted Bertrand game, and primitive restrictions ensuring the response derivatives have the required signs, are **not** available for all demand primitives. These are substantive scope limitations.