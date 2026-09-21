# R6 — Coalition-Stability Robustness: Design Freeze

## Status

- Stage: R6
- Branch: `revision/r6-execution`
- Input integration commit: `191e3f7a7ad893dc8892c8858d0008a45b216099`
- Governing workflow: `research-paper-workflow v2.2 @ 42574d6c5931275ccff3ef7e8b4acc188077332a`
- Purpose: separate robust government preference effects from institution-dependent stable-set conclusions
- Production manuscript: **frozen; no edits in R6**
- R7 and later stages: **out of scope**

This file freezes the institutional tests required by the R0–R9 revision plan before R6 calculations are used for conclusions.

## 1. Formal partitions and deviations

The institutional menu remains exactly

[
mathcal P=
{ho^{SW},ho_{12}^{SU},ho_{13}^{SU},ho_{23}^{SU},ho^{IS}}.
]

A deviating coalition (Ssubseteq{1,2,3}), (S
earnothing), forms one coalition containing exactly the deviators. Members of each pre-existing coalition who do not deviate remain together as the residual coalition when its size is at least two; singleton residuals remain singleton.

Thus, for example:

- from (ho^{IS}), deviation by ({1,2}) induces (ho_{12}^{SU});
- from (ho^{IS}), deviation by ({3}) also induces (ho_{12}^{SU}), with country 3 as the outsider;
- from (ho_{12}^{SU}), deviation by ({1,3}) induces (ho_{13}^{SU});
- from (ho_{12}^{SU}), deviation by ({1}) induces (ho^{SW}).

No non-deviator consent is required to preserve its residual coalition. Accession to a new coalition requires every member of that new coalition to be a deviator.

After every induced partition, the private-adoption game is **re-solved from scratch**. Adoption expenditures are not sunk across institutional comparisons. R6 remains a static continuation-payoff comparison, not a dynamic renegotiation model.

## 2. Blocking concepts

R6 compares exactly two concepts.

### S — strict blocking

A coalition (S) blocks partition (ho) through induced partition (ho') iff

[
W_i(ho')>W_i(ho)
qquad	ext{for every }iin S.
]

This is the canonical paper rule.

### W — weak/Pareto blocking

A coalition (S) blocks partition (ho) through (ho') iff

[
W_i(ho')ge W_i(ho)
qquad	ext{for every }iin S
]

and at least one deviator is strictly better off.

No third coalition concept will be added in R6.

## 3. Firm-adoption continuation rule

R6 uses the canonical full-bypass technology and the already certified selection-free fixed-cost regions.

### High fixed cost

[
F>2T_A.
]

No private adoption occurs under any SU or SW continuation.

### Intermediate fixed cost

[
F_L<F<2T_A,
qquad
F_L=max{T_W,T_A}.
]

In the symmetric baseline, every SU has the selection-free outsider-only adoption continuation and SW has no private adoption.

Under market-size asymmetry, the adoption game is rechecked partition by partition. R6 does not assume that the symmetric fixed-cost classification automatically survives.

If a continuation is multiple for any tested parameter point, R6 will report the payoff correspondence rather than select an equilibrium ad hoc. The pre-specified exact witnesses below are chosen only if the adoption continuation is selection free.

## 4. Symmetric institutional audit

For every ((c,v)inOmega_0), test both blocking concepts in:

1. the high-(F) region;
2. the intermediate-(F) region.

The canonical preference inequalities already certified may be reused, but the stable set must be independently reconstructed by enumerating all coalition deviations.

The audit must identify which stability conclusions rely on:

- strict preference differences; versus
- symmetry-induced indifference.

In particular, the alternative-SU deviations must not be dismissed without checking whether the common member is indifferent and the former outsider strictly gains.

## 5. Small market-size asymmetry

Use the already specified secondary market-size perturbation:

[
m_1=m_2=1,
qquad
m_3=1-delta,
qquad
0<delta<1.
]

No other asymmetry is introduced.

For an SU with members (i,j) and outsider (o), write (M_C=m_i+m_j).

### No-bypass continuation

[
W_i^{SU,N}
=
m_iK_M+M_CA+m_oC,
]

[
W_o^{SU,N}
=
m_oK_O+M_CB+m_oD.
]

### Outsider-only bypass continuation

[
W_i^{SU,O}
=
m_iK_I+M_CP+m_oC,
]

[
W_o^{SU,O}
=
m_oK_O+M_CP+m_oD-F.
]

### International standardization

[
W_i^{IS}
=
m_iK_I+(m_1+m_2+m_3)P.
]

### Separate national standards

[
W_i^{SW}
=
m_iK_W+m_iH+sum_{k
e i}m_kS.
]

R6 must prove local robustness around (delta=0) where possible and provide exact rational witnesses. A numerical grid alone is not a proof.

## 6. Pre-specified exact witnesses

Use the canonical interior point

[
(c,v)=left(rac1{10},rac6{25}ight).
]

High-(F) witness:

[
F_H=rac15.
]

Intermediate-(F) witness:

[
F_I=rac3{25}.
]

For asymmetry checks use

[
delta=rac1{100}
]

as the primary exact witness. Analytic interval results may be stronger, but the specification will not be changed if the witness fails.

## 7. Required R6 questions

R6 must answer separately:

1. What is the stable set under strict blocking in the symmetric high-(F) region?
2. What is the stable set under weak/Pareto blocking in the symmetric high-(F) region?
3. What is the stable set under each blocking rule in the symmetric intermediate-(F) region?
4. Which high-(F) stability result is driven by symmetry-induced indifference?
5. Does a small (m_3<1) perturbation select a regional partner, restore stability under weak blocking, or destroy all regional stability?
6. Does the intermediate-(F) unique-IS result survive the same small asymmetry and both blocking concepts?
7. Are the required private-adoption continuations selection free after every tested deviation?
8. Is any welfare conclusion only a finite-institutional-set Pareto ranking rather than an unrestricted first-best statement?

## 8. Stop conditions

R6 is an institutional robustness audit, not a search for a preferred coalition concept.

Not permitted:

- changing the product-market primitives;
- changing the private-adoption technology;
- adding transfer payments;
- introducing farsighted or dynamic coalition formation;
- treating past adoption costs as sunk after a deviation;
- redesigning the deviation rule after observing the stable set;
- moving to R7 before R6 is closed.

If the stable set is empty under one blocking rule, that is an admissible R6 result and must not be repaired by changing the rule.

## 9. Completion gate

R6 can close only after:

- all five formal partitions and all nonempty deviating coalitions are enumerated;
- strict and weak/Pareto blocking are both checked;
- symmetry-induced indifference is isolated explicitly;
- the specified market-size asymmetry is analyzed with adoption re-solved after deviations;
- exact witnesses and analytic/local robustness results are recorded;
- theorem ledger and revision-track status are updated;
- R6 verification is added to CI;
- a PR to `revision/research-track` passes full CI;
- the PR is squash-merged;
- post-merge integration CI passes.

R6 closure does not authorize production-manuscript rewriting. R7 remains the theory re-certification gate.
