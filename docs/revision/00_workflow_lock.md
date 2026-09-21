# Workflow Lock for Post-IJIO Revision Track

## Adopted workflow

This project adopts the latest **stable published** version of the reusable workflow rather than an unreleased repository head.

- Repository: \`ryotamatsuki/research-paper-workflow\`
- Adopted version: **v2.2**
- Immutable adopted commit: \`42574d6c5931275ccff3ef7e8b4acc188077332a\`
- Adoption date for this revision track: 2026-09-21

At the time of this lock, the workflow repository \`main\` is at:

- \`9eb616bd31ea3a9ef3c29e288228ed962c44c9cf\`
- documented as a **v2.3 minor revision candidate**, not the latest stable published release.

The v2.3 candidate strengthens Stage 12 journal-candidate-universe completeness. It is not adopted as the governing version for R0–R9 because this project requires a reproducible stable workflow reference. Its Stage-12 refinement may be consulted later as non-governing guidance when R9 reaches journal reselection.

## Canonical governing files frozen at v2.2

| File | Blob SHA |
|---|---|
| \`GOVERNANCE.md\` | \`cd414d384986981afbabcf042e2e19e97b7ea802\` |
| \`THEORY_PAPER_RESEARCH_PIPELINE.md\` | \`0edb869dca3ca9e74fe6171441942e41297a2644\` |
| \`checklists/THEOREM_CERTIFICATION_CHECKLIST.md\` | \`86670b13c61cd33f3995c2ac50fe677d24645230\` |
| \`checklists/FORMAL_VERIFICATION_CHECKLIST.md\` | \`fc82946981ab472189defb79e0da88eb012cd8a9\` |
| \`checklists/LITERATURE_AUDIT_CHECKLIST.md\` | \`3f9d0ad6741cf5dd0b40a41c6218553dc2e45f23\` |
| \`checklists/SYMBOLIC_VERIFICATION_CHECKLIST.md\` | \`a1201bd9355528272fc4018016270d9910769449\` |
| \`checklists/NUMERICAL_VERIFICATION_CHECKLIST.md\` | \`719d607f68c6dde90f78a4f89fc68d127eb19627\` |
| \`checklists/PAPER_SPECIFIC_CERTIFICATION_INHERITANCE_CHECKLIST.md\` | \`a7ef85b8784fb3792b75d6589f0e8377f4ebfec5\` |
| \`docs/VERSIONING_POLICY.md\` | \`cd65f1af610a8e2f3ec4a96858f0786eed0e0abc\` |

Authority remains:

\`GOVERNANCE.md → THEORY_PAPER_RESEARCH_PIPELINE.md → templates → checklists → examples\`.

## Inherited obligations for R0–R9

The paper-specific R0–R9 labels do not weaken the v2.2 workflow. In particular:

1. a proposed equilibrium and completeness/uniqueness of the equilibrium set are separate claims;
2. indifference, zero output, boundary and off-path states trigger dedicated attacks when relevant;
3. theorem quantifiers and functional-form scope must match the proof;
4. application-specific notation must be canonicalized and checked against plausible parent model classes and parent theorems;
5. independent adversarial certification is distinct from rerunning production code;
6. every theorem-bearing route must close a formal-verification applicability decision before theory freeze;
7. negative results, counterexamples, failed specifications and certification regressions remain permanent research artifacts.

## Formal-verification preliminary state

For the post-IJIO redevelopment, formal verification is provisionally classified:

\`PRELIMINARY APPLICABLE — TARGETS NOT YET FROZEN\`

Reason: R2–R3 are expected to involve quantified inequalities, strict-dominance/equilibrium conditions, threshold intersections and possible piecewise parameter regions. No Lean/formal artifact is started at R0–R2 design because theorem statements and scopes are not yet stable. The applicability decision must be reassessed at R7 before the new theory is frozen.
