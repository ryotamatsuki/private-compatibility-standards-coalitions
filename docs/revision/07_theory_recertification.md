# R7 — Theory Re-Certification and Claim-Scope Freeze

## Verdict

**MATHEMATICAL CORE RE-CERTIFIED SUBJECT TO FINAL CI — ROUTE B**

Input integration commit:

`b45798f003db52a980f8f9b21186f054ebe62007`

R7 performs an independent reconstruction rather than treating earlier green verification scripts as independent evidence. Production manuscript files remain unchanged.

## 1. Independent reconstruction

The clean-room evaluator `code/revision/check_r7_cleanroom.py` does not import `code/canonical.py` or any R2–R6 verification module.

It reconstructs the canonical Cournot first-order systems directly from the primitive inverse demand, independently solves the relevant product-market states, rebuilds consumer surplus, and then reconstructs the welfare and adoption objects needed by R3–R6.

The independent path reproduces:

- complete-compatibility quantities and profits;
- SU member-market and outsider-market blocks;
- SW blocks;
- the identity
  [
  W_M^{SU,N}-W^{IS}=mathscr E-mathscr D;
  ]
- the R3 partial-adoption residual-rent identity;
- the re-solved R3 adoption thresholds and the exact joint witness;
- the R4 zero-network boundary;
- the reciprocal-disadvantage factorization;
- the R5 common counterexample/witness under independently reconstructed differentiated demand;
- the R6 symmetry-indifference and market-size partner-selection identities.

This clean-room route is deliberately narrower than a complete alternative symbolic proof of every polynomial sign certificate. R4 root-count certificates and R5 full-box Bernstein certificates remain backed by their stage-specific exact proof artifacts; R7 independently reconstructs their economic inputs and exact witness implications.

## 2. Re-certified R3 result

Let

[
d=lambda c,qquad 0lelambdale1.
]

After outsider adoption, the independently solved member-market quantities are

[
x(d)=rac{1+d}{4(1-v)},
qquad
y(d)=rac{1-3d}{4(1-v)}.
]

The member-government post-adoption gap is exactly

[
oxed{
W_M^{SU,O}(d)-W^{IS}
=
-mathscr D+R(d,v)
}
]

with

[
oxed{
R(d,v)
=
rac{d[(5-4v)d+2(1-4v)]}
{32(1-v)^2}.
}
]

On the canonical network domain (0le v<1/4), (R) is strictly increasing in (dge0).

Conditional on the initial preference condition

[
mathscr E>mathscr D>0,
]

the exact classification is:

[
R(d)<mathscr D
quadLongleftrightarrowquad
	ext{post-adoption ranking favors IS},
]

[
R(d)<mathscr E
quadLongleftrightarrowquad
	ext{private adoption increases the relative incentive for IS}.
]

Hence:

- (R<mathscr D): actual SU-to-IS reversal;
- (mathscr D<R<mathscr E): IS incentive strengthens but SU remains preferred;
- (R>mathscr E): the relative IS incentive weakens.

These are **canonical-microfoundation** statements. R7 does not promote them to a functional-form-independent theorem.

## 3. Joint firm/government certificate

At the exact primitives

[
(c,v,lambda,F)
=
left(
rac1{10},
rac6{25},
rac12,
rac9{100}
ight),
]

the clean-room evaluator independently confirms:

- initial SU preference;
- incomplete adaptation (0<lambda<1);
- outsider adoption is strictly profitable;
- both reverse-member adoption restrictions hold;
- SW remains non-adopting under the required threshold;
- the post-adoption member government strictly prefers IS.

All inequalities are strict, and all relevant expressions are continuous on the interior domain. Therefore a nonempty open set of the same joint property exists.

This re-certifies G2-J as an **existence/open-set** claim, not a global characterization of every primitive.

## 4. R4 scope certificate

At the zero-network boundary,

[
oxed{
W_M^{SU,N}-W^{IS}
=
rac{c(13c-6)}{32}<0
qquad (0<c<1/3).
}
]

Therefore the canonical SU-to-IS reversal route cannot start at (v=0), because SU is not initially preferred.

The independent reconstruction also confirms the reciprocal-disadvantage factorization and hence the certified condition

[
mathscr D>0
iff
4c(1-v)>v
]

on the canonical domain.

The exact R4 root characterization of the positive-(Phi) region remains certified by the exact Descartes/Sturm artifact from R4. R7 finds no quantifier inflation in that statement.

The singleton-network sensitivity remains a **one-alternative-model result**, not a universal statement over all singleton specifications.

## 5. R5 portability certificate

R7 independently reconstructs the frozen R5 differentiated demand rather than importing the R5 solver.

At the exact common witness

[
(c,v,F)=
left(
rac1{10},
rac6{25},
rac15
ight),
]

both the independently solved differentiated Cournot and differentiated Bertrand versions satisfy:

- (Phi^X<0);
- (mathscr E^X<0);
- (mathscr D^X>0);
- a selection-free outsider-only adoption interval contains (F=1/5).

The stage-specific exact R5 proofs establish these negative political signs over the entire frozen audit box, not only at the witness.

