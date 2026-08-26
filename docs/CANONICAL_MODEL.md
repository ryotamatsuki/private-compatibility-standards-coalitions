# Canonical Model

This document is the mathematical source of truth for the Stage-8 frozen theory. It records definitions, formulas, assumptions, and verified relationships only. If any expression conflicts with the model primitives, follow the inconsistency procedure in [`../AGENTS.md`](../AGENTS.md); do not silently edit the theory and continue.

## 1. Players and Market Sizes

Countries and domestic firms:

\[
N=\{1,2,3\}.
\]

Main Model:

\[
m_1=m_2=m_3=1.
\]

Secondary market-size result only:

\[
m_1=m_2=1,
\qquad
m_3=1-\delta,
\qquad
0<\delta<1.
\]

The parameter \(\delta\) is not required for the Main mechanism.

## 2. Formal Standards Partitions

Separate national standards:

\[
\rho^{SW}=\{\{1\},\{2\},\{3\}\}.
\]

Regional standardization unions:

\[
\rho_{12}^{SU},
\qquad
\rho_{13}^{SU},
\qquad
\rho_{23}^{SU}.
\]

International standardization:

\[
\rho^{IS}=\{\{1,2,3\}\}.
\]

Use \(\rho\) for the formal partition. The symbol \(P\) is reserved for a Cournot profit block.

## 3. Timing

\[
\rho
\rightarrow
a^\ast(\rho,F)
\rightarrow
q^\ast(\rho,a^\ast)
\rightarrow
W_i(\rho,F)
\rightarrow
\mathcal S(F).
\]

Interpretation:

1. formal government partition;
2. private standard adoption;
3. Cournot competition;
4. government continuation welfare;
5. coalition stability.

## 4. Consumer Primitives and Demand

Consumer type:

\[
u\sim U[0,1].
\]

Utility from buying firm \(i\)'s product in market \(k\):

\[
u+g_i^k-p_i^k.
\]

Outside option:

\[
0.
\]

Let \(G_i^k\) denote the compatible group containing firm \(i\) in market \(k\). If

\[
|G_i^k|\ge2,
\]

then

\[
g_i^k
=
v\sum_{j\in G_i^k}q_j^k.
\]

For a singleton compatible group,

\[
g_i^k=0.
\]

Inverse demand:

\[
p_i^k
=
1+g_i^k-\sum_j q_j^k.
\]

## 5. Costs and Private Adoption

Compatible or domestic standard:

\[
MC=0.
\]

Foreign incompatible standard:

\[
MC=c.
\]

Additional-standard adoption cost:

\[
F>0.
\]

An additional formal standard is adopted once and the fixed cost is paid once, not once per market. If a firm adopts a bloc standard, the adoption applies to the markets covered by that bloc standard.

## 6. Government Objective

\[
W_i=CS_i+\Pi_i.
\]

Here \(\Pi_i\) is the worldwide profit of country \(i\)'s domestic firm, net of its private adoption costs. Foreign-firm profit is not included in domestic national welfare. Transfers are absent from the canonical model.

## 7. Canonical Parameter Domain

\[
\boxed{
\Theta_0
=
\left\{
(c,v,F):
F>0,
\quad
0<v<\frac14,
\quad
0<c<\frac{1-3v}{3(1-v)}
\right\}.
}
\]

Within this domain, the required Cournot quantities are strictly positive, total market quantity is below one in the relevant subgames, and consumer demand is interior.

Use **interior consumer participation**, not “full market participation.”

## 8. Cournot Building Blocks

### 8.1 Complete Compatibility

\[
q_I=\frac{1}{4(1-v)},
\qquad
P=\frac{1}{16(1-v)}.
\]

### 8.2 SU Member Market

Compatible zero-cost bloc firm:

\[
q_M
=
\frac{1+c}{2(2-3v)}.
\]

Excluded outsider:

\[
q_B
=
\frac{1-3c-3(1-c)v}{2(2-3v)}.
\]

Profit blocks:

\[
A
=
\frac{(1-v)(1+c)^2}{4(2-3v)^2},
\]

\[
B
=
\frac{[1-3c-3(1-c)v]^2}{4(2-3v)^2}.
\]

### 8.3 SU Outsider Market

Bloc firm:

\[
q_C
=
\frac{1-2c}{2(2-3v)}.
\]

Native outsider firm:

\[
q_D
=
\frac{1+2c-3v}{2(2-3v)}.
\]

Profit blocks:

\[
C
=
\frac{(1-v)(1-2c)^2}{4(2-3v)^2},
\]

