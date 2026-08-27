# IJIO Submission Requirements Audit

Verified/updated: 2026-08-27

Target journal: *International Journal of Industrial Organization* (IJIO), ISSN 0167-7187.

## Source hierarchy and access note

The current IJIO journal page is available from Elsevier and links to both the Guide for Authors and the journal submission system. The Guide for Authors URL is:

- https://www.sciencedirect.com/journal/international-journal-of-industrial-organization/publish/guide-for-authors

The Guide itself returned HTTP 403 to the automated verification client on 2026-08-27. Journal-specific fields that cannot be verified independently from accessible current first-party text are therefore marked **PORTAL RECHECK REQUIRED** rather than inferred from older author packs or from other Elsevier journals.

A current first-party Elsevier journals listing independently states that all IJIO articles use **double-anonymized peer review**. That field is therefore no longer treated as unknown, although live upload instructions must still be followed.

Current first-party sources used in this audit:

- IJIO journal page: https://shop.elsevier.com/journals/international-journal-of-industrial-organization/0167-7187
- Elsevier journals listing identifying IJIO double-anonymized review: https://shop.elsevier.com/journals/subjects/social-sciences-and-humanities/economics-econometrics-and-finance
- IJIO Guide for Authors link: https://www.sciencedirect.com/journal/international-journal-of-industrial-organization/publish/guide-for-authors
- IJIO Editorial Manager landing page: https://www.editorialmanager.com/IJIO/default.aspx
- EARIE IJIO page: https://earie.org/ijio/
- Recent EARIE IJIO submission notice, which identifies the cloud Editorial Manager endpoint: https://earie.org/ijio-special-issue-in-memory-of-dr-patrick-bajari/
- Elsevier highlights guidance: https://www.elsevier.com/researcher/author/tools-and-resources/highlights
- Elsevier GenAI policy for journals: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals
- Elsevier 18 August 2026 GenAI-policy update: https://www.elsevier.com/connect/updated-generative-ai-policies-for-journals-supporting-responsible-use-while-protecting-trust
- Elsevier publishing ethics: https://www.elsevier.com/about/policies-and-standards/publishing-ethics
- Elsevier research-data guidance: https://www.elsevier.com/researcher/author/tools-and-resources/research-data
- Elsevier data-statement guidance: https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-statement
- Elsevier submission-fee policy: https://www.elsevier.com/researcher/author/policies-and-guidelines/submission-fees

## Requirements matrix

