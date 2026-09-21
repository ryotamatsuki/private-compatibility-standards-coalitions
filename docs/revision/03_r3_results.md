# R3 — Partial Erosion and Preference Reversal

## Verdict

**R3 COMPLETE — GO**

R3 removes the exact-bypass knife edge from the submitted model. Private adoption is allowed to create full compatibility while leaving a residual marginal adaptation cost

\[
d=\lambda c,\qquad 0\le \lambda\le 1.
\]

The product-market equilibrium is re-solved rather than obtained by replacing \(c\) in an old formula. The result is an exact decomposition of the post-adoption government payoff:

\[
\boxed{
W_M^{SU,O}(d)-W^{IS}
=
-\mathscr D+R(d),
}
\]

where

\[
\boxed{
R(d)
=
\frac{d\left[(5-4v)d+2(1-4v)\right]}
{32(1-v)^2}.
}
\]

The no-adoption payoff remains

\[
W_M^{SU,N}-W^{IS}
=
\mathscr E-\mathscr D.
\]

Hence partial private adaptation reduces the regional member's relative SU advantage by

\[
\boxed{
\mathscr E-R(d).
}
\]

This yields three distinct regions:

- if \(R(d)<\mathscr D\), private adaptation reverses the ranking from SU to IS;
- if \(\mathscr D<R(d)<\mathscr E\), it strengthens the incentive for IS but does not reverse the ranking;
- if \(R(d)>\mathscr E\), it weakens the incentive for IS relative to no adoption.

Thus the revision now has a genuine success/failure condition rather than only the full-erosion endpoint.

A joint open region also exists in which:

1. SU is initially preferred;
2. outsider-only adoption is selection free;
3. SW has no private adoption;
4. adaptation is incomplete (\(0<\lambda<1\));
5. the government ranking nevertheless reverses to IS.

This is established analytically and with an exact rational witness.

---

## 1. Extension fixed for R3

The formal partition and timing remain unchanged.

If a firm privately adopts a foreign formal standard, it uses that standard in the relevant market and therefore joins the corresponding compatibility group exactly as in the submitted model.

The new element is that adoption need not eliminate the marginal adaptation burden completely. An adopter using the foreign standard bears

\[
d=\lambda c,
\qquad
0\le\lambda\le1.
\]

Interpretation:

- \(\lambda=0\): adoption eliminates the marginal adaptation cost, reproducing the submitted full-bypass case;
- \(0<\lambda<1\): adoption creates compatibility but leaves a positive residual marginal cost;
- \(\lambda=1\): adoption changes compatibility but gives no marginal-cost relief.

The point \(\lambda=1\) is **not** the no-adoption state, because compatibility has changed even though the marginal cost has not.

International standardization remains the regime in which all firms natively support the common standard and bear zero adaptation cost.

The extension is deliberately one-dimensional. It does not add partial network benefits, asymmetric \(\lambda\), continuous compatibility choice, or dynamics.

---

## 2. Member market after outsider adoption

Consider a member market of an SU after the outsider adopts the bloc standard.

All three firms now use the bloc standard and are mutually compatible. The two member firms have zero marginal cost; the outsider bears residual cost \(d\).

Let \(x(d)\) denote each member's output and \(y(d)\) the outsider's output.

The first-order conditions imply

\[
\boxed{
x(d)=\frac{1+d}{4(1-v)},
}
\]

\[
\boxed{
y(d)=\frac{1-3d}{4(1-v)}.
}
\]

Because the old admissible domain has \(c<1/3\) and \(0\le d\le c\), the outsider remains active.

The member-firm operating-profit block is

\[
\boxed{
A_R(d)
=
\frac{(1+d)^2}{16(1-v)},
}
\]

and the outsider's operating-profit block is

\[
\boxed{
B_R(d)
=
\frac{(1-3d)^2}{16(1-v)}.
}
\]

Total quantity is

\[
X_R(d)=\frac{3-d}{4(1-v)},
\]

so consumer surplus is

\[
\boxed{
K_R(d)
=
\frac{(3-d)^2}{32(1-v)^2}.
}
\]

At \(d=0\),

\[
A_R(0)=B_R(0)=P,
\qquad
K_R(0)=K_I,
\]

