# JICT 18-page short manuscript — coalition proof repair, scoped mathematical QA

Date: 2026-10-13 JST. Status: editorial-only repairs implemented on draft PR #33. Canonical R9 and previously certified 39-page JICT manuscript remain unchanged.

## Referee objections addressed

The 2026-10-13 39-versus-16-page pre-referee audit identified two MAJOR shortcomings in the shortened Section 5. Both are now addressed in the actual LaTeX source and anonymous supplement, and were compiled as **18-page main PDF + 18-page Online Supplement** under the existing elsarticle review layout.

**MAJOR 1 — explicit deviation technology.** Main `paper/jict_short/short_05_stability_scope.tex` now writes the exact R6 finite-game rule: for nonempty country deviator group `D`, `rho'(rho,D) = {D} union { B\D : B in rho, B\D != empty }`. The remaining members of each original bloc stay together, singleton deviations from `IS` leave the other two paired, self-mapped deviations are nonblocking, private firm choices are reoptimized, and transfers are excluded. Both strict (all deviators strictly improve) and weak/Pareto (all weakly improve, one strictly) blocking are defined.

**MAJOR 2 — full-bypass stability payoff bridge and exhaustive blocking.** Model section now defines the SW components:
`H=(1+2c)^2/16`, `S=(1-2c)^2/16`, `K_W=(3-2c)^2/32`, `W^{SW}=K_W+H+2S`.
Main section now includes the international, SW, member/outsider SU and post-bypass national-welfare expressions, and one explicit concise strict-block table covering: SW (N strictly blocks to IS), IS high-F (pair strictly blocks to SU), each SU high-F (solo split loses, grand shift loses to members, partner switch has indifferent common member, so no strict block), each SU intermediate-F (N strictly blocks to IS; members gain P-C and outsider J+F), and IS intermediate-F (any proper deviation forms SU and hurts all deviators). The remaining symmetric weak-blocking and asymmetry arguments are explicit.
New appendix `paper/jict_short/short_supplement_blocking.tex` is attached to the supplement by `code/revision/build_jict_short.py`, enumerates **all seven** nonempty deviating coalitions for every type of partition up to relabeling, and provides analytically auditable payoff comparisons and proof, not only a private code pointer.

## Exact math/claim change control

- `paper/jict_short/short_04_incentives.tex` **not edited**: residual-rent R3 proposition, proof, exact strict joint witness, and its quantifiers remain identical to the 16-page short version; previously confirmed equal to the certified R9 central theorem aside from cross-ref labels.
- `paper/sections/*.tex`, `paper/main.tex`, `paper/appendix/*.tex`, `paper/references.bib`, R2–R9 code and formal Lean proofs: **untouched**.
- Institutionality remains restricted to **full cost bypass d=0**; no general stable-coalition result at positive residual d has been asserted.
- Numerical smoke test at exact R6 anchor (c,v)=(1/10,6/25): W_SW=0.415 < W_IS≈0.733639 < W_M_SU(no bypass)≈0.741783; W_SU_outsider(no bypass)≈0.366060 < W_IS. At the intermediate F=3/25, W_IS−W_SU_member(bypass)≈0.008018 >0 and W_IS−W_SU_outsider(bypass)≈0.323931 >0. These are sign checks only; actual domain-wide claims are inherited from R6 analytic certificates and full regression checks.
- Strict versus weak-blocking comparison preserved: high-F symmetric SUs fail weak stability because a partner-switching deviator is indifferent while the former outsider gains; small asymmetry turns common member's difference into δ(A−C)>0. At intermediate F, strict gaps sustain unique IS under both rules.

## Reproducible build & presentation

- Authoring: **18-page** anonymous LaTeX main PDF, bookended by intro and references, no shrink-to-fit margins/font. Derived output source and separately anonymous **18-page** SI including old appendices A–F plus human-readable Appendix G; inherited Appendix D multi-line aligned thresholds receive TeX linebreak-only repairs and Appendix E code/Lean identifiers receive line-breakable formatting exclusively in the short SI copy.
- Locally compiled with BibTeX; no main PDF overfull boxes, missing LaTeX citations or references, and no clipping in rendered pages of stability proof.
- Dedicated GitHub Actions `JICT Short Manuscript Preview` run **38285532463: PASS**, with 18-page gate, anonymous main PDF, standalone source ZIP compiles and supplemental proof ledger ZIP independent clean room compiles. Branch-specific old `Paper CI` full R2–R9/Lean run **38285532454**: (check live run conclusion before advancing; do not pre-certify here).
- Detailed comparative earlier reviewer report: `docs/revision/19_jict_short_vs_full_adversarial_referee_20261013.md`.

## Reviewer conclusion

The two MAJOR mathematical readability defects are corrected within 18 pages. The reconstructed coalition theorem now has a finite-game admissible-deviation definition and an understandable proof bridge directly in main text, with exact case-level details in SI. Economic research contribution remains **conditional and demand/network-specification-specific**; shortening did not remove the prior skepticism about material general applicability. Recommend retaining this as the preferred **draft** (PR #33), proceeding to final side-by-side signoff and human review. Neither replace certified original nor merge/submit without explicit decision.
