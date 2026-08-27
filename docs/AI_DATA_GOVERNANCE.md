# AI Data Governance

Verified/updated: 2026-08-27

## Purpose

This document defines the privacy, confidentiality, and provider-terms gate for AI-assisted work on unpublished research in this repository. It does not certify historical provider settings that cannot be verified.

## Elsevier-side requirement

The current Elsevier generative-AI policy requires authors to check the terms and conditions of any AI tool used with unpublished manuscripts, research material, or data; maintain privacy and confidentiality; and ensure that the provider is not granted rights to use the material beyond providing the service, including model-training rights. Authors must also ensure that output-related terms do not restrict publication.

Primary source checked on 2026-08-27:

- https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals

## OpenAI-side current information

Official OpenAI sources checked on 2026-08-27 state, in summary:

- for personal ChatGPT services, content may be used to improve models unless the user opts out through Data Controls;
- turning off `Improve the model for everyone` prevents new conversations from being used to train models;
- Temporary Chat is not used to train models;
- ChatGPT Business, Enterprise, Edu, and the API do not use inputs/outputs to train models by default.

Primary sources:

- https://help.openai.com/en/articles/7730893-data-controls-faq
- https://openai.com/policies/how-your-data-is-used-to-improve-model-performance/
- https://openai.com/enterprise-privacy/

Provider policies can change and must be rechecked before use.

## Status for this research

| Item | Status | Meaning |
|---|---|---|
| Historical AI-provider data setting | **NOT VERIFIED** | Do not infer the setting used for earlier conversations. |
| Current account-level setting | **USER VERIFICATION REQUIRED** | This repository cannot establish the author's current account setting. |
| Prospective governance rule | **ESTABLISHED** | The hard gate below applies to future unpublished work. |

`NOT VERIFIED` is an audit status, not an automatic finding that publication is prohibited.

## Prospective hard gate

Before entering unpublished manuscript text, research ideas, code, or other non-public research material into an AI service:

1. verify the provider's current terms and privacy/confidentiality treatment;
2. verify whether inputs/outputs may be used for model training or broader model improvement;
3. use a service/configuration whose applicable terms are compatible with the publisher's confidentiality and rights requirements;
4. verify that publication rights in outputs are not restricted;
5. record the date, service/configuration, and evidence in the private AI-use audit;
6. if the status is unclear, do not use the service for the unpublished material.

A UI toggle is not a substitute for reading the applicable provider terms when publisher policy requires a contractual/rights check.

## Restricted and prohibited inputs

### Restricted unpublished research content

Use only after the prospective hard gate passes:

- unpublished manuscript text;
- unpublished model-development notes;
- unpublished research code;
- unpublished figures/tables or replication artifacts.

### Prohibited without a separate explicit policy basis

Do not enter into a general AI workflow:

- confidential reviewer reports;
- confidential editor correspondence;
- confidential submission-system content;
- third-party proprietary/confidential material that the author lacks permission to provide;
- personal or sensitive data not required for the research task.

## Evidence retention

Provider-setting screenshots, account-specific settings, prompt/output logs, and detailed historical records are confidential audit material. Store them outside the public repository, for example under the gitignored `.local-research-audit/` directory.

## Submission-time recheck

Immediately before IJIO submission, recheck:

- Elsevier AI/privacy requirements;
- OpenAI/provider terms relevant to any continued AI use;
- live IJIO portal instructions;
- whether any new confidential editorial material will enter the workflow.
