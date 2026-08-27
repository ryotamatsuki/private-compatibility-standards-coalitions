# Japanese Study Version Verification Report

## Canonical English base

- Repository: `ryotamatsuki/private-compatibility-standards-coalitions`
- Canonical English SHA: `c98309c75740df459ba356852b895d2d7a748d84`
- Verification date: 2026-08-27
- Japanese branch: `docs/japanese-study-version`
- Open PRs at task start and at pre-push recheck: none

The English manuscript, canonical model, bibliography, verification scripts, root Makefile, and existing CI configuration were not modified for the Japanese study version.

## Canonical mathematical verification

The repository-root command `make verify` was rerun against the canonical English base. Result: **PASS**.

The passing gates included:

- symbolic private-adoption identities and threshold factorizations;
- general-mass and symmetric selective-erosion identities;
- reciprocal-disadvantage and outsider post-bypass welfare identities;
- exact `\Omega_0` witness verification;
- analytical welfare sign certificates;
- numerical domain and first-order-condition checks;
- high-`F` stable-set regression;
- intermediate-`F` stable-set regression;
- market-size partner-selection regression.

Numerical verification remains a regression/sanity check and is not used as a substitute for the analytical proofs.

## English/Japanese correspondence audit

Command:

```bash
make -C paper-ja audit
```

Result:

```text
JAPANESE STRUCTURAL AUDIT: PASS (15 translated source files + 3 generated tables)
- ordered labels/citations: identical
- refs/eqrefs: identical multiplicity
- section hierarchy and theorem environments: identical
- display mathematics: identical after whitespace normalization
- inline mathematics: identical exact-token multiplicity
- generated tables: labels/mathematical tokens/tabular structure identical
```

The 15 translated source files are Sections 1--11 and Appendices A/B/C/F. Generated tables are checked separately because only their human-readable display text is translated; labels, mathematical tokens, and tabular structure remain canonical.

## Japanese LaTeX build

- Engine: LuaLaTeX with `luatexja`
- Bibliography: canonical `paper/references.bib` via BibTeX
- Output: `paper-ja/main-ja.pdf`
- Page count: **70 pages**
- Undefined references: none
- Undefined citations: none
- Multiply defined labels: none
- Overfull boxes: none detected in the final log
- Missing-character warnings: none detected in the final log
- Included appendices: A, B, C, F

The CI-compatible source does not depend on a user-installed proprietary Japanese font. The TeX Live `luatexja` environment resolved Japanese text with the bundled Harano Aji family during verification.

## Visual PDF verification

The final PDF was rendered with the repository-independent PDF rendering workflow at 200 dpi for representative pages covering:

- front matter and the start of the Introduction;
- the model timing figure;
- the central formal-stability theorem;
- Appendix welfare sign calculations;
- declarations and bibliography/end matter.

The inspected renders showed no clipped text, object overlap, black squares, broken Japanese glyphs, missing figures, or materially broken mathematical layout.

## Translation control rule

This Japanese version is an unofficial internal-study companion. It is not the submission manuscript and has no independent scientific priority. In case of any discrepancy, the English version controls.
