# IJIO Technical Return — 2026-09-07

Paper: **Private Compatibility and the Stability of Standards Coalitions**  
Submission: **IJIO-D-26-00585**  
Journal: *International Journal of Industrial Organization*

## Status

The editorial office returned the submission before external review for technical corrections only. The return requested:

1. manuscript source material (LaTeX, including figure files where applicable);
2. author information — names, affiliations, and email addresses — on the title page of the main document, with the corresponding author identified consistently with Editorial Manager.

This direct submission-specific instruction supersedes the earlier repository assumption that the uploaded main document should remain visibly anonymous.

## Author metadata applied

- Author: Ryota Matsuki
- Affiliation: Independent Researcher, Matsuyama, Ehime, Japan
- Email: ryota.matsuki@gmail.com
- Corresponding author: Ryota Matsuki

## Implementation rule

Do not alter the frozen theory or the canonical anonymous research source merely to satisfy the portal-specific technical return. Instead:

- keep `paper/main.tex` anonymous as the canonical research/replication source;
- generate an identified Editorial Manager copy in `submission/generated/ijio_em_source/`;
- package the exact source dependencies used by that identified document as `submission/generated/ijio_em_source.zip`;
- keep every source file at the same directory level because Elsevier Editorial Manager does not process TeX submissions containing subfolders;
- compile `submission/generated/manuscript.pdf` from the exact flat source package;
- retain `submission/generated/replication_package_anonymous.zip` as a separate identity-free reproducibility artifact.

## Verification gates

The technical-return repair is considered repository-ready only if CI confirms all of the following:

- frozen symbolic and numerical verification still passes;
- canonical anonymous manuscript still compiles;
- identified IJIO EM source archive contains no subfolders;
- identified `main.tex` contains Ryota Matsuki, the stated affiliation, email, and corresponding-author designation;
- the exact flat source archive compiles in a clean directory;
- the resulting PDF contains the required author metadata;
- anonymous replication package remains free of author identity and repository-owner identifiers;
- no theorem/model/paper-body changes are introduced by the repair.

## Portal execution

In Editorial Manager, open **Submissions Needing Approval by Author**, choose **Edit Submission**, replace/add the corrected manuscript and source files, rebuild the submission PDF, visually inspect the entire PDF, and only then approve the resubmission.

Final portal approval remains a user-controlled action because the live file-type labels, declarations, and certification checkboxes must be inspected at the time of resubmission.