so the submitted full-bypass block is recovered exactly.

---

## 3. Government payoff under partial erosion

For an SU member in the symmetric model, the outsider market is unchanged because the member has not adopted the outsider standard. Its profit there remains \(C\).

Hence

\[
W_M^{SU,O}(d)
=
K_R(d)+2A_R(d)+C.
\]

Subtracting IS gives

\[
W_M^{SU,O}(d)-W^{IS}
=
-\mathscr D+R(d),
\]

where

\[
\mathscr D=P-C
\]

and

\[
R(d)
=
\frac{d\left[(5-4v)d+2(1-4v)\right]}
{32(1-v)^2}.
\]

The identity was obtained by direct equilibrium substitution, not by imposing a proportional erosion parameter.

Since

\[
W_M^{SU,N}-W^{IS}
=
\mathscr E-\mathscr D,
\]

the change caused by private adoption is

\[
W_M^{SU,O}(d)-W_M^{SU,N}
=
-\mathscr E+R(d).
\]

Equivalently, the increase in the government's relative incentive for IS is

\[
\boxed{
\left(W^{IS}-W_M^{SU,O}(d)\right)
-
\left(W^{IS}-W_M^{SU,N}\right)
=
\mathscr E-R(d).
}
\]

This gives an equilibrium foundation for the diagnostic \(\alpha\)-representation. If \(\mathscr E>0\), one may define

\[
\alpha(d)
=
1-\frac{R(d)}{\mathscr E},
\]

but \(\alpha(d)\in[0,1]\) is a conclusion only when \(0\le R(d)\le \mathscr E\). It is not imposed as an assumption.

In this minimal extension the outsider market is unchanged, so the diagnostic reverse-side erosion parameter remains

\[
\beta=0.
\]

---

## 4. Monotonic residual-rent function

On the canonical network domain

\[
0<v<\frac14,
\]

and for \(d\ge0\),

\[
R(0)=0,
\]

and

\[
R'(d)
=
\frac{2(5-4v)d+2(1-4v)}
{32(1-v)^2}
>0.
\]

Therefore \(R(d)\) is strictly increasing.

This gives a unique ordering of the three economically distinct effects.

### Proposition R3.1 — Incentive and ranking boundaries

Suppose initially

\[
\mathscr E>\mathscr D>0.
\]

Then:

1. private adaptation strengthens the member government's incentive for IS iff
   \[
   R(d)<\mathscr E;
   \]
2. private adaptation reverses the ranking from SU to IS iff
   \[
   R(d)<\mathscr D;
   \]
3. if
   \[
   \mathscr D<R(d)<\mathscr E,
   \]
   the incentive for IS rises but SU remains preferred;
4. if
   \[
   R(d)>\mathscr E,
   \]
   private adaptation makes SU relatively more attractive than before adoption.

The equalities \(R(d)=\mathscr D\) and \(R(d)=\mathscr E\) are indifference boundaries.

### Proof

Before adoption,

\[
W_M^{SU,N}-W^{IS}
=
\mathscr E-\mathscr D>0.
\]

After partial adoption,

\[
W_M^{SU,O}(d)-W^{IS}
=
-\mathscr D+R(d).
\]

The post-adoption ranking favors IS exactly when the latter expression is negative, which is \(R(d)<\mathscr D\).

The relative IS incentive changes by \(\mathscr E-R(d)\), so it increases exactly when \(R(d)<\mathscr E\).

Since \(\mathscr E>\mathscr D\), the three stated regions follow. \(\square\)

---

## 5. Closed-form erosion thresholds

For any target level \(Z>0\), the equation

\[
R(d)=Z
\]

has one positive root because \(R\) is continuous, strictly increasing, and unbounded for \(d\ge0\).

Define

\[
\boxed{
d_Z
=
\frac{
-(1-4v)
+
\sqrt{
(1-4v)^2
+
32(5-4v)(1-v)^2 Z
}
}
{5-4v}.
}
\]

Then

\[
R(d)<Z
\iff
0\le d<d_Z.
\]

In particular,

\[
d_D=d_{\mathscr D},
\qquad
d_E=d_{\mathscr E}.
\]

Because

\[
\mathscr E>\mathscr D>0,
\]

