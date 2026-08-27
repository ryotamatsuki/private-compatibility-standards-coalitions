# Full-Paper Referee Audit and IJIO Submission Readiness

Audit date: 2026-08-27

Target journal: *International Journal of Industrial Organization* (IJIO)

This document records the submission-stage audit of the completed manuscript. It does not modify the Stage-8 frozen theory. The audit asks whether a skeptical editor or referee can reject the paper because of unclear positioning, a literature overlap, a logical inconsistency, incomplete technical support, a reproducibility gap, or avoidable presentation defects.

## Executive verdict

- Desk-reject risk: **MODERATE**.
- Novelty classification: **B — DISTINCT BUT NARROW**.
- Theory-hold status: **NO HOLD**. No contradiction in the frozen theory was found.
- IJIO readiness: **B — IJIO SUBMISSION PLAUSIBLE, MINOR REVISION NEEDED**.
- Central residual risk: the Main theorem establishes a stability reversal on a verified nonempty open set, but `Omega_0` includes the payoff and threshold inequalities required for the reversal. The paper therefore establishes existence and a mechanism, not a broad primitive characterization of when the reversal occurs.
- Central novelty defense: the closest standards papers contain regional versus multilateral standards, conversion/adaptation costs, coalition stability, and fixed multi-standard production costs, but the source audit did not identify the paper's particular sequence: formal coalition -> strategic standard-specific private adoption -> directional outsider-only bypass -> selective erosion of a member-market exclusion component -> government-ranking reversal -> change in the strict-blocking stable set.

The paper should not be made broader by adding a new extension before first submission. The appropriate submission strategy is to present the mechanism and its scope precisely.

## 1. Editor / desk-reject audit

### A1. Research question

PASS. The Introduction asks directly how firms' private ability to circumvent standards incompatibility affects the stability of formal standards coalitions and supplies the answer within the first several pages.

### A2. Unified mechanism

PASS. Standards, private compatibility, and coalition stability are not presented as independent ingredients. The common mechanism is

`firm adaptation -> product-market rents -> government incentives -> formal coalition stability`.

### A3. IO content

PASS WITH RISK. The paper contains a genuine IO chain: firms make a discrete compatibility investment, Cournot competition produces regime-specific profit and consumer-surplus blocks, and those continuation values enter government incentives. The institutional endpoint does not erase the IO mechanism.

### A4. Risk of reading as a trade/coalition paper

MODERATE. The government and coalition stages are prominent. The Introduction and Discussion correctly foreground firm conduct and product-market competition. This emphasis should be preserved in the submission version and cover letter.

### A5. Firm-conduct chain

PASS. The chain from compatibility choice through competition and national welfare to blocking incentives is explicit in the Introduction, Model, Selective Erosion, Discussion, Conclusion, and Figure 1.

### A6. Introduction length

MODERATE RISK. The Introduction is substantial in review format. It earns much of its length by explaining the distinction between formal membership and effective compatibility and by defending the contribution against close literatures. Further compression is possible, but aggressive shortening risks removing the novelty defense.

### A7. Related Literature

PASS WITH MODERATE LENGTH RISK. It is mechanism-organized rather than a bibliography dump. The Takarada, Gandal-Shy, Klimenko, private-compatibility, regulatory-cooperation, and coalition comparisons are directly tied to the paper's contribution.

### A8. Time to reach the model

MODERATE. In the review-mode PDF, Section 3 begins after the Introduction and Related Literature. The front end is defensible because novelty is narrow and must be established carefully, but editor attention is a constraint.

### A9. Manuscript length

MODERATE. Before the audit, the compiled review PDF was 66 pages, of which the substantive main text through the Conclusion occupied 62 pages and the A-G appendix files were empty/TODO scaffolds. After completing only technically necessary appendices, the candidate PDF is 75 pages: main text remains 62 pages, technical appendices occupy pp. 63-72, and the bibliography occupies pp. 73-75. The increase reflects removal of an incomplete-paper signal and addition of referee-facing sign proofs/correspondences, not a new extension.

### A10. Incomplete-paper signals

FIXED. All empty/TODO appendix scaffolds were completed, merged, or deleted. No unverified Partner Switching theorem was introduced.

