# R4 — Role of Network Effects and Baseline Specification

## Verdict

**R4 COMPLETE — GO TO R5**

Input integration state:

- branch: `revision/research-track`
- input commit: `179f8f499b32810aa7c46066c8785cbf74f2a706`
- governing workflow: `research-paper-workflow v2.2 @ 42574d6c5931275ccff3ef7e8b4acc188077332a`

R4 changes research records and verification only. The Stage-8 freeze and the production manuscript remain unchanged.

The central conclusion is deliberately decomposed. In the current symmetric Cournot microfoundation, positive network effects are **not** required for one-way private adoption or for the R3 partial-erosion accounting. They **are** required to generate the pre-adoption preference for a regional standards union (SU) that is needed for the SU-to-IS ranking-reversal path. The zero-network result therefore does not eliminate private circumvention; it eliminates the initial political ranking that makes the headline reversal possible.

The separate singleton-network audit also identifies a material specification dependence: the canonical convention that a singleton compatibility group receives zero network benefit is not a mere normalization for the pre-adoption government ranking.

---

## 1. Fixed-c feasibility

The canonical interior domain is

\[
0<v<\frac14,
\qquad
0<c<\frac{1-3v}{3(1-v)}.
\]

For fixed \(c\), the second inequality is equivalent to

\[
3v(1-c)<1-3c.
\]

Hence feasibility requires

\[
0<c<\frac13
\]

and

\[
0<v<\bar v(c),
\qquad
\bar v(c)
=
\min\left\{
\frac14,
\frac{1-3c}{3(1-c)}
\right\}.
\]

The two upper bounds coincide exactly at

\[
c=\frac19.
\]

Thus

\[
\bar v(c)=
\begin{cases}
\frac14,&0<c\le\frac19,\\[4pt]
\frac{1-3c}{3(1-c)},&\frac19<c<\frac13.
\end{cases}
\]

All boundaries remain open because the canonical model is an interior model.

---

## 2. Exact pre-adoption SU–IS welfare gap

Define

\[
\Phi(c,v)
=
W_M^{SU,N}(c,v)-W^{IS}(c,v).
\]

Direct substitution of the canonical welfare blocks gives

\[
\boxed{
\Phi(c,v)
=
\frac{N(c,v)}
{32(1-v)^2(2-3v)^2},
}
\]

where

\[
\begin{aligned}
N(c,v)
={}&36c^2v^4-144c^2v^3+232c^2v^2-176c^2v+52c^2\\
&-72cv^4+240cv^3-288cv^2+144cv-24c\\
&+36v^4-114v^3+81v^2-12v.
\end{aligned}
\]

The denominator is strictly positive on the feasible domain. Therefore the sign of \(\Phi\) is exactly the sign of \(N\).

At the zero-network boundary,

\[
\boxed{
\Phi(c,0)=\frac{c(13c-6)}{32}.
}
\]

Since \(0<c<1/3\),

\[
13c-6<\frac{13}{3}-6=-\frac53<0,
\]

so

\[
\boxed{
\Phi(c,0)<0
\qquad(0<c<1/3).
}
\]

This independently reproduces and absorbs the earlier R1 precheck in `04_network_role_precheck.md`. That file is retained as historical precheck evidence.

---

## 3. Root structure in the network parameter

The root count is certified analytically, not by a grid.

For each fixed \(c\), map the open feasible interval \(0<v<U\) to \(x>0\) by

\[
v=\frac{Ux}{1+x}.
\]

Multiplying by \((1+x)^4\) preserves the roots and gives a quartic in \(x\).

### 3.1 Case \(0<c\le1/9\)

Here \(U=1/4\). The transformed polynomial has coefficient signs

\[
+,-,-,-,-.
\]

More explicitly, the leading coefficient is

\[
\frac{9}{64}(145c^2-18c+3)>0,
\]

the constant coefficient is

\[
4c(13c-6)<0,
\]

and exact polynomial-root checks show that each of the three intermediate coefficient polynomials is strictly negative on \((0,1/9]\).

Descartes' rule therefore gives exactly one positive \(x\)-root, hence exactly one feasible \(v\)-root.

### 3.2 Case \(1/9<c<1/3\)

Here

\[
U=\frac{1-3c}{3(1-c)}.
\]

After clearing the positive common denominator, the leading coefficient is

\[
Q(c)=17c^3+109c^2-89c+11,
\]

