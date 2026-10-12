# R9 pre-submission economic-contribution referee report (v2.9)

Date: 2026-10-12. Target branch: revision/research-track; research audit branch: research/v29-frontier-addendum-20261012. The revised paper is *Private Compatibility and Government Incentives for Standards Harmonization* (JICT candidate). This is a **critical AI desk-editor/referee simulation**, not an external human referee review or a newly independent empirical source of truth. Prior R7/R9 results were consulted **only as claims to challenge**, not positive editorial evidence. This document does not alter manuscript, theorems, bibliography or JICT package.

## Decision: CONDITIONAL GO for continued manuscript path; SUBMISSION HOLD before Stage 14/15 final clearance

**Single consolidated blocker:** Can the author defend *substantive and distinguishable economic learning* from the R9 conditional equilibrium, rather than an algebraic three-sign classification in one fragile network demand specification? This requires an empirically/institutionally intelligible CS-versus-firm-rent mechanism and specific comparison to closest published standards/compatibility/regulatory-agreement literature. It does **not** automatically require a new theorem, intervention instrument, or positive-cost coalition-stability result.

This is a stronger and more candid verdict than the prior "technically ready, go submit" response. Technical readiness is still valid within its historical scope.

## Claims assessed

C1 (R3, §6): For a SU member given one-way outsider support, pre-adoption government SU–IS value = E−D; post-adoption = −D+R(d,v), where
```
R(d,v) = d * ((5-4*v)*d + 2*(1-4*v)) / (32*(1-v)^2).
```
If E>D>0, R<D => preference reversal; D<R<E => stronger IS incentive without reversal; R>E => weakening of IS incentive. Equality at thresholds is excluded in the strict classifications. The sign trichotomy follows algebraically given correct Cournot residual rent.
C2 (R3): One nonempty joint open region where positive residual cost, outsider-only adoption selection free, SW no adoption, and reversal all hold for the SAME primitive.
C3 (R4/R5): private one-way adoption can survive zero network and differentiated-demand alternative even when political reversal fails (indeed E<0 in audited differentiated-Cournot AND differentiated-Bertrand model). Scope result, not broad portability.
C4 (R6): static coalition stable-set transition tested at *full bypass* (d=0); sensitivity of symmetric high-F region to blocking and asymmetry. Do not implicitly extend C4 to 0<d<c.

## Independent clean-room market equilibrium reconstruction (not importing production verification modules)

The canonical singleton-zero-network microfoundation has two bloc firms producing x each, and one incompatible outside firm producing y in a member market.
Before outsider support, the FOCs from prices and unit costs are:
  1 − 3(1−v)*x − y = 0
  1 − 2*x − 2*y − c = 0
SymPy solves x=(1+c)/(2*(2−3*v)); y=(1−3*c−3*(1−c)*v)/(2*(2−3*v)).
Member-market CS=0.5*(2*x+y)^2 and each member firm's profit A=(1−v)*x^2. These independently reproduce manuscript K_M,A.

After outsider joins the compatibility group with remaining marginal cost d=lambda*c, the FOCs are:
  1 − 3*(1−v)*x − (1−v)*y = 0
  1 − 2*(1−v)*x − 2*(1−v)*y − d = 0
giving x=(1+d)/(4*(1−v)); y=(1−3*d)/(4*(1−v)).
CS=0.5*(2*x+y)^2, each member profit A_R=(1−v)*x^2.
SymPy verifies:
  [CS_after − CS_before] + 2*[A_R−A] == R(d,v)−E,
identically, using manuscript expressions for K_M,A,E,R.
Outsider-market profits are unchanged between the two states of a fixed SU; they therefore cancel in this private-adoption change. This is ONE independent welfare bridge, not certification of every paper deviation or formal theorem.

## Three real common-primitive private-adoption equilibrium regimes

Take rational c=9/125=.072; v=111/500=.222; F=9/100=.09.
At these common primitives:
  E=0.0006823047000448
  D=0.0002483980449969
  E−D=0.0004339066550479 > 0
  W(IS)=0.7056604833433562.

| lambda | R(d,v) | post SU−IS gap = R−D | lower adoption sufficient bound FL | outsider adoption upper bound F* | sign status |
| --- | ---: | ---: | ---: | ---: | --- |
| 1/10 | 0.0000942721763668 | −0.0001541258686301 | 0.0752678843496 | 0.1460645640566 | R<D / reversal |
| 3/10 | 0.0003488493996207 | +0.0001004513546238 | 0.0686015917333 | 0.1327825075013 | D<R<E / incentive strengthening only |
| 3/5 | 0.0008957974108022 | +0.0006473993658053 | 0.0609067020201 | 0.1139838442623 | R>E / incentive weakening |

