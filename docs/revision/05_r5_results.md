# R5 — Limited Competition-Form Portability Test

## Verdict

**R5 COMPLETE — PORTABILITY FAILS IN THE FROZEN DIFFERENTIATED-DEMAND MODEL**

Input integration state:

- branch: `revision/r5-execution`
- input commit: `585fda9beb409d108d76d3ff7536bb955960f939`
- governing workflow: `research-paper-workflow v2.2 @ 42574d6c5931275ccff3ef7e8b4acc188077332a`
- frozen R5 design: `docs/revision/05_r5_design_freeze.md`

R5 changes research records and verification only. The production manuscript remains frozen.

The R5 result is a **non-portability result**, but not a Bertrand-specific negative result. In the one pre-specified differentiated-demand environment, the pre-adoption SU advantage fails under both differentiated Cournot (R5-C) and differentiated Bertrand (R5-B). One-way outsider-only private adoption remains selection-free on a nonempty fixed-cost interval, but the government channel changes sign: the member-market term (mathscr E^X) is negative rather than positive. Private adoption therefore weakens the relative incentive for IS in this R5 environment.

Because R5-C already fails, the result cannot be attributed solely to price competition. The identified fragility is to the demand/welfare microfoundation used to regularize the canonical perfect-substitutes model, not just to Cournot versus Bertrand.

This conclusion is deliberately model-specific. R5 does **not** prove that preference reversal requires quantity competition or that no differentiated-Bertrand specification can generate it.

---

## 1. Frozen R5 demand environment

The model was frozen before solving.

Set

[
gamma=rac12.
]

For each national market,

[
B=(1-gamma)I+gammamathbf 1mathbf 1^	op.
]

Let (C_G) be the compatibility-group matrix, with the canonical zero-network-benefit convention for singleton groups. Define

[
M_G(v)=B-vC_G.
]

The representative consumer has quasi-linear gross utility

[
U(q)=mathbf 1^	op q-rac12q^	op Bq+rac v2q^	op C_Gq,
]

so inverse demand and consumer surplus are

[
oxed{p=mathbf 1-M_G(v)q},
]

[
oxed{CS(q)=rac12q^	op M_G(v)q}.
]

The audit box is

[
oxed{
0<c<rac13,qquad 0le v<rac14.
}
]

All costs, formal regimes, private-adoption scope, government objective, and timing are inherited from the canonical model. The primary R5 test uses the full-bypass adoption technology. No residual-cost parameter, asymmetry, alternative network rule, or second demand system is introduced.

---

## 2. Why R5 solves Cournot and Bertrand in the same new demand system

The canonical inverse demand is a perfect-substitutes boundary case. Direct differentiated Bertrand competition therefore requires a demand regularization.

R5 solves two games from exactly the same (M_G(v)):

- **R5-C:** firms choose quantities;
- **R5-B:** firms choose prices.

This is essential for attribution. A difference between the historical canonical model and R5 may reflect the new differentiated demand and welfare measure. Only an R5-C versus R5-B difference could be attributed to the strategic variable.

In fact, the central political result fails in **both** R5-C and R5-B.

---

## 3. Demand regularity and interiority

For complete compatibility,

[
M_I=B-vmathbf 1mathbf 1^	op,
]

with eigenvalues

[
rac12,quadrac12,quad 2-3v.
]

Hence (M_I) is positive definite on the R5 box.

For the two-firm compatibility group used under SU,

[
det M_{12}=rac{1-2v}{2}>0,
]

and the leading (2	imes2) principal minor is

[
rac34-v>0.
]

Thus direct demand is well defined throughout the box.

The R5-C quantities are

[
q_I^C=rac1{3-4v},
]

[
q_M^C=rac{3+c}{3(3-4v)},
qquad
q_B^C=
rac{3-6v-c(5-6v)}{3(3-4v)},
]

[
q_C^C=rac{3-4c}{3(3-4v)},
qquad
q_D^C=rac{3+2c-6v}{3(3-4v)},
]

and under SW,

[
q_H^C=rac{3+2c}{9},
qquad
q_S^C=rac{3-4c}{9}.
]

All are strictly positive on the R5 box. For example, the potentially tight SU outsider quantity satisfies

[
3-6v-c(5-6v)
>
rac43-4v
>
rac13.
]