while the other four coefficients are strictly negative throughout \((1/9,1/3)\), certified by exact Sturm root counts.

Therefore:

- if \(Q(c)>0\), the coefficient signs are \(+,-,-,-,-\), so there is exactly one feasible root;
- if \(Q(c)\le0\), there is no positive transformed root, hence no interior feasible root.

This proves uniqueness before the root is named. No monotonicity claim for the full function \(\Phi(c,v)\) is needed.

---

## 4. Existence boundary for the initial SU advantage

At the feasibility boundaries,

\[
N\left(c,\frac14\right)
=
\frac{9}{64}
\left(145c^2-18c+3\right)>0,
\]

and

\[
N\left(
c,
\frac{1-3c}{3(1-c)}
\right)
=
\frac{
17c^3+109c^2-89c+11
}{
9(1-c)^3
}.
\]

Define \(c^\ast\) as the unique root of

\[
Q(c)=17c^3+109c^2-89c+11
\]

in \((0,1/3)\). Exact root isolation gives

\[
\frac{1529167}{10^7}
<
c^\ast
<
\frac{1529168}{10^7},
\]

so

\[
c^\ast\approx0.1529167822964523.
\]

For every \(0<c<c^\ast\), let \(v_{SU}(c)\) denote the unique root of

\[
N(c,v)=0
\]

inside \((0,\bar v(c))\).

Then the complete characterization is

\[
\boxed{
\mathcal V_{SU}(c)
=
\begin{cases}
\left(v_{SU}(c),\bar v(c)\right),
&0<c<c^\ast,\\[4pt]
\varnothing,
&c^\ast\le c<\frac13.
\end{cases}
}
\]

At \(c=c^\ast\), the zero occurs only at the open feasibility boundary; there is no interior SU-advantage interval.

The result is an upper interval in feasible \(v\), but this does **not** authorize the broader claim that \(\Phi\) is globally monotone in \(v\).

---

## 5. Reciprocal disadvantage and the joint headline region

The reciprocal disadvantage is

\[
\mathscr D=P-C.
\]

Using the positive square roots of the canonical profit blocks,

\[
P>C
\iff
2-3v>2(1-v)(1-2c)
\iff
4c(1-v)>v.
\]

Hence

\[
\boxed{
\mathscr D>0
\iff
c>\frac{v}{4(1-v)}
\iff
v<v_D(c)
\equiv
\frac{4c}{1+4c}.
}
\]

At \(v=v_D(c)\),

\[
N(c,v_D(c))
=
-\frac{4c}{(1+4c)^4}
H(c),
\]

where

\[
H(c)=512c^3-224c^2-241c+18.
\]

Define \(c_\dagger\) as the unique root of \(H\) in \((0,1/3)\). Exact isolation gives

\[
\frac{7078518}{10^8}
<
c_\dagger
<
\frac{7078520}{10^8},
\]

so

\[
c_\dagger\approx0.07078518902206065.
\]

The exact ordering is

\[
0<c_\dagger
<
\frac1{12}
<
\frac19
<
c^\ast
<
\frac13.
\]

Since \(v_D<1/4\) exactly when \(c<1/12\), while \(v_D\) is above the feasibility ceiling for \(c>1/9\), the joint set

\[
\mathcal V_0(c)
=
\{v:\text{feasible},\ \Phi(c,v)>0,\ \mathscr D(c,v)>0\}
\]

is

\[
\boxed{
\mathcal V_0(c)
=
\begin{cases}
\left(v_{SU}(c),v_D(c)\right),
&c_\dagger<c<\frac1{12},\\[4pt]
\left(v_{SU}(c),\bar v(c)\right),
&\frac1{12}\le c<c^\ast,\\[4pt]
\varnothing,
&\text{otherwise}.
\end{cases}
}
\]

Therefore the pre-adoption headline condition \(\mathscr E>\mathscr D>0\) is possible exactly when

\[
\boxed{
c_\dagger<c<c^\ast.
}
\]

An exact rational joint witness is

\[
(c,v)=\left(\frac3{40},\frac9{40}\right),
\]

at which both \(\Phi>0\) and \(\mathscr D>0\).

---

## 6. What survives at zero network effects

### 6.1 Firm adoption

At \(v=0\), the full-bypass thresholds are

\[
\boxed{
T_A(0)=\frac{3c(2-3c)}{16},
}
\]

\[
\boxed{
T_U(0)=T_W(0)
=\frac{3c(2-c)}{16}.
}
\]

