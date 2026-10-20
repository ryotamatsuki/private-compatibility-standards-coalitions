# R19 strongest proved result; full target not proved

**Executive level: 2.** The requested "Primitive Conditions for Endogenous
Private Compatibility and Institutional Preference Reversal" is NOT
established. Below is the strongest fully proved partial theorem T-R,
not a renamed full mechanism theorem. The independent derivation and
referee proof are both retained. Numerical root examples are explicitly
separated from the all-parameter identities and sign arguments.

# R19 independent derivation: a primitive residual-cost incidence boundary

Research note by the primitive-theory sub-agent, 2026-10-20. This is a
**proved partial theorem**, not proof of all ten R19 Main-Theorem goals.
No original paper, R18 file, or canonical definition is changed.

## Economic primitives and equilibrium discipline

In each destination let baseline consumer utility be

\[
U_0(q)=\mathbf1^\top q-\tfrac12q^\top M_0q,
\quad M_0=(1-\gamma)I+\gamma\mathbf1\mathbf1^\top,
\quad 0\le\gamma\le1.
\]

Consumers take the external network vector as given. In a fully
compatible destination, fulfilled networks are \(v\mathbf1\mathbf1^\top q\).
Thus \(p=\mathbf1-Mq\), \(M=M_0-v\mathbf1\mathbf1^\top\), and
\(CS=q^\top M_0q/2\). At \(\gamma=1\), use exactly R13's
homogeneous uniform-type allocation/clearing foundation (not a strictly
concave representative-buyer fiction). Network singleton-zero conventions
are immaterial in this fully compatible destination but remain mandatory
in all other stages.

The two member firms have unit cost zero; the outsider has residual unit
cost \(d\ge0\). Let \(\ell>0\) denote the common own-markup coefficient
of the **specified** market game: \(p_i-r_i=\ell q_i\). This is a
derived conduct coefficient, not a utility primitive, and is specialized
below separately for Cournot and Bertrand. The general algebra applies
to a game only after its FOC and global Nash conditions have been proved.
It does not establish existence/uniqueness for arbitrary conduct.

Write

\[
b=\gamma-v\ge0,\qquad \tau=1-\gamma+\ell>0,
\qquad \kappa=1+2\gamma-3v+\ell=\tau+3b>0.
\]

The interior market equations are
\((M+\ell I)q=\mathbf1-(0,0,d)^\top\). Their unique solution is

\[
q_1=q_2=x(d)=\frac{\tau+bd}{\tau\kappa},\qquad
q_o=y(d)=\frac{\tau-(\tau+2b)d}{\tau\kappa}.
\]

Restrict to \(0\le d<\bar d=\tau/(\tau+2b)\), so all products
are active. Cournot with own quantity curvature \(1-v>0\) has strict
own concavity and its linear complementarity operator
\(M+\ell I=\tau I+b\mathbf1\mathbf1^\top\) is SPD; hence its
interior solution is the unique global quantity Nash. For differentiated
Bertrand, \(M\) is SPD when \(\gamma<1\) and \(0\le v\le\gamma\),
so fulfilled-expectations consumer demand is uniquely determined by its
complementarity system. The following independent argument establishes
global price Nash and uniqueness **in this fully compatible destination**.
It does not establish those properties for the other, partially
incompatible destinations in the entire adoption game.

**Global price-game lemma (fully compatible state).** Put
\(t=1-\gamma>0\), so \(M=tI+b\mathbf1\mathbf1^\top\). At any
nonnegative price vector, total fulfilled quantity uniquely satisfies
\(Q=\sum_j[1-p_j-bQ]_+/t\). When an active firm's own price rises,
\(Q\) falls and every rival quantity weakly rises, so rivals only
enter the active set. With \(n\) active products its own demand slope
is \(-h_n\), where
\(h_n=(t+(n-1)b)/[t(t+nb)]\). The positive \(h_n\) is weakly
increasing in \(n\) by a Schur-complement identity. Own demand is
continuous and piecewise affine; its slope only jumps downward while
the firm remains active. For prices above own cost, own profit is
strictly concave within each active segment and its derivative jumps
downward at rival-entry boundaries. Thus an interior FOC is a global
best reply over all own-active prices. It also dominates every no-sales
deviation, which earns zero. This proves existence of the displayed
all-active price Nash for \(d<\bar d\).

