# R12 — Model-neutral mechanism theorem, without altering R9 scientific results

**2026-10-20.** This is a *separately versioned proposed manuscript extension*, not a submitted file and **not** a certification of new IJIO-level novelty. Base is exactly PR #34 head \`08d6e6adb1a90bdf03fa223c0961ac04620f0fa2\`.

## Scientific freeze-preservation contract

1. \`paper/jict_short/short_04_incentives.tex\` retains **the complete original R9 content as an exact prefix**, including the original Proposition 1, Proposition 2, witness, proofs, equations and numerical illustration. A separately labelled \`Conduct-neutral mechanism\` subsection and \`Proposition 3\` are appended afterwards; existing theorem content is not replaced.
2. All other six original main-chapter sources, original 22-page supplementary files, \`paper/preamble.tex\`, tests and the original JICT source-builder remain unchanged.
3. The original draft PR #34 and submission-ready R9 package remain unmerged and untouched. No editorial status change.
4. This R12 article is a **longer research draft**, not yet proven compliant with the JICT 19-page short-paper presentation; submission re-packaging is a separate gate.

## Why R11 needed a mathematically material correction

The prior general-utility R11 construction assumed a quasilinear **integrable** demand potential \(\nabla U=p\) and the surplus convention \(CS=U-p\cdot q\). The actual R9 canonical model has \(p_i=1-Q+g_i\) but computes \(CS=Q^2/2\). Even when the inverse-demand Jacobian is symmetric, its consumer-surplus mapping need not coincide with \(U-p\cdot q\). The R11 incidence identity therefore **must not** be claimed as an exact generalization of R9.

R12 instead starts with independent but jointly economically justified product-price mapping \(p(q,a)\), consumer-welfare mapping \(S(q,a)\), and home cost curves \(C_h\). No specific functional form, competition conduct or integrability is imposed, so the exact R9 convention nests algebraically.

## Conduct-neutral stage (original paper's three countries and timing preserved)

Under SU, member firms 1 and 2 each have binary action of supporting the outsider standard. The outsider has binary action of supporting the bloc's standard. Define three *gross operating-profit* gains measured with each product subgame re-equilibrated:
- \(g_O^0\): outsider's additional-standard gain with members not adopting;
- \(\bar g_H\): the **maximum** member's reverse-adoption gain over all other SU adoption profiles;
- \(\bar g_{SW}\): the **maximum incremental** gain in the SW game from adding any one foreign standard against any other profile.

If
\[
\max\{0,\bar g_H,\bar g_{SW}\}<F<g_O^0, \tag{G1}
\]
the unique SU Nash continuation is outsider-only adoption and the unique SW continuation has no extra adoption. Members strictly prefer no adoption against *every* profile; conditional on that elimination the outsider strictly adopts. Adding any extra standard is strictly unprofitable under SW, regardless of the other standards adopted, and iterated unilateral removal eliminates all nonempty bundles. This sufficient condition is **stronger than and does not replace** R9's tighter, exact Cournot threshold and complete deviation audit.

This is an economically interpretable investment asymmetry: **one adaptation cost buys outsider access to two aligned markets, while the bloc members' reverse investment covers only an outside destination**. No particular profit functional form is required.

## General national welfare under arbitrary specified market conduct

Let \(a\in[0,1]\) be an artificial smooth *interpolation* between before and after the outsider's private adoption, not an additional feasible discrete strategy. In a representative member destination, there are two members \(h=1,2\) and outsider \(O\), three equilibrium quantities \(q(a)\), differentiated price vector \(p(q,a)\), consumer surplus function \(S(q,a)\), and member cost \(C_h(q_h)\). Member-destination market symmetry and destination-separable profits ensure that the representative member government's welfare is
\[
W_M^{SU}(a)
=S(q(a),a)+\sum_{h=1}^2
  \{p_h(q(a),a)\,q_h(a)-C_h(q_h(a))\}
+\pi_M^{\mathrm{outside}},
\]
with unchanged outsider-destination earnings and zero new fixed-investment expense for member firms. **Importantly, this sums the two member firms' home-destination profits only because it is exactly equal, by symmetry, to one home firm's profits in the two member destinations. It does not include foreign-owned income.**

Define, with \(j\in\{1,2,O\}\),
\[
H_j=S_{q_j}+\sum_{h=1}^{2}q_h p_{h,q_j}
+\mathbf 1_{\{j\in H\}}(p_j-C'_j),\quad
A=S_a+\sum_{h=1}^{2}q_h p_{h,a}.
\]
Using only the chain rule:
\[
W'_M=A+\sum_j H_jq'_j.
\tag{G2a}
\]
For outsider expansion \(q'_O>0\) and domestic sales diversion
\(\delta_h=-q'_h/q'_O\ge0\),
\[
-\frac{dW_M^{SU}}{dq_O}
=L(a)=\sum_h H_h\delta_h-H_O-\frac{A}{q'_O}.
\tag{G2b}
\]

These are **welfare incidence identities**, not new economic discoveries. The coefficients are calculated from price responses, consumer welfare, cost and competition equilibrium outcomes; they do not simply posit the *final ranking* sign.

If across the interpolation
\[
H_h\ge\underline H_h\ge0,\quad
\delta_h\ge\underline\delta_h\ge0,\quad
H_O\le\bar H_O,\quad
A/q'_O\le\bar A,
\]
then with \(\kappa=\sum_h\underline H_h\underline\delta_h-\bar H_O-\bar A\) and the initial welfare advantage \(G_0=W_M^{SU}(0)-W^{IS}>0\), the **checkable sufficient test**
\[
\kappa[q_O(1)-q_O(0)]>G_0>0
\tag{G2c}
\]
implies post-adoption strict government preference for IS. Combined with (G1), this is a **conduct-neutral sufficient theorem for the same endogenous-investment and preference-reversal mechanism**, not a theorem that every demand specification reverses.

The exact, less conservative threshold is
\[
G_0<\int_0^1q'_O(a)L(a)\,da
=W_M^{SU}(0)-W_M^{SU}(1),
\]
which is an endpoint accounting equivalence and **must not** be marketed as standalone novelty. The stricter (G2c) uses the *market-response, markup and consumer-surplus derivative bounds* as primitive information. The bounds can fail (or be overly conservative) even if the endpoint result holds.

## Exact nesting check of the original paper

For R9's canonical inverse-demand rule in the representative member market:
\[
p_1=p_2=1-Q+v(q_1+q_2+a q_O),\quad S=Q^2/2,
\]
algebra gives
\[
A=v(q_1+q_2)q_O,\quad
H_1=H_2=q_O+v(q_1+q_2)+p_1,\quad
H_O=q_O+va(q_1+q_2).
\]
These are substituted into the R12 chain-rule identity **without changing** the R9 model's consumer-surplus convention. The standalone SymPy test mechanically checks unrestricted arbitrary S, p, C for two, three and four home suppliers and this precise R9 specialization.

## What a critical IJIO referee would still require

1. **Economically defensible welfare:** R12 permits separate \(p(q,a)\), \(S(q,a)\) so that the original R9 specification truly nests, but a general equilibrium paper still must explain why the pair represents consumer choice and welfare consistently. Unrestricted pairings are algebraic but not automatically economically admissible.
2. **Feasibility, not mere relabeling:** Conditions (G1) and (G2c) must be checked in a market microfoundation without *assuming* government preference reversal. For fixed differentiated gamma=1/2, the R9 negative robustness result remains. R10 common Cournot/Bertrand exact witness shows jointly feasible firm adoption and endpoint reversal, but the **strong uniform (G2c) bounds have not been separately certified at that witness**; in fact local W' can change sign while endpoint W decreases.
3. **Originality:** The national-incidence expression overlaps the pass-through and sufficient-statistics literature. Any editorial claim must be confined to joint firms' endogenous adoption + asymmetric national welfare mechanisms, not "new incidence identity."
4. **Preservation:** R9's detailed \(R(d,v)\), all Cournot equations, Proposition 1/2, full-bypass five-partition coalition theorem, negative tests, numerical witness and proof packages are unchanged. The conditional R12 proposition adds no unproven assertion about the stability of the *new* arbitrary-conduct policy partition.
5. **Length and venue:** The additional content may exceed the JICT short-paper formatting bound. No journal-ready PDF is certified. Do not silently drop R9 results to meet the page count.

## Literature scope

Close overlap, inspected at official source/abstract level:
- Gandal & Shy (2001), *Standardization policy and international trade*, JIE 53:363–383, doi:10.1016/S0022-1996(00)00067-2 (national choice of recognition / regional standardization union).
- Besen & Farrell (1994), *Choosing How to Compete*, JEP 8:117–131, doi:10.1257/jep.8.2.117 (private compatibility).
- Weyl & Fabinger (2013), *Pass-Through as an Economic Tool*, JPE 121:528–583, doi:10.1086/670401 (general pass-through/incidence and surplus integration).
- Adachi & Fabinger (2022), *Pass-through, welfare, and incidence under imperfect competition*, JPubE 211:104589, doi:10.1016/j.jpubeco.2021.104589 (heterogeneous firms, non-government interventions, general pass-through welfare formulas).
- Buccella, Fanti & Gori (2026), *The compatibility decision game*, EINT, doi:10.1080/10438599.2025.2478583 (joint adoption and Cournot/Bertrand); full theorem-level overlap still pending.

**Author decision needed later:** Is the generic incidence result an editorially persuasive explanatory bridge rather than a tautological welfare rewrite? No automatic merge or submission is justified by symbolic algebra alone.


## 2026-10-20 adversarial second audit — nonvacuity of R12 (NEW)

**Finding 1: The first, uniform sign-bound formulation is NOT satisfied at the original certified R9 witness.**
For \((c,v,d,F)=(1/10,6/25,1/20,9/100)\), an economically interpretable continuous *accounting interpolation* moves from the original no-adoption network/cost configuration to the outsider-only adopted configuration:
\[
p_h(a)=1-Q+v(q_1+q_2+a q_O),\qquad
p_O(a)=1-Q+vaQ,\qquad
r_O(a)=c-a(c-d).
\]
The firms play Cournot at each interpolation value \(a\) (this is a proof device; firms' adoption strategies remain **binary** in the paper). The verified rational equilibrium:
\[
q_h(a)=\frac{5(22-a)}{16(3a+16)},\qquad
q_O(a)=\frac{-5(297a+26)}{16(3a+16)(6a-25)}.
\]
Each home firm's quantity strictly decreases, the outsider's quantity strictly increases on \([0,1]\). The representative member government's welfare change from the member market (the rest is unchanged) is:
\[
W(a)=\frac{6336a^4-153384a^3+3057749a^2-14082300a+54686900}
{512(3a+16)^2(6a-25)^2}.
\]
**Its derivative changes sign from negative at \(a=0\) to positive at \(a=1\).** Therefore an a-priori uniform positive lower bound \(\kappa\) on welfare loss cannot explain this very example. This is a **real weakness of R12's original G2 sufficient condition**, not a weakness of R9.

**Finding 2: An integrated conduct-neutral sufficient condition fixes this without assuming an ex-post reversal.**
Let \(I(a)=A+\sum_jH_jq'_j=dW/da\), using *independently specified market response, home prices and consumer-surplus derivatives*. When \(I\) is nondecreasing,
\[
\int_0^1 I(a)\,da\ \le\ \frac1n\sum_{\ell=1}^{n}I(\ell/n).
\]
Thus if the observable derivative right-sum is below \(-G_0\), reversal follows. This is a **sufficient inequality in local response objects**: a finite-resolution upper integral certificate, NOT the tautological endpoint condition \(W(1)-W(0)<-G_0\). It is still a standard integration bound, not novel pass-through theory.

**Finding 3: The original R9 witness satisfies the integrated test with an exact sign certificate.**
- \(G_0=2408509/295731200\approx0.00814425059>0\).
- Actual post-adoption gap \(=-1341/184832\approx-0.007255237\).
- \(\int I = -4554109/295731200\approx-0.01539948778\).
- The *16-cell right-rectangle upper bound* on \(\int I\) is \(\approx-0.00969830954<-G_0\approx-0.00814425059\). Exact rational numbers, not rounded inequalities, are compared by the script.
- \(W''(a)>0\) on **the entire interval** by a degree-five Bernstein positivity certificate with all six coefficients strictly positive:
  \[
  (278124832175,256619666720,243567051785,238056392390,
   1196726617702/5,246846088619).
  \]
  The denominator is \(64(3a+16)^4(6a-25)^4>0\).
- Source: \`research/r12/verify_r9_nonmonotone_incidence.py\`, which also confirms *both* endpoints agree **exactly** with the canonical R9 member-market profit and consumer-surplus blocks.

**Finding 4: The general G1 strict-investment-selection sufficient condition is ALSO nonvacuous in the original R9 case.**
All eight SU adoption profiles and 64 SW profiles were independently re-solved using the **original** (not smooth/quasilinear substitute) Cournot price/networks/cost equations; all unilateral deviations and **weak** pure equilibria were enumerated:
- \(F=0.09\).
- Outsider's gross gain against nonadopting members \(g_O^0\approx0.11800704153\) (also smallest gain against all other SU profiles at this witness).
- Largest unilateral SU-member investment gain \(\bar g_H\approx0.06502431769\).
- Largest incremental investment gain in SW \(\bar g_{SW}\approx0.06816794948\).
- Hence
  \[
  \max\{0,\bar g_H,\bar g_{SW}\}<0.09<g_O^0
  \]
  **strictly**, independent of selecting a favorable adoption equilibrium.
- Unique pure SU firm continuation = outsider-only, unique pure SW continuation = no adoption. Checks are exact rationals.
- Source: \`research/r12/verify_r9_generic_adoption_dominance.py\`.

**Joint assessment:** Existing R9's specific joint phenomenon **is** demonstrably encompassed by the combined general investment selection G1 + integrated incidence G3 mechanism, not just nested algebraically. No R9 original scientific result changes. The initial uniform pointwise G2 remains a separate stronger sufficient condition, **not** a necessary description of all valid configurations. The R12 new corollary makes that limitation explicit. Generality now has a verified exemplar; it is still **not** a universal sign theorem, full general demand/conduct existence theorem, equilibrium coalition stability extension, or automatically a novel contribution to IJIO.

**Critical reviewer caveat:** The original R9 single-market \`p_i\` / \`CS=Q^2/2\` accounting pair is embedded algebraically, but a general micro-founded welfare theory should explicitly justify why \(S\) and \(p\) can be specified separately rather than claiming all pairs arise from rational consumer choice. This is a substantive economics issue that symbolic math alone cannot solve.

## Specific IJIO editor decision — comparison

The actual 2026-09-21 editorial decision (Sandro Shelegia) praised a well-written, clear paper, but classified it as a fairly standard **three-country Cournot trade modelling** exercise using algebraic profit/welfare comparisons of the same linear subgames; it did not find a **portable economic mechanism/general insight** sufficient for external review, and explicitly doubted an IJIO publication path. The research question *itself* was not rejected as ill-posed, but **insufficient innovation/scientific significance** was expressly cited.

**Research judgment:** Model-general reformulation addresses the **specific portability criticism**, not a guaranteed novelty or original IJIO resubmission right. A referee could still regard G1 as standard finite-game dominance, G3 as numerical integration, and the new incidence identity as an application of existing pass-through theory. The next required research gate is either a materially sharper, economically primitive sufficient condition that carries across conduct without high-burden response assumptions, or a carefully delimited submission to a more suitable journal. Do not redesign the R9 economic question or modify original R9 results to force a general sign claim.

## Final submission QA blocker

R12 currently exceeded the 17–19-page internal JICT short-manuscript builder bound already before G3 was appended (compiled 21pp before this latest corollary); it is **not a compliant short submission package yet**. Keep the R9 JICT submission candidate untouched. Do not claim final compilation/length is green simply because standalone symbolic/adoption proofs pass.
