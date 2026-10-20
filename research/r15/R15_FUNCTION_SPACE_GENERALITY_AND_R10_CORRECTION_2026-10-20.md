# R15 — Independent admissibility audit and an infinite-dimensional nonlinear-demand theorem

**Checkpoint: 2026-10-20. Research only.** Do not alter the original R9 science, PR #34 JICT short candidate, R12 PR #37, R13 PR #38, or R14 PR #39. Current R15 source branch is a descendant of R14 and adds a new manuscript subsection as an exact append-only extension to the R13 chapter.

## 1. Material correction: R10 old joint Cournot–Bertrand witness is not valid in the R9/R13 consumer-expectations class

R10's differentiated-demand test starts with
\[
M_0=(1-\gamma)I+\gamma\mathbf1\mathbf1^{\top},\qquad
M=M_0-vC,\qquad p=\mathbf1-Mq,
\]
and sets \(CS_{old}=\frac12q^\top Mq\). This quadratic surplus is **internally appropriate to a different consumer environment** where compatible-network benefits are incorporated into the social marginal utility / inverse-price potential. It is **not** the buyer-takes-network-as-given, fulfilled-expectations surplus concept that was explicitly justified for R9/R13. In the latter environment,
\[
U_0(q)=\mathbf1^\top q-\frac12q^\top M_0q,\quad
p=\nabla U_0(q)+vCq,\quad
CS_{FE}=\frac12q^\top M_0q.
\]
The consumer treats \(g=vCq\) as given when choosing; its monetary benefit is capitalized into the observed price. The Cournot/Bertrand firms may account for how their strategies change the fulfilled network equilibrium. **The product-market FOCs, quantities, profits, and firm adoption equilibria are unchanged by this correction; the national consumer-surplus and hence government preference rankings change.**

At R10's former exact common witness
\[
(\gamma,v,c,d,F)=(23/25,33/500,2/125,1/500,1/40),
\]
the independently rederived exact rational SU-minus-IS member-government comparisons are:

| Consumer-welfare convention | Cournot pre / post | Bertrand pre / post |
|---|---:|---:|
| Former R10 internally networkized utility | \(+0.000246089 / -0.000058696\) | \(+0.005408743 / -0.000855474\) |
| **R9/R13 fulfilled expectations** | **\(-0.011737319 / -0.000089653\)** | \(+0.002774007 / -0.000907434\) |