R7 therefore treats the R5 non-portability result as binding scope evidence. No claim of competition-form or demand-system generality is certified.

## 6. R6 institutional certificate

R7 independently reconstructs the high-F comparison between (SU_{12}) and (SU_{13}) under symmetry.

For the common member,

[
W_1^{13,N}-W_1^{12,N}=0,
]

while the former outsider's change is strictly positive in the canonical headline region.

Thus the alternative SU:

- does not satisfy strict blocking, because one deviator is indifferent;
- does satisfy weak/Pareto blocking, because all deviators weakly gain and one strictly gains.

This re-certifies that the symmetric high-F three-SU stable set relies on the strict-blocking rule and symmetry-induced indifference.

With

[
m_1=m_2=1,qquad m_3=1-delta,
]

the independent identity

[
W_1^{12,N}-W_1^{13,N}
=
delta(A-C)
]

is reproduced. Since (A-C>0) on the relevant canonical domain, the specified asymmetry breaks the equality in favor of the two larger markets.

The intermediate-F unique-IS result rests on strict payoff differences, not equality, and remains classified as more institutionally robust within the canonical microfoundation.

## 7. Quantifier and equilibrium-scope audit

| Claim | Certified quantifier/scope | Not certified |
|---|---|---|
| G1-E | sufficient profile-specific inequalities imply outsider-only strict equilibrium | necessity; general novelty |
| G1-U | robust gain bounds are sufficient for strict-dominance/selection-free outsider-only continuation | necessity outside stated finite game |
| G2-L | local persistence around full bypass at strict interior points | global persistence for all primitives |
| G2-S | exact (R(d)) classification inside canonical Cournot extension | arbitrary demand/competition forms |
| G2-J | nonempty open set exists with incomplete adoption + reversal + selection-free continuation | all-equilibrium/global parameter characterization |
| N1 | (v=0, 0<c<1/3) boundary extension gives negative initial SU gap | all no-network models |
| N2–N4 | exact canonical fixed-c root/joint-region characterizations | monotonicity not separately proved; other demand systems |
| N7 | pre-specified S1 changes the canonical initial ranking | universal result over singleton specifications |
| R5 | exact failure throughout one frozen differentiated-demand box | all Bertrand or differentiated-product models |
| R6 high-F | stable-set conclusions under two explicitly defined blocking rules | farsighted, contractual, dynamic, transfer-enabled concepts |
| R6 intermediate-F | unique IS under tested rules and certified asymmetry ranges | arbitrary coalition-formation institutions |

No existence result is promoted to necessity or global uniqueness beyond its proved domain.

## 8. Assumption-dependence hierarchy

The surviving political reversal depends materially on:

1. the canonical three-country segmented-market structure;
2. the canonical demand/network microfoundation;
3. a parameter region with initial SU advantage;
4. positive reciprocal disadvantage;
5. a private-adoption continuation that is selection free;
6. sufficiently strong erosion of the member-market rent.

It does **not** require:

- exact zero residual adaptation cost;
- exact symmetric market size for the intermediate-F preference effect;
- the strict-blocking rule for the intermediate-F unique-IS result.

The initial SU advantage is nevertheless sensitive to the network/singleton specification and fails in the frozen R5 differentiated-demand model.

## 9. Welfare-scope audit

Within the certified intermediate-F institutional menu, all three countries strictly prefer IS to each SU continuation and to SW over the certified domain/witness ranges.

Permitted wording:

> IS Pareto-dominates the other four formal partitions within the model's five-partition institutional menu in the stated intermediate region.

Prohibited wording:

> IS is socially first-best.

No unrestricted planner problem has been solved.

## 10. Final R7 claim set

The following claims are eligible for R8 integration after final formal/CI closure:

1. a supporting selection-free one-way-adoption condition, explicitly positioned as high-overlap prior art;
2. the canonical residual-rent preference-effect decomposition and its success/intermediate/failure boundaries;
3. the open-set incomplete-adaptation joint witness;
4. explicit zero-network, singleton-network, and differentiated-demand failure/scope results;
5. the institutional distinction between robust intermediate unique-IS preference gaps and fragile symmetric high-F stable-set multiplicity.

## 11. Prohibited R8 overclaims

R8 must not state or imply:

- a general theorem that private compatibility promotes formal standardization;
- competition-form independence;
- demand-system independence;
- network-effect irrelevance for initial SU preference;
- universal robustness of the three-SU high-F stable set;
- novelty of one-way compatibility/adoption itself;
- necessity of the R2 sufficient conditions;
- unrestricted first-best welfare status;
- a priority/"first" claim.

## 12. Route decision

R3 is materially more than local robustness or payoff relabeling: it derives exact equilibrium-based thresholds and a nonlocal incomplete-adaptation open witness.

But R5 establishes a substantive portability failure while the one-way adoption mechanism survives.

The correct final research route is therefore

[
oxed{
	extbf{Route B — LIMITED GENERALIZATION}
}
]

rather than Route A.

R8 should reconstruct the paper as a **conditional mechanism paper** centered on success and failure conditions, with the canonical Cournot model as the principal microfoundation and the R4/R5/R6 failures as explicit boundaries.

R8 must not present a "general theory first" architecture.