## 2. Novelty kill test

### Classification

**B — DISTINCT BUT NARROW.**

The literature already contains essentially every surrounding ingredient. The defensible contribution is the particular continuation-payoff feedback generated by directional post-coalition private adoption.

### Twelve comparison dimensions

| Dimension | Prior literature | Current paper's incremental object |
|---|---|---|
| Formal standards regime | Yes | Not novel by itself |
| Regional coalition / standards union | Yes | Not novel by itself |
| Multilateral / international standard | Yes | Not novel by itself |
| Endogenous firm action | Yes | Not novel by itself |
| Converter / compatibility / multihoming | Yes | Not novel by itself |
| Fixed adoption or adaptation cost | Yes | Not novel by itself |
| Firm action after formal coalition formation | Partial antecedents | Separate strategic adoption stage after the partition is fixed |
| Directional outsider-only adoption | No close absorption identified | Key continuation state |
| Formal membership fixed while effective compatibility changes | No close absorption identified | Key institutional/technological separation |
| Continuation-payoff feedback into government ranking | Related policy feedback exists | Selective removal of the member-market component is the specific mechanism |
| Coalition blocking / stability | Yes | Not novel by itself |
| Stable-set change because of private adoption | No close absorption identified | Headline applied consequence |

### Takarada et al. (2020)

**Kill-test result: PASS; overlap risk HIGH.**

This is the closest single paper. It has a three-country Cournot standards environment, national/regional/multilateral standards, coalition/core stability, and an extension with fixed costs of producing under different standards. The fixed cost is regime-implied multi-standard production rather than a separate binary firm adoption game. It does not select a no-bypass versus outsider-only continuation state while holding a regional formal coalition fixed and therefore does not generate the selective-erosion transformation.

### Gandal and Shy (2001)

**Overlap risk: HIGH; mechanism not absorbed.**

They have three countries, network effects, conversion costs, government recognition, and standardization unions. Conversion is induced by the government's recognition environment rather than selected through the paper's standard-specific post-coalition fixed-cost adoption game. The difference must be stated narrowly; the paper cannot claim private workarounds themselves are new.

### Klimenko (2009)

**Overlap risk: MEDIUM-HIGH.**

Klimenko establishes that technical compatibility/interoperability policy, costly compatibility-related firm behavior, network externalities, and international agreements can interact strategically. The compatibility instrument is governmental in the closest agreement paper, and the two-country interoperability model does not contain the present formal regional-partition/private-outsider-bypass/stable-set sequence.

### Private compatibility literature

**Technology novelty: LOW; institutional-feedback novelty: MATERIAL BUT NARROW.**

Converters, interoperability, multihoming, multi-standard production, and endogenous standard adoption are established. Farrell-Saloner, Doğanoglu-Wright, Fischer-Serra, Schmidt-Steingress, and related work prevent any claim that private compatibility or costly adoption is new. The paper's contribution is the endogenous effect of a private standard-specific bypass on the continuation value of formal exclusion.

### Additional coalition/interoperability check

The 2026 audit added Guo, Liu, and Nault, “Join Up or Stay Away? Coalition Formation for Critical IT Infrastructure,” *Information Systems Research*. Their model links coalition formation and interoperability with post-membership resource investment. This is an important antecedent, but its cooperative infrastructure-investment stage does not reproduce the paper's firm-level directional adoption under a fixed formal standards partition.

## 3. Theory logic audit

The reconstructed sequence is internally consistent:

1. Governments are evaluated over formal partitions.
2. A partition assigns baseline standards and market coverage.
3. Firms may support additional formal standards at fixed cost `F`.
4. The used-standard rule determines destination-specific compatibility and marginal adaptation cost.
5. The four Cournot configurations generate quantities, operating-profit blocks, and consumer-surplus blocks.
6. Private adoption compares block differences against standard-specific fixed costs.
7. National welfare includes domestic consumer surplus plus the domestic firm's worldwide profit net of its own adoption costs.
8. Outsider-only adoption changes coalition-member continuation welfare without changing formal membership.
9. Governments use the resulting continuation payoffs in a strict-blocking partition game.
10. The stable formal partition set differs between the high- and intermediate-cost regions on `Omega_0`.

