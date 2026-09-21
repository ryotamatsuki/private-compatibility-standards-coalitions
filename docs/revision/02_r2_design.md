# R2 Design Freeze — General Conditions for One-Way Adoption

## Status

**R2 DESIGN FROZEN — EXECUTED; CONDITIONAL GO TO R3**

This document fixes the first R2 model family, candidate propositions, novelty tests, search budget and stop rules. Changing them after substantive derivation begins requires an explicit design amendment.

## Research question

Can outsider-only private standard adoption be derived from economically interpretable scope/cost/competition conditions rather than from the baseline three-country arithmetic \(F<2T_A\)?

## What R2 is not allowed to establish by definition

R2 does not count as progress if it only states:

> the outsider adopts when its net gain is positive and members do not adopt when theirs is negative.

That is an equilibrium condition, not an economic explanation.

R2 must explain why a strict interval with asymmetric incentives exists, or identify why it fails.

## R2 model family

### Formal standard scope

Let \(C\) be a nonempty set of markets governed by one formal bloc standard \(s_C\), and let \(o\) denote an outsider market governed by \(s_o\).

Formal membership is fixed during the private-adoption game.

### Firms and adoption actions

- outsider firm \(o\): \(a_o\in\{0,1\}\), where \(a_o=1\) means support \(s_C\);
- each bloc-member firm \(i\in C\): \(a_i\in\{0,1\}\), where \(a_i=1\) means support \(s_o\).

Supporting an additional standard does not change formal coalition membership.

### Product-market continuation

Markets are segmented in the first R2 model. For each destination \(k\), adoption profile \(a\), and relevant product-market equilibrium \(e\), define operating profit

\[
\pi_j^k(a;e).
\]

Where the product-market equilibrium is unique, suppress \(e\). Where it is multiple, continuation value is a correspondence unless an independently justified selection rule is stated.

R2 does **not** assume Cournot, linear demand, or the old \(A,B,C,P\) blocks at the generic-theory stage.

Worldwide operating profit is the sum of destination profits. Cross-market coupling in the baseline R2 family comes through the adoption technology/cost rather than product-market demand.

This segmentation restriction is explicit. It is a first generalization step, not a claim about arbitrary multi-market games.

### Adoption benefit

For each adopter \(j\),

\[
B_j(a_{-j};C)
=
\sum_k
\left[
\pi_j^k(1,a_{-j})-\pi_j^k(0,a_{-j})
\right].
\]

Net adoption gain is

\[
\Delta_j(a_{-j};C)
=
B_j(a_{-j};C)-K_j(a_{-j};C).
\]

### Cost family

First cost specification:

\[
K_o(C)=F_o+\sum_{k\in C}f_{ok},
\]

\[
K_i(o)=F_i+f_{io}.
\]

\(F_j\) is standard-level setup/certification/design cost. \(f_{jk}\) is destination-specific implementation cost.

The baseline R2 specification interprets adoption as a package that implements the supported standard across the defined covered-market set. R2 will **not** silently extend this result to cases where a firm may avoid \(f_{jk}\) by declining deployment in market \(k\).

A mandatory scope test will therefore add an optional deployment/market-participation variant. If avoiding individual \(f_{jk}\) materially changes the scope result, that is a boundary of G1 rather than a nuisance to be designed away.

## Candidate results

### G1-E — profile-specific strict equilibrium

For the outsider-only candidate \(a_o=1,\;a_i=0\) for all \(i\in C\), establish the exact no-deviation inequalities.

A sufficient strict-equilibrium condition is:

\[
\Delta_o(a_C=0;C)>0
\]

and, for every \(i\in C\),

\[
\Delta_i(a_o=1,a_{C\setminus\{i\}}=0;C)<0.
\]

This proves a strict Nash equilibrium only. It does not prove uniqueness.

### G1-U — selection-free unique outsider-only adoption

Test stronger robust conditions:

\[
\inf_{a_{-o}}\Delta_o(a_{-o};C)>0,
\]

\[
\sup_{a_{-i}}\Delta_i(a_{-i};C)<0
\qquad\forall i\in C.
\]

If the infimum/supremum are over the full finite adoption-action space and these inequalities are strict, outsider adoption and each member's non-adoption are strict dominant actions. The outsider-only action profile is then the unique Nash equilibrium, including exclusion of non-degenerate mixed equilibria.

The proof must explicitly state the strategy space over which the bounds are taken.

### Common-\(F\) representation

Only when a common standard-level fixed cost \(F\) is substantively justified, define variable-cost-adjusted robust benefits

\[
\underline G_o(C)
=
\inf_{a_{-o}}
\left[
B_o(a_{-o};C)-\sum_{k\in C} f_{ok}
\right],
\]

\[
\overline G_i
=
\sup_{a_{-i}}
\left[
B_i(a_{-i};C)-f_{io}
\right].
\]

Then the robust unique-adoption interval is

\[
\max_{i\in C}\overline G_i
<
F
<
\underline G_o(C).
\]

The research content is not this algebra. R2 must derive conditions under which

\[
\underline G_o(C)
>
\max_{i\in C}\overline G_i
\]

holds for a meaningful model family.

### G1-S — discrete scope comparative static

Coalition scope is discrete. For a candidate additional market \(k\notin C\), use

\[
\Delta_k\underline G_o(C)
=
\underline G_o(C\cup\{k\})-\underline G_o(C).
\]

