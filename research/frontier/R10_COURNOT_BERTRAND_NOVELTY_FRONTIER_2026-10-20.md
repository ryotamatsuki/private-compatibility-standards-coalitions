# R10 exploratory frontier — common-primitive Cournot/Bertrand government reversal

**Date:** 2026-10-20. **Research only.** Preserve R9's 19-page JICT manuscript, the 22-page supplementary appendix, original certified proofs, branch \`revision/r9-jict-astra-final-polish\`, and PR #34 **byte-for-byte**. Do not merge this work into that manuscript without a distinct author-approved gate.

## Research question and original counterweight

Does the national-welfare preference reversal caused by **endogenous outsider-only private compatibility adoption** survive replacing quantity competition with differentiated-product price competition *at the same primitive parameters, with residual compliance costs strictly positive*, and are there conditions under which the competition mode itself reverses how the remaining compliance cost affects home national welfare?

Existing R5 / Appendix E.4 holds product substitutability at \(\gamma=1/2\). On its specified box \(0<c<1/3,\ 0\le v<1/4\), both differentiated Cournot and Bertrand were certified to have the **initial SU advantage negative**, while unilateral private adoption is feasible: the main preference reversal is therefore impossible in that particular demand specification. These are negative results, NOT a theorem that price competition or all differentiated demand rules out preference reversal.

## Exploratory mathematical result A: exact same-parameter witness (VERIFIED, novelty UNVERIFIED)

Use inverse demand \(p=\mathbf 1-M_G q\), with
\[
M_G=(1-\gamma)I+\gamma\mathbf1\mathbf1^\top-vC_G,
\]
where \(C_G\) marks same-standard compatibility groups of size at least two; singleton groups receive zero compatibility gain. Adapted foreign firms still pay \(d\) in destinations whose standard they newly support, while firms selling through unsupported foreign standards pay \(c\). Fix:

\[
\gamma=23/25,\quad c=2/125,\quad v=33/500,\quad F=1/40,\quad d=1/500=c/8>0.
\]

Use exactly **the same primitives** under Cournot (quantity) and Bertrand (price). The pure-strategy firm-stage game includes both member firms and the outsider under SU, each deciding whether to support the other standard (8 adoption profiles). Under SW, each of three firms chooses whether to support none, one or both other standards (64 adoption profiles). IS is the all-same-standard comparison.

Re-solve product-market prices, outputs, consumer surplus and firm operating profit after **every** adoption profile, with each firm's profit net of the fixed cost per additional supported standard. Then check every unilateral alternative in the finite adoption game.

| Exact-sign quantity, approximate display | Cournot | Bertrand |
|---|---:|---:|
| Member SU-minus-IS welfare **before** private adoption, as the counterfactual pre-adoption comparison | +0.0002460888 | +0.0054087429 |
| Member SU-minus-IS welfare **after** selected outsider adoption | -0.0000586961 | -0.0008554743 |
| Smallest strict deviation margin at SU equilibrium | +0.0191814193 | +0.0048164151 |
| Smallest strict deviation margin at SW equilibrium | +0.0101387739 | +0.0131303608 |
| Pure equilibria in each SU and SW continuation | exactly one | exactly one |