No inconsistency was found in timing, action sets, the compatibility mapping, who pays `F`, national-welfare accounting, outsider welfare, strict blocking, symmetry, the secondary asymmetry result, or equality-boundary treatment.

## 4. Headline result reconstruction

The audit independently reconstructed the Main chain from the canonical blocks:

- `T_A = P-B`, `T_U = A-C`, `T_W = A-S`.
- `F_L = max{T_W,T_A}` and `F* = 2T_A`.
- Before outsider bypass: `W_i^{SU,N}-W_i^{IS} = E_i-D_i`.
- After outsider-only bypass: `W_i^{SU,O}-W_i^{IS} = -D_i`.
- Hence `E_i-D_i -> -D_i`.
- For `(c,v) in Omega_0` and `F>2T_A`, the stable set contains precisely the three symmetric regional SUs.
- For `(c,v) in Omega_0` and `F_L<F<2T_A`, the stable set is `{rho^{IS}}`.

The audit does not infer global monotonicity in `F`.

## 5. Claim-to-test verification matrix

| Paper claim | Symbolic / analytical verification | Numerical regression | Status |
|---|---|---|---|
| Four Cournot equilibria | `verify_symbolic.solve_focs`, `verify_blocks` | direct FOC consistency | PASS |
| Consumer-surplus blocks | `verify_blocks` | domain checks | PASS |
| Corrected `W^{IS}` | exact symbolic identity | general-domain checks | PASS |
| `T_U` formula | exact symbolic identity | domain regression | PASS |
| `T_A,T_U,T_W>0` | factor/sign support for `T_A,T_U`; exact definitions | 20,000-point domain regression | PASS |
| `T_W>T_U` | exact positive factorization | domain regression | PASS |
| SU/SW adoption-gain thresholds | `verify_private_adoption_identities` | headline continuation regression | PASS |
| Selective erosion before bypass | general-mass exact identity | witness sanity check | PASS |
| Selective erosion after bypass | general-mass exact identity | witness sanity check | PASS |
| Erosion size and political cross-difference | exact identities | witness sanity check | PASS |
| `P-C` primitive threshold | exact factorization and threshold algebra | open-neighborhood check | PASS |
| `J` identity and positivity support | exact numerator/endpoints/curvature | witness `J>0` | PASS |
| `W_M^{SU,N}>W^{SW}` | `verify_welfare_inequalities.py` sign certificate | 20,000-point domain regression | PASS |
| `W^{IS}>W^{SW}` | same | same | PASS |
| `W^{IS}>W_O^{SU,N}` | same | same | PASS |
| `Omega_0` witness | exact rational witness identities | witness + 41x41 open-neighborhood grid | PASS |
| High-F stable set | analytical theorem proof | stable-set regression | PASS |
| Intermediate-F stable set | analytical theorem proof | stable-set regression | PASS |
| Market-size partner ranking | exact general-mass identity | multiple-delta regression | PASS |
| `delta -> 0` symmetry restoration | exact symbolic identity | delta-zero regression | PASS |
| Low-F accounting | exact symbolic accounting | not used as Main proof | PASS |

The numerical checks are regression/mismatch detectors, not proofs. Domain-wide sign claims used by the Main stability theorem now have explicit analytical certificates in Appendix B and a separate symbolic verification script.

## 6. Appendix disposition

- Appendix A — **COMPLETE**. Cournot derivations, positivity, interiority, and domain checks.
- Appendix B — **COMPLETE**. Analytical welfare sign certificates and `J>0` support.
- Appendix C — **COMPLETE**. Private-adoption pure-strategy equilibrium correspondence and selection-free headline regions.
- Appendix D (old generic Proofs scaffold) — **DELETE**. Redundant with self-contained Main proofs and technical Appendices A-B.
- Appendix E (old Parameter Domain scaffold) — **MERGE into Appendix A**.
- Appendix F in the old A-G plan / current Appendix D — **COMPLETE**. Low-F multistandarding comparison only; no new Main stability theorem.
- Appendix G (Partner Switching) — **DELETE**. P3 remains conditional/unverified and is not revived.

## 7. Length and architecture audit

Changes made for cognitive load rather than cosmetic shortening:

- Removed all empty appendix scaffolds.
- Moved the long `J>0` polynomial sign argument from Section 7 to the technical welfare appendix.
- Retained self-contained Main theorem proofs in the main text because the blocking logic is part of the economic result rather than algebraic housekeeping.
- Did not compress Sections 3-8 in ways that would change assumptions, theorem content, or scope statements.
- Did not promote low-F material or market-size asymmetry.

Residual length risk remains moderate because review mode is 75 pages, but 10 pages are now genuine technical appendices and 3 pages are bibliography. The substantive main text is unchanged at approximately 62 review pages.

## 8. Figure and table audit

### Figures

- Figure 1 (timing): **HELPFUL**. It makes the institutional/private/product-market sequence immediately visible.
- Figure 2 (selective erosion): **HELPFUL / near-essential**. It visually isolates `E_i-D_i -> -D_i` and explicitly labels itself conceptual.
- Figure 3 (fixed-cost regions at the witness): **HELPFUL**. It earns its space by showing the nondegenerate interval in `F`. Its caption explicitly says it is a numerical illustration at the verified witness and not a proof or global parameter-space theorem.

All three figures are retained.

### Tables

- Table 1 (Cournot blocks): **ESSENTIAL / HELPFUL** because the paper reuses many blocks.
- Table 2 (adoption thresholds): **HELPFUL** because it prevents threshold/state confusion.
- Table 3 (headline stability regions): **HELPFUL**. It differs from Figure 3 by providing the formal regime/stable-set classification rather than only the visual fixed-cost interval.

All three tables are retained.

## 9. Claim consistency and stability-versus-efficiency audit

The Abstract, Introduction, Selective Erosion section, Coalition Stability section, Discussion, and Conclusion consistently identify the contribution as a change in the continuation value of formal exclusion.

The manuscript explicitly distinguishes:

- formal membership from effective technological compatibility;
- technological substitution from the narrower political-incentive cross-difference;
- coalition stability from social efficiency;
- partner ranking from coalition stability;
- a nonempty open-set result from a global characterization.

No inference from unique IS stability to world-welfare optimality is retained.

## 10. Parameter-region presentation

The safe interpretation is maintained:

- `Omega_0` is a **nonempty open set**;
- the intermediate `F` region is a **nondegenerate interval**;
- `(c,v)=(0.10,0.24)` is a **verified witness establishing nonemptiness**, not a proof by numerical example.

The paper does not use “generic,” “large parameter region,” “almost everywhere,” or equivalent unproved claims.

The residual theoretical presentation risk is that `Omega_0` is defined partly by the payoff inequalities needed for the theorem, including `Phi_0>0`. A skeptical referee can therefore describe Proposition 1 as an existence/microfoundation result rather than a sharp primitive characterization. The manuscript should accept that description rather than oversell the result.

## 11. Referee attack memo