For R5-B, write

[
H(v)=8v^2-16v+7,
qquad
L(v)=(1-2v)H(v),
qquad
r(v)=3-4v.
]

Then

[
q_I^B=
rac{r}{4(1-v)(2-3v)},
]

[
q_M^B=
rac{r[7-12v+c(3-4v)]}{8L},
]

[
q_B^B=
rac{r[16v^2-24v+7-c(16v^2-32v+13)]}{8L},
]

[
q_C^B=
rac{r[7-12v+c(16v-10)]}{8L},
]

[
q_D^B=
rac{r[16v^2-24v+7+c(6-8v)]}{8L},
]

and

[
q_H^B=rac{3(7+6c)}{56},
qquad
q_S^B=rac{3(7-10c)}{56}.
]

These are also strictly positive throughout the open box. Therefore the headline results do not rely on an unexamined exit or zero-demand corner.

---

## 4. Common welfare and adoption notation

For either strategic-variable version (Xin{C,B}), define the usual product-market blocks

[
P^X, A^X, B^X, C^X, D^X, H^X, S^X
]

and consumer-surplus blocks

[
K_I^X, K_M^X, K_O^X, K_W^X.
]

The SU-member pre-adoption welfare gap is

[
Phi^X
=
W_M^{SU,N,X}-W^{IS,X}.
]

Define

[
mathscr D^X=P^X-C^X
]

and

[
mathscr E^X
=
(K_M^X-K_I^X)+2(A^X-P^X).
]

The accounting identity remains

[
oxed{
Phi^X=mathscr E^X-mathscr D^X.
}
]

Under full outsider adoption of the bloc standard, member markets become the complete-compatibility configuration, while the outsider market is unchanged. Hence

[
oxed{
W_M^{SU,O,X}-W^{IS,X}
=
-mathscr D^X.
}
]

This structural identity survives the competition-form change. What changes is the sign of (mathscr E^X).

Adoption thresholds are also defined exactly as in the canonical bookkeeping:

[
T_A^X=P^X-B^X,
qquad
T_U^X=A^X-C^X,
qquad
T_W^X=A^X-S^X.
]

For selection-free outsider-only SU adoption and no SW adoption, use

[
F_L^X=
max{0,T_A^X,T_U^X,T_W^X},
]

and require

[
F_L^X<F<2T_A^X.
]

---

## 5. R5-C: differentiated Cournot comparator

### 5.1 Pre-adoption SU advantage fails

The exact gap is

[
oxed{
Phi^C(c,v)
=
rac{N_C(c,v)}
{18(3-4v)^2},
}
]

where

[
egin{aligned}
N_C={}&
36c^2v^2-88c^2v+54c^2
-72cv^2+120cv-60c\
&+36v^2-27v.
end{aligned}
]

For fixed (v), (N_C) is strictly convex in (c), because

[
rac{partial^2N_C}{partial c^2}
=
4(18v^2-44v+27)>0
]

on (0le v<1/4).

The endpoint values are

[
N_C(0,v)=9v(4v-3)le0,
]

and

[
N_Cleft(rac13,vight)
=
rac{144v^2+29v-126}{9}<0.
]

At the only endpoint equality ((c,v)=(0,0)),

[
N_C(c,0)=6c(9c-10)<0
]

for (0<c<1/3).

Therefore

[
oxed{
Phi^C(c,v)<0
quad
	ext{for all }
0<c<rac13, 0le v<rac14.
}
]

The member government already prefers IS before private adoption.

### 5.2 Reciprocal disadvantage survives

[
oxed{
mathscr D^C
=
rac{
8c(3-2c)(1-v)
}{
9(3-4v)^2
}
>0.
}
]

Thus after outsider adoption,

[
W_M^{SU,O,C}-W^{IS,C}
=
-mathscr D^C<0.
]

### 5.3 The government effect reverses sign

The R5-C member-market term is

[
oxed{
mathscr E^C
=
rac{M_C(c,v)}
{18(3-4v)^2},
}
]

with

[
egin{aligned}
M_C={}&
36c^2v^2-56c^2v+22c^2
-72cv^2+72cv-12c\
&+36v^2-27v.
end{aligned}
]

The same convex-endpoint argument proves

[
oxed{
mathscr E^C<0
}
]

