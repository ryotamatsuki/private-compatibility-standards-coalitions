# IJIO Submission Checklist

Verified/updated: 2026-08-27

| Item | Status | Note |
|---|---|---|
| Frozen Stage-8 theory unchanged | READY | This governance PR does not alter model primitives, formulas, equilibrium concepts, or theorem statements. |
| Latest main audited before branch creation | READY | Starting main `75b4fae03e7a2ab8b63309d91138dcb26c1452b8`. |
| Journal scope / IJIO fit | READY | Official Elsevier IJIO page confirms theoretical IO scope. |
| Live submission system | PORTAL RECHECK REQUIRED | Editorial Manager confirmed; enter through current official IJIO/EARIE route. |
| Exact regular-article portal label | PORTAL RECHECK REQUIRED | Select ordinary research/full-length article, not a special issue. |
| Peer-review anonymization model | READY | Current first-party Elsevier journal listing states that all IJIO articles use double-anonymized review. |
| Anonymous reviewer manuscript | READY | Reviewer manuscript contains `Anonymous Author`. |
| Author-identifying repository link absent from manuscript | READY | No public repository URL is added to reviewer manuscript. |
| Anonymous replication package | READY | Built without git history/repository owner/email/local paths; keep identity-free. |
| Separate title page | USER INPUT REQUIRED | Source prepared; official author/affiliation/contact/ORCID/address required. |
| Cover letter | USER INPUT REQUIRED | Content prepared; corresponding-author identity and submission certifications remain. |
| Abstract | READY | 161 words; no priority/efficiency overclaim. |
| Keywords | READY | Six conservative indexing terms. |
| JEL classifications | READY | L13, L15, F15, C71. |
| Highlights | READY | Five bullets; all <=85 characters. |
| Graphical abstract | NOT REQUIRED | No evidence of IJIO requirement; not prepared. |
| Data availability statement | READY | No empirical data used. |
| Code availability statement | READY | Anonymous replication package prepared by build target. |
| Manuscript-preparation AI declaration | READY | ChatGPT, purposes, human review/responsibility stated before references. |
| Research-process AI disclosure | READY | Separate computational-verification/AI-assisted research-methods disclosure added. |
| AI-assisted research-code disclosure | READY | Code development/editing and reproducibility-script assistance explicitly disclosed. |
| AI output not treated as proof/source | READY | Explicit in manuscript and governance documents. |
| Verification wording | READY | Uses analytical re-derivation and computational cross-check language; numerical checks are not proof. |
| AI-use public governance | READY | `docs/AI_USE_GOVERNANCE.md` and audit template added. |
| Detailed private AI audit | AUTHOR RETENTION REQUIRED | Store under gitignored `.local-research-audit/` or equivalent; do not commit confidential prompts/evidence. |
| Pre-AI provenance verdict | READY | `BASELINE-MODEL + EXTENSION-IDEA`; current theorem chain not found in thesis. |
| Thesis/current-paper comparison | READY | Structural and theorem-level comparison recorded in `docs/RESEARCH_PROVENANCE_GOVERNANCE.md`. |
| Thesis citation solely to prove pre-AI origin | NOT REQUIRED / NOT ADDED | Keep AI disclosure separate from prior-work disclosure. |
| Thesis prior-publication rule | PORTAL RECHECK REQUIRED | Elsevier generally excepts academic theses; IJIO-specific Guide remains inaccessible to automated client. |
| Thesis public dissemination status | NOT VERIFIED | Exact-title public search found no copy; institutional-repository status remains unresolved. |
| Material thesis text reuse | NO ISSUE IDENTIFIED IN STRUCTURAL REVIEW | No exhaustive forensic similarity scan claimed; investigate any later-discovered substantial prose/proof reuse. |
| Historical AI-provider data setting | NOT VERIFIED | Do not infer past setting. This is not automatically a submission prohibition. |
| Current AI-provider/account setting | USER INPUT REQUIRED | Verify current applicable provider terms/data controls before further unpublished AI use. |
| Prospective AI privacy hard gate | READY | `docs/AI_DATA_GOVERNANCE.md`. |
| Confidential reviewer/editor material AI rule | READY | Excluded from ordinary AI workflows. |
| AI-generated figure declaration | NOT REQUIRED | Figures are ordinary Python/Matplotlib analytical outputs. |
| Funding declaration | USER INPUT REQUIRED | Must be factual; not inferred. |
| Competing-interest declaration | USER INPUT REQUIRED | Must be factual; not inferred. |
| CRediT statement | USER INPUT REQUIRED | Author/coauthor roles not supplied. |
| Corresponding author | USER INPUT REQUIRED | Name, affiliation, email and postal address needed outside reviewer manuscript. |
| ORCID | USER INPUT REQUIRED | Supply if applicable/required. |
| Other prior preprint/dissemination status | USER INPUT REQUIRED | SSRN/arXiv/RePEc/working-paper/conference status must be confirmed. |
| Not under review elsewhere | USER INPUT REQUIRED | Explicit author certification required. |
| All authors approve submission | USER INPUT REQUIRED | Explicit author certification required. |
| Suggested-reviewer field | PORTAL RECHECK REQUIRED | Candidate pool ready if requested. |
| Reviewer conflicts | USER INPUT REQUIRED | All candidates remain UNKNOWN until author confirms no conflicts. |
| Opposed reviewers | NOT REQUIRED | None proposed absent a genuine conflict. |
| Submission fee | PORTAL RECHECK REQUIRED | Current Guide inaccessible; do not infer free/paid. |
| Open-access choice/APC | NOT REQUIRED FOR INITIAL SUBMISSION | Decide only if/when publisher requests a publication route. |
| Paper CI on governance PR | PASS | Initial PR-head run `33044319506` passed all workflow steps. |
| Submission-file build | PASS | Full `make submission` gate passed in run `33044319506`. |
| Clean-room replication QA | PASS | Anonymous replication-package clean-room rebuild/verification passed in run `33044319506`. |
| Final PDF visual QA | PENDING FINAL PACKAGE | Inspect the exact artifact used for final portal submission after all administrative inputs are resolved. |
| Final submit authorization | BLOCKED BY DESIGN | Requires explicit author authorization in a separate step. |

## Readiness rule

AI/provenance governance status is **CONDITIONAL GO**. The reproducibility/build gates pass; remaining conditions are the current-provider/data-control check, live IJIO portal recheck, and factual user-input items required for submission.

`BLOCKED BY DESIGN` on the final-submit action is intentional and does not prevent package completion. All `USER INPUT REQUIRED` items must be resolved before portal execution reaches certification/final submission.
