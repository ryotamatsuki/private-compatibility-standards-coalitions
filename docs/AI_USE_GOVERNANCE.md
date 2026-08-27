# AI Use Governance

Verified/updated: 2026-08-27

## Purpose

This document governs public-safe disclosure and audit practice for AI-assisted work on *Private Compatibility and the Stability of Standards Coalitions*. It does not alter the frozen Stage-8 theory.

The governing principle is accurate separation of:

1. AI assistance in manuscript preparation;
2. AI assistance in the research process, including research-code development/editing;
3. human scientific judgment and responsibility; and
4. confidential/internal audit records that must not be committed to this public repository.

## Disclosure architecture

### Layer 1 — manuscript preparation

The declaration immediately before the references identifies ChatGPT (OpenAI), the manuscript-preparation purposes for which it was used, and human review/responsibility.

### Layer 2 — research process

The manuscript separately describes AI-assisted theoretical exploration, algebraic checking, source discovery, and research-code/reproducibility-script development and review. This disclosure also states the verification hierarchy and makes clear that AI output is neither mathematical proof nor a scholarly source.

### Layer 3 — confidential audit record

Detailed tool/model records, prompts/outputs where retained, provider-setting evidence, historical research files, and provenance evidence belong under `.local-research-audit/` or another non-public location. `.local-research-audit/` is gitignored.

## Permitted description of actual use

Subject to evidence available for each stage, AI assistance may include:

- theoretical and alternative-case exploration;
- research-gap, literature, and source discovery;
- manuscript organization, drafting, revision, and editing;
- algebraic checking;
- symbolic/numerical verification assistance;
- research-code development and editing;
- reproducibility-script preparation and review.

Do not reduce the actual use to grammar-only assistance. Conversely, do not attribute scientific authorship to AI.

## Human scientific control

The human author retains final scientific control over the research question, current model specification and assumptions, theorem statements, acceptance/rejection of theoretical claims, economic interpretation, scope, and final manuscript claims.

This statement does not assert that AI played no role in exploration, refinement, drafting, or code assistance. It records who made the final scientific decisions.

## Verification hierarchy

AI output is not treated as proof or as an authoritative source. The approved workflow is:

```text
human scientific decision
    -> analytical derivation / re-derivation
    -> independently executable symbolic cross-checks
    -> numerical admissible-domain checks
    -> source-level bibliographic verification
    -> final human acceptance of the claim
```

Numerical verification is never proof. Because AI assistance may have been used for both expressions and code, use `computationally cross-checked` or `checked by independently executable scripts` rather than an unqualified claim of independent mathematical verification where that stronger claim is not justified.

## Bibliographic control

AI-generated or AI-suggested references are not authoritative. Material bibliographic claims must be checked against original articles, publisher records, DOI records, or other authoritative sources before use.

## Record retention

Where available, retain a private record of:

- tool/service;
- model/version only when reliably known;
- date/stage;
- purpose and category;
- relevant prompt/output where retained and appropriate;
- human review and decision;
- verification artifact;
- relevant commit/PR/canonical document;
- provider data/privacy setting and evidence.

Historical records that do not exist must be marked `NOT AVAILABLE` or `NOT VERIFIED`, never reconstructed as fact.

## Public-repository rule

Do not commit full prompts/outputs, unpublished historical source material, confidential correspondence, provider-account screenshots, or detailed private provenance evidence merely to strengthen an audit trail. The public repository stores governance, reproducible scientific artifacts, and a template; the detailed audit stays private.

## Current policy basis

Primary policy source checked on 2026-08-27:

- Elsevier, Generative AI policies for journals: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals
- Elsevier, Updated generative AI policies for journals (18 August 2026): https://www.elsevier.com/connect/updated-generative-ai-policies-for-journals-supporting-responsible-use-while-protecting-trust

Policy must be rechecked at submission because publisher requirements can change.
