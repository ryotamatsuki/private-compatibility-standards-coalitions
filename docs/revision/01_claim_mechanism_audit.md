# R1 — Claim and Mechanism Audit

## Verdict

**R1 COMPLETE — GO TO R2 DESIGN/EXECUTION UNDER NARROWED CLAIM DISCIPLINE**

The old theory is not found mathematically defective by this audit. The central post-IJIO problem is that the strongest economic interpretation was broader than what the model structure independently demonstrated.

The key change in research posture is:

> The revision must distinguish a valid model-specific result from a portable mechanism. It must not obtain "generality" by merely renaming current Cournot payoff differences.

## Inputs

- historical submission-source state: \`28bed286bd03b43bce8294b9eaebfcc7ceb6ca2a\`;
- \`docs/CANONICAL_MODEL.md\`;
- \`docs/THEOREM_LEDGER.md\`;
- Sections 5–8 of the submitted manuscript;
- \`docs/LITERATURE_POSITIONING.md\`;
- sanitized IJIO editorial assessment in \`00_ijio_outcome.md\`;
- research-paper-workflow v2.2 at \`42574d6...\`.

## Editor criticism mapped to the manuscript

| Editorial concern | Existing object | R1 diagnosis | Revision requirement |
|---|---|---|---|
| standard three-country Cournot exercise | Sections 4–5 | product-market blocks do most of the work | move the adoption-scope logic into an application-neutral model before Cournot specialization |
| results obtained by comparing configurations of same linear subgames | \(A,B,C,P,K_M,K_I\) comparisons | mathematically valid but configuration-heavy | state exactly which equilibrium properties, not which labels, generate the sign |
| conclusions depend on those configurations | post-bypass member markets become exactly IS while outsider market is unchanged | this is the strongest structural dependence | R3 must relax exact erosion and derive the residual effect from an explicit market extension |
| insufficient portable general insight | Theorem 1 / Corollary 1 | the accounting decomposition is interpretable, but the ranking reversal is short once its conditions are imposed | derive adoption asymmetry and erosion conditions from primitives, and characterize failure cases |
| no realistic IJIO path | journal positioning | not a revision invitation | do not optimize the research track for IJIO resubmission |

## Four claims that must never be conflated

### C-A — Outsider-only adoption exists

A profile in which the outsider adopts the bloc standard while members do not is a Nash equilibrium.

Status in old model: **LEGACY VERIFIED in the stated intermediate-\(F\) region**.

This is an existence statement unless stronger best-response conditions are established.

### C-B — Outsider-only adoption is unique / selection-free

No other adoption equilibrium is relevant in the stated region.

Status in old headline region: **LEGACY VERIFIED by strict best responses**.

R2 must separate profile-specific existence from global uniqueness. A no-profitable-deviation check for one profile is not uniqueness evidence.

### C-C — Private adoption strengthens the government's incentive toward IS

Let \(G_i\) denote the member government's relative gain from IS. The old exact-bypass model gives

\[
G_i^O-G_i^N=\mathscr E_i.
\]

Status: **LEGACY VERIFIED IDENTITY CONDITIONAL ON THE OLD CONTINUATION MAPPING**.

This does not itself imply preference reversal.

### C-D — Private adoption reverses the government ranking

The member initially prefers SU but after bypass prefers IS.

Status: **LEGACY VERIFIED on \(\Omega_0\)**.

This requires both an initial SU advantage and a sufficiently adverse post-adoption change.

A change in member preference still does not, by itself, prove a change in the stable coalition set.

## Claim-by-claim audit

| ID | Existing result | Mathematical type | Main dependencies | R1 status for redevelopment |
|---|---|---|---|---|
| L1 | Cournot equilibrium blocks | exact parametric equilibrium | linear demand, Cournot, network specification, interior domain | LEGACY CERTIFIED; microfoundation only |
| L2 | corrected welfare expressions | exact accounting | L1, government objective | LEGACY CERTIFIED |
| L3/L4 | adoption threshold signs/order | inequality results | Cournot blocks, canonical domain | LEGACY CERTIFIED; model-specific |
| L5 | full adoption correspondence | equilibrium characterization | binary adoption, segmented markets, standard-specific fixed cost | LEGACY CERTIFIED; R2 parent input |
| I1 | \(\mathscr E_i-\mathscr D_i\to-\mathscr D_i\) | accounting identity under a continuation mapping | member markets become exactly IS after outsider adoption; outsider market unchanged | LEGACY VALID; REOPENED FOR GENERALIZATION |
| T1 | Selective-Erosion Theorem | conditional ranking result | I1 plus \(\mathscr E_i>\mathscr D_i>0\) | LEGACY VALID; economic generality NOT CERTIFIED |
| C1 | political-incentive cross-difference | identity | exact erosion mapping | LEGACY VALID; R3 must replace exact erosion by equilibrium-derived partial erosion |
| P1 | three-country microfoundation | existence/open-set result | full canonical Cournot model | LEGACY CERTIFIED; should become example/microfoundation if R2–R3 succeed |
| T2 | SU→IS stable-set reversal | coalition-stability theorem | symmetry, strict blocking, five-partition menu, selection-free adoption regions | LEGACY CERTIFIED WITH CORRECTION; SECONDARY in revised hierarchy |
| P2 | market-size partner ranking | conditional comparative result | no adoption, one-dimensional asymmetry | SECONDARY; likely appendix unless it supports R6 |
| P4 | low-\(F\) IS comparison | sufficient-region result | universal multistandarding and duplicate fixed costs | APPENDIX only |

## Where the old "general mechanism" is structurally narrow

The submitted Section 6 has two exact continuation properties:

1. outsider adoption turns every coalition-member market into the complete-compatibility product-market configuration used under IS;
2. coalition members' product-market state in the outsider market does not change.

These imply that the entire member-market term \(\mathscr E_i\) disappears while \(\mathscr D_i\) is untouched.

Therefore, the submitted theorem is not circular, but much of the substantive economics is encoded in the continuation mapping. The new project may use the old decomposition as a diagnostic identity, but may not treat it as proof of portability.

## Network-effect dependency correction

The old theorem ledger contains a historical killed claim labelled "network effects are necessary" and correctly rejected that as a universal statement. R1 now adds a more precise baseline statement:

- the abstract bookkeeping distinction between exclusion benefit and reciprocal disadvantage can be written without a network-effect parameter;
- however, in the **current symmetric Cournot microfoundation**, setting \(v=0\) yields
  \[
  W_M^{SU,N}-W^{IS}=\frac{c(13c-6)}{32}<0
  \quad\text{for }0<c<1/3.
  \]
- hence the old headline ranking-reversal path cannot start at \(v=0\) in that baseline model, because members do not initially prefer SU.

Until a concrete alternative microfoundation is established, the revision must not use the broad phrase "network effects are unnecessary for the mechanism" without explaining this distinction.

See \`04_network_role_precheck.md\`.

## Application-neutral canonicalization

The minimal application-neutral structure surviving R1 is:

1. a formal institution partitions markets/participants and creates a set \(C\) of markets governed by one common formal standard;
2. a private agent can make a discrete investment that supports this standard without changing formal membership;
3. one investment can affect multiple markets in \(C\);
4. reverse adaptation by formal members is technologically and economically separate;
5. private adaptation changes continuation product-market payoffs, which governments then use to rank formal regimes.

This is **not yet a novel theorem**. It is the representation that must be tested against generic fixed-cost adoption and economies-of-scope theory in R2.

## R1 route decision

**GO to R2**, with the following restrictions:

- do not call G1 novel before theorem-absorption mapping;
- do not use the old \(2T_A\) arithmetic as the proof of a general result;
- target existence and uniqueness as separate propositions;
- derive a nonempty asymmetric-adoption region from scope/cost/competition restrictions, or record failure;
- keep R3 partial erosion separate from R2 adoption asymmetry;
- keep coalition stability secondary until R6.

## R1 completion state

- old theorem ledger preserved: YES;
- new ledger created separately: YES;
- R4 \(v=0\) precheck performed: YES;
- preliminary parent-theorem/literature risks identified: YES;
- manuscript rewriting authorized: NO;
- R2 design authorized: YES.