For every lambda, E>D>0, F_L(d)<F<F*(d), 0<d<c, and the selected continuation is the R3 selection-free outsider-only adoption state. All numbers were calculated from rational inputs with SymPy and checked via independent FOC re-solve; full all-partition re-derivation beyond inherited R3 certification not repeated. Strict comparisons imply local open neighborhoods. **These three joint-feasibility witnesses are NEW PRESCREEN computations, not manuscript-certified propositions.** Do not add to main paper without the normal mathematics/claim-scope verification and rebuild.

National welfare effect of outsider adoption under a fixed SU:
| lambda | member-market consumer surplus change | member worldwide producer profit change (member markets) | net national welfare change |
|---|---:|---:|---:|
| .1 | +0.0876261899283 | −0.0882142224520 | −0.0005880325237 |
| .3 | +0.0831868854035 | −0.0835203407039 | −0.0003334553004 |
| .6 | +0.0765680750599 | −0.0763545823492 | +0.0002134927108 |

**Interpretation:** private standards bypass enhances member-market consumers' surplus while eroding incumbents' rents. In the third regime, the residual marginal cost weakens competitive erosion enough for consumer benefits to exceed profit losses. This changes the political comparison of formal institutions *at the private firm's endogenous continuation*. Mere surplus/profit tug-of-war is known and not per se new; this particular institutional feedback is the proposed application-level advance.

**Effect-size / fragility attack:** all net values at this witness are small relative to W(IS); the relative shift of the IS incentive in these regimes is about +0.0833%, +0.0473%, and −0.0303% of W(IS). These magnitudes are **one example, not global bounds**. If one merely diagnoses W=CS+theta*domestic profit, the zero net switch is at theta≈0.993334, 0.996008 and 1.002796, respectively, which warns of sign fragility in this witness under political weighting. theta !=1 would change the canonical national-welfare definition; do not claim this is a contradiction of the normatively correct W=CS+profit theorem, or introduce it as a paper parameter without authorized theoretical rollback.

## Assumption-dependence challenge

For c=1/10, the initial SU advantage E−D crosses zero at v≈0.2204586042558472 in the frozen model (admissible v<1/4). This is a narrow high-network parameter subrange *at that c*, not a universal bound across c.
R4 proved v=0 eliminates starting SU advantage, though one-way adoption persists; alternative S1 that grants singletons their own network benefit eliminates starting SU advantage on the tested old canonical domain. R5 found differentiated-demand pre-SU advantage and E>0 fail **under both Cournot and Bertrand** on its pre-registered audit box, even though firms continue one-way adoption.
**MAJOR editorial question:** why is the canonical zero-singleton network specification substantively credible? Are the extra rents tied to cross-producer standard interoperability rather than a discontinuous assumed proprietary network advantage? Clarify as a conditional technology/economy, with honest bounded failure results. This is economic-model significance, not a proof error.

## Closest-literature and independent editorial-value audit

- Gandal and Shy (2001), *Standardization policy and international trade* (JIE): government regional standards unions + network effects / conversion costs are NOT new. The proposed difference is ex post firm support at fixed formal institutional membership, with producer/consumer continuation payoffs; absence of a matching exact theorem in verified corpus is not firstness. [publisher article + existing paper bibliography].
- Takarada et al. (2020), *Standards policy and international trade: Multilateralism versus regionalism* (JPET, DOI 10.1111/jpet.12425): regulatory standards, welfare/core and cost of multiple standards already modeled. Their regulatory externality differs from technical interoperability; explain that **government coalition stability itself is old**.
- Innocenti & Menicucci (2021), *Partial compatibility in oligopoly* (JEBO DOI 10.1016/j.jebo.2021.05.005): firm compatibility stage + price competition and quality asymmetry are prior art; do not claim novel unilateral compatibility. https://flore.unifi.it/handle/2158/1241542
- Ding–Ko–Shen (2022), *Partial compatibility in two-sided markets: Equilibrium and welfare analysis* (Economic Modelling DOI 10.1016/j.econmod.2022.105989): unique coalition-proof private compatibility patterns and welfare are already known in platforms; government formal coalition actor is different, but mere actor substitution cannot carry novelty. https://www.sciencedirect.com/science/article/pii/S0264999322002322
- Maggi & Mrázová, *Harmonization...What Else? The Role for International Regulatory Agreements*, NBER WP 33318 December 2024, updated preprint in July 2026. Regulatory harmony can arise without formal agreement, and formal public cooperation may have a role in inducing efficient diversity, not simply more harmonization. This creates a **strong political-economic precursor** to private coordination changing the role of public harmonization. Exact R9 product-compatibility Cournot residual-rent result is NOT shown to be absorbed; methodological setting differs (regulatory policy, heterogeneous preferences and inter/intra-industry trade). https://www.nber.org/papers/w33318 ; updated SSRN https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5076021
- Schmidt & Steingress (2022), *No double standards*, JIE DOI 10.1016/j.jinteco.2022.103619: endogenous private adoption and economically large impacts of harmonized standards already established; its quantitative/evidence component is beyond R9 and makes unconditional real-world significance harder to assert. https://ideas.repec.org/a/eee/inecon/v137y2022ics0022199622000514.html