Moreover,

\[
T_U(0)-T_A(0)=\frac{3c^2}{8}>0
\]

and

\[
2T_A(0)-T_W(0)
=
\frac{3c(2-5c)}{16}>0
\]

for every \(0<c<1/3\).

Thus a positive selection-free fixed-cost interval remains:

\[
\boxed{
\frac{3c(2-c)}{16}
<
F
<
\frac{3c(2-3c)}{8}.
}
\]

For example, \((c,F)=(1/10,1/20)\) lies strictly inside this interval.

Therefore one-way private circumvention does not require a positive network effect in the canonical Cournot adoption game.

### 6.2 Government preference

By contrast,

\[
\Phi(c,0)<0
\]

throughout \(0<c<1/3\). Hence the member government already prefers IS to SU before private adoption. The SU-to-IS **ranking reversal** cannot occur at \(v=0\), even though one-way private adoption can.

This is the key separation required by R4.

---

## 7. R3 partial erosion at zero network effects

R3 established

\[
W_M^{SU,O}(d)-W^{IS}
=
-\mathscr D+R(d,v),
\]

where

\[
R(d,v)
=
\frac{
d[(5-4v)d+2(1-4v)]
}{
32(1-v)^2
}.
\]

At \(v=0\),

\[
\boxed{
R(d,0)=\frac{d(5d+2)}{32}.
}
\]

Thus the partial-erosion identity remains well-defined and exact when network effects vanish.

Also,

\[
\mathscr E(c,0)
=
\frac{c(5c+2)}{32}
=
R(c,0),
\]

and

\[
\mathscr D(c,0)
=
\frac{c(1-c)}4.
\]

Because \(R(d,0)\) is strictly increasing in \(d\ge0\), for \(0\le d<c\),

\[
R(d,0)<\mathscr E(c,0).
\]

So private adoption can still increase the government's relative incentive for IS at \(v=0\). It simply cannot produce an SU-to-IS reversal because SU was not preferred initially.

The network comparative static of the residual rent is

\[
\frac{\partial R}{\partial v}
=
\frac{
d(2dv-3d+4v+2)
}{
16(v-1)^3
}.
\]

For \(d>0\), \(0<v<1/4\), and \(d\le c<1/3\), the numerator is positive and the denominator is negative, so

\[
\frac{\partial R}{\partial v}<0.
\]

Positive network effects therefore reduce the residual post-adoption member-market rent in this R3 extension, but they are not required for the identity itself.

---

## 8. Stage-by-stage role of network effects

| Result / mechanism | v=0成立 | positive v required? | Certified condition |
|---|---:|---:|---|
| outsider-only adoption | YES | NO | at \(v=0\), \(T_W<F<2T_A\) is nonempty for all \(0<c<1/3\) |
| adoption equilibrium uniqueness / selection-free continuation | YES | NO | strict threshold ordering; R2 dominance logic |
| initial SU preference | NO | YES in current Cournot microfoundation | \(0<c<c^\ast\) and \(v>v_{SU}(c)\) |
| reciprocal disadvantage \(\mathscr D>0\) | YES | NO | \(v<v_D(c)=4c/(1+4c)\) |
| partial erosion identity | YES | NO | \(R(d,0)=d(5d+2)/32\) |
| private adoption raises relative IS incentive | CAN | NO | \(R(d)<\mathscr E\); at \(v=0\), any \(d<c\) |
| SU→IS ranking reversal | NO | YES in current Cournot microfoundation | initial SU preference plus post-adoption \(R(d)<\mathscr D\) |
| coalition-stability change | R6 | R6 | institution-dependent; not certified in R4 |

The table deliberately distinguishes an incentive change from an actual ranking reversal.

---

## 9. Singleton-network specification audit

The canonical primitive is

\[
u+g_i^k-p_i^k,
\qquad
p_i^k=1+g_i^k-\sum_jq_j^k,
\]

with

\[
g_i^k
=
v\sum_{j\in G_i^k}q_j^k
\quad\text{only if }|G_i^k|\ge2,
\]

and

\[
g_i^k=0
\quad\text{for a singleton group}.
\]

This convention affects every pre-adoption block containing a singleton:

- SU member market: outsider block \(B\), and strategically \(A,K_M\);
- SU outsider market: native-outsider block \(D\), and strategically \(C,K_O\);
- SW: all firms are singletons, so its canonical product-market blocks are independent of \(v\);
- one-adopter continuation states: the remaining non-adopter is a singleton.

