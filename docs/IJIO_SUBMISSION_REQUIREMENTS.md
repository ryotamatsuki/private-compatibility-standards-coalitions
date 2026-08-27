# IJIO Submission Requirements Audit

Verified: 2026-08-27

Target journal: *International Journal of Industrial Organization* (IJIO), ISSN 0167-7187.

## Source hierarchy and access note

The current IJIO journal page is available from Elsevier and links to both the Guide for Authors and the journal submission system. The Guide for Authors URL is:

- https://www.sciencedirect.com/journal/international-journal-of-industrial-organization/publish/guide-for-authors

The Guide itself returned HTTP 403 to the automated verification client on 2026-08-27. Journal-specific fields that cannot be verified independently from accessible current first-party text are therefore marked **PORTAL RECHECK REQUIRED** rather than inferred from older author packs or from other Elsevier journals.

Current first-party sources used in this audit:

- IJIO journal page: https://shop.elsevier.com/journals/international-journal-of-industrial-organization/0167-7187
- IJIO Guide for Authors link: https://www.sciencedirect.com/journal/international-journal-of-industrial-organization/publish/guide-for-authors
- IJIO Editorial Manager landing page: https://www.editorialmanager.com/IJIO/default.aspx
- EARIE IJIO page: https://earie.org/ijio/
- Recent EARIE IJIO submission notice, which identifies the cloud Editorial Manager endpoint: https://earie.org/ijio-special-issue-in-memory-of-dr-patrick-bajari/
- Elsevier highlights guidance: https://www.elsevier.com/researcher/author/tools-and-resources/highlights
- Elsevier GenAI policy for journals: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals
- Elsevier research-data guidance: https://www.elsevier.com/researcher/author/tools-and-resources/research-data
- Elsevier data-statement guidance: https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-statement
- Elsevier submission-fee policy: https://www.elsevier.com/researcher/author/policies-and-guidelines/submission-fees

## Requirements matrix

