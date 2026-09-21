# R7 — Novelty Reassessment

## Verdict

**LIMITED NOVELTY SURVIVES — ROUTE B CANDIDATE**

Input state:

- repository: `ryotamatsuki/private-compatibility-standards-coalitions`
- integration input: `b45798f003db52a980f8f9b21186f054ebe62007`
- execution branch: `revision/r7-execution`
- workflow: `research-paper-workflow v2.2 @ 42574d6c5931275ccff3ef7e8b4acc188077332a`

This audit evaluates the actual R2–R6 results rather than the original institutional labels. It does not authorize a "first" claim.

## 1. Main conclusion

The revision does **not** support a broad new theorem that private compatibility generally induces broader public standardization.

The strongest defensible contribution is narrower:

> In the canonical three-country Cournot microfoundation, private outsider adaptation can change a member government's relative preference for multilateral standardization. With incomplete cost relief, the sign is governed by an equilibrium-derived residual-rent term. The model therefore provides explicit success, intermediate, and failure regions. This political preference effect is materially specification dependent: it fails in the pre-specified differentiated-demand portability model even though one-way private adoption survives.

This is a **conditional mechanism result**, not a general compatibility theorem.

## 2. Proposition-level absorption map

| Revision result | Closest parent literature | Absorption verdict | R7 contribution status |
|---|---|---|---|
| G1-E / G1-U: outsider-only adoption and selection-free dominance conditions | Farrell–Saloner converters; Manenti–Somma one-way compatibility; Buccella–Fanti–Gori endogenous compatibility | **PARTIALLY / SUBSTANTIALLY ABSORBED** | supporting lemma only |
| G1-S: common fixed-cost scope changes adoption slack | Gorman fixed-cost economies of scope; Cho–McCardle dependent technology adoption | **SUBSTANTIALLY ABSORBED AS PARENT-CLASS LOGIC** | not a standalone novelty claim |
| G1-C / G1-O: asymmetric adopter cost and optional deployment qualifications | generic adoption/real-option and fixed-cost scope logic | **PARTIALLY ABSORBED** | robustness bookkeeping |
| G2-L: reversal survives positive residual marginal adaptation cost | converter/compatibility literature has partial compatibility; standards-policy literature has government incentives | **NOT DIRECTLY ABSORBED, BUT MODEL-SPECIFIC** | surviving result |
| G2-S: residual-rent thresholds separate reversal, strengthening-only, and weakening | no located parent theorem reproduces this exact government-ranking partition from private adaptation | **NOT DIRECTLY ABSORBED, BUT MODEL-SPECIFIC** | principal surviving result |
| G2-J: incomplete adoption + selection-free firm equilibrium + preference reversal coexist on an open set | closest literatures contain the ingredients separately | **NOT DIRECTLY ABSORBED, BUT MODEL-SPECIFIC** | joint feasibility certificate |
| N1–N7 | baseline/network/specification diagnostics | not a separate parent-theorem contribution | scope/failure results |
| R5 negative portability | differentiated competition / compatibility literature | not a novelty theorem; a falsification/scope result | essential limit on G2 |
| R6 strict-vs-weak/asymmetry results | coalition formation/core literature | blocking-rule sensitivity is standard in parent class | institutional robustness/scope, not headline novelty |

## 3. Strong antecedents

### Private converters and one-way compatibility

Farrell and Saloner's converter analysis establishes that private conversion technologies can alter equilibrium compatibility and need not improve welfare. Farrell and Simcoe later systematize converters/multihoming as one of several alternative paths to compatibility.

Manenti and Somma explicitly derive one-way and two-way compatibility outcomes. Buccella, Fanti and Gori analyze endogenous compatibility under Cournot competition, network effects, and quasi-fixed compatibility costs, including asymmetric compatibility regimes.

**R7 implication:** one-way compatibility or one-way private adoption cannot be presented as a new theoretical phenomenon.

### Fixed-cost scope and dependent adoption

Gorman gives general conditions for economies of scope in the presence of fixed costs. Cho and McCardle show how economies or diseconomies of scope in fixed adoption costs create interdependence among multiple technology-adoption decisions.

**R7 implication:** the R2 scope result is useful for organizing this model but is not an independent theorem-level novelty claim.

### Standards policy and formal harmonization

Gandal and Shy study government standards policy, conversion costs, network effects, and standardization unions. Takarada and related standards-policy work compare regional and multilateral standards arrangements and coalition stability. Kawabata/Takarada work likewise studies regional versus deeper multilateral harmonization in oligopoly settings.

Schmidt and Steingress model costly firm adoption of harmonized standards and quantify how harmonization changes firms' adoption incentives and trade.

**R7 implication:** neither government standards coalitions nor endogenous firm adoption of harmonized standards is new by itself.

### Private adaptation versus formal agreements

Farrell and Simcoe emphasize that decentralized compatibility, converters, and formal standard setting can be substitutes or complements. Maggi and Mrázová study fixed costs of regulatory diversity, spontaneous harmonization, and the residual role for formal international agreements.

