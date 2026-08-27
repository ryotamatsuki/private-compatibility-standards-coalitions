# IJIO Submission Readiness — AI, Provenance, and Data Governance

Verified/updated: 2026-08-27

Target: *International Journal of Industrial Organization* (IJIO)

Theory status: **FROZEN — NO SCIENTIFIC-CONTENT CHANGE IN THIS AUDIT**

## Executive verdict

```text
CONDITIONAL GO
```

The manuscript can proceed toward IJIO submission from an AI-disclosure and research-provenance standpoint after the changes recorded here. The current paper now separates manuscript-preparation disclosure from research-process/code disclosure, documents pre-AI provenance without using it to minimize AI assistance, and establishes prospective privacy/data-governance rules. Remaining conditions are administrative or factual: historical provider settings are not verified, the current account-level data setting must be checked by the author, the live IJIO Guide/portal still requires a final recheck for inaccessible journal-specific fields, thesis public-dissemination status is not fully verified, and the final PR/CI gate must pass.

## Live policy findings

Primary sources checked on 2026-08-27 include:

- Elsevier generative-AI policy: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals
- Elsevier policy update dated 18 August 2026: https://www.elsevier.com/connect/updated-generative-ai-policies-for-journals-supporting-responsible-use-while-protecting-trust
- Elsevier publishing ethics / prior-publication guidance: https://www.elsevier.com/about/policies-and-standards/publishing-ethics
- IJIO journal page: https://shop.elsevier.com/journals/international-journal-of-industrial-organization/0167-7187
- IJIO Guide for Authors: https://www.sciencedirect.com/journal/international-journal-of-industrial-organization/publish/guide-for-authors
- OpenAI Data Controls FAQ: https://help.openai.com/en/articles/7730893-data-controls-faq
- OpenAI model-improvement data policy: https://openai.com/policies/how-your-data-is-used-to-improve-model-performance/
- OpenAI enterprise privacy: https://openai.com/enterprise-privacy/

The IJIO Guide URL remained inaccessible to the automated policy client (HTTP 403), so unresolved journal-specific fields remain `PORTAL RECHECK REQUIRED`. A current first-party Elsevier journal listing states that IJIO uses double-anonymized peer review; the reviewer manuscript therefore remains anonymous and the public repository URL is excluded from the reviewer manuscript and anonymous replication package.

## Compliance matrix

| Requirement | Status | Action / evidence |
|---|---|---|
| Manuscript-preparation AI disclosure | **READY** | ChatGPT named; purposes and human review/responsibility stated immediately before references. |
| Research-process AI disclosure | **READY** | Separate unnumbered research-methods disclosure added. |
| AI-assisted research-code disclosure | **READY** | Research-code development/editing and reproducibility-script assistance described in research-process disclosure. |
| Human scientific responsibility | **READY** | Final scientific control over question, specification, claims, interpretation, and scope stated without denying AI-assisted exploration. |
| AI output not treated as proof/source | **READY** | Explicit in research-process disclosure and governance. |
| Symbolic/numerical verification characterization | **READY** | Described as computational cross-checks; numerical checks are not proof. |
| Bibliographic source verification | **READY** | Original/publisher/DOI/authoritative-source verification required. |
| AI-use audit trail | **READY AS GOVERNANCE** | Public template supplied; detailed record kept privately. |
| Historical AI-provider setting | **NOT VERIFIED** | Must remain unknown unless evidence is available. |
| Current AI-provider setting | **USER VERIFICATION REQUIRED** | Verify applicable account/provider terms before further unpublished work. |
| Prospective privacy/data hard gate | **READY** | `docs/AI_DATA_GOVERNANCE.md`. |
| Thesis prior-publication treatment | **GENERAL ELSEVIER RULE VERIFIED / IJIO RECHECK** | Academic theses are generally excepted from prior-publication restrictions; journal-specific rule must be rechecked. |
| Thesis public dissemination | **NOT VERIFIED** | Exact-title web search found no public copy, but institutional-repository status is not proven. |
| Thesis/current-paper structural comparison | **READY** | Public-safe provenance matrix recorded. |
| Current-theorem overlap with thesis | **NO SUBSTANTIAL CURRENT-RESULT OVERLAP IDENTIFIED** | Current private-adoption/selective-erosion/stability theorem chain has no thesis counterpart. |
| Text-reuse risk | **NO MATERIAL ISSUE IDENTIFIED IN STRUCTURAL REVIEW** | No claim of exhaustive forensic similarity scan; investigate any later-discovered substantial prose/proof reuse. |
| Double-anonymous review | **VERIFIED FROM CURRENT ELSEVIER LISTING** | Keep reviewer manuscript/replication package anonymous. |
| Public GitHub URL in reviewer files | **ABSENT / READY** | Continue to exclude. |
| Final IJIO portal fields | **PORTAL RECHECK REQUIRED** | Recheck live Guide and Editorial Manager before upload/certification. |
| Final build / CI | **PENDING PR GATE** | Must pass repository verification and submission package build. |

## Pre-AI research provenance verdict

```text
BASELINE-MODEL + EXTENSION-IDEA
```

### Confirmed pre-AI antecedents

The available undergraduate research predating generative AI contains:

- the three-country/one-firm-per-country standards framework;
- segmented Cournot competition;
- heterogeneous consumer willingness to pay and compatibility/network effects;
- a foreign-standard incompatibility unit cost;
- separate, regional, and international standardization regimes;
- national welfare combining consumer surplus and domestic-firm worldwide profit;
- an explicit future-research proposal in which firms themselves choose whether to use another country's standard / join the compatibility network.

### Not present as completed results in the thesis

