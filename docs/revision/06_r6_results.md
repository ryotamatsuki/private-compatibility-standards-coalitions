# R6 — Preference Effects versus Coalition Stability

## Verdict

**R6 COMPLETE — INSTITUTIONAL DEPENDENCE IDENTIFIED; GO TO R7**

Input integration state:

- branch: `revision/research-track`
- input commit: `191e3f7a7ad893dc8892c8858d0008a45b216099`
- execution branch: `revision/r6-execution`
- governing workflow: `research-paper-workflow v2.2 @ 42574d6c5931275ccff3ef7e8b4acc188077332a`

R6 changes research records and verification only. The production manuscript remains frozen.

The main R6 conclusion is a separation result. The canonical government preference reversal in the intermediate-(F) region is supported by strict payoff differences and is robust to both blocking concepts tested here and to small market-size asymmetry. By contrast, the symmetric high-(F) claim that all three regional standards unions are stable depends on the strict-blocking convention: under weak/Pareto blocking the symmetric high-(F) stable set is empty because alternative regional coalitions can block through one indifferent common member and one strictly improving former outsider.

A small pre-specified market-size asymmetry breaks that indifference. With (m_1=m_2=1) and (m_3=1-delta), the two larger countries select (SU_{12}); for sufficiently small (delta>0), (SU_{12}) is uniquely stable under **both** blocking rules. Thus the three-SU multiplicity is not robust, but regional stability itself is not destroyed by the stronger blocking rule once the symmetry knife edge is removed.

---

## 1. Coalition-formation rules

The institutional menu is

[
mathcal P=
{ho^{SW},ho_{12}^{SU},ho_{13}^{SU},ho_{23}^{SU},ho^{IS}}.
]

A deviating coalition forms one coalition containing exactly its members. Non-deviators who belonged to the same old coalition remain together as the residual coalition. Firm adoption is re-solved after every induced partition. No adoption expenditure is treated as sunk across institutional comparisons.

Two blocking concepts are tested.

### Strict blocking