For uniqueness, an inactive zero-cost member would have positive choke
price \(1-bQ\), since with nonnegative prices and \(n\) active brands,
\(Q\le n/(t+nb)<1/b\) when \(b>0\). It could profitably enter;
the case \(b=0\) has choke one directly. Hence both members are active
at any Nash. If only the outsider were inactive, no profitable entry
would require \(\chi=1-bQ\le d\). The greatest possible absolute
own-price demand slope is \(h_3=1/\ell\). Absence of a profitable
small **upward** price deviation for member \(i\) therefore requires
\(q_i\le p_i/\ell\), including the kink where outsider entry begins.
Summing and using \(p_1+p_2=2-(t+2b)Q\) implies
\(Q\le2/(t+2b+\ell)\), hence
\(\chi\ge(t+\ell)/(t+2b+\ell)=\bar d\), contradicting
\(d<\bar d\). Active firms cannot have nonpositive markups at Nash:
negative margin is dominated by no sales, while at zero margin and
positive demand a small upward price deviation is profitable. Finally,
all-active prices are smooth and solve the invertible SPD linear system,
so their solution is unique. This completes global existence and
uniqueness in the fully compatible residual family. QED.

For a member government's combined component from the two symmetric
member destinations,

\[
m_C(d)=CS(d)+2\ell x(d)^2
=(1+\gamma+2\ell)x(d)^2+2\gamma x(d)y(d)+\tfrac12y(d)^2.
\]

The two domestic-profit terms arise from **the same home firm's profits
in two symmetric destinations**; this is not a change to the national
ownership welfare convention.

## Theorem T-R: sharp residual-cost incidence

Define primitive/conduct expressions

\[
\rho=1+2\gamma-\frac{4\ell b}{\tau},\qquad
A=\tau^2+4(1-\gamma)\tau b+
       [6(1-\gamma)+4\ell]b^2>0.
\]

Then throughout the stated interior domain,

\[
\boxed{R_{\gamma,v,\ell}(d):=m_C(d)-m_C(0)
=\frac{-\rho d+A d^2/(2\tau^2)}{\kappa^2}.}
\]

Consequently \(R''=A/(\tau^2\kappa^2)>0\). If \(\rho\le0\),
then \(R\) is nondecreasing on \(d\ge0\) (strict away from the
possible endpoint \(d=\rho=0\)). If \(\rho>0\), then its unique
unconstrained minimum is

\[
d_{\min}=\rho\tau^2/A,
\]

and \(R\) is strictly decreasing before that minimum and increasing
afterward. It is negative on \(0<d<2d_{\min}\), and returns to zero
at \(2d_{\min}\), subject always to truncation at \(\bar d\) and
the technological restriction \(d\le c\).

**Proof.** Solving the symmetric two-equation system gives \(x,y\).
Substitute those affine quantities into the displayed quadratic welfare
expression. The linear coefficient is
\([-(1+2\gamma)+4\ell b/\tau]/\kappa^2\), and direct expansion
of the quadratic coefficient yields \(A/(2\tau^2\kappa^2)\).
Every term of \(A\) is nonnegative for the specified domain and
\(\tau^2>0\). Differentiating the polynomial gives all monotonicity,
minimum and zero assertions. No welfare sign is assumed. QED.

### Separate conduct derivations and the strict contrast

**Original homogeneous R9 Cournot.** Set \(\gamma=1\) and
\(\ell=1-v\), derived by differentiating the original firm's
quantity profit while anticipating fulfilled expectations. Then
\(\rho=4v-1<0\) for \(0\le v<1/4\), and the theorem gives

\[
R(d)=\frac{d[(5-4v)d+2(1-4v)]}{32(1-v)^2},
\]

**exactly** the R9 residual-rent function. Its positive slope is preserved.

**Differentiated Bertrand.** For \(0\le v\le\gamma<1\), invert
the fully compatible demand matrix. Own price FOC gives

\[
\ell=1/(M^{-1})_{ii}
=\frac{(1-\gamma)(1+2\gamma-3v)}{1+\gamma-2v}>0.
\]

Substitution gives

\[
\rho=
\frac{2\gamma^2-10\gamma v-3\gamma+12v^2+v-2}
     {-3\gamma+5v-2}>0.
\]

To prove the strict sign, the denominator is at most
\(2\gamma-2<0\). The numerator is convex in \(v\). Its endpoint
values over \([0,\gamma]\) are
\((2\gamma+1)(\gamma-2)<0\) at zero and
\(2(\gamma-1)(2\gamma+1)<0\) at \(\gamma\), so convexity bounds
it above by a strictly negative endpoint maximum. Thus **every** such
substitute differentiated-Bertrand interior branch has \(R'(0)<0\),
the opposite of R9's \(R'(0)>0\). This is a primitive sign theorem,
not a re-labelled R18 envelope.

**The contrast is not attributable solely to conduct.** Under
differentiated Cournot, \(\ell=1-v\) and

\[
\rho_C=
\frac{2\gamma^2-2\gamma v+\gamma+4v^2-3v-2}
     {\gamma+v-2}.
\]

For \(0\le v<1/4\) and \(v\le\gamma\le1\), the unique primitive
substitution threshold is