| Requirement | Current verified rule | Current paper status | Action / final status |
|---|---|---|---|
| Journal scope | IJIO explicitly welcomes theoretical and empirical industrial-organization work, including strategic behavior, market structure, technological change and regulation. | Strong fit when the firm-compatibility-to-product-market channel is foregrounded. | **READY** |
| Submission system | IJIO uses Editorial Manager. A 2025 EARIE IJIO notice gives `https://www2.cloud.editorialmanager.com/ijio/default2.aspx`. The generic `www.editorialmanager.com/IJIO/default.aspx` mirror currently displays a development-site warning. | No portal action taken. | **PORTAL RECHECK REQUIRED**: enter through the current link reached from the official IJIO/EARIE page, not a stale mirror. |
| Article type | Current IJIO output is published as original/research articles. Exact Editorial Manager label for a regular unsolicited paper was not independently retrievable. | Full theoretical paper. | **PORTAL RECHECK REQUIRED**; select the ordinary research/full-length article type, not a special issue, once the live labels are visible. |
| Peer-review anonymization model | Current Guide text could not be retrieved. Publicly accessible current sources do not establish single- versus double-anonymized review. | `paper/main.tex` already identifies the author only as `Anonymous Author`. | **READY ON SAFE SIDE**: submit anonymous reviewer manuscript and separate title page; recheck live portal instructions. |
| Separate title page | Current journal-specific requirement not independently retrievable. | Separate title-page source prepared with author fields isolated from reviewer manuscript. | **READY / PORTAL RECHECK** |
| Cover letter | Journal-specific requirement not independently retrievable. | One-page IJIO-specific cover letter prepared. | **READY** even if optional. |
| Highlights | Elsevier guidance specifies 3–5 bullets, each <=85 characters, in a separate editable file; Elsevier says highlights are not part of editorial consideration and are not required until final files. Current IJIO articles display highlights. | Five compliant bullets prepared. | **READY; upload if requested/accepted.** |
| Graphical abstract | No accessible current IJIO evidence that it is required. | Not prepared. | **NOT REQUIRED UNLESS PORTAL SAYS OTHERWISE.** |
| Abstract limit | Current IJIO limit could not be source-verified because the Guide is inaccessible. | Abstract is 161 words. | **READY**; safely short, but live limit should still be checked. |
| Keywords | Current IJIO numeric limit could not be source-verified. Generic Elsevier guides often cap keywords and current IJIO papers use compact lists. | Reduced to six high-information keywords for conservative compatibility. | **READY / PORTAL RECHECK** |
| JEL classification | Current IJIO published papers display JEL classification. | L13; L15; F15; C71. | **READY** |
| Initial manuscript format | Current IJIO-specific text could not be retrieved. Elsevier supports LaTeX workflows generally. | `elsarticle`, review mode, author-year references, compiled PDF. | **READY / PORTAL RECHECK** |
| LaTeX/source files | Elsevier supports LaTeX source workflows; exact initial-upload rule is journal-specific. | Complete modular LaTeX source exists. | **READY** |
| Figures | Figures are reproducibly generated as PDF by Python/Matplotlib and embedded in manuscript. | Three figures; no generative-image AI used. | **READY** |
| Tables | Tables are reproducibly generated as editable LaTeX. | Three tables. | **READY** |
| Supplement / replication material | Elsevier treats code/software/models as research data and supports supplementary/repository linking; IJIO-specific mandate could not be retrieved. | Anonymous replication package is generated without git history or author identifiers. | **READY** |
| Research-data statement | Elsevier journals commonly collect data statements in the submission flow; current IJIO articles display a Data availability section. | No empirical data were used. | **READY**: explicit no-empirical-data statement included. |
| Code availability | Elsevier defines software/code/models/algorithms as research data and encourages sharing where appropriate. | Symbolic/numerical verification and figure/table generation are reproducible. | **READY**: anonymous replication ZIP prepared. |
| Competing interests | Elsevier publishing ethics require disclosure of relevant competing interests; the factual author declaration is not stored in the repository. | Unknown. | **USER INPUT REQUIRED** |
| Funding | Funding must be disclosed accurately; factual funding status is not stored in the repository. | Unknown. | **USER INPUT REQUIRED** |
| CRediT | Current 2026 IJIO articles display CRediT contribution statements; whether the portal makes it mandatory at first submission could not be independently verified. | Authorship/coauthor roles not supplied. | **USER INPUT REQUIRED / PORTAL RECHECK** |
| Generative AI declaration | Current Elsevier journal policy requires disclosure when AI makes substantive manuscript-preparation changes. The declaration should name the tool, purpose and human oversight and appear immediately before references. | ChatGPT (OpenAI) materially assisted organization, drafting/revision, source checking and preparation/review of reproducibility scripts; all content was human-reviewed and independently checked. | **REQUIRED AND PREPARED** |
| AI-generated figures | Elsevier requires disclosure when GenAI creates/alters images. | Figures are ordinary Python/Matplotlib analytical output; no generative-image tool is part of the figure pipeline. | **NOT APPLICABLE** |
| Preprints/prior dissemination | Elsevier generally permits electronic preprints, subject to journal-specific and anonymization rules. | Public GitHub repository exists; prior preprint/working-paper dissemination status is not confirmed. | **USER INPUT REQUIRED**; reviewer manuscript does not link the public repository. |
| Simultaneous submission/originality | Elsevier ethics prohibit simultaneous journal submission and require appropriate authorship approval. | Current factual status not independently certified. | **USER CONFIRMATION REQUIRED** |
| Suggested reviewers | Current IJIO portal requirement could not be retrieved. | Six-person subject-fit pool prepared from current official academic profiles. | **READY IF REQUESTED; conflict status USER CONFIRMATION REQUIRED.** |
| Opposed reviewers | No evidence that exclusions are required. | None proposed. | **NONE** unless a genuine conflict is supplied. |
| Submission fee | Elsevier states that journals charging a fee flag it in their Guide and submission process. IJIO's current fee could not be source-verified from the inaccessible Guide. | No payment action. | **PORTAL RECHECK REQUIRED**; do not infer a fee or no-fee status. |
| Open access / APC | IJIO is a subscription journal with open-access options; an exact current APC was not verified for this package. | No OA selection made. | **DECISION NOT NEEDED BEFORE INITIAL SUBMISSION**; recheck publisher price if OA is chosen. |
| Page/word limit | No current IJIO-specific hard page or word cap could be independently verified. | 75 review-mode pages before submission declarations; theory body unchanged. | **PORTAL RECHECK REQUIRED** |
| References | Current manuscript uses `elsarticle-harv` author-year format and all citations pass CI. | Complete. | **READY** |
| ORCID | Current IJIO-specific requirement could not be verified. | Not supplied. | **USER INPUT REQUIRED IF AVAILABLE / PORTAL RECHECK** |
| Corresponding author | Submission systems require a designated corresponding author and contact information. | Not supplied in the anonymous manuscript. | **USER INPUT REQUIRED** |

## Operational submission rule

The package is designed so that no journal-specific uncertainty changes the frozen economics. At portal-entry time, recheck only the administrative fields marked **PORTAL RECHECK REQUIRED** against the live Editorial Manager screens and the then-accessible IJIO Guide for Authors.

Do **not** use the public repository URL inside the reviewer manuscript or anonymous replication package until the journal's anonymization model is confirmed. Do **not** press the final submission/approval button without explicit author authorization.
