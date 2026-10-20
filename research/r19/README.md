# R19 research-only result

**Overall Level2 retained; requested Level3/4 NOT attained.**
Start with R19_LEVEL_3_4_FINAL_VERDICT.md, then the main theorem/proofs,
Stage0 diagnosis and source-graded prior-art audit. The new primitive
residual subtheorem, exact counterexamples and price-kink proof are saved
rather than presented as a successful joint primitive theorem.

Reproduce from repository root with Python3.12:

```bash
python -m pip install sympy==1.13.3 numpy==2.1.3 scipy==1.14.1 matplotlib==3.10.8
python research/r19/replay_work/replay_inherited.py
python research/r19/verify_r19.py
python research/r19/build_manuscript.py
```

The last command also requires pdflatex, bibtex, elsarticle and its
bibliography style, standard LaTeX math packages and fonts. A full Git
checkout is needed to read immutable R18 and PR34 objects. Its output
build/r19-manuscript combines exact R9 sources with the audited R19
section; it is a research proposal, not the JICT production package.
All R19 outputs are added files. Every inherited source remains intact.
The GitHub workflow runs the same checks and uploads logs/proofs/PDF.