\[
D
=
\frac{(1+2c-3v)^2}{4(2-3v)^2}.
\]

### 8.4 Separate National Standards (SW)

Native firm:

\[
q_H=\frac{1+2c}{4},
\qquad
H=\frac{(1+2c)^2}{16}.
\]

Foreign firm:

\[
q_S=\frac{1-2c}{4},
\qquad
S=\frac{(1-2c)^2}{16}.
\]

### 8.5 Consumer Surplus Blocks

\[
K_I
=
\frac{9}{32(1-v)^2},
\]

\[
K_M
=
\frac{(3-c-3v+3cv)^2}{8(2-3v)^2},
\]

\[
K_O
=
\frac{(3-2c-3v)^2}{8(2-3v)^2},
\]

\[
K_W
=
\frac{(3-2c)^2}{32}.
\]

## 9. Corrected Welfare Expressions

International standardization:

\[
\boxed{
W^{IS}
=
K_I+3P
=
\frac{3(5-2v)}{32(1-v)^2}.
}
\]

SU member without private bypass:

\[
\boxed{
W_M^{SU,N}
=
K_M+2A+C.
}
\]

SU outsider without private bypass:

\[
\boxed{
W_O^{SU,N}
=
K_O+2B+D.
}
\]

Separate national standards:

\[
\boxed{
W^{SW}
=
K_W+H+2S
=
\frac{28c^2-20c+15}{32}.
}
\]

Verified relationships on \(\Theta_0\):

\[
W_M^{SU,N}>W^{SW},
\]

\[
W^{IS}>W^{SW},
\]

\[
W^{IS}>W_O^{SU,N}.
\]

### Historical Error — Do Not Reuse

The old incorrect IS expression is

\[
\frac{3(5-v)}{32(1-v)^2}.
\]

It may appear only when explicitly labelled as a historical error. It is not a canonical welfare formula.

## 10. Private-Adoption Thresholds

Define

\[
T_A=P-B,
\]

\[
T_U=A-C,
\]

\[
T_W=A-S.
\]

The unilateral SU-member adoption threshold satisfies

\[
T_U
=
\frac{3c(2-c)(1-v)}{4(2-3v)^2}.
\]

The difference between the SW unilateral threshold and the SU-member unilateral threshold is

\[
T_W-T_U
=
\frac{v(1-2c)^2(8-9v)}{16(2-3v)^2}
>0.
\]

Therefore

\[
T_W>T_U.
\]

On \(\Theta_0\),

\[
T_A>0,
\qquad
T_U>0,
\qquad
T_W>0.
\]

For an SU coalition \(C=\{i,j\}\) with outsider \(o\), outsider adoption of the bloc standard is profitable when

\[
F<(m_i+m_j)T_A.
\]

For a member adopting the outsider standard, the unilateral threshold is

\[
F<m_oT_U
\]

when the other member has not adopted, and

\[
F<m_oT_A
\]

when the other member has adopted.

For SW, the foreign-standard adoption subgame for target market \(k\) has unilateral threshold \(m_kT_W\) and post-rival-adoption threshold \(m_kT_A\).

## 11. Main \(F\)-Thresholds

Define

\[
F_L=\max\{T_W,T_A\},
\]

\[
F^\ast=2T_A.
\]

The Main-Theorem region requires

\[
F_L<F^\ast.
\]

High fixed cost:

\[
F>F^\ast.
\]

Intermediate fixed cost:

\[
F_L<F<F^\ast.
\]

A sufficient low-\(F\) region for universal multistandarding in the symmetric model is

\[
0<F<\min\{T_U,T_A\}.
\]

## 12. Government Continuation Payoffs under SU

Let \(C=\{i,j\}\) be the regional coalition, \(o\) the outsider, and

\[
M_C=m_i+m_j.
\]

No bypass, coalition member \(i\):

\[
W_i^{SU,N}
=
m_iK_M+M_CA+m_oC.
\]

No bypass, outsider:

\[
W_o^{SU,N}
=
m_oK_O+M_CB+m_oD.
\]

International standardization:

\[
W_i^{IS}
=
m_iK_I+(m_1+m_2+m_3)P.
\]

Outsider-only bypass, coalition member \(i\):

\[
W_i^{SU,O}
=
m_iK_I+M_CP+m_oC.
\]

Outsider-only bypass, outsider:

\[
W_o^{SU,O}
=
m_oK_O+M_CP+m_oD-F.
\]

## 13. Selective-Erosion Decomposition