- SU equilibrium: two member firms support only their regional standard; the outsider alone additionally supports the regional standard.
- SW equilibrium: no firm supports a foreign standard.
- All evaluated demand matrices are symmetric positive definite, all product-market outputs strictly positive, and all alleged equilibrium unilateral-deviation margins strictly positive.
- The listed sign tests are computed from **exact rational SymPy matrix solutions**, with decimal values only for display. The independent *reproduction script* is \`r10_verify_joint_competition.py\`, which also asserts these inequalities.
- By strict inequalities and continuity of the interior equilibrium and payoff mappings, **a nonempty open neighborhood of primitives** retains these properties under both modes simultaneously.
- **Important scope:** The pre-adoption payoff is a counterfactual government ranking holding firms at no adoption, not a separate firm-stage equilibrium at this low F. The result does not certify government first-stage endogenous partition selection, welfare optimality of IS, global policy stability, or a theorem for arbitrary \(\gamma\).
- This is a *model-specific common-primitives existence theorem candidate*, not yet a new publication-grade economic theorem.

## Exploratory mathematical result B: competition-mode switch in residual-cost welfare incidence (VERIFIED, novelty HIGH-RISK)

Condition on the **fully compatible member destination market** after outsider adoption, with two zero-cost domestic members and outsider marginal cost \(d\). Define
\[
m=1-v>0,\qquad b=\gamma-v,\qquad 0<b<m.
\]
Here \(M=(m-b)I+b\mathbf1\mathbf1^\top\). National welfare associated with this member market equals consumer surplus plus the profits of **both home members** in this market; other destination profits do not depend on this local \(d\).

Solve the market by its **own** FOCs for each mode. The *exact derivatives at \(d=0\)* are:
\[
\left.\frac{\partial W^{C}}{\partial d}\right|_0
=\frac{2b^2+bm-2m^2}{4(2m-b)(b+m)^2},
\quad
\left.\frac{\partial W^{B}}{\partial d}\right|_0
=\frac{(b-2m)(b+m)^2}{4m^2(2b+m)(3b+2m)}.
\]
For \(0<b<m\), **Bertrand's derivative is always strictly negative**. Cournot's derivative is positive precisely when
\[
\frac bm>\frac{\sqrt{17}-1}{4}\simeq0.7807764.
\]
Thus in a parameter region in which both modes are regular, **Cournot and Bertrand give opposite national-welfare responses to a small residual foreign adaptation cost**. At the exact witness above, \(m=467/500,\ b=427/500\), so Cournot's sign is positive, Bertrand's negative.

This is a conditional product-market / market-incidence comparative static. It is **not** by itself a new government-equilibrium theorem. Moreover, competing supply responses and welfare differences across Cournot/Bertrand are a substantial classical literature, so claiming that the comparative static is itself independent novelty without a full direct-theorem absorption audit would be unsound.

## Closest-prior-art and absorption-risk register

| Original work | Direct theorem/mechanism visibly supported by examined source | Overlap threat / what remains to verify |
|---|---|---|
| **Gandal & Shy (2001)**, *Standardization policy and international trade*, JIE, doi:10.1016/S0022-1996(00)00067-2 | Government recognition and international versus regional unions with network externalities and conversion costs; regional SU can benefit two members when conversion costs are large. | Direct source for **national-level standardization rankings**. Must check full welfare inequalities and endogenous cost-adaptation alternatives before claiming government reversal new. Abstract accessed; full original theorem mapping not completed. |
| **Buccella, Fanti & Gori (2026)**, *The compatibility decision game: network externalities and the (variable) costs of achieving compatibility*, EINT 35(2):284–306, doi:10.1080/10438599.2025.2478583 | Cournot **and Bertrand** endogenous firm compatibility, variable compatibility costs, unilateral/anti-coordination equilibria and welfare effects. | **Very high threat** for adoption/competition-mode results. Available original abstract; full paper inaccessible through search. A direct model-to-model theorem audit is mandatory. |
| **Buccella, Fanti & Gori (2023)**, *Strategic product compatibility in network industries*, Journal of Economics, doi:10.1007/s00712-023-00834-x | Endogenous compatibility and fixed cost induce multiple private equilibrium configurations; appendix treats differentiated products. | Firm compatibility alone, unilateral adoption or differentiation are NOT novel. Primary Springer full article inspected. |
| **Toshimitsu (2016)**, *Price and Quantity Competition in a Differentiated Duopoly With Network Compatibility Effects*, Japanese Economic Review 67:495–512, doi:10.1111/jere.12109 | Mode comparison with network effects and compatibility; welfare ranking and endogenous selection of price/quantity strategically depend on substitutability. | Strong absorption threat for mode-comparison welfare sign result B. Abstract and bibliography read; full mathematical theorem mapping pending. |
| **Eaton & Grossman (1986)**, *Optimal Trade and Industrial Policy Under Oligopoly*, QJE 101:383–406, doi:10.2307/1891121 | Optimal **national** intervention can switch between subsidy and tax depending on whether firms are Cournot or Bertrand; domestic consumption matters. | General strategic-trade national-incidence channel precedes this work. Cross-mode sign difference alone is likely an instance, not a frontier contribution. Abstract verified; exact source model remains to inspect. |
| **Maggi & Mrázová (2024)**, *Harmonization…What Else?*, NBER 33318, doi:10.3386/w33318 | Firms' fixed costs and regulatory diversity can yield harmonization **without an agreement**; cooperation may instead preserve diversity. | Direct mechanism threat to interpreting private compliance as inducing public international harmonization. Original public abstract inspected, full proof not yet mapped. |
| **Kawabata & Takarada (2021)**, *Deep trade agreements and harmonization of standards*, Southern Economic Journal, doi:10.1002/soej.12500 | Regional/FTA standards can impede or favor later multilateral harmonization; public standard choice and policy architecture studied. | Known building/stumbling effects. Distinguish private post-agreement adaptation from public standard selection. Full theorem comparison pending. |
| **López & Vives (2019)**, *Overlapping Ownership, R&D Spillovers, and Antitrust Policy*, JPE 127:2394–2437, doi:10.1086/701811 | Main Cournot model robust to differentiated Bertrand in innovation/investment context. | Methodological precedent for robust alternative competition mode, **not** source for claiming own theorem's novelty. |

Original source links: https://www.sciencedirect.com/science/article/pii/S0022199600000672 ; https://ideas.repec.org/a/taf/ecinnt/v35y2026i2p284-306.html ; https://link.springer.com/article/10.1007/s00712-023-00834-x ; https://onlinelibrary.wiley.com/doi/10.1111/jere.12109 ; https://collaborate.princeton.edu/en/publications/optimal-trade-and-industrial-policy-under-oligopoly/ ; https://www.nber.org/papers/w33318 ; https://onlinelibrary.wiley.com/doi/10.1002/soej.12500 ; https://www.journals.uchicago.edu/doi/10.1086/701811 .

## Novelty decision (NOT blanket IJIO GO)

1. **GO for mathematical exploration:** previous fixed-\(\gamma=1/2\) portability failure can be repaired with a second parameter region and a nonempty common-primitives **incomplete-cost-relief** existence witness. This is more persuasive robustness support than simply appending a failing Bertrand check.
2. **NO-GO for claiming the competition-mode difference is a standalone new theoretical contribution.** Welfare sign reversals between Bertrand/Cournot are well explored. Formula B is a restricted instance and may be directly absorbed by Eaton–Grossman/Toshimitsu or later compatibility models.
3. **UNDECIDED for independent IJIO-level novelty:** A complete-parameter characterization identifying what makes the joint government/adoption mechanism different from existing private compatibility plus policy ranking models has not been demonstrated. An existence witness is not sufficient by itself to reverse the earlier editor's originality assessment.
4. **Keep R9 manuscript and PR #34 unchanged.** Do NOT patch the submitted-object candidates as a side effect of this frontier. A separately approved R10 research gate would be required for manuscript integration.

## Next mandatory gate (bounded)

- **A1: primary-source absorption audit:** obtain full Buccella–Fanti–Gori (2026), Toshimitsu (2016), Gandal–Shy (2001), Eaton–Grossman (1986), Maggi–Mrázová (2024); map **the actual theorem**, adoption-game timeline, national welfare and government stage.
- **A2: gamma frontier:** isolate analytically the \(\gamma\) threshold for the government's initial SU preference for each mode **under interiority**, and jointly certify the selection-free \(F\) interval and positive \(d\) with independent interval/Sturm or Bernstein certificates.
- **A3: economic contribution test:** is the new result a necessary/sufficient **economic condition** (not merely an extra calibrated witness), and does it yield a distinctive policy comparative static/testable prediction not already in the closest parent model?
- **Kill condition:** if the only result is a Cournot–Bertrand common witness and a familiar cost-pass-through sign contrast, classify as **robustness extension to the existing JICT paper**, not a new IJIO-strength mechanism.
- **Decision rule:** no substantive changes, no PR #34 merge, and no journal submission triggered by this research branch. User should separately decide integration versus timely JICT submission.

**Methods limitations:** Rational checks are exact in the chosen linear-demand game, not an independent researcher replication or full formal proof across all \(\gamma\). Direct full texts of several threatening papers were unavailable. No journal manuscript or submission status changed.