The earlier work does not contain the current:

- fixed-cost private-adoption stage;
- support-set and used-standard formulation;
- formal/effective compatibility distinction;
- five-partition stability game;
- strict-blocking stability correspondence;
- selective-erosion/private-circumvention theorem;
- `F`-dependent SU-to-IS stability reversal;
- low-`F` multistandarding branch;
- current theorem chain.

## Thesis/current-paper comparison

| Dimension | Earlier thesis | Current paper | Assessment |
|---|---|---|---|
| Research question | Government standardization, network effects, inefficient bloc | How private compatibility changes formal-coalition stability | Material development |
| Countries/firms | 3 countries, 1 firm each | Same baseline | Inherited |
| Product markets | Segmented Cournot | Segmented Cournot, re-derived/corrected | Inherited/reformalized |
| Compatibility/network effects | Yes | Yes, formalized by used-standard compatibility groups | Inherited/reformalized |
| Incompatibility cost | Unit cost `c` | Marginal adaptation/incompatibility cost `c` | Inherited/reformalized |
| Regimes | SW/SU/IS in sequential government game | Five formal partitions | Extended |
| Firm standard choice | Not solved; proposed as future extension | Endogenous fixed-cost standard support | Materially new formalization |
| Coalition concept | Sequential accession/acceptance game | Strict blocking over partitions | New equilibrium/stability structure |
| Main result | Possible inefficient SU; firm-government preference gap | Private bypass selectively erodes bloc rent and can reverse stability | New mechanism/result |

## Current-paper originality assessment relative to the thesis

The thesis is an intellectual antecedent and benchmark, not evidence of published novelty. Current novelty claims remain governed by the external prior-art audit and `docs/LITERATURE_POSITIONING.md`.

At the theorem level, the thesis does not establish the present private-adoption thresholds, selective-erosion identity/theorem, three-country microfoundation of that mechanism, or the strict-blocking SU-to-IS stability reversal. The repository also records that historical welfare formulas required correction and that the old SW-equilibrium result was dropped; those historical results must not be reintroduced.

## Exact disclosure architecture

1. **Manuscript-preparation declaration** — immediately before references, focused on organization/drafting/revision/source checking/reproducibility-script preparation and human review/responsibility.
2. **Research-process disclosure** — separate unnumbered section covering theoretical exploration, algebraic checking, source discovery, code development/editing, and the verification hierarchy.
3. **Private AI/provenance audit** — detailed records, prompts/outputs where retained, historical evidence, and provider-setting evidence kept outside the public repository.
4. **Prior-dissemination disclosure, if required** — only if IJIO/Elsevier rules or a material overlap finding requires citation, acknowledgment, cover-letter, or portal disclosure. The thesis is not inserted into the reviewer manuscript merely to prove pre-AI provenance.

## AI-assisted code treatment

AI assistance may have been used in developing/editing SymPy, numerical, figure/table, validation, and reproducibility scripts. The disclosure therefore does not treat code assistance as ordinary manuscript editing. Code correctness is supported by execution, analytical re-derivation, symbolic identity checks, numerical domain checks, deterministic output generation, and clean-room replication-package QA. These checks validate stated outputs; they do not convert AI output into proof.

## Privacy/data governance

### Historical

```text
Historical AI-provider data setting: NOT VERIFIED
```

No inference is made about past ChatGPT account settings without evidence.

### Current

```text
Current account-level setting: USER VERIFICATION REQUIRED
```

### Future hard gate

Before further unpublished work is supplied to an AI service, verify provider terms, training/model-improvement treatment, confidentiality/privacy, output rights, and record evidence privately. Confidential reviewer/editor/submission-system material is excluded from ordinary AI workflows.

## Scientific-authorship assessment

The evidence supports the following workflow description:

```text
pre-AI research interest and baseline model
    -> pre-AI firm-standard-choice extension idea
    -> human control of the current scientific specification
    -> AI-assisted exploration / drafting / code assistance
    -> human theorem and claim decisions
    -> analytical derivation / re-derivation
    -> symbolic/numerical cross-checks
    -> source-level literature verification
    -> final human scientific judgment
```

This does not claim that every current idea existed before AI, and it does not minimize substantial AI assistance. It distinguishes intellectual provenance, assistance, verification, and responsibility.

## Review pass

| Reviewer perspective | Status | Finding |
|---|---|---|
| A — Elsevier AI policy | **PASS** | Two-layer disclosure now covers manuscript preparation and research-process/code use. |
| B — IJIO submission policy | **MINOR / PORTAL RECHECK** | Double-anonymous review is verified from a current Elsevier listing; inaccessible Guide/portal-specific fields remain. |
| C — Publication ethics / prior work | **MINOR / RECHECK** | Thesis is generally permissible under Elsevier policy and no current-theorem duplication is identified; exact public-dissemination and IJIO-specific thesis rule remain to be confirmed. |
| D — Scientific authorship / provenance | **PASS** | Pre-AI baseline + extension idea are documented without claiming that current theorems predated AI. |
| E — Reproducibility engineering | **PENDING CI** | Repository pipeline must pass on the PR head. |

## Remaining blockers / conditions

Before final portal certification:

- verify the current AI-provider/account data setting and applicable terms for any continued unpublished work;
- recheck the live IJIO Guide and Editorial Manager fields;
- resolve user-input items already tracked in `submission/checklist.md` (funding, conflicts, authorship/contact information, simultaneous-submission certification, etc.);
- confirm any known thesis repository/public dissemination if the author has such information;
- require the final PR head to pass Paper CI and submission-package QA.

No theory repair is authorized or required by this governance audit.
