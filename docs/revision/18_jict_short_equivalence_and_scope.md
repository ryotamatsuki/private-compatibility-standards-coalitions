# R9 JICT short manuscript — self-containment / scientific-equivalence audit

Date: 2026-10-13 JST
Branch: `revision/r9-jict-short-20261013`, based on pre-existing `revision/r9-jict-length-audit-20261013`, not merged to `revision/research-track`.
Full certified R9 original is preserved, with the 39-page JICT reviewer version and 15-page Online Supplement.

## Actual local clean-room TeX prototype

Source: `paper/jict_short/main.tex` and six `short_*.tex` source sections, shared original `paper/preamble.tex` / `paper/references.bib`, original reproducibly generated residual-rent figure + table.
Local `latexmk -pdf` + BibTeX compiled without unresolved reference/citation warnings. **16 pages** on 612x792 pt paper, using the **same `elsarticle[review,authoryear]` document class** as the prior JICT reviewer PDF (no fake font, margin, or line-spacing adjustment). The earlier actual original CI PDF was **39 pages**. Existing Online Supplement source compiles to **15 pages** with new prose-only main-paper cross-reference names.
Local build script tested in a mock repository layout with exactly matching generated artifacts: `python code/revision/build_jict_short.py` => PASS (16 pages anonymous / 15 pages supplement). New branch GitHub Actions clean-room CI is independently required; do not call that result PASS until it actually completes.

## Main text result crosswalk

| Full manuscript content | Short version | Verifiability |
|---|---|---|
| Governments/formal partitions, compatibility group, consumer demand, cost, timing, welfare, strict coalition blocking | `short_02_model.tex`, `short_05_stability_scope.tex` | All economic primitives in main, definitions explicit |
| Cournot profit/consumer surplus blocks and market interior domain | `short_02_model.tex` | Actual formulas and member-market FOCs shown; full proof in Online Supplement A/B |
| Unique outsider-only private adoption on fixed-cost interval | `short_03_adoption.tex` | Core thresholds and selection-free sufficient conditions in main; all deviations in Supplement C/D |
| Government before/after ranking `E-D -> -D+R(d,v)`, R'(d)>0 and three-way outcome | **`short_04_incentives.tex`** | R9 final equation + proposition + proof **preserved in full** from `paper/sections/06_selective_erosion.tex`; only labels/cross-reference names changed |
| Exact same-primitives strict incomplete-adaptation witness & open-set proof | **`short_04_incentives.tex`** | Existing exact rational witness, SU/SW strict adoption inequalities and continuity certificate retained in main |
| Canonical full-bypass strict coalition stability and blocking/asymmetry sensitivity | `short_05_stability_scope.tex` | Named theorem, strict inequalities / proof sketch in main; full blocking comparisons in Supplement B/E/F. Not extended to positive d |
| Zero network, alternative singleton network, differentiated Cournot/Bertrand failure | `short_05_stability_scope.tex` | Quantifier/qualification in main; derivation in Supplement E |
| Consumer welfare vs home producer rents, limits, conditional policy application | `short_06_discussion.tex` | Scope and testability retained, no unauthorized empirical model |
| Close prior literature | `short_01_introduction.tex` | Gandal/Shy, Takarada et al., Innocenti/Menicucci, Ding/Ko/Shen, Schmidt/Steingress, Maggi/Mrazova, relevant trade/standards literature; no firstness claims |

## What was deliberately cut or moved

- The original seven-page model description, extensive prose on formal partitions and network allocation, and graphical timing illustration: reduced to clear definitions and timing in Section 2.
- Extended national welfare tables for all five partitions and the exhaustive fixed-cost deviation catalogs: moved to already existing Online Supplement. The main shows enough formulas to reconstruct the key resident government effect.
- Peripheral figures and tables about high-F coalition stability and robustness; retained only the residual-rent figure and region table tied to the headline result.
- Repeated statements of the same E,D,R identity across Intro, Model, Discussion, Conclusion.
- Supplemental root/stability polynomial calculations; kept the meaningful negative boundary/strict quantifiers.
- Works not cited in the shorter text were not artificially retained in the compiled bibliography; the canonical bibliographic master is untouched.

## Critical limitations that remain

1. Compact presentation potentially under-explains the government-stage stability proof, now a theorem plus proof sketch with SI full cases. A skeptical editor must compare clarity against the original before allowing final submission.
2. The 16-page reviewer PDF is **not** formal journal acceptance; the scientific contribution remains a limited, specification-sensitive conditional theory.
3. The original SI is 15 pages, only its **cross-reference prose** is adapted to the shorter section architecture; mathematics untouched, but the contents require explicit submission tagging as Online Supplement.
4. The model still depends materially on the singleton-zero-network convention, and the differentiated-demand generality failure remains; no hidden algebraic repair.
5. JICT's typical <20-page guideline is satisfied in local preview; final GitHub Actions must confirm the journal-specific build, anonymous source, supplement, and no broken references.

## Mandatory next release gate

- Ensure short-preview GitHub workflow is green on the actual branch/PR (BibTeX, main pages <20, anonymous source, supplement compilation), alongside inherited full Paper CI (R2–R9 mathematical/Lean/reproducibility and 39-page historical package).
- Inspect actual PDF formatting and ensure all figures and output references resolve and no page breaks obscure the key statements.
- Run a skeptical-editor *side-by-side* evaluation on the 39-page and 16-page manuscripts; if essential definitions/proof logic are lost, repair the short branch, not the certified R9 text.
- Do **not merge automatically** or freeze Stage 15 without user approval. User instructed creation of a separate branch, not replacement of the canonical integration branch.
- Before actual JICT submission, author must confirm identity, prior disclosures, originality, no simultaneous submissions, substantive AI declaration and live portal output.