| # | Potential objection | Severity | Current disposition |
|---|---|---|---|
| 1 | This is Takarada et al. plus another fixed cost. | MAJOR | Literature revision + kill test; central mechanism not absorbed |
| 2 | Gandal-Shy already has conversion costs and standardization unions. | MAJOR | Narrow distinction made: no separate strategic post-coalition adoption state there |
| 3 | Private compatibility is only a converter/multihoming technology. | MAJOR for novelty | Technology novelty disclaimed; contribution is continuation-payoff feedback |
| 4 | The `2T_A` outsider threshold is mechanically driven by a two-market bloc. | MAJOR scope | Acknowledge geographic-scope effect; selective-erosion identity itself is written for general market masses |
| 5 | Why should the outsider adopt after the coalition forms? | MODERATE | Derived from its profit gain `(m_i+m_j)T_A-F` |
| 6 | Why is `F` exogenous? | MODERATE | Explicit limitation/future work only |
| 7 | Why only three countries? | MODERATE | Minimal environment for fragmentation/regionalism/multilateralism; larger networks are future work |
| 8 | Why Cournot? | MODERATE | Closed-form microfoundation; no Bertrand robustness claim |
| 9 | Why strict blocking? | MAJOR | Conventional maintained concept; alternative concepts explicitly outside scope |
| 10 | Why no transfers or side payments? | MAJOR | Explicit substantive limitation; would change blocking incentives |
| 11 | Is symmetry driving the Main result? | MODERATE | Symmetry deliberately demonstrates asymmetry is unnecessary; it does create high-F partner indifference |
| 12 | Is the result driven by network effects? | MODERATE | No necessity claim; network effects remain part of the microfoundation |
| 13 | Does unique IS stability imply efficiency? | MINOR | Explicitly rejected throughout |
| 14 | What happens at low `F`? | MODERATE | Completed Appendix D; kept outside headline theorem |
| 15 | `Omega_0` assumes much of the desired ranking. | MAJOR | Residual theorem-strength risk; paper claims existence on a nonempty open set, not full characterization |
| 16 | Off-headline adoption games may have multiple equilibria. | MODERATE | Appendix C gives the correspondence; headline regions use strict best responses and are selection free |
| 17 | The used-standard rule for multi-standard firms is imposed. | MODERATE | Explicit modeling rule; further endogenous usage choice is outside frozen model |
| 18 | Why should an IJIO reader care about coalition stability? | MODERATE | IO chain foregrounded: firm conduct -> Cournot rents -> policy incentives |
| 19 | The manuscript is long. | MODERATE | Main text stable at ~62 review pages; technical support moved to appendices |
| 20 | Coalition formation and interoperability have additional antecedents. | MODERATE novelty | Guo-Liu-Nault added and distinguished |
| 21 | Outsider adoption cost is absent from member welfare. Is that an accounting error? | MODERATE technical | No: foreign-firm profit is not national welfare; outsider welfare correctly includes `-F` |
| 22 | What occurs at threshold equalities? | MINOR | Indifference/correspondence treatment explicit; Main theorem uses strict intervals |

Twenty-two referee objections were identified. Seven generated direct manuscript or technical-support revisions; the remainder were already answered, are scope qualifications, or require a genuine extension and therefore are left for future work rather than added now.

## 12. Top-five referee-response simulation

### Objection 1 — Takarada absorption

**Simulated referee report.** The paper appears very close to Takarada et al. (2020), which already studies a three-country Cournot model with national, regional, and multilateral standards, coalition stability, and a fixed-cost extension. It is unclear whether adding another fixed-cost margin is enough for a separate contribution.

**Simulated author response.** We agree that Takarada et al. is the closest benchmark and have revised the paper to make that proximity explicit. Our claim is not novelty from a fixed cost. In their fixed-cost extension, multi-standard production costs follow from the government standards regime. In our model the formal regional coalition is first fixed and firms then choose standard-specific additional support. This creates a strict intermediate-cost region in which the outsider alone adopts the bloc standard while members do not reciprocate. Holding formal membership fixed, this private response removes the member-market exclusion component but leaves the reciprocal outsider-market disadvantage. The resulting transformation changes government continuation payoffs and the strict-blocking stable set. We have narrowed all novelty language accordingly.

### Objection 2 — `Omega_0` is too close to assuming the result

**Simulated referee report.** The definition of `Omega_0` contains `Phi_0>0`, `P>C`, and the threshold ordering needed for the conclusion. Proposition 1 therefore risks reading as a tautological parameter-set definition plus a numerical example rather than a substantive comparative-statics theorem.

**Simulated author response.** We agree that Proposition 1 is an existence/microfoundation result, not a global primitive characterization. The paper does not claim otherwise. The selective-erosion theorem is an exact structural payoff identity stated before the three-country parameter restriction. `Omega_0` then identifies a strict open set of the canonical primitive model on which the relevant ranking and adoption-state inequalities hold simultaneously. Nonemptiness is established by an exact verified witness and continuity, and the intermediate fixed-cost interval is nondegenerate. We have removed any wording suggesting that this is a broad or generic parameter characterization. Deriving a sharper primitive description of the entire reversal region would be useful but is not needed for the mechanism established here.

### Objection 3 — strict blocking and no transfers

**Simulated referee report.** The stability result may be an artifact of a restrictive coalition concept. With consent, transfers, bargaining, farsightedness, or a different accession rule, the stable set may change substantially.