For coalition member \(i\), define the net exclusion surplus in coalition-member markets:

\[
\boxed{
\mathscr E_i
=
m_i(K_M-K_I)+M_C(A-P).
}
\]

Define the reciprocal disadvantage in the outsider market:

\[
\boxed{
\mathscr D_i
=
m_o(P-C).
}
\]

Without private bypass:

\[
\boxed{
W_i^{SU,N}-W_i^{IS}
=
\mathscr E_i-\mathscr D_i.
}
\]

With outsider-only private bypass:

\[
\boxed{
W_i^{SU,O}-W_i^{IS}
=
-\mathscr D_i.
}
\]

Central identity:

\[
\boxed{
\mathscr E_i-\mathscr D_i
\longrightarrow
-\mathscr D_i.
}
\]

## 14. Primitive Reciprocal-Disadvantage Condition

\[
P>C
\iff
c>\frac{v}{4(1-v)}.
\]

This is the primitive condition generating \(\mathscr D_i>0\) when the outsider market has positive mass.

## 15. Main Open Parameter Set

In the symmetric Main Model,

\[
\mathscr E
=
(K_M-K_I)+2(A-P),
\]

\[
\mathscr D
=
P-C,
\]

\[
\Phi_0
=
\mathscr E-\mathscr D
=
W_M^{SU,N}-W^{IS}.
\]

Define

\[
\boxed{
\Omega_0
=
\left\{
(c,v):
0<v<\frac14,
\quad
0<c<\frac{1-3v}{3(1-v)},
\quad
\Phi_0>0,
\quad
P>C,
\quad
\max\{T_W,T_A\}<2T_A
\right\}.
}
\]

This definition writes the \((c,v)\) projection of the baseline admissible domain explicitly; \(F\) is selected separately by the high- or intermediate-\(F\) theorem region.

Verified witness:

\[
(c,v)=(0.10,0.24).
\]

At this point,

\[
T_U\approx0.0661011,
\]

\[
T_A\approx0.0818242,
\]

\[
T_W\approx0.1003198,
\]

\[
\mathscr E\approx0.0161623,
\]

\[
\mathscr D\approx0.00801809,
\]

\[
\Phi_0\approx0.00814425>0.
\]

The witness is for nonemptiness and numerical verification; it is not a substitute for the analytical argument.

## 16. Coalition Stability

The canonical solution concept is strict blocking in an exclusive-membership partition game. A deviating coalition blocks a partition only when every deviator is strictly better off under the induced alternative partition.

For every \((c,v)\in\Omega_0\):

### High \(F\)

If

\[
F>2T_A,
\]

then

\[
\boxed{
\mathcal S(F)
=
\left\{
\rho_{12}^{SU},
\rho_{13}^{SU},
\rho_{23}^{SU}
\right\}.
}
\]

Do not claim a unique \(SU_{12}\) in the symmetric Main Model.

### Intermediate \(F\)

If

\[
F_L<F<2T_A,
\]

then

\[
\boxed{
\mathcal S(F)=\{\rho^{IS}\}.
}
\]

Thus the Main applied result is a stability transition from the set of regional SUs to international standardization as private compatibility becomes sufficiently cheaper.

## 17. Secondary Market-Size Result

For

\[
m_1=m_2=1,
\qquad
m_3=1-\delta,
\qquad
0<\delta<1,
\]

and no private adoption,

\[
W_1^{12}-W_1^{13}
=
\delta(A-C)>0.
\]

This identifies the preferred regional partner. It is secondary and does not generate the Main selective-erosion mechanism.

## 18. Low-\(F\) Result

For sufficiently low \(F>0\) in the symmetric model, universal private multistandarding makes effective product-market compatibility identical to IS while fragmented formal regimes retain duplicate adoption costs:

\[
W_i^{SU}=W_i^{IS}-F,
\]

\[
W_i^{SW}=W_i^{IS}-2F.
\]

This is an Appendix result, not the central contribution.

## 19. Network-Effect Status

Do not state that network effects are necessary for the general selective-erosion mechanism.

Canonical positioning:

> Network effects are accommodated by the model and can affect formal coalition incentives, but the general selective-erosion mechanism is not fundamentally a network-externality theorem.

## 20. Canonical Paper Identity

The theoretical spine to preserve in all later work is:

\[
\boxed{
\text{canonical Cournot standards model}
\rightarrow
\text{selective-erosion theorem}
\rightarrow
\text{three-country microfoundation}
\rightarrow
\text{regional SU}\rightarrow\text{IS stability reversal}
}
\]