| Requirement | Current verified rule | Current paper status | Action / final status |
|---|---|---|---|
| Journal scope | IJIO explicitly welcomes theoretical and empirical industrial-organization work, including strategic behavior, market structure, technological change and regulation. | Strong fit when the firm-compatibility-to-product-market channel is foregrounded. | **READY** |
| Submission system | IJIO uses Editorial Manager. A recent EARIE IJIO notice identifies the cloud Editorial Manager endpoint; a generic mirror has displayed a development-site warning. | No portal action taken. | **PORTAL RECHECK REQUIRED**: enter through the current official IJIO/EARIE route. |
| Article type | Current IJIO output is published as original/research articles. Exact Editorial Manager label for a regular unsolicited paper was not independently retrievable. | Full theoretical paper. | **PORTAL RECHECK REQUIRED**; select the ordinary research/full-length article type once live labels are visible. |
| Peer-review anonymization model | Current Elsevier first-party journal listing states that all IJIO articles use double-anonymized peer review. | `paper/main.tex` identifies the author only as `Anonymous Author`; separate title page is prepared. | **READY**: keep reviewer manuscript and anonymous replication package identity-free; follow live upload instructions. |
| Separate title page | Current journal-specific upload requirement not independently retrievable. | Separate title-page source prepared with author fields isolated from reviewer manuscript. | **READY / PORTAL RECHECK** |
| Cover letter | Journal-specific requirement not independently retrievable. | One-page IJIO-specific cover letter prepared. | **READY** even if optional. |
| Highlights | Elsevier guidance specifies 3–5 bullets, each <=85 characters, in a separate editable file. | Five compliant bullets prepared. | **READY; upload if requested/accepted.** |
| Graphical abstract | No accessible current IJIO evidence that it is required. | Not prepared. | **NOT REQUIRED UNLESS PORTAL SAYS OTHERWISE.** |
| Abstract limit | Current IJIO limit could not be source-verified because the Guide is inaccessible. | Abstract is 161 words. | **READY / PORTAL RECHECK** |
| Keywords | Current IJIO numeric limit could not be source-verified. | Six compact keywords. | **READY / PORTAL RECHECK** |
| JEL classification | Current IJIO published papers display JEL classification. | L13; L15; F15; C71. | **READY** |
| Initial manuscript format | Current IJIO-specific initial-upload text could not be retrieved. | `elsarticle`, review mode, author-year references, compiled PDF. | **READY / PORTAL RECHECK** |
| LaTeX/source files | Elsevier supports LaTeX source workflows; exact initial-upload rule is journal-specific. | Complete modular LaTeX source exists. | **READY** |
| Figures | Figures are reproducibly generated as PDF by Python/Matplotlib and embedded in manuscript. | Three figures; no generative-image AI used. | **READY** |
| Tables | Tables are reproducibly generated as editable LaTeX. | Three tables. | **READY** |
| Supplement / replication material | Elsevier treats code/software/models as research data and supports supplementary/repository linking; IJIO-specific mandate could not be retrieved. | Anonymous replication package is generated without git history or author identifiers. | **READY** |
| Research-data statement | Elsevier journals collect/encourage data statements; current IJIO articles display data-availability material. | No empirical data were used. | **READY** |
| Code availability | Elsevier treats software/code/models/algorithms as research outputs/data. | Symbolic/numerical verification and figure/table generation are reproducible. | **READY**: anonymous replication ZIP prepared. |
| Manuscript-preparation GenAI declaration | Elsevier requires disclosure when AI substantively assists manuscript preparation; current policy specifies tool, purpose, and human oversight, with the declaration before references. | ChatGPT (OpenAI) materially assisted organization, drafting/revision, source checking, and preparation/review of reproducibility scripts. | **REQUIRED AND PREPARED** |
| Research-process AI disclosure | Current Elsevier policy distinguishes research-process AI use from manuscript preparation and requires reproducible description in the Methods/research-methods material. | Separate `Computational verification and AI-assisted research methods` disclosure added. | **REQUIRED AND PREPARED** |
| AI-assisted research-code development | Elsevier's current FAQ specifically treats study design, code development, and data analysis as research-process uses; AI writing/editing research code should be declared in detail in Methods. | Research-code development/editing and reproducibility-script assistance are disclosed; code is executed and cross-checked against analytical derivations. | **REQUIRED AND PREPARED** |
| AI output as proof/source | Elsevier permits supportive use but requires human expertise, verification, and responsibility; inappropriate use includes replacing genuine intellectual contribution. | AI output is explicitly not treated as proof or an authoritative scholarly source. | **READY** |
| AI provider privacy/confidentiality | Elsevier requires authors to check tool terms, protect unpublished material, and ensure the provider is not granted broader rights including training rights beyond service provision. | Historical provider setting is not verifiable from repository evidence; prospective governance established. | **USER VERIFICATION REQUIRED / GOVERNANCE READY** |
| AI-use records | Elsevier recommends retaining records of tool/model/use and, where appropriate, prompts/outputs and human review. | Public audit template exists; detailed records are kept outside the public repository. | **READY AS GOVERNANCE** |
| AI-generated figures | Elsevier requires separate treatment when GenAI creates/alters images. | Figures are ordinary Python/Matplotlib analytical output. | **NOT APPLICABLE** |
| Academic thesis / prior publication | Elsevier's general ethics guidance treats an academic thesis as an exception to prior-publication restrictions, but journal-specific rules may differ, particularly around anonymous review. | Earlier thesis is a pre-AI benchmark and provenance artifact; current theorem chain materially differs. | **GENERAL ELSEVIER RULE READY / IJIO PORTAL RECHECK** |
| Thesis public dissemination | Exact-title web search on 2026-08-27 did not identify a public copy; this does not establish absence from an institutional archive. | Public status not established. | **NOT VERIFIED; USER INPUT / PORTAL RECHECK** |
| Thesis citation solely for AI provenance | No policy basis was identified requiring an author to cite a thesis merely to prove pre-AI intellectual provenance. | Thesis is not added to reviewer manuscript for that purpose. | **DO NOT ADD SOLELY FOR AI DEFENSE** |
| Text recycling / substantial overlap | Publisher ethics require original work and appropriate treatment of reused material. | Structural comparison identifies inherited baseline model but no current selective-erosion/stability theorem counterpart in the thesis; no exhaustive forensic prose scan claimed. | **READY WITH CONTINUING HARD GATE** |
| Public repository and anonymization | Double-anonymized review requires reviewer materials not to disclose identity. | Public GitHub repository exists, but reviewer manuscript and anonymous replication package omit its URL/history/owner identity. | **READY** |
| Competing interests | Elsevier publishing ethics require disclosure of relevant competing interests. | Unknown. | **USER INPUT REQUIRED** |
| Funding | Funding must be disclosed accurately. | Unknown. | **USER INPUT REQUIRED** |
| CRediT | Current IJIO articles display CRediT contribution statements; first-submission portal requirement could not be independently verified. | Authorship/coauthor roles not supplied. | **USER INPUT REQUIRED / PORTAL RECHECK** |
| Preprints/working papers | Elsevier generally permits electronic preprints subject to journal-specific/anonymization rules. | Other preprint/working-paper/conference dissemination is not confirmed. | **USER INPUT REQUIRED** |
| Simultaneous submission/originality | Elsevier ethics prohibit simultaneous journal submission and require author approval. | Factual status not independently certified. | **USER CONFIRMATION REQUIRED** |
| Suggested reviewers | Current IJIO portal requirement could not be retrieved. | Six-person subject-fit pool prepared. | **READY IF REQUESTED; conflict status USER CONFIRMATION REQUIRED.** |
| Opposed reviewers | No evidence that exclusions are required. | None proposed. | **NONE** unless a genuine conflict is supplied. |
| Submission fee | Current Guide inaccessible. | No payment action. | **PORTAL RECHECK REQUIRED** |
| Open access / APC | IJIO offers open-access options; exact current APC not verified for this package. | No OA selection made. | **DECISION NOT NEEDED BEFORE INITIAL SUBMISSION** |
| Page/word limit | No current IJIO-specific hard page/word cap independently verified. | Review-mode manuscript prepared. | **PORTAL RECHECK REQUIRED** |
| References | Manuscript uses `elsarticle-harv` author-year format and citations are included in the reproducible build. | Complete. | **READY** |
| ORCID | Current IJIO-specific requirement could not be verified. | Not supplied. | **USER INPUT REQUIRED IF AVAILABLE / PORTAL RECHECK** |
| Corresponding author | Submission system requires author/contact metadata outside the anonymous reviewer manuscript. | Not supplied in reviewer manuscript. | **USER INPUT REQUIRED** |

## Operational submission rule

At portal entry, recheck every field marked **PORTAL RECHECK REQUIRED** against the live Editorial Manager screens and the then-accessible IJIO Guide for Authors.

Do **not** add the public repository URL or an identifying thesis citation to the reviewer manuscript or anonymous replication package solely for provenance purposes. If a live journal rule requires prior-work disclosure, place it in the journal-prescribed location while preserving double-anonymous review.

Do **not** press the final submission/approval button without explicit author authorization.
