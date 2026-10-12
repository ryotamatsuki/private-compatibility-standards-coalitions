# JICT short manuscript, frozen-theory editorial experiment

Independent 18-page double-spaced JICT reviewer manuscript (17--19-page release gate); canonical R9 manuscript is untouched. Main source is `main.tex`, with six shortened sections. Math in `short_04_incentives.tex` is the R9 residual-rent proof preserved in its entirety with only renamed cross-references.

To build: `make figures tables && python code/revision/build_jict_short.py`; output: `submission/generated/jict_short_manuscript.pdf` and the short-version anonymous Online Supplement plus one-level LaTeX archives. Journal's typical under-20 pages is respected without font or margin tricks.

The original R2–R9 theorem/certification scope is unchanged. This is a **draft preview** for independent editorial review, not a publication freeze or a journal submission. Compare it to the preserved 39-page R9 JICT package before approving replacement; the short text reduces breadth and detailed derivations but retains core equations, partial-adaptation open-set witness, and negative results.

The post-referee revision specifies the coalition-deviation map and restores the separate-standards welfare payoff. The full-bypass stability theorem now has a compact five-partition blocking proof in the main text and a complete seven-coalition ledger in anonymous Online Supplement Appendix G. These are exposition-only changes; the R3 residual-rent proof and exact joint equilibrium witness are unchanged. Dedicated CI checks both source archives, the 17--19-page body target, supplementary Appendix G, and anonymous PDFs.
