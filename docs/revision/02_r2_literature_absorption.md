# R2 — Theorem-Absorption and Prior-Art Map

## Status

**R2 LITERATURE ABSORPTION COMPLETE FOR THE G1 DECISION**

This is not the final paper-wide Stage-6/Stage-7 literature certificate. It is the R2-specific parent-theorem audit required before treating G1 as a new general theorem.

## Candidate result in application-neutral form

The strongest R2 common-cost statement is

\[
\max\{0,L_U(C)\}<F<U(C),
\]

where \(U(C)\) is the outsider's robust scope-adjusted gain from supporting the bloc standard and \(L_U(C)\) is the strongest reverse-adoption gain among bloc members.

The interval is nonempty iff

\[
U(C)>\max\{0,L_U(C)\}.
\]

For coalition expansion \(C\to C\cup\{h\}\), the feasibility slack rises iff

\[
\Delta_hU(C)>\Delta_hL_+(C).
\]

If the interval is nonempty both before and after expansion, this is also the condition for its length to rise; if the initial interval is empty, the increased slack must additionally cross zero.

The novelty audit asks whether these statements amount to more than known fixed-cost scope effects plus known one-way compatibility.

---

## Absorption matrix

| Prior work | Verified overlap | Mapping to G1 | Absorption verdict | Residual distinction |
|---|---|---|---|---|
| Gorman (1985), *Conditions for Economies of Scope in the Presence of Fixed Costs*, RAND Journal of Economics 16(3), 431–436, DOI 10.2307/2555569 | establishes necessary/sufficient conditions for economies of scope with fixed costs and local cost complementarity/anticomplementarity | common setup cost shared across outputs/markets is a classic source of scope economies | **PARTIALLY ABSORBED** | G1 is a strategic adoption game with asymmetric directions and a lower reverse-adoption threshold, not a cost-function theorem |
| Cho & McCardle (2009), *The Adoption of Multiple Dependent Technologies*, Operations Research 57(1), 157–169, DOI 10.1287/opre.1080.0534 | scope in fixed adoption costs can create economic dependence among technology-adoption decisions and can speed or delay adoption | directly weakens any claim that scope-dependent fixed adoption cost is new | **PARTIALLY ABSORBED** | G1 compares different strategic adopters and formal-standard scopes rather than timing multiple upgrades within one firm |
| Matutes & Régibeau (1989), *Standardization Across Markets and Entry*, Journal of Industrial Economics 37(4), 359–371 | standardization across multiple submarkets is a strategic choice; a standardized component can commit a firm to common pricing and affect entry scope | multi-market scope and standardization have long been jointly modeled | **PARTIALLY ABSORBED** | their mechanism is price commitment/entry deterrence, not post-coalition fixed-cost support of another standard |
| Buccella, Fanti & Gori (2023), *Strategic product compatibility in network industries*, Journal of Economics 140, 141–168, DOI 10.1007/s00712-023-00834-x | compatibility is a strategic Cournot choice with network effects and quasi-fixed compatibility costs; one-way compatibility can emerge | directly absorbs "fixed compatibility costs can generate one-way compatibility" as a novelty claim | **DIRECTLY ABSORBS THAT CLAIM** | no formal government bloc whose geographic scope creates the outsider-versus-reverse threshold comparison |
| Manenti & Somma (2008), *One-Way Compatibility, Two-Way Compatibility and Entry in Network Industries*, International Journal of the Economics of Business 15(3), 301–322, DOI 10.1080/13571510802465096 | one-way converters and asymmetric compatibility equilibria under property-right/side-payment structures | directly absorbs "one-way compatibility can be an equilibrium" as a novelty claim | **DIRECTLY ABSORBS THAT CLAIM** | different mechanism; no common setup-cost scope comparison tied to a formal standards coalition |
| van Wegberg (2004), *Compatibility choice by multi-market firms*, Information Economics and Policy 16(2), 235–254, DOI 10.1016/j.infoecopol.2003.09.011 | explicitly argues and models that changing a firm's multi-market/product-market scope changes its preference for compatibility | directly threatens any qualitative claim "larger multi-market scope changes compatibility incentives" | **STRONG PARTIAL ABSORPTION** | G1 separates the outsider upper threshold from the strongest reverse-adoption lower threshold under an institutionally fixed bloc |
| Rutenberg & Shaftel (1971), *Product Design: Subassemblies for Multiple Markets*, Management Science 18(4), B220–B231, DOI 10.1287/mnsc.18.4.B220 | multi-market standard-module problem with a module fixed cost plus a separate fixed cost when the module is used in a market | closely anticipates the cost architecture \(F+\sum f_k\) | **PARTIALLY ABSORBS COST ARCHITECTURE** | no strategic compatibility/adoption game or government coalition |
| Chen, Otsuki & Wilson (2006), *Do Standards Matter for Export Success?*, World Bank Policy Research Working Paper 3809 | models standards-related fixed compliance costs across export destinations and market diversification | standards compliance and destination-specific fixed costs are established trade mechanisms | **PARTIALLY ABSORBED** | does not study a single bloc standard chosen after a formal coalition and strategic reverse compatibility |

