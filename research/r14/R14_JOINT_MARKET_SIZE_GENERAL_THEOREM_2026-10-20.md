# R14 — Model-neutral joint market-size window with endogenous private compatibility

**Date 2026-10-20. Status: general half-space lemma proved; original R9 exact Cournot instance verified; independent originality NOT certified.** Research-only draft. Original R9 manuscript, certified Cournot propositions, complete residual-cost theory, numerical witness, 22-page appendix, coalition theorem and failed-scope tests remain unchanged.

## Scope of generalization, preserving all existing results

Keep the original **three countries, two-member standards union, foreign outsider, segmented destination markets, the two-stage private standard-support investment decisions and public comparison SU vs IS**. Existing R13 buyers optimize quasilinear utility and fulfill network expectations; the adoption strategy remains discrete and fixed cost per newly supported standard. We do **not** change the network specification, cost relief parameter, adoption timing, policy objective, government ranking or baseline equilibrium.

Let the two member destination markets each have normalized size 1, and the outsider destination size \(t>0\). Scale all destination-level consumer utility and operating profits by that destination's consumer mass, **holding the per-capita demand / competition / network mapping fixed**. This is the original manuscript's explicit \(m_k\) convention for heterogeneous market masses. A firm buys support for the other standard once at a fixed *real* fee \(F\); a larger destination does not alter the number of standards or the fee. The original symmetric benchmark is \(t=1\).

**Caveat:** If the absolute number of network subscribers, rather than the per-capita network-share rule, enters the network benefit \(G_i\), the per-capita payoffs may depend on \(t\), breaking the affine results. This condition must be stated explicitly to claim generality.

## Theorem T: model-neutral joint policy/adoption market-size window

Assume for every standards regime and discrete adoption profile that a well-defined product-market equilibrium exists, with per-unit-mass firm operating payoffs \(P_{ik}^{r,s}\) and destination consumer surplus \(S_k^{r,s}\) independent of \(t\). This equilibrium may be Cournot, Bertrand or another conduct game (subject to existence and fulfillment of buyer expectations); neither linear demand nor an FOC shape is needed for the following result.

For the *candidate* continuation, let the SU outsider buy the member standard, while neither member buys the outsider standard. Under SW, let no firm buy any foreign standard. The candidate SU outsider's investment must yield \(g_O^0>F\) against nonadopting members. For every SU member and every other action profile, impose
\[
F>\Delta P_h^{SU}(t;\mathbf s_{-h}),
\]
and for every SW firm and profile/unsupported destination standard \(k\), impose
\[
F>\Delta P_{i,k}^{SW}(t;\mathbf s_{-i},s_i),
\]
where \(\Delta P\) is the **gross equilibrium re-solved worldwide operating-profit gain from adding that standard**. These are *primitive-to-stage-payoff* restrictions, each **affine in \(t\)** because market payoffs are segmented and scale by destination mass. They select the outsider-only SU and no-adoption SW continuation uniquely by iterated strict-dominance elimination (member adoption actions eliminated first, then outsider adopts) without imposing an arbitrary Nash selection. Their intersection in \(t\) is an open interval (possibly empty) because it is an intersection of finitely many strict one-dimensional affine half-spaces.

Now write a member's **pre-adoption** government SU-minus-IS ranking as
\[
\Delta_N(t)=E-tD
\]
and its **post-adoption** ranking as
\[
\Delta_O(t)=R-tD.
\]
\(E\) and \(R\) are the member-destination national-welfare differences, comparing SU/no adoption and SU/outsider-only adoption with IS, respectively. \(D>0\) is the per-unit outsider-market home-firm operating-profit disadvantage in the SU regime relative to IS. **The same \(D\)** applies before and after outsider-only adoption because the two member firms have not bought the outsider standard and their outsider-market access remains unchanged. This is crucial. \(E,R,D\) are determined by the *underlying* product-market equilibrium, buyer surplus and national ownership, **not** by assuming the desired ranking.

If \(E>R\ge0\) and \(D>0\), then
\[
\Delta_N(t)>0>\Delta_O(t)
\quad\Longleftrightarrow\quad
\frac{R}{D}<t<\frac{E}{D}.
\tag{T1}
\]
If \(R<0\), replace the lower bound by \(t>0\); if \(E\le R\), no reversal is possible. Let \(I_A=(L_A,H_A)\) be the **intersection of every strict firm-stage adoption incentive inequality** and \(t>0\) (possibly empty; endpoints can be infinite). Then the complete simultaneous sufficient region is
\[
\boxed{\quad
\max\{0,R/D,L_A\}<t<\min\{E/D,H_A\}.
\quad}
\tag{T2}
\]
Under the candidate continuation, strict margins and a regular product-market equilibrium ensure the result persists in an open set of primitives.

