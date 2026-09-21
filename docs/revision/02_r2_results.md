# R2 — General Conditions for One-Way Private Adoption

## Verdict

**R2 COMPLETE — CONDITIONAL GO TO R3**

Mathematically, R2 succeeds: outsider-only adoption can be characterized without Cournot or linear demand, existence and selection-free uniqueness can be separated, and a nonempty common-cost region can be tied to a transparent comparison between the geographic scope of the bloc standard and the strongest reverse-adoption incentive.

As a standalone novelty claim, however, G1 is **not strong enough to carry the paper**. Fixed-cost economies of scope, multi-market compatibility incentives, and one-way compatibility all have substantial prior art. R2 therefore retains G1 as a supporting lemma for R3 rather than a new headline theorem.

The route to R3 remains open because R2 produces an economically operative condition that R3 can combine with partial erosion of government rents:

\[
\boxed{
\text{one-way private adoption requires the outsider's robust scope-adjusted gain to exceed the strongest reverse-adoption gain.}
}
\]

R3 must show whether that asymmetric adoption state can still change government incentives once exact bypass is relaxed.

---

## 1. R2 model actually solved

Let \(C\) denote the set of markets governed by one formal bloc standard \(s_C\), and let \(o\) denote the outsider market governed by \(s_o\).

The private-adoption action set is binary:

\[
a_o\in\{0,1\},
\qquad
a_i\in\{0,1\}\quad (i\in C).
\]

Here \(a_o=1\) means that the outsider firm supports \(s_C\), while \(a_i=1\) means that member firm \(i\) supports \(s_o\).

Formal membership does not change.

For a fixed formal coalition \(C\), let the product-market continuation equilibrium be unique or otherwise fixed by an independently justified continuation selection. The R2 result is conditional on that continuation value. If a later product-market extension admits multiple continuation equilibria, the adoption stage inherits a correspondence and must be re-certified.

### Segmented-market locality

R2 imposes the following first-step locality restriction:

1. the outsider's support of \(s_C\) changes its continuation profits only in markets governed by \(s_C\);
2. a member's support of \(s_o\) changes its continuation profits only in the outsider market;
3. worldwide operating profit is the sum of destination profits.

This does not mean that formal coalition scope is irrelevant to competition. The local equilibrium gain in a given destination may depend on the formal coalition \(C\), because the set of mutually compatible firms in that market may change when the coalition changes.

---

## 2. Reduced-form continuation gains

For outsider firm \(o\), define the gross operating-profit gain from adopting \(s_C\):

\[
B_o(C)
=
\sum_{k\in C}
\beta_{ok}(C),
\]

where

\[
\beta_{ok}(C)
=
\pi_o^k(a_o=1;C)-\pi_o^k(a_o=0;C).
\]

Under the package-adoption specification, the outsider pays

\[
K_o(C)
=
F_o+\sum_{k\in C}f_{ok}.
\]

Define its fixed-cost-exclusive, scope-adjusted adoption value:

\[
\boxed{
U(C)
=
B_o(C)-\sum_{k\in C}f_{ok}.
}
\]

Then the outsider's adoption gain is

\[
\Delta_o(C)=U(C)-F_o.
\]

For member \(i\), let \(z_{-i}\in\{0,1\}^{C\setminus\{i\}}\) denote the reverse-adoption choices of the other members. Define

\[
\gamma_i(z_{-i};C)
=
\pi_i^o(a_i=1,z_{-i};C)
-
\pi_i^o(a_i=0,z_{-i};C).
\]

Member \(i\)'s adoption cost is

\[
F_i+f_{io}.
\]

Two member-side thresholds are required:

\[
\ell_i^0(C)
=
\gamma_i(0;C)-f_{io},
\]

which is the unilateral reverse-adoption value at the outsider-only candidate profile, and

\[
\bar\ell_i(C)
=
\max_{z_{-i}\in\{0,1\}^{C\setminus\{i\}}}
\gamma_i(z_{-i};C)-f_{io},
\]

which is the strongest reverse-adoption value over the full finite action space.

Define

\[
L_E(C)=\max_{i\in C}\ell_i^0(C),
\]

and

\[
L_U(C)=\max_{i\in C}\bar\ell_i(C).
\]

The subscript \(E\) refers to profile-specific equilibrium existence and \(U\) to the stronger dominance-based uniqueness test.

---

## 3. G1-E — exact strict-equilibrium condition

### Proposition R2.1 — Outsider-only strict equilibrium

Under segmented-market locality, the outsider-only action profile

\[
a_o=1,
\qquad
a_i=0\quad\forall i\in C
\]

is a strict Nash equilibrium if and only if

\[
\boxed{
F_o<U(C)
}
\]

and

\[
\boxed{
F_i>\ell_i^0(C)
\quad\forall i\in C.
}
\]

### Proof

At the proposed profile, outsider \(o\)'s only unilateral deviation is from adoption to non-adoption. Its payoff difference between adoption and non-adoption is

\[
U(C)-F_o.
\]

Hence adoption is strictly optimal exactly when \(F_o<U(C)\).

For each member \(i\), all other members are non-adopters at the proposed profile. The member's payoff difference between adoption and non-adoption is

\[
\gamma_i(0;C)-f_{io}-F_i
=
\ell_i^0(C)-F_i.
\]

Non-adoption is strictly optimal exactly when \(F_i>\ell_i^0(C)\).

All players therefore have a strict best response at the outsider-only profile if and only if the stated inequalities hold. \(\square\)

### Interpretation

This result is deliberately modest. It proves a strict equilibrium, not uniqueness. A different member-adoption profile may still be another equilibrium.

---

## 4. G1-U — selection-free uniqueness by strict dominance

### Theorem R2.2 — Robust one-way adoption

Suppose

\[
F_o<U(C)
\]

and, for every member \(i\),

\[
F_i>\bar\ell_i(C).
\]

Then:

1. outsider adoption is a strict dominant action;
2. every member's non-adoption is a strict dominant action;
3. the outsider-only profile is the unique Nash equilibrium;
4. there is no non-degenerate mixed-strategy Nash equilibrium.

### Proof

Under segmented-market locality, outsider \(o\)'s adoption gain does not depend on members' reverse-adoption actions. Thus \(F_o<U(C)\) makes adoption strictly better than non-adoption against every \(a_{-o}\).

For each member \(i\),

\[
\bar\ell_i(C)
=
\max_{z_{-i}}\left[\gamma_i(z_{-i};C)-f_{io}\right].
\]

Therefore \(F_i>\bar\ell_i(C)\) implies

\[
\gamma_i(z_{-i};C)-f_{io}-F_i<0
\]

for every \(z_{-i}\). Non-adoption is strictly better against every opponents' action profile.

Every player therefore has a unique strict dominant action. The unique Nash equilibrium is the corresponding dominant-action profile. A non-degenerate mixed equilibrium cannot put positive probability on a strictly dominated action. \(\square\)

### Qualification

These are sufficient dominance conditions for unique outsider-only adoption. They are not necessary conditions for uniqueness in an arbitrary member subgame.

---

## 5. Common setup cost and the nonempty one-way interval

Now impose the substantively stronger restriction

\[
F_o=F_i=F
\quad\forall i\in C,
\qquad
F>0.
\]

This removes adopter-specific setup-cost asymmetry as an explanation for one-way adoption.

### Corollary R2.2A — Strict-equilibrium interval

The outsider-only profile is a strict Nash equilibrium for every

\[
\boxed{
\max\{0,L_E(C)\}<F<U(C).
}
\]

The interval is nonempty if and only if

\[
\boxed{
U(C)>\max\{0,L_E(C)\}.
}
\]

### Corollary R2.2B — Selection-free interval

The robust dominance conditions of Theorem R2.2 hold for every

\[
\boxed{
\max\{0,L_U(C)\}<F<U(C).
}
\]

Such a positive common-\(F\) interval exists if and only if

\[
\boxed{
U(C)>\max\{0,L_U(C)\}.
}
\]

This is the R2 core condition.

It is stronger than the statement "adopt if net benefit is positive": it asks whether the same setup cost can simultaneously be low enough for the outsider and high enough for every reverse adopter.

---

## 6. Scope–competition decomposition

Define the **feasibility slack**

\[
S(C)
=
U(C)-\max\{0,L_U(C)\}.
\]

A nonempty interval exists exactly when

\[
S(C)>0.
\]

Its actual length is

\[
W(C)=\max\{0,S(C)\}.
\]

Consider a formal-coalition expansion from \(C\) to \(C'=C\cup\{h\}\).

The outsider threshold changes by

\[
\Delta_h U(C)
=
U(C')-U(C).
\]

Using the market decomposition,

\[
\Delta_h U(C)
=
\underbrace{\beta_{oh}(C')-f_{oh}}_{\text{direct gain in the added market}}
+
\underbrace{
\sum_{k\in C}
\left[
\beta_{ok}(C')-\beta_{ok}(C)
\right]
}_{\text{competition/compatibility feedback in old bloc markets}}.
\]

The strongest reverse-adoption threshold changes by

\[
\Delta_h L_+(C)
=
\max\{0,L_U(C')\}
-
\max\{0,L_U(C)\}.
\]

Therefore

\[
\boxed{
S(C')-S(C)
=
\Delta_h U(C)-\Delta_h L_+(C).
}
\]

### Proposition R2.3 — Scope expansion criterion

A coalition expansion raises the **feasibility slack** if and only if

\[
\boxed{
\Delta_h U(C)>\Delta_h L_+(C).
}
\]

If the common-cost one-way interval is nonempty before and after the expansion, the same condition is necessary and sufficient for the interval to widen.

If the initial interval is empty, an expansion creates a nonempty interval if and only if

\[
\boxed{
\Delta_h U(C)-\Delta_h L_+(C)>-S(C).
}
\]

Thus an improvement in feasibility slack need not create an equilibrium interval when the starting gap is too large.

### Economic content

A larger formal bloc does two things that must not be conflated:

1. it may raise the outsider's return to supporting the bloc standard because one adoption reaches another market;
2. it may also change product-market competition and the strongest incentive of bloc members to support the outsider standard.

Thus "larger bloc \(\Rightarrow\) more outsider adoption" is not a general theorem. The relevant object is the increase in the outsider's robust scope-adjusted gain **relative to** the induced increase in the strongest reverse-adoption gain.

This corrects the overly simple scope intuition that would follow from looking only at the upper threshold.

---

## 7. Homogeneous market-mass specialization

To make Proposition R2.3 economically transparent, suppose that coalition expansion does not alter the per-unit continuation gains in old markets.

Let

\[
M_C=\sum_{k\in C}m_k
\]

be bloc market mass.

Let the outsider's net per-unit-market gain from supporting the bloc standard be

\[
r_o>0,
\]

and let the strongest member reverse-adoption net gain per unit of outsider-market mass be

\[
r_m\ge0.
\]

Then

\[
U(C)=M_C r_o,
\]

and

\[
L_U(C)=m_o r_m.
\]

The selection-free common-\(F\) interval is nonempty exactly when

\[
M_Cr_o>m_or_m.
\]

Equivalently,

\[
\boxed{
\frac{M_C}{m_o}
>
\frac{r_m}{r_o}.
}
\]

This is the R2 scope-dominance condition.

It separates:

- **formal-standard geographic scope**, \(M_C/m_o\);
- **product-market competition**, \(r_m/r_o\);
- **the common setup cost**, which must lie between the two induced thresholds.

A larger bloc is more likely to support one-way adoption only when the extra geographic reach is not offset by stronger reverse-adoption incentives or adverse product-market feedback.

---

## 8. G1-C — adopter-specific fixed costs

Without a common setup cost, one-way adoption requires

\[
F_o<U(C)
\]

and

\[
F_i>\bar\ell_i(C)
\quad\forall i.
\]

### Proposition R2.4 — Cost asymmetry

If

\[
U(C)>0,
\]

then there exists a nonempty set of nonnegative adopter-specific setup costs generating selection-free outsider-only adoption:

\[
0\le F_o<U(C),
\]

\[
F_i>\max\{0,\bar\ell_i(C)\}
\quad\forall i.
\]

Therefore adopter-specific fixed-cost asymmetry does not destroy one-way adoption; it generally makes it easier to generate.

### Research implication

This result is mathematically useful as robustness but weak as a novelty claim. If firms are simply assigned sufficiently different fixed costs, one-way adoption is not surprising. The common-\(F\) result is the more informative R2 benchmark because asymmetry then has to come from scope and product-market continuation gains.

---

## 9. Optional-deployment boundary test

The package specification forces outsider support for \(s_C\) to be deployed across the covered bloc markets and charges every \(f_{ok}\).

Now consider the additive special case in which, after paying \(F_o\), the outsider may choose any deployment subset \(S\subseteq C\). Let

\[
u_k=\beta_{ok}-f_{ok}.
\]

Then the outsider's fixed-cost-exclusive value is

\[
U^{opt}(C)
=
\max_{S\subseteq C}
\sum_{k\in S}u_k
=
\sum_{k\in C}\max\{u_k,0\}.
\]

For a pure option-set expansion that leaves old-market payoffs unchanged,

\[
U^{opt}(C\cup\{h\})-U^{opt}(C)
=
\max\{u_h,0\}\ge0.
\]

### Boundary-test conclusion

Pre-registered H2.4 is **not supported in its strong form**.

Optional deployment does not by itself make the outsider's adoption value fall when the market set expands. Instead:

- a profitable new destination raises the adoption value;
- an unprofitable new destination can be skipped and has zero effect;
- negative scope effects require either package deployment or product-market feedback that changes the payoffs from old destinations.

Thus optional deployment weakens the predictive content of *formal* bloc scope by making some bloc markets irrelevant at the margin, but it does not create a negative pure option-set effect.

This is retained as a boundary result rather than designed away.

---

## 10. Mapping to the submitted Cournot model

For the old regional SU with coalition \(C\) and outsider \(o\),

\[
\beta_{ok}=m_k(P-B)=m_kT_A.
\]

With no destination-specific implementation cost,

\[
U(C)=M_CT_A.
\]

For member \(i\), the reverse-adoption gain in the outsider market is

\[
m_oT_U
\]

when no rival member has adopted, and

\[
m_oT_A
\]

after a rival has adopted. Hence

\[
\ell_i^0(C)=m_oT_U,
\]

and

\[
\bar\ell_i(C)=m_o\max\{T_U,T_A\}.
\]

The R2 selection-free SU-only common-cost interval is therefore

\[
\boxed{
m_o\max\{T_U,T_A\}
<
F
<
M_CT_A.
}
\]

A nonempty interval exists exactly when

\[
\boxed{
M_CT_A
>
m_o\max\{T_U,T_A\}.
}
\]

For the symmetric submitted model,

\[
M_C=2,
\qquad
m_o=1,
\]

so this becomes

\[
\max\{T_U,T_A\}<F<2T_A.
\]

The submitted paper uses the stronger lower bound

\[
F_L=\max\{T_W,T_A\}
\]

because it additionally requires no private adoption under the separate-national-standards regime. Since the old model proves \(T_W>T_U\), its headline interval implies the R2 SU-only dominance interval.

### Numerical witness

At the submitted witness

\[
(c,v)=(0.10,0.24),
\]

the old verified values are approximately

\[
T_U=0.0661011,
\qquad
T_A=0.0818242,
\qquad
T_W=0.1003198.
\]

Hence the R2 SU-only selection-free interval is

\[
0.0818242<F<0.1636484,
\]

while the stronger submitted headline interval that also shuts down SW adoption is

\[
0.1003198<F<0.1636484.
\]

This shows exactly which part of the old \(2T_A\) result is a scope effect and which additional restriction came from the broader institutional comparison.

---

## 11. Pre-registered hypothesis outcomes

| Hypothesis | R2 outcome | Reason |
|---|---|---|
| H2.1 nonempty outsider-only region can arise from scope/common cost | **SUPPORTED** | common-\(F\) interval exists iff \(U(C)>\max\{0,L_U(C)\}\); homogeneous specialization gives \(M_Cr_o>m_or_m\) |
| H2.2 bloc scope raises outsider adoption only conditionally | **SUPPORTED AND STRENGTHENED** | \(\Delta U>\Delta L_+\) raises feasibility slack; creation of a previously empty interval additionally requires crossing zero |
| H2.3 adopter-specific costs need not eliminate one-way adoption | **SUPPORTED** | Proposition R2.4 |
| H2.4 optional deployment can weaken/eliminate scope advantage | **PARTLY REFUTED / REFINED** | under additive pure option-set expansion, value is weakly increasing; an added bad market is skipped |
| H2.5 generic result may be absorbed by prior scope/adoption theory | **SUPPORTED** | literature audit finds substantial direct and partial absorption |

---

## 12. Failure cases retained

### F1 — package expansion can destroy the interval

If an added market has sufficiently negative net direct value and no offsetting positive feedback, then

\[
\Delta_hU(C)<0.
\]

The common-cost one-way interval can shrink or vanish.

### F2 — competition feedback can dominate direct scope gain

Even if the new market directly raises outsider value, the interval shrinks whenever

\[
0<\Delta_hU(C)<\Delta_hL_+(C).
\]

Thus the new member's induced reverse-adoption incentive can dominate the geographic scope effect.

### F3 — equilibrium existence does not imply uniqueness

If

\[
F_i>\ell_i^0(C)
\]

holds at the outsider-only profile but

\[
F_i\le\bar\ell_i(C)
\]

for some member, the outsider-only profile can be a strict equilibrium while another adoption equilibrium remains possible.

### F4 — optional deployment can make formal scope locally irrelevant

If the newly available market has

\[
u_h\le0,
\]

then in the additive optional-deployment case

\[
\Delta_h U^{opt}(C)=0.
\]

Formal coalition expansion need not change the outsider's private-adoption threshold.

---

## 13. R2 research assessment

### What is now genuinely established

The old factor \(2T_A\) is not merely a three-country arithmetic curiosity. It is the submitted-model specialization of a broader scope condition in which one setup decision can generate product-market gains over a formal bloc while reverse adoption has a different market scope.

The robust common-cost condition is

\[
U(C)>\max\{0,L_U(C)\}.
\]

The change in the coalition-expansion feasibility slack is governed by

\[
\Delta U-\Delta L_+,
\]

which explicitly allows product-market competition to defeat the raw scope advantage.

### What is not established

R2 does not establish that this theorem is literature-level novel as a standalone contribution.

It does not yet establish that:

- partial compatibility preserves the government ranking effect;
- the R2 adoption region intersects a nonempty R3 preference-reversal region;
- the mechanism survives Bertrand competition;
- the full coalition stable set survives alternative blocking concepts.

### R2 handoff to R3

Proceed to R3, but treat G1 as a **supporting structural lemma**.

The R3 headline test is now sharper:

> Conditional on an R2-certified outsider-only adoption state, when does incomplete private adaptation reduce the member-market rent from a regional standard enough to increase, and possibly reverse, the government's preference for multilateral standardization?

R3 must preserve the distinction among:

1. one-way adoption;
2. increased incentive for IS;
3. actual preference reversal;
4. formal coalition-stability reversal.

Production-manuscript rewriting remains prohibited.