strict monotonicity gives

\[
0<d_D<d_E.
\]

For \(c>0\), define the corresponding residual-cost shares

\[
\lambda_D=\frac{d_D}{c},
\qquad
\lambda_E=\frac{d_E}{c}.
\]

Within the admissible interval \(0\le\lambda\le1\):

- ranking reversal occurs for \(\lambda<\lambda_D\);
- incentive strengthening without reversal occurs for \(\lambda_D<\lambda<\lambda_E\);
- incentive weakening occurs for \(\lambda>\lambda_E\),

with the obvious truncation when either threshold exceeds 1.

This is the requested R3-S economic characterization.

---

## 6. R3-L — local robustness

Take any baseline parameter point satisfying the submitted headline conditions strictly:

\[
\mathscr E>\mathscr D>0,
\]

and an interior fixed cost satisfying the submitted selection-free outsider-only adoption inequalities.

At \(\lambda=0\),

\[
R(0)=0<\mathscr D,
\]

and all product-market quantities and threshold functions are continuous in \(d=\lambda c\).

Therefore there exists \(\varepsilon>0\) such that for every

\[
0\le\lambda<\varepsilon
\]

the same private-adoption pattern persists and

\[
W_M^{SU,O}(\lambda c)<W^{IS}.
\]

Hence exact zero residual cost is not required for the submitted ranking reversal.

This is a local robustness result only. The nonlocal result below is separate.

---

## 7. Re-solving the adoption stage

R3 must not use the old adoption thresholds unchanged.

### 7.1 Outsider adoption of the bloc standard

Before adoption, outsider profit in each member market is \(B\).

After adoption with residual cost \(d\), it is \(B_R(d)\).

Define

\[
\boxed{
T_O(d)=B_R(d)-B.
}
\]

For a symmetric two-member SU, outsider adoption is strictly profitable iff

\[
\boxed{
F<2T_O(d).
}
\]

At \(d=0\),

\[
T_O(0)=P-B=T_A,
\]

so the old upper threshold \(2T_A\) is recovered.

### 7.2 One member adopts the outsider standard

In the outsider market, suppose one member adopts the outsider standard and bears residual cost \(d\).

Let:

- \(q_N(d)\): native outsider quantity;
- \(q_A(d)\): adopting member quantity;
- \(q_S(d)\): non-adopting member quantity.

The unique interior Cournot solution is

\[
q_N(d)
=
\frac{(1-v)(1+c)+d(1-2v)}
{2(1-v)(2-3v)},
\]

\[
q_A(d)
=
\frac{(1-v)(1+c)-d(3-4v)}
{2(1-v)(2-3v)},
\]

\[
q_S(d)
=
\frac{1-3v-3c(1-v)+d}
{2(2-3v)}.
\]

The adopter's operating profit is

\[
A_A(d)=(1-v)q_A(d)^2.
\]

Hence the unilateral SU-member reverse-adoption threshold is

\[
\boxed{
T_U(d)=A_A(d)-C.
}
\]

Under SW, the same post-adoption state is reached from a different pre-adoption state, so the unilateral foreign-adoption threshold is

\[
\boxed{
T_W(d)=A_A(d)-S.
}
\]

Their difference does not depend on \(d\):

\[
T_W(d)-T_U(d)=C-S>0
\]

on the canonical domain.

### 7.3 Adoption after the other member has adopted

If both members adopt the outsider standard, all three firms are compatible. The two adopted members each bear \(d\), while the native outsider has zero marginal cost.

Each adopted member produces

\[
q_{AA}(d)
=
\frac{1-2d}{4(1-v)}
\]

and earns

\[
A_{AA}(d)
=
\frac{(1-2d)^2}{16(1-v)}.
\]

Before the second member adopts, it is the singleton in the one-adopter state and earns

\[
q_S(d)^2.
\]

Therefore its post-rival threshold is

\[
\boxed{
T_A^{R}(d)
=
A_{AA}(d)-q_S(d)^2.
}
\]

At \(d=0\),

\[
T_U(0)=T_U,
\qquad
T_W(0)=T_W,
\qquad
T_A^{R}(0)=T_A.
\]

### 7.4 Selection-free partial-adoption region