\[
\gamma_C^*(v)=
\frac{2v-1+\sqrt{17+20v-28v^2}}4\in(v,1).
\]

One has \(\rho_C>0\) below this threshold, zero at equality, and
\(\rho_C<0\) above it. To see uniqueness, the numerator has derivative
\(4\gamma-2v+1>0\) on the stated domain; its values at \(\gamma=v\)
and one are respectively \(2(2v+1)(v-1)<0\) and
\((4v-1)(v-1)>0\), while the denominator is negative. Thus
R9's increasing residual-protection effect requires sufficiently strong
substitution in this extended Cournot family; price versus quantity
competition alone is not an adequate explanation of the sign contrast.
This analytic threshold is an additional proved primitive boundary.

## Endogenous-adoption/policy comparative-static corollary

Keep the outsider's pre-adoption operating profit per member destination
\(\pi_o^B(c)\) fixed. Its two-destination gross adoption benefit is

\[
G_o(d)=2[\ell y(d)^2-\pi_o^B(c)].
\]

On \(0\le d<\bar d\),

\[
G_o'(d)=-\frac{4\ell(\tau+2b)y(d)}{\tau\kappa}<0.
\]

For fixed real adoption fee \(F>0\), its strict adoption condition
against nonadopting members is equivalent to

\[
d<d_A:=\frac{\tau}{\tau+2b}
\left[1-\kappa\sqrt{\frac{\pi_o^B(c)+F/2}{\ell}}\right],
\]

provided \(d_A>0\) and intersecting \([0,\bar d)\). This is the
outsider's exact best-response threshold; it alone does **not** exclude
member investments or alternative investment equilibria. At the R16
primitives, \(\pi_o^B(c)=511244968167/31263041459387500\) and
\(d_A\approx0.01058951937\), so the actual \(d=0.002\) lies
strictly below it. The cutoff lies below \(c=0.016\): eventual
outsider non-adoption limits the observed policy comparative statics.

Outsider adoption is therefore privately less attractive as residual cost
increases. If \(\rho>0\) and \(d<d_{\min}\), the **same** change
lowers member national welfare in SU, so it increases the member's
relative IS preference. These opposing directions coexist on any
interval on which strict outsider-only adoption is actually sustained;
the corollary does not assert that such an equilibrium is sustained for
all \(d\), and does not assume the initial SU ranking.

Economics: residual import cost shifts sales toward the two member
firms, but the baseline consumption loss outweighs their producer gain
when \(4\ell b/\tau<1+2\gamma\). This inequality is automatically
true under the stated differentiated-Bertrand primitive range, whereas
the original homogeneous Cournot branch reverses it at \(v=1/4\).
Thus a larger *private* compatibility gain is not a universal sufficient
statistic for the government's institutional preference.

## Sharp post-adoption institutional boundary

Let \(D=f_C-f_B(c)>0\) be the export disadvantage, derived from its
own destination market. National accounting gives
\(W_M^{SU,O}(d)-W_M^{IS}=R(d)-D\). The unique positive untruncated
root is

\[
d_D=\frac{\rho\tau^2+
\sqrt{\rho^2\tau^4+2A D\tau^2\kappa^2}}{A}.
\]

The strict post-adoption IS ranking holds for \(0\le d<d_D\),
again intersected with the active-product, technological and endogenous
adoption domains. This is a closed-form boundary **conditional on a
separately established export loss**, not a primitive proof that
\(D>0\) or that the initial SU ranking holds. Those remain obstacles
to the full R19 Level-3 theorem.

## Exact R16 witness and scope

At \(\gamma=23/25,v=33/500\),
\(\ell=1321/11175\), \(\tau=443/2235\),
\(\rho=222258/276875>0\),
\(d_{\min}=4923014700/123066192803\approx0.0400029820\),
and \(\bar d=22150/213019\approx0.1039813350\).
The actual \(d=1/500,c=2/125\) obey
\(0<d<c<d_{\min}\). Thus the residual-cost comparison has the
opposing directions across the entire technological range \([0,c]\)
on the valid full-compatibility interior branch. This alone does not
certify the entire investment game over that range.

**What is proved beyond R18:** a closed primitive sign restriction,
strict convex residual-incidence shape, explicit minimum and zero,
conduct-specific opposite signs proved over classes (not single points),
and a joint private-gain/policy comparative-static opposition.

**What is not proved:** full main Level-3 theorem, common all-stage
primitive adoption inequalities, initial SU superiority without the
R18 response envelopes, general nonlinear price-game uniqueness, or
scholarly priority of this partial theorem. A novelty audit must compare
standard oligopoly national-incidence/pass-through results before
calling the contrast independently new. The \(R(d)-D\) identity and
quadratic root alone are not original economic mechanisms.