---

## Required mapping

### G1-E

**Candidate:** outsider-only adoption is a strict equilibrium when the outsider's adoption gain is positive and every member's unilateral reverse-adoption gain is negative.

**Canonical form:** binary-action Nash inequalities.

**Closest prior class:** generic finite games plus costly compatibility games.

**Verdict:** DIRECTLY ABSORBED AS GAME-THEORETIC LOGIC.

**Residual value:** bookkeeping/certification, not theorem novelty.

### G1-U

**Candidate:** robust gain bounds make outsider adoption and member non-adoption strict dominant actions, yielding a unique equilibrium.

**Canonical form:** strict dominance in a finite binary-action game.

**Closest prior class:** elementary dominance theorem.

**Verdict:** DIRECTLY ABSORBED AS GAME-THEORETIC LOGIC.

**Residual value:** ensures selection-free continuation for the economic mechanism.

### Common-\(F\) scope-dominance condition

**Candidate:**

\[
U(C)>\max\{0,L_U(C)\}.
\]

**Canonical form:** one shared setup cost lies between an outsider upper threshold and a reverse-adoption lower threshold.

**Closest prior classes:** fixed-cost economies of scope; multi-market compatibility; costly one-way compatibility.

**Verdict:** PARTIALLY ABSORBED.

**Residual candidate:** the institutional directionality — one formal bloc standard aggregates the outsider's gains across the bloc while reverse support targets the outsider standard — creates two distinct endogenous thresholds under the same setup cost.

This residual is too narrow to be a standalone headline contribution at R2.

### Scope expansion result

**Candidate:**

\[
S(C\cup\{h\})-S(C)
=
\Delta_hU(C)-\Delta_hL_+(C).
\]

**Canonical form:** scope expansion changes both the adopter's upper threshold and the strongest counter-adopter threshold; their difference is a feasibility slack, not an interval length unless it is positive.

**Closest prior class:** van Wegberg (2004) plus general multi-market scope theory.

**Verdict:** PARTIALLY ABSORBED / RESIDUAL CONDITION RETAINED.

The specific two-threshold decomposition is useful for R3 because it identifies when coalition expansion actually widens the region producing the asymmetric continuation state. No global priority claim is authorized.

---

## R2 novelty verdict

\[
\boxed{
\text{G1 is mathematically valid but not certified as a standalone novel general theorem.}
}
\]

Classification:

**SUPPORTING STRUCTURAL LEMMA — HIGH PRIOR-ART OVERLAP**

The route remains open only because the R2 condition can be combined with the R3 government-incentive mechanism. The paper should not be repositioned around "general one-way adoption" or "economies of scope in compatibility."

No "first" claim is authorized.

---

## Identifiers used for this R2 audit

- Gorman (1985): DOI 10.2307/2555569
- Cho & McCardle (2009): DOI 10.1287/opre.1080.0534
- Matutes & Régibeau (1989): Journal of Industrial Economics 37(4), 359–371; DOI commonly indexed as 10.2307/2098373
- Buccella, Fanti & Gori (2023): DOI 10.1007/s00712-023-00834-x
- Manenti & Somma (2008): DOI 10.1080/13571510802465096
- van Wegberg (2004): DOI 10.1016/j.infoecopol.2003.09.011
- Rutenberg & Shaftel (1971): DOI 10.1287/mnsc.18.4.B220
- Chen, Otsuki & Wilson (2006): World Bank Policy Research Working Paper 3809