**Simulated author response.** We agree and treat this as a scope limitation rather than a robustness claim. The contribution is not a new coalition solution concept. We deliberately use strict blocking in an exclusive-membership partition game to isolate how post-formation firm conduct changes the payoff table supplied to the coalition game. Transfers and alternative formation concepts can change which payoff differences support a deviation and therefore require separate analysis. The manuscript now states this limitation repeatedly and does not extrapolate Theorem 2 to those environments.

### Objection 4 — the result is a three-country/two-market arithmetic effect

**Simulated referee report.** Outsider adoption is attractive because one bloc-standard investment opens two member markets, whereas member adoption of the outsider standard affects only one market. The headline result may therefore be little more than `2T_A` versus one-market thresholds.

**Simulated author response.** The geographic scope of the bloc standard is indeed economically important for selecting the outsider-only continuation state, and the paper states that the factor two is a scope effect rather than a duplicated fixed cost. The selective-erosion identity itself is not a `2T_A` arithmetic identity: for general market masses it maps the member's regional-versus-IS gap from `E_i-D_i` to `-D_i` whenever a directional outsider bypass completes compatibility in coalition-member markets without reciprocal member adoption. The three-country model supplies one transparent microfoundation in which the required directional state is selected endogenously. We therefore interpret the stability theorem as a specific implementation of a more general continuation-payoff mechanism, not as an n-country theorem.

### Objection 5 — IJIO fit

**Simulated referee report.** The final object is coalition stability among governments, so the paper may fit international cooperation or political economy better than industrial organization.

**Simulated author response.** The coalition payoff is endogenous to an explicit IO stage rather than assigned exogenously. Formal standards determine compatibility and marginal-cost positions; firms choose whether to pay a fixed cost for additional-standard support; that choice changes Cournot competition, operating profits, and consumer surplus; governments then evaluate the resulting national continuation payoffs. The causal mechanism is therefore firm conduct -> product-market competition -> coalition-specific rents -> government incentives -> formal stability. We have foregrounded this chain in the Abstract, Introduction, Figure 1, Discussion, and Conclusion and avoid presenting the paper as a new coalition-theory contribution.

## 13. Reproducibility audit

Required gates:

- `make verify` — PASS.
- `make figures` — PASS.
- `make tables` — PASS.
- `make tables-check` — PASS.
- `make paper` — PASS.
- Symbolic verification — PASS.
- Analytical welfare sign certificates — PASS.
- Numerical verification — PASS.
- High-F stable-set regression — PASS.
- Intermediate-F stable-set regression — PASS.
- Market-size partner-selection regression — PASS.
- Citation/reference/duplicate-label gate — PASS.

The workflow now uploads the exact compiled manuscript PDF and log as a short-retention audit artifact so that visual review is performed on the same head that passed CI.

## 14. PDF visual audit

The exact-head CI PDF was rendered page by page and all 75 pages were inspected, with full-resolution checks of the title/abstract, Figure 1, Tables 1-3, Figures 2-3, the Main theorem pages, Appendix opening pages, low-F appendix, and bibliography.

No clipping, overlap, blank pages, broken glyphs, broken equations, unreadable figure/table overflow, extreme widow/orphan problem, or bibliography corruption was identified. A duplicated prose reference (“Appendix Appendix D”) was found in Section 7 during visual inspection and corrected before the final candidate build.

The only persistent LaTeX box warning before that one-line correction was a pre-existing `Overfull \\hbox` of approximately 2.22 pt associated with the Introduction/output routine. It is not visibly clipped in the rendered PDF. No underfull warnings remained.

## 15. IJIO scorecard

| Dimension | Score /10 | Audit view |
|---|---:|---|
| Research question clarity | 9 | Direct and mechanism-centered |
| Novelty | 7 | Distinct but narrow; close precedents are real |
| IO relevance | 8 | Firm conduct and Cournot stage are substantive |
| Standards-economics contribution | 8 | Clear formal/effective compatibility distinction |
| Coalition-formation contribution | 7 | Payoff feedback is useful; solution concept is conventional |
| Theoretical correctness | 9 | Reconstructed and independently verified |
| Main theorem strength | 7 | Exact stability reversal, but only on an existence/open-set region |
| Robustness / scope discipline | 9 | Strong restraint; no false robustness claims |
| Literature positioning | 9 | Source-level kill tests and claim controls are strong |
| Exposition | 8 | Clear but long in review mode |
| Figure/table quality | 8 | Functional and correctly scoped |
| Reproducibility | 10 | Symbolic, analytical, numerical, generated figures/tables, CI PDF |
| Referee defensibility | 8 | Major predictable attacks explicitly answered |
| IJIO fit | 8 | Good IO chain, though institutional endpoint creates some fit risk |