Define

\[
\boxed{
F_L(d)
=
\max\left\{
0,\,
T_W(d),\,
T_A^{R}(d)
\right\},
}
\]

and

\[
\boxed{
F^\ast(d)=2T_O(d).
}
\]

If

\[
\boxed{
F_L(d)<F<F^\ast(d),
}
\]

then:

- the SU outsider strictly adopts the bloc standard;
- SU members strictly do not adopt the outsider standard against either member action;
- SW has no private adoption;
- the continuation is selection free.

The extra \(0\) in \(F_L(d)\) avoids treating a negative profit threshold as a positive fixed-cost restriction.

---

## 8. Joint adoption-and-ranking region

The R3 headline object is the intersection, not the separate existence of two regions.

Define

\[
\Omega_3
=
\left\{
(c,v,\lambda,F):
\begin{array}{l}
(c,v)\text{ satisfies the old interior feasibility conditions},\\
0<\lambda<1,\quad d=\lambda c,\\
\mathscr E>\mathscr D>0,\\
R(d)<\mathscr D,\\
F_L(d)<F<F^\ast(d)
\end{array}
\right\}.
\]

Every point in \(\Omega_3\) has:

1. initial member preference for SU;
2. incomplete private adaptation;
3. selection-free outsider-only adoption under SU;
4. no private adoption under SW;
5. post-adoption member preference for IS.

All inequalities are strict and the closed-form objects are continuous on the interior domain. Therefore \(\Omega_3\) is open.

It remains to prove nonemptiness.

---

## 9. Exact nonlocal witness

Use the submitted baseline point

\[
(c,v)=\left(\frac1{10},\frac6{25}\right)
\]

but set

\[
\lambda=\frac12,
\qquad
d=\frac1{20},
\qquad
F=\frac9{100}.
\]

The old pre-adoption gap is

\[
W_M^{SU,N}-W^{IS}
=
\frac{2408509}{295731200}
\approx0.00814425>0.
\]

The partial-adoption post-gap is

\[
\boxed{
W_M^{SU,O}(d)-W^{IS}
=
-\frac{1341}{184832}
\approx-0.00725524<0.
}
\]

Thus the member ranking reverses even though one-half of the original marginal adaptation cost remains.

The re-solved adoption thresholds are

\[
T_U(d)
=
\frac{42273}{1245184}
\approx0.0339492,
\]

\[
T_W(d)
=
\frac{2122041}{31129600}
\approx0.0681679,
\]

\[
T_A^{R}(d)
=
\frac{2024181}{31129600}
\approx0.0650243,
\]

and

\[
F^\ast(d)
=
2T_O(d)
=
\frac{459189}{3891200}
\approx0.118007.
\]

Therefore

\[
F_L(d)=T_W(d)\approx0.0681679
<
0.09
<
0.118007
=
F^\ast(d).
\]

So the same parameter point simultaneously satisfies the adoption and preference-reversal conditions.

Because \(\lambda=1/2\) and \(F=0.09\) are interior and every inequality is strict, continuity gives a nonempty open neighborhood contained in \(\Omega_3\).

This goes beyond the R3-L local argument around \(\lambda=0\).

---

## 10. Strong witness-line robustness

At

\[
(c,v)=\left(\frac1{10},\frac6{25}\right),
\]

the post-adoption welfare gap simplifies for arbitrary \(\lambda\in[0,1]\) to

\[
W_M^{SU,O}(\lambda c)-W^{IS}
=
\frac{202\lambda^2+40\lambda-741}{92416}.
\]

This expression is increasing on \([0,1]\), and at \(\lambda=1\),

\[
202+40-741=-499<0.
\]

Hence the member prefers IS after adoption for every

\[
0\le\lambda\le1
\]

at this \((c,v)\).

The fixed-cost interval also remains nonempty for each \(\lambda\in[0,1]\). Exact differences are

\[
F^\ast(\lambda c)-T_W(\lambda c)
=
\frac{
3(16725\lambda^2-78350\lambda+164283)
}
{7782400},
\]

and

\[
F^\ast(\lambda c)-T_A^R(\lambda c)
=
\frac{
3(33825\lambda^2-166550\lambda+212263)
}
{7782400}.
\]