A coalition (S) blocks (ho) through (ho') iff

[
W_i(ho')>W_i(ho)
quad	ext{for every }iin S.
]

### Weak/Pareto blocking

A coalition (S) blocks iff

[
W_i(ho')ge W_i(ho)
quad	ext{for every }iin S
]

and at least one deviator is strictly better off.

These are the only coalition concepts used in R6.

---

## 2. Symmetric high-(F) region

Take ((c,v)inOmega_0) and

[
F>2T_A.
]

No private adoption occurs under SU or SW.

The certified symmetric rankings are

[
W_M^{SU,N}>W^{IS}>W_O^{SU,N}
]

and

[
W_M^{SU,N}>W^{SW}.
]

### 2.1 Strict blocking

The legacy result is reproduced:

[
oxed{
mathcal S_S(F)
=
{ho_{12}^{SU},ho_{13}^{SU},ho_{23}^{SU}}.
}
]

SW is blocked by a two-country SU, and IS is blocked by a two-country SU.

Consider (SU_{12}). A deviation by ({1,3}) to (SU_{13}) gives country 1 exactly the same member payoff and moves country 3 from outsider to member:

[
W_1^{13,N}-W_1^{12,N}=0,
]

[
W_3^{13,N}-W_3^{12,N}
=
W_M^{SU,N}-W_O^{SU,N}>0.
]

Because country 1 is not **strictly** better off, this deviation does not strictly block. The same argument applies cyclically to all three SUs.

### 2.2 Weak/Pareto blocking

Under weak/Pareto blocking, the same deviation **does** block (SU_{12}): country 1 weakly improves by equality, while country 3 strictly improves.

Hence every symmetric SU is blocked by an alternative SU.

SW remains blocked by an SU, and IS remains strictly blocked by an SU. Therefore

[
oxed{
mathcal S_W(F)=arnothing.
}
]

This is an exact empty-stable-set result, not a failure to find a stable partition.

### 2.3 What drives the difference

The difference between the two concepts is entirely the symmetry-induced equality of the common member's payoff across alternative regional partners.

The strict member-versus-IS preference

[
W_M^{SU,N}>W^{IS}
]

is not an indifference artifact. The **stability** of each particular symmetric SU under strict blocking is.

---

## 3. Symmetric intermediate-(F) region

Now take

[
F_L<F<2T_A.
]

The continuation is selection free: each SU outsider alone adopts the bloc standard and SW has no adoption.

For a member,

[
W^{IS}-W_M^{SU,O}
=
P-C
=
mathscr D>0.
]

For the outsider,

[
W^{IS}-W_O^{SU,O}
=
J+F>0.
]

Thus every country strictly prefers IS to the continuation under any SU.

Also

[
W^{IS}>W^{SW}.
]

Therefore every SU and SW are strictly blocked by the grand coalition. Conversely, from IS:

- a two-country deviation to an SU makes both deviators SU members and strictly worse off;
- a singleton deviation from IS makes that country the outsider to the residual SU and strictly worse off;
- the grand coalition reproduces IS.

Hence the result is identical under both blocking concepts:

[
oxed{
mathcal S_S(F)
=
mathcal S_W(F)
=
{ho^{IS}}.
}
]

Unlike the symmetric high-(F) result, this conclusion is supported by strict payoff gaps throughout the relevant deviation comparisons.

---

## 4. Small market-size asymmetry

Set

[
m_1=m_2=1,
qquad
m_3=1-delta,
qquad
0<delta<1.
]

No product-market primitive is changed.

For a no-bypass SU with members (i,j), outsider (o), and (M_C=m_i+m_j),

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

For outsider-only bypass,

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

IS gives

[
W_i^{IS}
=
m_iK_I+(m_1+m_2+m_3)P.
]

SW gives

[
W_i^{SW}
=
m_iK_W+m_iH+sum_{k
e i}m_kS.
]

---

## 5. High-(F) asymmetry: local theorem

Define

[
G_{MSW}=W_M^{SU,N}-W^{SW}>0,
]

and

[
Delta_{MO}=W_M^{SU,N}-W_O^{SU,N}>0
]

at the symmetric point. The second inequality follows from

[
W_M^{SU,N}>W^{IS}>W_O^{SU,N}.
]

For (SU_{12}), exact algebra gives

[
oxed{
W_1^{12,N}-W_1^{IS}
=
Phi+delta(P-C).
}
]

Since (Phi>0) and (P-C>0), the two large-country members continue to prefer (SU_{12}) to IS.

Against SW,

[
oxed{
W_1^{12,N}-W_1^{SW}
=
G_{MSW}-delta(C-S).
}
]

Because

[
C-S=T_W-T_U>0,
]

this remains positive for all sufficiently small (delta>0).

The key partner-selection identity is

[
oxed{
W_1^{12,N}-W_1^{13,N}
=
delta(A-C)
=
delta T_U>0.
}
]

Thus country 1 strictly prefers partnering with the other large country 2 rather than the smaller country 3. Symmetrically, country 2 strictly prefers (SU_{12}) to (SU_{23}).

Finally, when country 2 moves from outsider under (SU_{13}) to member under (SU_{12}),

[
oxed{
W_2^{12,N}-W_2^{13,N}
=
Delta_{MO}+delta(B-C).
}
]

This is strictly positive in a neighborhood of (delta=0).

Therefore there exists (arepsilon_H>0) such that for every

[
0<delta<arepsilon_H,
]

[
oxed{
mathcal S_S(F)
=
mathcal S_W(F)
=
{ho_{12}^{SU}}.
}
]

The proof is constructive:

- (SU_{12}) cannot be blocked by (SU_{13}) because country 1 strictly loses;
- it cannot be blocked by (SU_{23}) because country 2 strictly loses;
- its members prefer it to IS and, locally, to SW;
- (SU_{13}) and (SU_{23}) are strictly blocked by the pair ({1,2}) moving to (SU_{12});
- SW and IS are strictly blocked by the pair ({1,2}).

Thus the weak-blocking empty set at exact symmetry is not locally robust to this market-size perturbation.

---

## 6. Intermediate-(F) asymmetry: local theorem

The private-adoption game must first remain selection free.

Under (SU_{12}), the outsider-adoption upper threshold remains

[
2T_A.
]

Under (SU_{13}) or (SU_{23}), coalition mass is (2-delta), so outsider adoption requires

[
F<(2-delta)T_A.
]

The reverse-adoption and SW no-adoption lower bounds weakly fall or remain unchanged because all market masses are at most one. Therefore, for any symmetric interior fixed cost

[
F_L<F<2T_A,
]

there exists a positive neighborhood of (delta=0) in which every SU still has the unique outsider-only continuation and SW still has no adoption.

Conditional on that continuation, exact identities are especially simple. For any SU member (i),

[
oxed{
W_i^{IS}-W_i^{SU,O}
=
m_o(P-C)>0.
}
]

For the SU outsider (o),

[
oxed{
W_o^{IS}-W_o^{SU,O}
=
m_oJ+F>0.
}
]

Hence every SU is strictly blocked by the grand coalition whenever all market masses are positive.

IS cannot be blocked by a pair deviation because each pair member would lose (m_o(P-C)>0). It cannot be blocked by a singleton departure because the departing country would become an SU outsider and lose (m_iJ+F>0).

The only additional uniqueness check is SW. Since every country strictly prefers IS to SW at (delta=0), continuity gives a positive interval in which the grand coalition also strictly blocks SW.

Therefore there exists (arepsilon_I>0) such that

[
0<delta<arepsilon_I
]

implies

[
oxed{
mathcal S_S(F)
=
mathcal S_W(F)
=
{ho^{IS}}.
}
]

The intermediate-(F) stability result is therefore locally robust to both the blocking-rule change and the specified market-size asymmetry.

---

## 7. Exact rational witnesses

Use

[
(c,v)=left(rac1{10},rac6{25}ight).
]

### 7.1 High-(F)

Let

[
F_H=rac15.
]

At this point

[
F_H-2T_A
=
rac{141451}{3891200}>0,
]

so no adoption occurs.

The high-(F) asymmetry certificates remain positive even at (delta=1):

[
G_{MSW}-(C-S)
=
rac{239669}{819200}>0,
]

[
Delta_{MO}+(B-C)
=
rac{247331}{819200}>0,
]

and

[
A-C=T_U=rac{1083}{16384}>0.
]

Hence, at this exact ((c,v,F_H)),

[
oxed{
mathcal S_S
=
mathcal S_W
=
{ho_{12}^{SU}}
quad
	ext{for every }0<delta<1.
}
]

The general R6 claim remains only local; this full interval is an exact witness-line strengthening.

### 7.2 Intermediate-(F)

Let

[
F_I=rac3{25}.
]

The symmetric strict margins satisfy

[
F_I-T_W
=
rac{8061}{409600}>0,
]

and

[
2T_A-F_I
=
rac{33969}{778240}>0.
]

For every

[
0<deltalerac12,
]

the smallest two-country coalition mass is (3/2), and

[
rac32T_A-F_I
=
rac{42591}{15564800}>0.
]

Thus every SU still has outsider-only adoption and SW has no adoption throughout that interval.

The IS-versus-SW country-specific gaps are linear in (delta) and remain positive even at (delta=1):

[
left.
(W_1^{IS}-W_1^{SW})
ight|_{delta=1}
=
rac{3193}{11552}>0,
]

[
left.
(W_3^{IS}-W_3^{SW})
ight|_{delta=1}
=
rac{321}{3800}>0.
]

Therefore

[
oxed{
mathcal S_S
=
mathcal S_W
=
{ho^{IS}}
quad
	ext{for every }0<deltalerac12
}
]

at the exact intermediate witness.

The primary exact asymmetry witness (delta=1/100) is therefore strictly interior to the certified interval.

---

## 8. Exhaustive stable-set table

| Market sizes | Fixed-cost region | Strict blocking | Weak/Pareto blocking | Main reason |
|---|---|---|---|---|
| symmetric | high (F) | all three SUs | empty set | alternative SU has one indifferent common member and one strict gainer |
| symmetric | intermediate (F) | IS only | IS only | IS strictly dominates each SU continuation for all three countries |
| (m_3=1-delta), small (delta>0) | high (F) | (SU_{12}) only | (SU_{12}) only | asymmetry breaks partner indifference and selects the two large markets |
| (m_3=1-delta), small (delta>0) | intermediate (F) | IS only | IS only | strict preference gaps survive and adoption remains selection free |

The exhaustive deviation enumeration covers all five partitions and all seven nonempty deviating coalitions.

---

## 9. Institutional interpretation

R6 changes the interpretation of the old stability theorem.

The robust economic object is the **government preference effect**:

- in the canonical intermediate-(F) continuation, each SU member strictly prefers IS by the reciprocal-disadvantage gap;
- the outsider also strictly prefers IS once its own adoption fixed cost is included.

The less robust object is the exact high-(F) symmetric stable set.

At exact symmetry, strict blocking protects each SU because a common member is indifferent across regional partners. Weak/Pareto blocking removes that protection and produces an empty stable set. A small asymmetry then restores a unique regional stable coalition by turning the common member's equality into a strict partner ranking.

Therefore:

[
oxed{
	ext{preference reversal is more robust than the exact symmetric stable-set correspondence.}
}
]

This is the hierarchy required by the revision plan.

---

## 10. Welfare-language audit

In the intermediate-(F) symmetric model, and in the certified small-asymmetry neighborhood, every country strictly prefers IS to every SU continuation, and every country also strictly prefers IS to SW.

Consequently, **within the finite institutional menu (mathcal P) and with firm adoption re-solved under each regime**, IS Pareto-dominates the other formal partitions in that region. Summing national welfare therefore also ranks IS above those menu alternatives.

This does **not** imply:

- unrestricted global first-best efficiency;
- optimality among policies outside (mathcal P);
- optimality with transfers, taxes, dynamic investment, or other omitted instruments.

No stronger welfare claim is authorized.

---

## 11. R6 theorem status

| ID | Result | Status |
|---|---|---|
| R6-S | legacy symmetric strict-blocking stable sets are reproduced | **PROVED** |
| R6-WH | symmetric high-(F) stable set under weak/Pareto blocking is empty | **PROVED** |
| R6-WI | symmetric intermediate-(F) stable set under weak/Pareto blocking is ({IS}) | **PROVED** |
| R6-I | high-(F) three-SU stability under strict blocking relies on symmetry-induced indifference for alternative-SU deviations | **PROVED** |
| R6-AH | small market-size asymmetry selects (SU_{12}) as the unique high-(F) stable partition under both blocking rules | **PROVED LOCALLY** |
| R6-AI | unique intermediate-(F) IS stability survives small market-size asymmetry under both blocking rules | **PROVED LOCALLY** |
| R6-WF | IS Pareto-dominates the other four formal partitions in the certified intermediate region, within the stated institutional menu | **PROVED / MENU-LOCAL** |

---

## 12. Route implication

R6 does not repair the portability failure found in R5 and does not restore a broad general-theory claim.

It instead clarifies which part of the canonical result is economically substantive and which part is institutional:

- the intermediate-(F) preference reversal and unique-IS result are comparatively robust within the canonical microfoundation;
- the exact symmetric high-(F) three-SU stable set is solution-concept sensitive;
- regional stability itself can reappear under the stronger blocking concept once a small market-size asymmetry removes the equality that generated cycling.

Accordingly, R6 supplies an institutional-robustness boundary for R7.

[
oxed{
	ext{R6 COMPLETE — GO TO R7 FOR NOVELTY REASSESSMENT AND THEORY RE-CERTIFICATION.}
]

R7 has not been started in this stage.

---

## 13. Reproducibility

Machine verification:

`python code/revision/check_r6_coalition_stability.py`

The script checks:

- exact asymmetry identities;
- re-solved adoption inequalities;
- all five partitions;
- all seven nonempty deviating coalitions;
- strict and weak/Pareto blocking;
- symmetric high/intermediate stable sets;
- exact asymmetric high/intermediate witnesses;
- the (deltale1/2) intermediate adoption interval certificate.

No numerical grid is used to establish the stable-set claims.
