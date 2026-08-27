# IJIO Submission Checklist

Verified/updated: 2026-08-27

| Item | Status | Note |
|---|---|---|
| Frozen Stage-8 theory unchanged | READY | Canonical source files are outside submission edits. |
| Latest main audited before branch creation | READY | Starting main `0d4d7c883a137c3ca7e2902c8c2466b63abea30e`. |
| Journal scope / IJIO fit | READY | Official Elsevier IJIO page confirms theoretical IO scope. |
| Live submission system | PORTAL RECHECK REQUIRED | Editorial Manager confirmed; use current link reached from official IJIO/EARIE page because generic mirror shows a development warning. |
| Exact regular-article portal label | PORTAL RECHECK REQUIRED | Select ordinary research/full-length article, not a special issue. |
| Peer-review anonymization model | PORTAL RECHECK REQUIRED | Anonymous manuscript + separate title page prepared conservatively. |
| Anonymous reviewer manuscript | READY | Reviewer manuscript contains `Anonymous Author`. |
| Author-identifying repository link absent from manuscript | READY | No public repo link is added to reviewer manuscript. |
| Separate title page | USER INPUT REQUIRED | Source prepared; official author/affiliation/contact/ORCID/address required. |
| Cover letter | USER INPUT REQUIRED | Content prepared; corresponding-author identity and submission certifications remain. |
| Abstract | READY | 161 words; no priority/efficiency overclaim. |
| Keywords | READY | Six conservative indexing terms. |
| JEL classifications | READY | L13, L15, F15, C71. |
| Highlights | READY | Five bullets; all <=85 characters. |
| Graphical abstract | NOT REQUIRED | No evidence of IJIO requirement; not prepared. |
| Data availability statement | READY | No empirical data used. |
| Code availability statement | READY | Anonymous replication package prepared by build target. |
| Generative-AI declaration | READY | Required by current Elsevier policy for substantive manuscript-preparation use. |
| AI-generated figure declaration | NOT REQUIRED | Figures are ordinary Python/Matplotlib analytical outputs. |
| Funding declaration | USER INPUT REQUIRED | Must be factual; not inferred. |
| Competing-interest declaration | USER INPUT REQUIRED | Must be factual; not inferred. |
| CRediT statement | USER INPUT REQUIRED | Author/coauthor roles not supplied. |
| Corresponding author | USER INPUT REQUIRED | Name, affiliation, email and postal address needed. |
| ORCID | USER INPUT REQUIRED | Supply if applicable/required. |
| Prior preprint/dissemination status | USER INPUT REQUIRED | SSRN/arXiv/RePEc/working-paper/conference status must be confirmed. |
| Not under review elsewhere | USER INPUT REQUIRED | Explicit author certification required. |
| All authors approve submission | USER INPUT REQUIRED | Explicit author certification required. |
| Suggested-reviewer field | PORTAL RECHECK REQUIRED | Candidate pool ready if requested. |
| Reviewer conflicts | USER INPUT REQUIRED | All candidates remain UNKNOWN until author confirms no conflicts. |
| Opposed reviewers | NOT REQUIRED | None proposed absent a genuine conflict. |
| Submission fee | PORTAL RECHECK REQUIRED | Current Guide inaccessible; do not infer free/paid. |
| Open-access choice/APC | NOT REQUIRED FOR INITIAL SUBMISSION | Decide only if/when publisher requests a publication route. |
| Anonymous replication package | READY | Generated without git history, repository owner, email or local paths. |
| Paper CI | READY | Must remain green on final package head. |
| Submission-file build | READY | `make submission` creates reviewer and administrative files. |
| Final PDF visual QA | PENDING BUILD | Must inspect exact package artifact after final build. |
| Final submit authorization | BLOCKED BY DESIGN | Requires explicit author authorization in a separate step. |

## Readiness rule

`BLOCKED BY DESIGN` on the final-submit action is intentional and does not prevent package completion. All `USER INPUT REQUIRED` items must be resolved before portal execution reaches the certification/final-submit stage.