Do not write \(\partial/\partial |C|\) unless a separate continuous scope/market-size variable is introduced.

The first target is a sufficient condition for \(\Delta_k\underline G_o(C)>0\) that includes:

- additional operating-profit gain in market \(k\);
- destination-specific incremental implementation cost;
- any effect of the enlarged adoption target on profit in markets already in \(C\).

If the segmented continuation makes the last interaction exactly zero, state that explicitly. Construct or identify a model variant in which the interaction is negative enough to reverse monotonicity. "Larger bloc → more adoption" is therefore a conditional result, not a maintained assumption.

### G1-C — cost asymmetry

Permit \(F_o\neq F_i\). Determine whether one-way adoption survives under an interpretable robust gain-cost ordering. Do not force common \(F\) solely to recover the old result.

## Mapping to the old model

Under the submitted three-country symmetric Cournot model:

- outsider adoption of the two-market bloc gives gross operating-profit gain \(2(P-B)=2T_A\);
- a member's unilateral reverse adoption gives \(A-C=T_U\);
- a member adopting after the other member gives \(P-B=T_A\).

The old intermediate-\(F\) region is therefore a specialization of the R2 action logic. R2 must show what part of that structure survives when the exact Cournot blocks are removed.

## Pre-registered hypotheses

- **H2.1:** a nonempty outsider-only adoption region can be generated by scope/common-cost structure rather than by the number "2" in the three-country model.
- **H2.2:** expanding bloc scope raises outsider adoption attractiveness only under a discrete marginal-benefit condition; monotonicity is not universal.
- **H2.3:** adopter-specific fixed costs need not eliminate one-way adoption if strict gain-cost ordering survives.
- **H2.4:** optional market deployment can weaken or eliminate the scope advantage; this is a required boundary test.
- **H2.5:** the generic adoption result may be absorbed by established economies-of-scope/fixed-cost adoption theory. If so, classify G1 as application-level rather than theorem novelty.

## Existence versus uniqueness target

R2 targets **both**, but as separate results:

1. first derive the exact conditions for outsider-only adoption to be a strict equilibrium (G1-E);
2. only then test stronger dominance conditions for a selection-free unique equilibrium (G1-U).

If G1-U fails but G1-E survives, the project may continue only with explicit equilibrium-selection/multiplicity treatment.

## Parent-theorem absorption tests

Before calling G1 new, map the application-neutral result against at least:

- Gorman (1985), fixed costs and economies of scope;
- Cho & McCardle (2009), dependent technology adoption and scope in adoption cost;
- Matutes & Régibeau (1989), standardization across markets;
- Buccella, Fanti & Gori (2023), strategic compatibility with quasi-fixed costs;
- Manenti & Somma (2008), one-way compatibility.

Required output:

`candidate G1 statement → canonical mathematical form → closest parent theorem/model → mapping → residual novelty, if any`.

Absorption by prior theory is not a failed research stage; it is a result that changes the contribution classification.

## Search / model budget

R2 is limited to:

1. the generic segmented-market adoption model above;
2. one common-plus-incremental-cost specialization;
3. one optional-deployment/market-participation boundary test if needed;
4. mapping back to the old Cournot model;
5. theorem-absorption audit.

Not permitted inside R2:

- differentiated Bertrand;
- residual/partial compatibility parameter \(\lambda\);
- dynamics/sunk renegotiation;
- new coalition solution concepts;
- repeated addition of parameters to manufacture a successful region.

Those belong to later stages if authorized.

## R2 stop rules

### GO toward R3

At least one of the following must hold with evidence:

- a nonempty strict outsider-only region is derived from interpretable primitive restrictions and produces a scope/failure condition not reducible to a sign definition; or
- the generic theorem is known/absorbed, but its application yields a genuinely new restriction that becomes economically operative in R3.

### CONDITIONAL GO

G1-E is established but uniqueness or scope monotonicity is unresolved, and the limitation can be isolated without changing the model family.

### NO-GO for substantive generalization

Stop expansion and move toward Route C if:

- G1 is only "positive net gain implies adoption";
- nonempty asymmetry is inserted directly as an assumption with no underlying explanation;
- all claimed scope content is a direct standard economies-of-scope corollary with no residual prediction useful for R3;
- the only way to obtain the desired result is repeated unregistered model alteration.

### UNRESOLVED

Use this, not a negative theorem, when proof, equilibrium characterization, or search coverage remains incomplete.

## Preliminary formal-verification mapping

Formal verification remains `PRELIMINARY APPLICABLE`.

Potential proof-critical targets if G1 survives:

- dominance inequalities imply unique equilibrium;
- common-\(F\) interval equivalence;
- joint parameter-region nonemptiness when R3 is added;
- boundary/threshold ordering.

No proof-assistant implementation is authorized until R2/R3 theorem statements stabilize and R7 reassesses applicability.


## Execution closure

R2 was executed without changing the pre-registered model/search budget. Results are in `02_r2_results.md`; theorem-absorption mapping is in `02_r2_literature_absorption.md`; verification code is `code/revision/check_r2_adoption.py`. The outcome is **CONDITIONAL GO TO R3**: the adoption theory is valid and yields an operative scope-versus-reverse-incentive condition, but G1 has high prior-art overlap and is not a standalone headline contribution.