Each quadratic is decreasing on \([0,1]\) and remains strictly positive at \(\lambda=1\). Therefore, for every \(\lambda\in[0,1]\), some positive \(F\) yields outsider-only SU adoption, no SW adoption, and post-adoption preference for IS.

The fixed cost need not be the same for every \(\lambda\). This is a family-of-regions result, not a common-\(F\) comparative-static claim.

---

## 11. Failure conditions

R3 explicitly records when private compatibility does **not** promote broader formal coordination.

### Failure A — erosion insufficient for ranking reversal

If

\[
R(d)\ge\mathscr D,
\]

then the member does not strictly prefer IS after adoption.

### Failure B — incentive rises but ranking does not reverse

If

\[
\mathscr D<R(d)<\mathscr E,
\]

private adaptation moves the government toward IS but does not cross the ranking boundary.

### Failure C — private adaptation moves the government away from IS

If

\[
R(d)>\mathscr E,
\]

the residual member-market rent is so large that the IS incentive is weaker than before adoption.

### Failure D — firms do not select the required continuation

Even if

\[
R(d)<\mathscr D,
\]

the mechanism is not operative unless the firm game selects outsider-only adoption. If

\[
F^\ast(d)\le F_L(d),
\]

there is no positive fixed-cost interval with the required selection-free continuation under the R3 comparison.

### Failure E — endpoint interpretation error

The state \(\lambda=1\) must not be compared with no adoption as if they were technologically identical. At \(\lambda=1\), compatibility has changed; only marginal-cost relief is absent.

---

## 12. Relation to the diagnostic \(\alpha,\beta\) decomposition

The ex ante diagnostic expression was

\[
(1-\alpha)\mathscr E-(1-\beta)\mathscr D.
\]

R3 does not assume \(\alpha\) or \(\beta\).

The equilibrium solution implies

\[
\beta=0
\]

for this minimal extension and, when \(\mathscr E>0\),

\[
\alpha(d)
=
1-\frac{R(d)}{\mathscr E}.
\]

Therefore the general diagnostic expression becomes

\[
(1-\alpha(d))\mathscr E-\mathscr D
=
R(d)-\mathscr D,
\]

exactly matching the equilibrium payoff.

This is the desired direction of derivation:

\[
\text{market primitives}
\rightarrow
\text{Cournot equilibrium}
\rightarrow
R(d)
\rightarrow
\alpha(d),
\]

not the reverse.

---

## 13. R3 hypothesis assessment

| Question | Result |
|---|---|
| Does exact equality with IS in member markets drive the old result? | **NO.** Ranking reversal survives on an open set with \(0<\lambda<1\). |
| Is local continuity the only robustness result? | **NO.** Exact thresholds \(d_D,d_E\) and a nonlocal \(\lambda=1/2\) open witness are derived. |
| Can private adaptation strengthen IS incentives without reversing preferences? | **YES**, when \(\mathscr D<R(d)<\mathscr E\). |
| Can private adaptation fail to promote IS at all? | **YES**, when \(R(d)>\mathscr E\). |
| Are adoption and government preference checked on the same primitives? | **YES.** \(\Omega_3\) imposes both conditions jointly. |
| Is the old adoption threshold reused unchanged? | **NO.** \(T_O,T_U,T_W,T_A^R\) are re-solved under \(d=\lambda c\). |
| Does R3 prove competition-form independence? | **NO.** That remains R5. |

---

## 14. Route decision after R2–R3

Provisional route:

\[
\boxed{\text{Route A — substantive generalization, subject to R4–R7 certification}}
\]

Reason:

- R2 provides a scope-versus-reverse-adoption condition rather than only the old factor \(2\);
- R3 removes exact cost elimination and derives success/failure boundaries from equilibrium;
- the government effect is no longer only the endpoint identity
  \(\mathscr E-\mathscr D\to-\mathscr D\);
- the required firm-adoption state and preference reversal coexist on a nonempty open set.

This is **provisional**, not a journal-quality certification. R4 must now characterize the role of network effects, and R5 must test one alternative competition form if R4 does not invalidate the route. R7 remains the theory re-certification gate.

Production-manuscript rewriting remains prohibited.