Related political-economy work (including Barrett–Yang and Suwa Eisenmann–Verdier) shows that adaptation/redesign costs and network effects can affect government incentives toward international standards or regulatory harmonization.

**R7 implication:** the broad question "can private adaptation substitute for formal cooperation?" is occupied. The surviving paper-specific contribution must be the **conditional sign structure** generated by the canonical model, not the broad question.

## 4. Why G2 is not fully absorbed

The search did not locate a prior theorem with the same full mapping:

[
	ext{private outsider adaptation}
ightarrow
R(d)
ightarrow
egin{cases}
R(d)<mathscr D & 	ext{preference reversal},\
mathscr D<R(d)<mathscr E & 	ext{IS incentive strengthens but no reversal},\
R(d)>mathscr E & 	ext{IS incentive weakens}.
end{cases}
]

The novelty is therefore not the existence of converters, fixed costs, network effects, public standards, or coalition formation individually. It is the equilibrium-derived decomposition that identifies when a private workaround erodes enough of a regional member's rent to move its **government** toward or away from multilateral standardization.

However, R5 proves that the sign of the member-market term is not portable to the single pre-specified differentiated-demand environment. In both R5-C and R5-B,

[
mathscr E^X<0
]

throughout the audit box. Thus the G2 sign structure cannot be advertised as a general result across demand/competition microfoundations.

The correct classification is:

[
oxed{	ext{NOT DIRECTLY ABSORBED, BUT MODEL-SPECIFIC}}
]

rather than structurally general theorem novelty.

## 5. Whole-game absorption judgment

No single located predecessor reproduces the full game consisting of:

1. governments choosing among SW/SU/IS formal partitions;
2. firms privately adding standards at a reusable fixed cost;
3. an outsider-only adoption continuation;
4. a government preference decomposition before and after adoption;
5. an incomplete-adaptation residual-rent threshold;
6. a resulting institutional stability comparison.

This prevents a verdict of **direct whole-game absorption**.

But the ingredients are heavily occupied individually, and the new interaction does not survive the R5 portability test. Therefore the contribution cannot be defended merely as a new general architecture.

## 6. Killed claims

The following claims are not authorized for R8:

- "one-way private compatibility is novel";
- "fixed-cost scope creates a new adoption theorem";
- "private compatibility generally promotes international standardization";
- "the preference reversal is competition-form independent";
- "the mechanism does not depend materially on the demand/network microfoundation";
- "network effects are irrelevant to the political result";
- "the high-F three-SU stable set is robust to coalition rules";
- any "first paper to show" formulation unsupported by a substantially stronger literature audit.

## 7. Surviving contribution set

R8 may build around four levels, in descending order of importance.

1. **Conditional government-incentive mechanism.**  
   The canonical model derives an exact residual-rent condition that separates preference reversal, incentive strengthening without reversal, and incentive weakening.

2. **Non-knife-edge robustness within the canonical microfoundation.**  
   Full elimination of the adaptation cost is unnecessary: a nonempty open set with (0<lambda<1) retains selection-free outsider adoption and actual reversal.

3. **Explicit failure and specification boundaries.**  
   Zero-network, singleton-network, and differentiated-demand tests identify where the political result fails, while private one-way adoption can survive.

4. **Institutional application.**  
   Under the canonical continuation, intermediate-F unique IS stability is supported by strict payoff differences and is more robust than the exact symmetric high-F stable-set correspondence.

## 8. Novelty classification

The surviving novelty is primarily:

- **economic/application-level:** linking private technical adaptation to governments' relative incentives over formal standardization regimes;
- **integrative:** combining firm adoption and government coalition incentives in one sequential structure;
- **conditional mathematical characterization:** exact residual-rent success/failure thresholds inside the canonical microfoundation.

It is **not** a broad new theorem on fixed-cost adoption, compatibility, or coalition formation.

## 9. Route implication

R2 generalizes the firm-adoption logic beyond the original factor-two threshold, but high prior-art overlap prevents that from carrying the paper as a new general theory.

R3 adds more than local continuity: it provides exact thresholds and a nonlocal open witness with incomplete adaptation. This is enough to avoid Route C.

R4 and especially R5 show that the political preference effect remains tied to restrictive market structure. This rules out Route A.

No mathematical failure or complete prior-art absorption has been found, so Route D is not warranted.

Accordingly the R7 novelty audit supports:

[
oxed{	ext{Route B — LIMITED GENERALIZATION}}
]

subject to completion of clean-room and formal recertification.

## 10. Literature evidence status

This R7 search used proposition- and mechanism-level searches across the standards, compatibility, technology-adoption, regulatory-harmonization, and coalition-formation literatures. Bibliographic and abstract/model-level evidence was sufficient to kill broad novelty claims and identify parent classes.

It does not claim exhaustive proof that no unpublished or obscure theorem duplicates G2. The defensible statement is narrower: among the strongest located parent classes and closest papers, no direct theorem absorption of the full G2 residual-rent government-ranking result was identified.

No priority/"first" claim is certified.
