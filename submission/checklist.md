# IJIO Submission Checklist

Verified/updated: 2026-09-07

| Item | Status | Note |
|---|---|---|
| Frozen Stage-8 theory unchanged | READY | Technical-return repair does not alter model primitives, formulas, equilibrium concepts, theorem statements, or paper-body arguments. |
| IJIO technical return | ACTIONED IN REPOSITORY | Editorial office requested LaTeX source material and author information on the title page of the main document before external review. |
| Author name | READY | Ryota Matsuki. |
| Affiliation | READY | Independent Researcher, Matsuyama, Ehime, Japan. |
| Email | READY | ryota.matsuki@gmail.com. |
| Corresponding author | READY | Ryota Matsuki; generated main document marks him as corresponding author. |
| Identified main manuscript | READY PENDING CI | `generated/manuscript.pdf` is built from the dedicated IJIO EM source and must contain author, affiliation, email, and corresponding-author information. |
| LaTeX source archive | READY PENDING CI | `generated/ijio_em_source.zip`; one-level archive with no subfolders, containing only source dependencies used by the manuscript. |
| Editorial Manager subfolder rule | ENFORCED | Source-package builder flattens `\input` and `\includegraphics` dependencies and rejects directory paths. |
| Canonical anonymous manuscript | PRESERVED | `paper/main.tex` remains `Anonymous Author`; it is not the returned identified main document. |
| Anonymous replication package | PRESERVED | `generated/replication_package_anonymous.zip` remains identity-free and separate from the IJIO EM source archive. |
| Separate title page | READY | Populated with Ryota Matsuki, Independent Researcher, Matsuyama, Ehime, Japan, email, and corresponding-author designation. |
| Cover letter identity fields | READY | Signature populated; final originality/funding/competing-interest certifications remain factual user inputs. |
| Author-identifying repository link absent from manuscript | READY | No public repository URL is added to the generated IJIO main manuscript. |
| Abstract | READY | 161 words. |
| Keywords | READY | Six indexing terms. |
| JEL classifications | READY | L13, L15, F15, C71. |
| Highlights | READY | Five bullets; all <=85 characters. |
| Data availability statement | READY | No empirical data used. |
| Code availability statement | READY | Anonymous replication package retained. |
| Manuscript-preparation AI declaration | READY | Existing disclosure retained in the paper. |
| Research-process AI disclosure | READY | Existing computational-verification/AI-assisted research-methods disclosure retained. |
| AI-generated figure declaration | NOT REQUIRED | Figures are ordinary Python/Matplotlib analytical outputs. |
| Funding declaration | USER INPUT REQUIRED | Must be factual; not inferred. |
| Competing-interest declaration | USER INPUT REQUIRED | Must be factual; not inferred. |
| CRediT statement | USER INPUT REQUIRED | Confirm single-author roles if the live portal requires them. |
| ORCID | PORTAL / USER RECHECK | Enter only if a verified ORCID is available/required. |
| Other prior preprint/dissemination status | USER INPUT REQUIRED | Confirm SSRN/arXiv/RePEc/working-paper/conference/public manuscript status. |
| Not under review elsewhere | USER CONFIRMATION REQUIRED | Explicit certification required at final approval. |
| All human authors approve submission | USER CONFIRMATION REQUIRED | Single-author submission; explicit certification still required at final approval. |
| Suggested-reviewer field | PORTAL RECHECK REQUIRED | Candidate pool remains available if requested. |
| Reviewer conflicts | USER INPUT REQUIRED | Confirm no conflicts before using suggested reviewers. |
| Submission fee | PORTAL RECHECK REQUIRED | Check live IJIO Editorial Manager / current Guide for Authors. |
| Open-access choice/APC | NOT REQUIRED FOR TECHNICAL RETURN | Decide only if/when publisher requests a publication route. |
| Clean-room IJIO EM source compile | READY PENDING CI | Workflow unzips the exact source archive in a fresh directory, compiles it, and checks author/affiliation/email in the PDF. |
| Clean-room replication QA | READY PENDING CI | Existing anonymous package rebuild/verification remains in CI. |
| Final PDF visual QA | PENDING FINAL PACKAGE | Inspect exact rebuilt Editorial Manager PDF before approval. |
| Final submit / Approve Submission | BLOCKED BY DESIGN | Requires explicit author authorization after live-portal inspection. |

## Technical-return execution rule

For IJIO-D-26-00585, use the identified `generated/manuscript.pdf` together with `generated/ijio_em_source.zip`. Do not substitute the canonical anonymous `paper/main.pdf` for the returned main document.

The Editorial Manager source archive and the anonymous replication archive serve different purposes and must remain separate.