throughout the R5 box.

Because

[
left(W^{IS,C}-W_M^{SU,O,C}ight)
-
left(W^{IS,C}-W_M^{SU,N,C}ight)
=
mathscr E^C,
]

private adoption **weakens**, rather than strengthens, the government's relative incentive for IS.

### 5.4 One-way private adoption still exists

Exact sign checks give

[
T_A^C>0,
qquad
T_U^C>0,
]

[
T_W^C-T_U^C
=
rac{
v(3-4c)^2(15-16v)
}{
81(3-4v)^2
}
ge0,
]

and

[
2T_A^C-T_W^C>0.
]

Therefore

[
oxed{
F_L^C<2T_A^C
}
]

throughout the R5 box, so a positive selection-free outsider-only adoption interval exists.

The firm-adoption mechanism survives even though the political SU-advantage mechanism does not.

---

## 6. R5-B: differentiated Bertrand target

Let

[
D_B(v)
=
(1-v)^2(1-2v)(2-3v)H(v)^2>0.
]

The exact Bertrand expressions can be sign-normalized as

[
oxed{
Phi^B
=
rac{(4v-3)Q_Phi(c,v)}
{64D_B(v)},
}
]

[
oxed{
mathscr E^B
=
rac{(4v-3)Q_E(c,v)}
{64D_B(v)},
}
]

[
oxed{
mathscr D^B
=
rac{(3-4v)Q_D(c,v)}
{32D_B(v)},
}
]

and

[
oxed{
T_A^B
=
rac{(3-4v)Q_A(c,v)}
{32D_B(v)}.
}
]

The polynomials (Q_Phi,Q_E,Q_D,Q_A) are generated exactly from the Bertrand first-order system in `code/revision/check_r5_competition_portability.py`.

### 6.1 Exact Bernstein sign certification

Map the closed audit rectangle to the unit square by

[
x=3c,
qquad
y=4v.
]

Each sign polynomial is converted exactly to the tensor-product Bernstein basis. Nonnegative Bernstein coefficients certify nonnegativity over the whole rectangle; the listed boundary zero coefficients are then handled by exact boundary factorizations.

| Polynomial | Degree ((c,v)) | Zero Bernstein coefficients | Smallest positive coefficient |
|---|---:|---|---:|
| (Q_Phi) | ((2,7)) | ((0,0)) | (51/8) |
| (Q_E) | ((2,7)) | ((0,0),(2,7)) | (11/6) |
| (Q_D) | ((2,5)) | ((0,0)) | (1) |
| (Q_A) | ((2,7)) | ((0,0)) | (151/16) |
| (Q_{2A-W}) | ((2,8)) | ((0,0)) | (549927/512) |
| (Q_{2A-U}) | ((2,7)) | ((0,0)) | (12) |
| (Q_{W-U}) | ((2,4)) | none | (3479/12) |

At (v=0),

[
Q_Phi(c,0)=14c(58-59c)>0,
]

[
Q_E(c,0)=6c(42-71c)>0,
]

[
Q_D(c,0)=40c(7-5c)>0,
]

[
Q_A(c,0)=26c(14-13c)>0
]

for (0<c<1/3).

Since (4v-3<0), the exact signs are

[
oxed{
Phi^B<0,
qquad
mathscr E^B<0,
qquad
mathscr D^B>0,
qquad
T_A^B>0.
}
]

Thus the Bertrand model has the same qualitative political decomposition as R5-C:

- IS is preferred before adoption;
- IS remains preferred after adoption;
- private adoption weakens the relative IS incentive because (mathscr E^B<0).

### 6.2 Selection-free outsider-only adoption survives

The remaining exact sign certificates give

[
T_U^B>0,
]

[
T_W^B-T_U^Bge0,
]

[
2T_A^B-T_W^B>0,
]

and

[
2T_A^B-T_U^B>0.
]

Therefore

[
oxed{
F_L^B<2T_A^B
}
]

throughout the R5 box.

Again, the private-adoption mechanism survives while the political ranking-reversal mechanism does not.

---

## 7. Exact common witness

Use

[
(c,v,F)
=
left(
rac1{10},
rac6{25},
rac15
ight).
]

### R5-C

[
Phi^C
=
-rac{79079}{780300}
approx-0.101344,
]