It does **not** directly affect complete-compatibility IS, nor the R3 post-adoption member market once all three firms are compatible.

A deliberately minimal sensitivity model, S1, removes only the singleton exception and assigns the same own-group formula to every compatibility group. S1 is analyzed separately in `04_singleton_network_sensitivity.md`; it is not a replacement for the canonical model.

The certified S1 result is strong: on the **original canonical feasible domain**, the pre-adoption SU advantage disappears everywhere,

\[
\Phi_{S1}(c,v)<0.
\]

At the same time, a one-way-adoption interval still exists at the canonical witness \((c,v)=(1/10,6/25)\).

Therefore the zero-benefit singleton convention is not a harmless normalization for the initial political ranking. It is a substantive assumption supporting the particular Cournot microfoundation's SU advantage, while neither the abstract R2 one-way-adoption mechanism nor the R3 all-compatible residual-rent formula logically depends on that convention.

No claim is made that S1 is the unique alternative specification or that all alternatives eliminate the SU advantage.

---

## 10. Adversarial checks

A. **Root uniqueness:** certified by Descartes transforms plus exact coefficient-sign/Sturm checks; no grid inference.

B. **Feasibility:** roots are counted only after mapping the correct fixed-\(c\) open interval.

C. **Open boundary:** positive boundary values at \(v=1/4\) or \(v=\bar v(c)\) imply an interior positive neighborhood only by continuity; the boundary itself is never included.

D. **Cubic roots:** \(c^\ast\) and \(c_\dagger\) are defined by exact cubics and rational isolating intervals, not floating-point roots.

E. **Joint region:** \(\Phi>0\) and \(\mathscr D>0\) are intersected at the same \((c,v)\); separate existence is not used.

F. **Firm/government separation:** zero-network private adoption survives while the pre-adoption SU preference does not.

G. **R3 boundary extension:** for \(v=0\), \(0\le d\le c<1/3\) preserves the R3 interior quantity condition \(1-3d>0\).

H. **Specification sensitivity:** S1 is labelled as a separate sensitivity model and is not used to prove a canonical theorem.

I. **No plot proof:** all general statements are backed by exact factorization, polynomial signs, Descartes/Sturm counts, or rational witnesses.

---

## 11. R4 theorem status

| ID | Result | Status |
|---|---|---|
| N1 | no initial SU advantage at \(v=0\) | **PROVED** |
| N2 | complete characterization of \(\mathcal V_{SU}(c)\) | **PROVED** |
| N3 | SU advantage is possible iff \(0<c<c^\ast\) | **PROVED** |
| N4 | joint \(\Phi>0,\mathscr D>0\) region | **PROVED** |
| N5 | one-way private adoption can occur at \(v=0\) | **PROVED** |
| N6 | R3 partial-erosion identity survives at \(v=0\) | **PROVED** |
| N7 | singleton-network specification dependence | **CONDITIONAL** — S1 is fully proved; no universal statement over all alternative network specifications is claimed |

---

## 12. Route decision

R4 does not overturn R2 or R3. It sharpens their interpretation.

- R2's one-way-adoption logic survives at zero network effects.
- R3's residual-rent/partial-erosion identity also survives at zero network effects.
- The **current Cournot microfoundation's initial SU advantage**, and therefore its SU-to-IS reversal path, requires positive network effects on a precisely characterized parameter region.
- The initial SU advantage is additionally sensitive to the zero-benefit singleton convention.

Accordingly,

\[
\boxed{
\text{Route A remains provisionally open, with explicit specification dependence.}
}
\]

The pre-specified R5 competition-form test is authorized. R5 must be treated as a portability test, not as a search for a successful alternative model. A failure of the initial-SU condition under the pre-specified differentiated-Bertrand model would materially strengthen the case for Route B or C at the later route gate.

**R5 is not started in this stage.**

---

## 13. Reproducibility

Machine verification:

`python code/revision/check_r4_network_role.py`

The script checks the canonical identity, feasibility split, exact boundary formulas, root counts, algebraic-root isolation, reciprocal-disadvantage condition, zero-network adoption thresholds, R3 zero-network residual-rent formula, rational witnesses, and the S1 sensitivity result.

The earlier `docs/revision/04_network_role_precheck.md` is retained unchanged as a historical precheck. Its result is now subsumed by N1.
