# Reproducible theory / figure / table pipeline

This directory implements the machine-side companion to the frozen Stage-8 theory.

- `canonical.py` — the only Python-side source for canonical formulas and controlled paper-facing formula renderings.
- `verify_symbolic.py` — re-derives the four Cournot subgames from FOCs and verifies the core Stage-8 identities symbolically.
- `verify_numeric.py` — deterministic witness, neighborhood, admissible-domain, and direct-FOC sanity checks. Numerical checks are not proofs.
- `make_figures.py` — reproducibly generates timing, selective-erosion, and verified-witness F-region illustrations.
- `make_tables.py` — reproducibly generates the three planned LaTeX table fragments.

Standard commands from the repository root:

```bash
make verify
make figures
make tables
make paper
```

`make all` additionally syntax-checks generated table fragments. Generated figures, tables, LaTeX intermediates, and verification JSON are intentionally ignored by Git and rebuilt from source.

At scaffold stage, `references.bib` contains no verified entries and the manuscript contains no citations. The Makefile therefore suppresses BibTeX only while both remain absent; once verified entries and citation commands exist, normal `latexmk`/BibTeX processing is enabled automatically.
