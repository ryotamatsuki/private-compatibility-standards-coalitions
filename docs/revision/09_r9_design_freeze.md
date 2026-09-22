# R9 — Final Audit and Journal Repositioning: Design Freeze

## Status

- Stage: R9
- Branch: `revision/r9-execution`
- Input integration commit: `602ed89d1a03df2b3f6d2eda26d37bb59aa53a01`
- Governing workflow: `research-paper-workflow v2.2 @ 42574d6c5931275ccff3ef7e8b4acc188077332a`
- R7/R8 route: **Route B — LIMITED GENERALIZATION / conditional mechanism paper**
- Actual journal submission: **out of scope unless separately authorized**

R9 may repair presentation, package structure, journal-specific formatting, declarations, and any defect uncovered by the final audit. It may not create a new economic result to improve journal positioning.

## 1. Final audit gates

R9 must close all of the following:

1. **Mathematics** — recheck the manuscript-facing residual-rent identity, its sign partition, the incomplete-adaptation witness, the zero-network boundary, and the stability-scope statements against certified R2–R7 artifacts.
2. **Claim scope** — no portability, priority, first-best, or coalition-robustness claim beyond the R7 freeze.
3. **Novelty** — recheck the surviving G2 contribution against the closest standards, compatibility, fixed-cost adoption, regulatory-harmonization, and coalition literatures.
4. **Reproducibility** — full clean build, R2–R8 regression, Lean, figures/tables, source package, and anonymous replication package.
5. **Abstract/introduction** — every headline claim must map to a certified result and must disclose the R5/R6 limitations.
6. **Journal rules** — after target selection, prepare a target-specific package and verify current official requirements.

Any substantive mathematical failure reopens the earliest affected stage and marks dependent material STALE.

## 2. Journal-selection rule

The candidate set is rebuilt from the R8 contribution rather than inherited from the pre-IJIO ladder. The first target must satisfy all of:

- accepts applied theoretical industrial-organization work;
- has a natural readership for compatibility/standardization, technology adoption, competition, or trade-policy questions;
- does not require the paper to claim functional-form-independent generality;
- current AI policy permits the disclosed, human-supervised AI-assisted research/writing process;
- manuscript and supplement can be made compliant with current format/length rules without deleting certified material.

## 3. Provisional target

The provisional first target is **Journal of Industry, Competition and Trade (JICT)**, subject to final package audit.

Reasons:

- its 2026 scope explicitly includes applied theory, market functioning, firm strategy, competition, innovation/new technologies, and international trade;
- its readership is closer to the revised conditional-mechanism paper than a general-interest journal;
- current Springer Nature AI policy permits disclosed, human-supervised drafting/restructuring and analytical assistance;
- the journal accepts mathematical LaTeX manuscripts and supplementary information;
- the current stated median submission-to-first-decision time is short, reducing the cost of a scope mismatch.

The manuscript must not be represented as a general theory of compatibility. The cover letter must state the conditional mechanism and its explicit non-portability result.

## 4. JICT package constraints

As checked on 2026-09-22 against the official Springer Nature journal pages:

- double-blind peer review;
- separate title page with author identity/contact and acknowledgements/disclosures;
- reviewer manuscript and associated review materials anonymized;
- abstract 150–250 words;
- 4–6 keywords;
- JEL codes requested;
- mathematical LaTeX accepted;
- editable source files required;
- LaTeX online submission should avoid subfolders;
- papers are typically under 20 double-spaced pages and must not exceed 40 pages;
- supplementary information is supported;
- competing-interest and author-contribution information are supplied in the portal;
- AI/LLM use must be documented, with human accountability retained.

The target package will therefore separate the anonymous reviewer manuscript from an anonymous online mathematical supplement containing the detailed appendices.

## 5. Completion gate

R9 closes only after:

- final mathematical/claim audit PASS;
- novelty recheck recorded;
- journal comparison and target decision recorded;
- target-specific manuscript/supplement/title-page/cover-letter/source package built;
- reviewer manuscript page count is at most 40 pages;
- abstract/keywords/JEL/anonymization/declarations pass journal-specific checks;
- full branch CI PASS;
- R9 closure record and revision-track status updated;
- PR to `revision/research-track` PASS and merged;
- post-merge integration CI PASS.

Completion of R9 means **research track closed and JICT submission package technically ready**, subject only to live-portal fields and the author's explicit final submission action.