All exact signs are verified by \`research/r15/audit_r10_welfare_convention.py\`. Therefore **the earlier assertion “this one parameter vector proves the same government reversal in Cournot and Bertrand under the existing paper's welfare basis” is withdrawn**. Bertrand reversal survives at this parameter vector; Cournot *does not*, although SU outsider-only and SW no-adoption firm equilibrium selection remain valid.

Do **not** silently correct R10 by choosing whichever consumer-surplus convention makes the desired sign true. The former R10 welfare concept can be studied as a **different** model, but it does not establish the original R9 result's portability under the R13 buyer foundation. The old R10 marginal national-incidence comparisons must also be explicitly relabeled “internally networkized utility”; they are not a national-welfare theorem for the fulfilled-expectations R9 class.

**Negative search, not an impossibility theorem.** A broad exploratory search of differentiated linear models using \(CS_{FE}\), positive outputs and positive-definite full-feedback price matrices found no same-primitive joint Cournot/Bertrand witness in the scanned ranges. This is **NOT** proof of nonexistence; the full-feedback PD restriction excludes the homogeneous-brand R9 limit for many network strengths, and a different regular price-game specification may succeed. Do not generalize this numerical nonfinding.

## 2. Strong positive result: an infinite-dimensional class of nonlinear buyer demands preserves all R9 central results

Work *within exactly* R13's atomistic-buyer, fulfilled-network model, for the homogeneous-brand Cournot subfamily. Rather than demanding linear \(D(Q)=1-Q\), let
\[
p_i(q;s)=D(Q)+G_i(q;s),\quad
Q=\sum_i q_i,\quad
G_i(q;s)=v\sum_j C_{ij}(s)q_j,
\]
with the **original** singleton-zero binary group indicator \(C(s)\), original \(c,d,F\), original 3-country partitions, market separation and firm-owned profit accounting. Define consumers' optimizing surplus
\[
CS_D(Q)=\int_0^Q D(z)\,dz-QD(Q).
\]
Fix original certified numerical primitives
\[
v=6/25,\quad c=1/10,\quad d=1/20,\quad F=9/100,
\]
and write \(D_0(Q)=1-Q\) for the original R9.

**Theorem R15 (nonparametric demand-neighborhood persistence).** There exists \(\eta_*>0\) such that **for every** \(C^2\) inverse willingness-to-pay schedule \(D\) satisfying
\[
\|D-D_0\|_{C^2([0,6])}<\eta_*
\]
(with a decreasing interior inverse demand and suitable harmless extension outside the buyer-relevant quantity range), **every** destination-market subgame for **every** SU/SW/IS adoption profile has a unique regular Cournot equilibrium continuously depending on \(D\); each equilibrium reached in the R9 baseline remains interior. In the discrete post-partition investment stage, SU uniquely selects outsider-only private adaptation, SW uniquely selects no adaptation, and the representative member government strictly prefers SU to IS before adaptation but strictly prefers IS after adaptation.

**Proof in three steps:**

1. The original Cournot FOC for a firm with destination marginal cost \(r_i\) is
\[
\Phi_i(q;D,s)=D(Q)+G_i(q;s)-r_i+
q_i[D'(Q)+vC_{ii}(s)]=0.
\]
At \(D=D_0\), \(D_0'=-1,D_0''=0\), the negative FOC Jacobian is a **symmetric** matrix
\[
J_s=M_s+\mathrm{diag}(\mathrm{diag}M_s),
\quad M_s=\mathbf1\mathbf1^{\top}-vC(s).
\]
Its leading principal minors are strictly positive for every possible 3-firm compatibility pattern (27 labeled patterns, many redundant), as mechanically checked with **exact rational arithmetic**. Thus its smallest eigenvalue, uniformly over the finite set of patterns, is \(\alpha>0\). All relevant baseline equilibrium quantities are positive and their payoffs finite.

2. Let \(\delta D=D-D_0\) with \(\|\delta D'\|_\infty,\|\delta D''\|_\infty<\eta\). For \(q_i\in[0,2]\) the perturbation of the FOC Jacobian entry is
\[
\delta J_{ij}=
(1+\mathbf1_{i=j})\delta D'(Q)+q_i\delta D''(Q),
\]
with \(|\delta J_{ij}|\le4\eta\), hence spectral norm \(\le12\eta\). For \(\eta<\alpha/12\) the symmetric part of the negative FOC Jacobian remains uniformly positive definite. Since each firm's payoffs are strictly concave in its own quantity on the compact strategy box, Rosen's diagonal strict-concavity / strong monotonicity argument yields a **unique** market Nash equilibrium. At the baseline, any \(q_i\ge2\) gives \(p_i\le1-(1-v)Q+\eta<0\), so 0 strictly dominates such outputs (for sufficiently small \(\eta\)): the artificial box does not exclude a profitable output. This is an equilibrium-strategy argument; the unit-demand consumer foundation concerns the interior buyer-clearing outcomes, not extrapolated negative-price off-equilibrium combinations. Local invertibility and strong monotonicity give continuous equilibrium payoffs as \(D\) changes.

3. There are only finitely many adoption profiles. At \(D_0\), the original R9 exact audit established strict SU/SW dominance (uniform investment margin)
\[
\max\{\bar g_H,\bar g_{SW},0\}<F<g_O^0
\]
with max member gain \(\simeq0.0650243\), max SW incremental gain \(\simeq0.0681679\), \(F=0.09\), outsider gain \(\simeq0.1180070\). The original government gaps are **strict**:
\[
\Delta_N(0)=+2408509/295731200>0,\quad
\Delta_O(0)=-1341/184832<0.
\]
All these finitely many stage-game payoffs and welfare values vary continuously with \(D\); hence a common \(\eta_*>0\) preserves their signs simultaneously, the selected pure action profiles, and the policy reversal. \(\square\)

**Quantifier is material.** This is a theorem for **every schedule in a nonempty \(C^2\) ball**, an infinite-dimensional class, not just a particular quadratic/polynomial alternative. It proves the original core mechanism is **not a knife-edge consequence of exactly linear inverse demand**. The theorem still uses the original firm Cournot conduct, the original network-group rule, and original model's market separation. It does **not** establish arbitrary Bertrand equilibrium existence or universality of government reversal across all demand schedules.

**Existence robustness is not free novelty.** The strong-monotonicity tool is classical: Rosen (1965), *Existence and Uniqueness of Equilibrium Points for Concave N-Person Games*, Econometrica 33(3):520–534, DOI 10.2307/1911749. The research contribution would be showing the **joint endogenous compatibility/policy** mechanism persists over that functional neighborhood, not inventing Rosen's uniqueness theorem.

## 3. Explicit non-linear demand exemplar, economically grounded

As an independently reproducible illustration (not a substitute for the open-ball theorem), choose
\[
D_\varepsilon(Q)=1-Q+\varepsilon\,\frac{Q^2}{4(1+Q^2)},
\quad\varepsilon=1/100.
\]
This is smooth and strictly decreasing on the buyer-relevant interior; consumer surplus follows **from the same inverse quantile**, not from a separately selected welfare proxy:
\[
CS_\varepsilon(Q)=\frac{Q^2}{2}
+\frac{\varepsilon}{4}
  \left(Q-\arctan Q-\frac{Q^3}{1+Q^2}\right).
\]

Compute the nonlinear Cournot FOCs in each destination for **all** 8 SU, 64 SW and 1 IS adoption profiles, including every possible unilateral standard-switching deviation. Under \(v=.24,c=.10,d=.05,F=.09\):

| Certified numerically (double precision; tolerance 1e-10) | Result |
|---|---|
| SU initially preferred to IS | \(+0.008337181\) |
| SU after outsider adapts, relative to IS | \(-0.007230147\) |
| Unique SU pure Nash adoption continuation | outsider alone adds bloc standard |
| Unique SW pure Nash adoption continuation | no firm adapts |
| Strict minimum unilateral SU margin | \(+0.028225974\) |
| Strict minimum unilateral SW margin | \(+0.021617375\) |

All pure investment profiles are evaluated, and market uniqueness is supported by the exact baseline Jacobian certificate and analytically small derivative perturbation. This **numeric instance** is not advertised as an exact rational certificate (the nonlinear roots generally are algebraic/transcendental through the surplus integral). The **existence over a function-space ball** comes from the analytic theorem; the explicit \(\varepsilon=0.01\) calculations are independent supporting evidence rather than its entire proof.

Code: \`research/r15/verify_infinite_dimensional_neighborhood.py\`. Combined R10-correction / nonlinear-microfoundation check: \`research/r15/audit_r10_welfare_convention.py\`; isolated reproducibility workflow: \`.github/workflows/r15-function-space.yml\`.

## 4. Relation to the editor's exact criticisms and possible novelty

- IJIO 2026-09-21 editor explicitly objected to dependence on a stylized three-country Cournot linear-demand calculation, and to the absence of a **portable economic mechanism**. The new **infinite-dimensional demand-neighborhood theorem** rigorously refutes the narrower interpretation that the original preference reversal exists only at one exactly linear demand function.
- The broader R12/R13 sufficient condition (private adoption inequality + consumer-justified domestic welfare incidence) is independent of choosing Cournot or Bertrand *when the specific market equilibrium exists and the inequalities are verified*. Thus **there are two rigorously distinct layers**: (A) general market-conduct **conditional mechanism theorem**, and (B) nonparametric Cournot **nonvacuity/open-set theorem**.
- We must NOT claim layer (B) itself proves portability to non-Cournot *equilibria*. The prior R10 cross-conduct positive witness was invalid under the R13 welfare basis; a fresh consistent Bertrand candidate remains a task, not a current result.
- Katz and Shapiro (1985), *Network Externalities, Competition, and Compatibility*, AER 75(3):424–440, pioneered fulfilled expectations network models. The original article's firm decision may treat consumers' network expectations as fixed **even under firm deviation**. The R9/R13 original Cournot FOCs differentiate the fulfilled network response to an announced firm quantity, a distinct commitment/observability timing assumption. This must be clearly stated to make the microfoundation credible.
- Gandal & Shy (2001), *Standardization Policy and International Trade*, JIE 53:363–383, considers standardization unions and unequal country populations already. Thus R14's size condition is NOT intrinsically novel. What remains potentially distinctive is the **endogenous post-union private adaptation stage causing a government ranking reversal, jointly certified across a neighborhood of demand primitives**.
- The paper's final originality assessment still requires direct theorem-by-theorem primary-source comparison with Buccella–Fanti–Gori (2026) and the above classics. Proving local continuity is not intrinsically new mathematics; demonstrating *this* endogenous government mechanism robustly may still be a legitimate substantive extension.

## 5. Status / kill rules

- **PASS:** R9 immutable source and math; R13 consumer optimization derivation; R14 joint size interval in original Cournot; R15 exact welfare-consistency audit; R15 nonparametric-demand theorem (proof as above); non-linear instantiated full-game calculation.
- **RETRACT:** old R10 “same parameters yield R9-consistent government reversal for both quantity/price competition” claim.
- **OPEN:** consistent price-competition equilibrium with selected adaptation and policy reversal; fully nonparametric primitives that deliver sufficient conditions beyond continuity; closest-original-theorem absorption audit; concise manuscript integration.
- **DO NOT:** modify R9 PR #34, overwrite or delete R10 research logs (retain with dated correction), merge R12–R15 into the journal submission without separate independent review. Page length is explicitly **deferred by user instruction**.
