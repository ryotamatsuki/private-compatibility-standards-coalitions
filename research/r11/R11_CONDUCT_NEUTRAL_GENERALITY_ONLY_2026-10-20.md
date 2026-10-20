# R11 — Conduct-neutral generalization only: preserving every R9 result

**Research note: 2026-10-20. Status: MATHEMATICAL IDENTITIES AND SUFFICIENT-CONDITION LEMMAS; NOT NOVELTY CERTIFIED.**

## Non-negotiable research boundary

- **DO NOT MODIFY** existing 19-page R9/JICT main manuscript, the 22-page supplement, original Cournot main propositions, equilibrium/coalition classifications, closed-form \(R(d,v)\), established negative robustness tests, or numerical witnesses.
- This note supplies only an **upper-level generality layer**: embed the unchanged certified model in a general class of market equilibria, which can be Cournot, Bertrand, nonlinear demand and heterogeneous marginal-cost models, subject to specified welfare and equilibrium assumptions.
- The result is **conditional across market specifications**. The fixed-\(\gamma=1/2\) prior counterexample forbids claiming universal preference reversal.
- This new branch starts at frozen manuscript PR #34 head \`08d6e6ad\` and consists only of \`research/r11/**\`. Never merge or revise submission files absent a later explicit approval.

## Model G: generalized standards adoption and product-market conduct

Take \(k\ge2\) symmetric standards-union (SU) member economies and one outsider; each economy has one firm, one segmented destination market, and quasilinear consumer welfare. The competing regime IS harmonizes the standard across all countries. Under SU a firm may pay the same real fixed cost \(F>0\) **per additional foreign standard supported**, with one investment covering all \(k\) member destinations using that standard. Under SW (all standards separate) a foreign standard is supported at cost \(F\) each. The original paper is recovered at \(k=2\) with its specified demand, network rule, production costs and Cournot continuation.

For each standards partition \(r\) and adoption profile \(s\), take a **well-defined unique product-market equilibrium** \(E(r,s)\), with destination-separable payoffs and a specified integrable quasilinear demand system. This market equilibrium may arise from quantity choice, price choice or another conduct model. Let \(P_i^r(s)\) be the firm's **worldwide operating profit before incremental investment fees**, \(CS_i^r(s)\) be destination consumer surplus, and \(W_i^r(s)=CS_i^r(s)+P_i^r(s)-F|s_i|\) be national welfare. This stipulates no specific linear-demand or Cournot FOC.

## Lemma G1: conduct-neutral asymmetric-adoption sufficient conditions

Under SU each firm has binary additional-standard action \(s_i\in\{0,1\}\). Define the *worst-case outsider* operating-profit gain
\[
\underline g_O=\min_{s_{-O}}
  \{P_O^{SU}(1,s_{-O})-P_O^{SU}(0,s_{-O})\},
\]
and the *largest member* unilateral operating-profit gain
\[
\overline g_H=\max_{i\in H,\,s_{-i}}
  \{P_i^{SU}(1,s_{-i})-P_i^{SU}(0,s_{-i})\}.
\]
Under SW define \(\overline g_{SW}\) as the largest possible incremental gain in operating profit from adding **one** currently unsupported foreign standard, maximized over all firm/action profiles. All extrema exist because the standard-adoption strategy sets are finite.

If
\[
\boxed{\quad\max\{0,\overline g_H,\overline g_{SW}\}<F<
              \underline g_O,\quad}
\tag{G1}
\]
then: under SU outsider adoption is strictly dominant and all member adoptions are strictly dominated; the unique pure Nash continuation is outsider-only adoption. Under SW every additional foreign standard is strictly unprofitable regardless of the other actions, so the unique continuation is no adoption.

**Proof.** For each SU member the most favorable gross adoption gain is below \(F\); choosing no additional standard strictly dominates adopting it. Outsider adoption returns at least \(\underline g_O>F\) even against any member action, so it strictly dominates nonadoption. In SW any nonempty subset can be reduced by one supported foreign standard with a strictly positive net payoff improvement because its incremental gross gain is below \(F\); this gives no foreign standards as a strict dominant choice for every firm. Uniqueness follows.