Total: **115/140 (8.21/10 average)**.

## 16. Journal strategy

### Primary — International Journal of Industrial Organization

- FIT: **GOOD / AMBITIOUS**.
- EXPECTED CONTRIBUTION BAR: strong mechanism novelty and clear IO relevance.
- MAIN RISK: the contribution is narrow relative to close standards/trade papers, and `Omega_0` is an existence region rather than a broad primitive characterization.

### Fallback 1 — Review of Industrial Organization

- FIT: **VERY GOOD**.
- EXPECTED CONTRIBUTION BAR: rigorous IO theory with a clear competition/policy mechanism.
- MAIN RISK: the international standards/coalition component may look more specialized than the journal's core IO audience, but the firm-conduct channel fits well.

### Fallback 2 — Journal of Industry, Competition and Trade

- FIT: **VERY GOOD**.
- EXPECTED CONTRIBUTION BAR: solid theory connecting firm behavior, competition, trade, and policy.
- MAIN RISK: positioning must avoid reading as abstract coalition theory.

### Fallback 3 — Review of International Economics

- FIT: **GOOD**.
- EXPECTED CONTRIBUTION BAR: meaningful theoretical contribution to trade/integration with real-world relevance.
- MAIN RISK: standards compatibility and IO structure must be connected clearly to economic integration rather than presented as purely institutional theory.

### Fallback 4 — The Manchester School

- FIT: **GOOD**.
- EXPECTED CONTRIBUTION BAR: significant, original, rigorous micro/game-theory contribution with reach beyond a very narrow application.
- MAIN RISK: its stated aversion to limited-scope work makes the narrow three-country implementation a possible objection.

### Fallback 5 — Journal of Economics

- FIT: **GOOD** for formal theory.
- EXPECTED CONTRIBUTION BAR: a clean theoretical mechanism with rigorous proof.
- MAIN RISK: less direct standards/IO audience than specialized alternatives.

### Fallback 6 — Economics of Governance

- FIT: **MODERATE-GOOD**.
- EXPECTED CONTRIBUTION BAR: formal analysis of interaction among governments/institutions and international agreements.
- MAIN RISK: the paper's strongest contribution is product-market/standards IO rather than governance theory.

### Fallback 7 — Bulletin of Economic Research

- FIT: **MODERATE**.
- EXPECTED CONTRIBUTION BAR: original and substantial theoretical work of broad interest.
- MAIN RISK: the mechanism may be too specialized for its broad-interest criterion.

### Fallback 8 — Economics Bulletin

- FIT: **TECHNICALLY POSSIBLE BUT FORMAT-MISMATCHED**.
- EXPECTED CONTRIBUTION BAR: original, correct result of specialist interest.
- MAIN RISK: the present full paper is far too long and would require a separate short-paper redesign. It is not the preferred fallback for the current manuscript.

## 17. Final submission recommendation

The audit does not support a theory HOLD and does not support abandoning IJIO. It also does not justify calling the paper risk-free or broadly novel.

Recommended decision:

**B — IJIO SUBMISSION PLAUSIBLE, MINOR REVISION NEEDED.**

The remaining risks are referee-facing rather than hidden technical defects:

1. narrow novelty relative to Takarada et al. and Gandal-Shy;
2. the existence/open-set nature of `Omega_0` rather than a full primitive characterization;
3. dependence of the applied stability theorem on strict blocking/no transfers;
4. review-mode length and front-end cognitive load;
5. the need to keep the IO causal chain prominent in editor-facing materials.

None of these should be addressed by adding an unverified extension before first submission. The correct strategy is disciplined positioning, a concise cover letter, and submission of the current mechanism-focused paper after the final CI/PDF hard gate.
