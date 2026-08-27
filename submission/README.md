# IJIO Submission Package

Target: *International Journal of Industrial Organization* (IJIO)

This directory contains the upload-ready administrative and reproducibility layer for **Private Compatibility and the Stability of Standards Coalitions**. It does not change the frozen Stage-8 economic model.

## Intended upload set

After the remaining author metadata are supplied and the live Editorial Manager screens are rechecked, the generated upload set is:

- `generated/manuscript.pdf` — anonymous reviewer manuscript.
- `generated/title_page.pdf` — separate non-anonymous title page; currently contains explicit `TBD -- USER INPUT REQUIRED` placeholders.
- `generated/cover_letter.pdf` — IJIO-specific cover letter; currently contains a corresponding-author placeholder and a certification placeholder.
- `highlights.txt` — five Elsevier-compliant highlights, each <=85 characters.
- `generated/replication_package_anonymous.zip` — reviewer-safe source/code package with no git history or repository-owner identifiers.

## Administrative source files

- `metadata.md` — copy/paste submission-system metadata.
- `declarations.md` — data/code/AI statements and author-dependent declarations.
- `checklist.md` — READY / NOT REQUIRED / USER INPUT REQUIRED / PORTAL RECHECK status.
- `reviewer_candidates.md` — subject-fit candidate pool; conflicts must be confirmed by the author before use.
- `reproducibility_readme.md` — README embedded in the anonymous replication package.
- `cover_letter.tex` and `title_page.tex` — sources for generated PDFs.

## Hard rule

This package may be used to prepare a draft submission, but **no final Submit / Approve Submission / Confirm action is authorized without explicit author approval**.

The current Guide for Authors URL returned HTTP 403 to the automated verification client. Any item marked `PORTAL RECHECK REQUIRED` must therefore be rechecked against the live IJIO Editorial Manager workflow immediately before upload.