[
mathscr D^C
=
rac{1064}{23409}
approx0.045453,
]

[
mathscr E^C
=
-rac{130837}{2340900}
approx-0.055892.
]

The adoption thresholds are

[
T_A^C
=
rac{336899}{2340900}
approx0.143919,
]

[
T_U^C
=
rac{1805}{31212}
approx0.057830,
]

[
T_W^C
=
rac{87037}{780300}
approx0.111543.
]

Hence

[
F_L^C
=
T_A^C
<
rac15
<
2T_A^C.
]

### R5-B

[
Phi^B
=
-rac{53617141587261}{615261340595200}
approx-0.087145,
]

[
mathscr D^B
=
rac{133095975}{2309106176}
approx0.057640,
]

[
mathscr E^B
=
-rac{18153719048511}{615261340595200}
approx-0.029506.
]

The adoption thresholds are

[
T_A^B
=
rac{46252347421011}{307630670297600}
approx0.150350,
]

[
T_U^B
=
rac{511510875}{8521625216}
approx0.060025,
]

[
T_W^B
=
rac{44245363371}{417559635584}
approx0.105962.
]

Hence

[
F_L^B
=
T_A^B
<
rac15
<
2T_A^B.
]

So the **same exact primitives** generate selection-free outsider-only adoption in both R5-C and R5-B, but neither model has an SU-to-IS ranking reversal.

---

## 8. Required R5 test classification

| Required test | R5-C | R5-B |
|---|---|---|
| pre-adoption SU advantage | **FAILS — PROVED** | **FAILS — PROVED** |
| outsider-only adoption equilibrium | **EXISTS; selection-free interval proved** | **EXISTS; selection-free interval proved** |
| private adoption strengthens relative IS incentive | **NO — opposite sign, (mathscr E^C<0)** | **NO — opposite sign, (mathscr E^B<0)** |
| actual SU→IS preference reversal | **IMPOSSIBLE in audit box** | **IMPOSSIBLE in audit box** |

No finite-grid non-result is used. The failure statements are exact over the frozen audit box.

---

## 9. What R5 does and does not establish

R5 establishes:

1. one-way private standard adoption is portable to this differentiated-demand environment;
2. the political selective-erosion mechanism is not;
3. the failure is already present under quantity competition with the same differentiated demand;
4. therefore the R5 failure cannot be described as a Bertrand effect;
5. the sign of the member-market term (mathscr E) is a central portability condition that must be surfaced explicitly at R7.

R5 does **not** establish:

- that preference reversal requires Cournot competition;
- that all differentiated-product models have (mathscr E<0);
- that all Bertrand models fail;
- that (gamma=1/2) is uniquely natural;
- that the canonical model is mathematically invalid.

The correct interpretation is specification dependence.

---

## 10. Implication for the research route

R2 remains useful as a structural result about one-way adoption. R3 remains a valid robustness result **inside the canonical Cournot microfoundation**. R4 and R5, however, jointly show that the political headline mechanism is substantially more specification dependent than the original paper suggested:

- R4: initial SU advantage depends on positive network effects and is sensitive to the singleton-network convention;
- R5: initial SU advantage and positive member-market exclusion term fail in the frozen differentiated-demand environment under both Cournot and Bertrand.

Accordingly, Route A is **materially weakened**. R5 does not itself choose Route B or C because R7 is the designated novelty/generality recertification gate.

The next stage may proceed to R6 only as an institutional robustness audit of the still-valid canonical preference results. R6 must not be used to restore competition-form generality.

[
oxed{
	ext{R5 COMPLETE — NON-PORTABILITY IDENTIFIED; R6 AUTHORIZED, NOT STARTED.}
}
]

Production-manuscript rewriting remains prohibited.

---

## 11. Reproducibility

Machine verification:

`python code/revision/check_r5_competition_portability.py`

The script:

- derives R5-C and R5-B equilibria from the frozen primitives;
- checks positive-definite demand matrices and interior quantities;
- derives welfare and adoption blocks;
- proves the R5-C signs by exact convexity/end-point certificates;
- proves the R5-B signs using exact rational Bernstein-basis certificates;
- verifies the full-bypass accounting identity;
- verifies the exact common witness;
- verifies the positive selection-free fixed-cost intervals.
