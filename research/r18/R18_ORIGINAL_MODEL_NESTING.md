# R18 — Original R9 exact nesting, negative results and conservation ledger

R18 is a separate **overlay** based on R17 SHA 786bbf43444d735b8dafabd41ceb1d05ac878525. PR #34 head 08d6e6adb1a90bdf03fa223c0961ac04620f0fa2 is **not** updated. R18 touches only research/r18/** and one new CI workflow; CI compares unchanged paper/, docs/ and code/ against R17's immutable parent.

| Original item | Canonical source/result | R18 correspondence | Independent status |
|---|---|---|---|
| Three countries, two-member SU, outsider, SW/IS | short_02_model.tex, native and extra standards | Groups B/C; 2 member markets, 1 outsider, fixed F per extra standard | Same partitions, timing and native group |
| R9 quantity FOCs and inverse demand | p_i=1-Q+v sum_compatible q, singleton network zero; Cournot anticipates fulfilled networks | market() with M=ones-vC and q=(M+diag(Mii))^-1(ones-cost), positive interior | Exact symbolic Cournot q and stage re-solved |
| Consumer surplus and national accounts | CS=Q²/2 and W_i=CS_i+worldwide home profit-F n_i | m_B, m_C combine CS plus two member producers ONLY by symmetry; f_B is ONE home export profit | Exact matched W gap and R13 derivation |
| Complete adaptation d=0 | old profit blocks P,A,B,C,K_I,K_M | limit m_C(0)=K_I+2P, export f_B(c)=C | Identity, no legacy update |
| Partial residual cost d=lambda c | R(d,v) in short_04_incentives.tex | m_C(d)-m_C(0)=R(d,v) in original Cournot | Checked at rational witness; source R(d,v) untouched |
| Pre/post government ranking | E-D and R(d,v)-D | D0=m_B(c)+f_B(c)-m_C(0)-f_C; D1=m_C(d)+f_B(c)-m_C(0)-f_C | Exact numerical/rational match |
| Full endogenous investment game | 8 SU and 64 SW action profiles; interval for F | independently re-solve all 8/64 profiles and every unilateral alternative | Exact SymPy rational strict one-way equilibrium for two witnesses |
| R9 strict full-bypass coalition stability | five partitions, strict blocking, d=0 only | no generalized stability claim from R18 | Preserved **only original proved scope** |
| R9 v=0 and singleton-positive failures | no initial SU advantage or other excluded configurations | v=0,c=1/10: D0=-47/3200, no reversal theorem | Explicitly retained |
| R5 differentiated gamma=1/2 failure | differentiated Cournot/Bertrand example fails initial SU ranking | no blanket cross-conduct assertion | Retained |
| R10 false common-parameter portability | R15 correction | original R10 CS_old != FE CS; R18 keeps the **retraction** | No resurrection |
| R15 nonlinear Cournot and R16 nonlinear Bertrand | function-space continuation / numerical quartic | R18 has no new all-C3 uniqueness proof | Inherited only with exact original qualifications |

The source proof of all-original-parameter mathematical equivalence is the R9 block formulas, canonical R13 nesting and the parent CI, not the R18 table alone. A new theorem cannot retroactively make the **strict-blocking** coalition stability theorem valid for positive residual d or every market model.

**Protection check:** expected only these new file paths: research/r18/**, .github/workflows/r18-general-theorem-audit.yml. GitHub CI uses git diff --exit-code from R17 for paper docs code and full path whitelist. The commit history retains all prior source blobs without alteration; this is not a claim about bytes of the historical Editorial Manager upload, which R0 itself says could not be fully verified.