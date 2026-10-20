# R18 — Independent execution record (2026-10-20)

Executor: independent SymPy exact rational reconstruction; research-only. Full reproducible command:

python -m pip install sympy==1.13.3
python research/r18/verify_r18.py

Expected script assertions: positive interior q and price-cost margins at tested market profiles; full 8 SU, 64 SW, 1 IS firm action enumeration; *every* unilateral investment deviation; unique SU outsider-only and SW no-adoption; exact scope fee gap; exact quadratic envelope representation and global interval endpoints; exact L0>0>U1 with pre>=L0 and post<=U1; exact zero-network negative counterexample.

**R9 Cournot:** 17 distinct market matrices covered by independently selected stage portfolios; 8/64 profile sets. Outsider one-interface gross gain 0.11800704152960527, maximal SU member reverse 0.06502431769120066, maximal SW incremental 0.06816794947574013; F=.09. Exact initial national ranking 2408509/295731200, after -1341/184832. New initial lower certificate 1041/924160 and post upper -3061/1478656. All strict.

**R16 differentiated Bertrand:** 17 distinct stage-market matrices covered (R16 reported 19 including additional price-deviation contexts); 8/64 firm portfolio sets. Outsider one-interface gross 0.02981641506151359, member/SW largest single incremental gain 0.015157171798828134; F=.025. Pre +0.0027740073314800945, post -0.0009074338893336889; new pre bound +0.0013170012026892915, post bound -0.0005916273735105906. Exact rationals held internally and emitted by script. All strict.

**Negative v=0:** pre gap -47/3200 at c=1/10, no reversal. **Bertrand global price Nash:** R18 independently re-solves interior FOCs and all firm portfolio deviations, not all alternative PRICE deviations; rely on R16's prior 211 exact feasible price checks and 171 entry inequalities, not a new certification. **C3 neighborhood:** R16 claim remains conditional/in need of expanded proof; R18 does not mark PASS.

**Protection:** R18 parent 786bbf43444d735b8dafabd41ceb1d05ac878525 from PR #42; CI checks exact absence of changes to inherited paper/docs/code and allows only R18 paths and its new workflow. Neither PR #34 nor R17 sources are modified. This log is a record of local execution; GitHub Actions status must be reported separately only after actual run completes.