**Economic sufficient bound, not a new conclusion**: if the outsider receives a uniform destination-by-destination gain at least \(\underline\delta_O>0\) in each of the \(k\) member markets under every profile, and \(\overline g_H\le\bar\delta_H,\ \overline g_{SW}\le\bar\delta_{SW}\), then (G1) is feasible whenever
\[
k\,\underline\delta_O>
\max\{0,\bar\delta_H,\bar\delta_{SW}\}.
\tag{G1'}
\]
This formalizes fixed-investment **market-scope asymmetry** without a Cournot formula; it does **not** say adoption must occur as \(k\) grows, because endogenous profits and network effects may change with \(k\).

## Lemma G2: exact model-independent national-incidence identity

For an adoption-intensity *interpolation* \(a\in[0,1]\) between SU pre-adoption and outsider-only adaptation, let the equilibria along this hypothetical path be interior, unique, continuously differentiable and locally stable; only the endpoints need be feasible discrete adoption profiles. In one representative member destination let \(q(a)\) be the vector of outputs, \(p(a)=\nabla_q U(q(a),a)\), \(U(q,a)\) the differentiable quasilinear consumer gross-surplus potential, and \(C_h(q_h)\) member-firm production costs. There are \(k\) member firms \(h\in H\) and one outsider \(O\). Symmetry of member destinations implies
\[
W_M^{SU}(a)
  =CS(q(a),a)+\sum_{h\in H}\pi_h(q(a),a)
     +\pi_M^{\mathrm{outside}},
\]
where the last term is constant as the outsider adapts only in member destinations. The sum of member firms' profits in one representative member market equals the representative nation's one home firm's total operating profits over the \(k\) symmetric member markets, **not** national ownership of all \(k\) firms.

As \(CS=U(q,a)-\sum_j p_jq_j\) and \(\pi_h=p_hq_h-C_h(q_h)\),
\[
W_M^{SU}(a)=U(q(a),a)-p_O(a)q_O(a)
  -\sum_{h\in H}C_h(q_h(a))+
    \pi_M^{\mathrm{outside}}.
\]
Consequently, without applying any firms' Cournot/Bertrand first-order conditions:
\[
\boxed{\quad
\frac{dW_M^{SU}}{da}
=\underbrace{U_a}_{\text{direct compatibility utility}}
 -\underbrace{q_O \frac{dp_O}{da}}_{\text{foreign price / terms of trade}}
 +\underbrace{\sum_{h\in H}
     [p_h-C'_h(q_h)]\frac{dq_h}{da}}_{\text{displaced domestic markup rents}}.\quad}
\tag{G2}
\]
This is an accounting/envelope identity. **It is not a newly discovered theorem of IO theory.** It holds for differentiable, integrable nonlinear demands and any product-market conduct yielding equilibrium \((p,q)\), including Cournot and Bertrand. Its scientific usefulness is a *primitive/observable channel bridge* to the specific government's preference reversal. It does not universally assign a sign.

The exact change across endpoints is the integral of (G2) over the path. Define \(\Lambda=\int_0^1\{ \sum_{h\in H}\mu_h(-q'_h)+q_Op'_O-U_a\}\,da\), \(\mu_h=p_h-C'_h(q_h)\). Then \(W_M^{SU}(1)-W_M^{SU}(0)=-\Lambda\).

A **pointwise sufficient, operational test** avoiding postulating the conclusion is: for a known initial welfare advantage \(G_0=W_M^{SU}(0)-W_M^{IS}>0\), if across \(0\le a\le1\) the home markup-displacement term \(D(a)=\sum_h\mu_h(-q'_h)\ge\underline D\), and the *combined consumer/foreign-price offset* \(B(a)=U_a-q_Op'_O\le\bar B\), with
\[
\underline D-\bar B>G_0,
\tag{G2'}
\]
then \(\Lambda>G_0\) and the government strictly reverses its initial ranking. The constants are **restrictions that must be verified** from a chosen demand/conduct microfoundation or identified response estimates; simply asserting them would be circular.

## Proposition G3: conduct-neutral sufficient theorem (not an unconditional prediction)

Assume (i) Model G; (ii) adoption inequalities (G1); (iii) \(G_0>0\); (iv) either the exact test \(\Lambda>G_0\) or independently verified sufficient bounds (G2'). Then:
1. the unique SU adoption continuation is outsider-only and SW has no adoption;
2. the SU member's counterfactual pre-adoption ranking favors SU;
3. its **post-adoption** ranking strictly favors IS;
4. if underlying payoffs and selected equilibrium branches vary continuously with primitives and all strict margins remain separated from zero, this coexistence holds on an open neighborhood.

**Proof.** Item 1 from G1. Symmetry and market-separability establish G2; integration gives \(W_M^{SU}(1)-W_M^{SU}(0)=-\Lambda\). Thus \(W_M^{SU}(1)-W_M^{IS}=G_0-\Lambda<0\). By continuity of strict signs and dominance margins all inequalities persist locally.

**Crucial limit:** G3 is a useful **general sufficient-condition envelope**, not a novel unconditional economic result; G1 has standard dominance logic and G2 is known welfare accounting. It does not assert the government's formal partition is a subgame-perfect equilibrium or extend the original coalition stability theorem. The original R9 theorem statements remain unchanged.

## Reviewer-level assessment of generality

**Positive:** Independent of linear/unit demand; price vs quantity as strategic choice; differentiated goods and smooth network utility; constant vs differentiable production costs; member bloc size \(k\) under symmetry. It identifies a *national* incidence condition absent from a simple industry-surplus-only test, and separates endogenous compatibility adoption from political incentives.

**Negative:** Results are conditional; G2 is standard welfare accounting closely related to pass-through sufficient-statistics theory. Strong inequalities (G1), (G2') might be difficult to check in more general games. If the only new result is an algebraic identity + strict-dominance bounds, the 2026-09-21 IJIO desk-reject assessment of insufficient standalone innovation can still apply. Avoid claims like “general theory” without explicitly qualifying the assumptions.

**Known failure boundary:** Prior R5 \(\gamma=1/2\) differentiated Cournot and Bertrand show no initially favorable member SU ranking, despite endogenous outsider adoption in some configurations. This directly prevents generalizing the sign to *every* demand or network system. R10 showed a separate \(\gamma=23/25\) rational witness under both modes, which confirms non-vacuous open existence but is not evidence that all modes/parameter domains reverse.

## Closest-literature checks (source-retrieval status)

- **Weyl & Fabinger (2013)**, *Pass-Through as an Economic Tool*, JPE, doi:10.1086/670401 — general incidence and integration of local-to-total surplus effects under imperfect competition. High absorption: never claim (G2) is new. Author/publisher abstract verified.
- **Adachi & Fabinger (2022)**, *Pass-through, welfare, and incidence under imperfect competition*, J Public Econ, https://www.sciencedirect.com/science/article/pii/S0047272721002255 — sufficient-statistics generalization to heterogeneous firms; another high absorption threat.
- **Besen & Farrell (1994)**, *Choosing How to Compete*, JEP, doi:10.1257/jep.8.2.117 — one-way private compatibility and strategic competition; private adoption itself is known.
- **Gandal & Shy (2001)**, *Standardization Policy and International Trade*, JIE, doi:10.1016/S0022-1996(00)00067-2 — government SU/IS incentive structure directly related.
- **Buccella, Fanti & Gori (2026)**, *The Compatibility Decision Game*, EINT, doi:10.1080/10438599.2025.2478583 — asymmetric compatibility equilibria with Cournot and Bertrand, variable costs. Original abstract and publisher notes verified, full theorem mapping incomplete.
- **Toshimitsu (2016)**, *Price and Quantity Competition...*, JER, doi:10.1111/jere.12109 — competition-mode welfare and product compatibility, strong overlap risk for mode switching.

## Safe next research stage (only if explicitly authorized later)

Test (G1)/(G2') in **two genuinely different, independently specified microfoundations**, e.g. (A) differentiated Bertrand with nonlinear logit consumer demand, (B) differentiated Cournot with nonquadratic utility or CES, including the full endogenous adoption game under both. Do not weaken market-interiority, symmetry and smoothness assumptions silently. If some primitive fails, report the counterexample and retain R9. No rewrite of R9/JICT main results until a separate go/no-go gate.

**Verification:** \`research/r11/verify_general_incidence.py\` mechanically verifies (G2) for arbitrary differentiable \(U,C_h\) and arbitrary equilibrium derivatives with \(k=2,3,4\). This is algebraic verification, **not** a certificate for the strategic game, novelty, or publishability.