**Proof.** Market-separable and size-scaled consumer welfare and firm payoffs are affine in \(t\). Thus each firm's incremental profit from supporting one foreign standard is affine. Their strict inequalities form an open interval; member adoption is strictly dominated and outsider adoption is profitable once members are removed. National accounts decompose into a home-destination component (\(E\) or \(R\)) and the unchanged outsider-destination home-firm disadvantage \(-tD\). Comparing signs yields (T1). Intersect the government and firm intervals to obtain (T2). No product-market conduct FOCs are used. Strictness plus continuity yields openness. \(\square\)

**Conceptual content beyond a tautological ranking:** A common outsider-market exposure \(tD\) shifts **both** the pre- and post-adoption government rankings in parallel, while outsourced adaptation reduces the **home/member-market protection advantage by \(E-R\)** without removing that foreign-market disadvantage. The foreign-market size must be (i) large enough that a government still cares about mutual access after unilateral private adaptation, but (ii) not so large that the original regional coalition was already unattractive. The same size affects the firms' **reverse private investment incentives**, so the economic policy region is further truncated by the adoption-game bounds. The theorem connects *two endogenous stages* and a political incidence constraint; it does **not** call the linear intersection mathematics novel.

## Exact original R9 benchmark certificate — verified over an interval, not a grid

Fix **the original** certified parameters \((v,c,d,F)=(6/25,1/10,1/20,9/100)\). Recalculate all eight SU and all 64 SW firm-standard-adoption profiles, with both member destination masses exactly 1 and outsider destination mass \(t\). Each three-firm Cournot market is re-solved using the original network-group (including singleton-zero) rule and destination marginal costs. The exact piecewise-affine halfspace intersection over **204** strict investment and government inequalities gives
\[
\Delta_N(t)=\frac{4779709}{295731200}-t\frac{39}{4864},
\qquad
\Delta_O(t)=\frac{141}{184832}-t\frac{39}{4864},
\]
and the *complete verified sufficient open region*
\[
\boxed{\qquad
\frac{47}{494}<t<
\frac{933888}{707347}
\qquad}
\tag{R14.1}
\]
with all 204 inequalities nonnegative at both endpoints and strictly positive inside (apart from the binding endpoint equalities). The **lower limit** is government's post-adoption IS preference; the **upper limit** is an SW firm's incentive to support an additional standard. The government pre-adoption upper limit by itself is \(E/D=4779709/2371200\), but the private-adoption condition binds first.

At \(t=1\), the original certified R9 gap is reproduced exactly:
\[
\Delta_N(1)=\frac{2408509}{295731200}>0,\qquad
\Delta_O(1)=-\frac{1341}{184832}<0.
\]
All SU/SW pure strategy deviations are also verified at the exact interior midpoint of the interval, including weak Nash candidates; only the intended unique continuations survive. The exact full-interval certificate is reproducible with
\`research/r14/verify_joint_size_window.py\`; [CI run 39385517652](https://github.com/ryotamatsuki/private-compatibility-standards-coalitions/actions/runs/39385517652) **PASS**.

## Reviewer-level assessment, closest research and limits

- **Generalizes original model's socioeconomic reach:** R9 was presented at equal market mass \(t=1\). A **nontrivial open range of asymmetric market sizes** admits both selected private investment and the government preference reversal with **all the original payoffs and proof results unchanged**. This is more than a single robustness point.
- **Mechanism is portable across market conduct** as the structural theorem (T2) relies only on segmented-mass-proportional market payoffs, national incidence and fixed-cost standard support. It remains *conditional*: it does NOT show that every Bertrand or non-Cournot game has nonempty firm-and-policy intersection.
- **Separate model validation:** The numerical interval (R14.1) is proved in the **original Cournot microfoundation only**. Do not cite it as an exact interval for Bertrand or nonlinear demand.
- **Closest substantial overlap:** Gandal & Shy (2001), *Standardization Policy and International Trade*, contains a distinct **Country Size and Standardization Unions** section, so size affects public recognition incentive in existing original literature. This theorem's potentially distinguishable content is the additional **post-union firm adaptation-stage filtering**, not country size per se. Buccella, Fanti & Gori (2026) and classical compatibility adoption literature challenge asymmetric adaptation novelty; full direct theorem-absorption audit remains pending.
- **Novelty verdict:** Stronger exogenous parameter generalization and a genuinely joint adoption/policy equilibrium interval, but the closed-form inequality-intersection is not automatically an independent new theoretical contribution. It directly addresses the old editor's model-specific calculation criticism by identifying a conduct-neutral structural connection. Avoid claims of generality beyond market segmentation, payoff mass scaling, network-share regularity and industry game equilibrium existence.

**Governance:** Do not edit or replace R9/JICT PR #34, certified R9 equations/Appendix, R12 PR #37 or R13 PR #38. R14 is a distinct experimental branch. Page-count concerns are intentionally postponed, as requested; none of the original journal candidate files is changed.
