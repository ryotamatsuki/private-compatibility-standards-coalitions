# Anonymous Replication Package

Paper: *Private Compatibility and the Stability of Standards Coalitions*

This package reproduces the symbolic checks, analytical welfare-sign certificates, numerical regressions, figures, tables and manuscript build used in the paper. It intentionally contains no git history, repository-owner name, repository URL, author email or author-identifying metadata.

## Environment

Recommended:

- Python 3.12
- `pip install -r requirements.txt`
- a LaTeX installation providing `latexmk`, `elsarticle`, `booktabs`, `amsmath`, `amssymb`, `amsthm`, `graphicx`, `xurl`, and `hyperref`

Pinned Python dependencies are recorded in `requirements.txt`.

## Reproduction commands

From the package root:

```bash
make verify
make figures
make tables
make tables-check
make paper
```

Or run the full pipeline:

```bash
make all
```

Expected gates:

- symbolic verification: PASS;
- analytical welfare-sign certificates: PASS;
- numerical verification: PASS;
- high-private-cost stable-set regression: PASS;
- intermediate-private-cost stable-set regression: PASS;
- market-size partner-ranking regression: PASS;
- figure generation: PASS;
- table generation and syntax check: PASS;
- citation/reference/label gate: PASS;
- manuscript compile: PASS.

## Source hierarchy

`docs/CANONICAL_MODEL.md` is the human-readable mathematical source of truth and `code/canonical.py` is the machine-readable canonical implementation. The verification scripts do not replace analytical proofs in the manuscript; they provide independent symbolic and numerical checks.

## Data statement

No empirical data are used. Numerical output evaluates closed-form theoretical expressions and regression-style stability checks over the model's admissible parameter domain.