**Source depth:** primary published abstracts and prior project literature audits; not all final proofs read for competing papers. No conclusive global theorem-absorption certificate or evidence of exact published duplication. Missing references in submitted R9 manuscript should be assessed for material relevance and added only after real source/version checking, not padded mechanically.

## Why publication could be justified (skeptical editor's best affirmative case)

The paper identifies a constrained but analytically reproducible wedge between technological standards interoperability and nations' incentives to maintain *formal* regional institutions. Its endogenous continuation demonstrates that an outsider can privately bypass a bloc without reciprocal relief for members; the government can thereby strengthen, reverse or weaken its preference for formal internationalization depending on retained residual cost, and these sign regions are jointly compatible with the firm's fixed-cost adoption game. The negative demand/network tests warn why private interoperability cannot be read as a sufficient condition for deeper formal harmonization. JICT is an applied-theory and policy-outcomes journal; a transparent *conditional diagnosis* may be material even without unrestricted implementation instruments or functional-form-independent generality.

## Strongest skeptical desk rejection (not merely mathematical)

The manuscript's central three-way proposition is a rearrangement of government payoff differences from a restricted linear Cournot example. The surprising movement is driven by a fragile national consumer-surplus/incumbent-profit cancellation and by a network specification that turns off network benefits for a solitary compatible supplier, while differentiated demand eliminates the starting regional institutional rent in a pre-specified test. The paper shows limited generality and does not characterize formal coalition stability under its main positive residual-cost extension. Similar incentives concerning compatibility, spontaneous harmonization, and political agreements are known from earlier studies. A field editor could reasonably question why this conditional parameter-region map changes economists' understanding enough to justify a full paper, particularly if no compelling standards-policy institution exemplifies this one-sided bypass.

## Question completeness test (v2.9)

- Title promises private compatibility and government **incentives**; R3 C1/C2 deliver exactly that, within canonical assumptions.
- Abstract discusses coalition stability only as FULL bypass / institutional application and honestly acknowledges high-F rule sensitivity; positive d coalition stability is **BOUNDED LIMITATION**, not automatically ESSENTIAL FOLLOW-UP, so long as title/abstract do not upgrade that application to headline general result.
- No formal policy instrument is claimed and discussion admits no empirically identified application; *WHY* government preferences change is modeled; *SHOULD* menu-local IS Pareto comparison conditional only; *COULD* real implementation outside scope. Defend diagnostic-only applied theory with real institutional mapping before Stage 14.
- R5 alternative-demand failure must be explicitly incorporated as a success/failure **economic lesson** (private adoption is more portable than government preference reversal) and not treated as proof that no broader welfare effect exists.
- An algebraic threshold trichotomy alone is insufficient; C2 joint feasibility + C3 genuine failure boundaries + the economic continuation channel must collectively carry the paper.

## Exact bounded pre-submission repair and exit gate

ONE required issue to close: **economic editorial significance of conditional government-rent effect under essential network primitives**.

Tasks, no unapproved new model:
1. In Introduction/Discussion (not changing propositions), explain separately CS gain and incumbent-profit loss after outsider compatibility, and how the government institution preference changes; identify empirical observable setup/adaptation cost and specific unilateral-compliance regime plausibly mapped onto network effects. Avoid asserting case study without institutional source.
2. Make transparent that for some feasible primitives all three private-adoption/political-sign regimes exist; if including this NEW common-primitives table in manuscript, first independently certificate-check equations, R3 deviation inequalities/quantifiers, and generated table/CI (earliest necessary verification stage, not silent prose only). Optional if editorial case can be made without the table; it is not mandatory to build a new theorem.
3. In Related Literature, explicitly locate final theorem-level positioning relative to Gandal/Shy, Takarada, Innocenti–Menicucci, Ding, and Maggi–Mrázová's latest version. Cite only relevant articles with verified bibliographic data and accurate scope.
4. Stage 11 clean-room skeptical editor redo: answer "what would an IO economist learn that closest parent theorem does not establish?" and "is that economically meaningful despite S1/R5 failures?" using authored model results; no R7/R9 status labels as proof of value.
5. Preserve reviewer disagreement/human sign-off explicitly; an AI referee simulation is NOT independent human peer review.
6. Only then move to Stage 14 final journal rules, declarations, anonymity and bundle QA and Stage 15 submission freeze.

**Decision:** CONDITIONAL GO for present R9 submission path, with named contribution-value closure required. Do not construct a new dynamic theory; no change to R9's historical mathematical certification. JICT target remains a fit judgment; rejection risk remains material.
