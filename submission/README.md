# IJIO Submission Package

Target: *International Journal of Industrial Organization* (IJIO)

This directory contains the upload-ready administrative and reproducibility layer for **Private Compatibility and the Stability of Standards Coalitions**. It does not change the frozen Stage-8 economic model.

## Technical return dated 2026-09-07

The IJIO editorial office returned the submission before external review for two technical corrections:

1. provide the LaTeX source material, including any figure files actually used by the manuscript;
2. place author name, affiliation, email address, and corresponding-author designation on the title page of the main document.

The submission pipeline therefore now produces a separate identified Editorial Manager manuscript/source package while preserving the canonical anonymous research manuscript and anonymous replication package separately.

## Author metadata for the returned submission

- Author: Ryota Matsuki
- Affiliation: Independent Researcher, Matsuyama, Ehime, Japan
- Email: ryota.matsuki@gmail.com
- Corresponding author: Ryota Matsuki

## Intended upload set for the technical return

- `generated/manuscript.pdf` — identified main manuscript generated from the Editorial Manager source package.
- `generated/ijio_em_source.zip` — flat, one-level LaTeX/BibTeX/source archive for Editorial Manager; contains the identified `main.tex` and all source dependencies actually referenced by the manuscript.
- `generated/title_page.pdf` — separate identified title page, retained in case the live portal requests it as a distinct file.
- `generated/cover_letter.pdf` — IJIO-specific cover letter with corresponding-author details populated; final certification text still requires factual confirmation before submission.
- `highlights.txt` — five Elsevier-compliant highlights, each <=85 characters.
- `generated/replication_package_anonymous.zip` — separate reviewer-safe source/code package with no git history or repository-owner identifiers.

## Administrative source files

- `metadata.md` — copy/paste submission-system metadata and the technical-return record.
- `declarations.md` — data/code/AI statements and author-dependent declarations.
- `checklist.md` — READY / NOT REQUIRED / USER INPUT REQUIRED / PORTAL RECHECK status.
- `reviewer_candidates.md` — subject-fit candidate pool; conflicts must be confirmed by the author before use.
- `reproducibility_readme.md` — README embedded in the anonymous replication package.
- `cover_letter.tex` and `title_page.tex` — sources for generated PDFs.

## Build logic

`make submission` now:

1. verifies the frozen symbolic and numerical model;
2. generates figures and tables;
3. constructs a flat one-level Editorial Manager source archive from the canonical paper sources;
4. replaces only the anonymous author marker in the generated EM copy with the identified author block;
5. compiles `generated/manuscript.pdf` from that flat identified source package;
6. keeps `paper/main.tex` anonymous for the separate replication package;
7. runs source-archive, author-metadata, PDF, and anonymization gates.

This separation is deliberate: the IJIO technical return requires author information in the main document, while the reproducibility archive remains identity-free.

## Hard rule

No final Submit / Approve Submission / Confirm action is authorized without explicit author approval. Recheck the live Editorial Manager file labels and any remaining declaration/fee fields immediately before approval.
