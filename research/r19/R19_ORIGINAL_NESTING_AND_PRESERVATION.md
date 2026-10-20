# R19 exact nesting and preservation ledger

R19 starts from actual R18 head `6cd349daec244def5cb4ed475cc448ed091b9c22`.
Original PR34 head remains `08d6e6adb1a90bdf03fa223c0961ac04620f0fa2`.
Only new research/r19 files and one new R19 workflow are allowed. No old
paper, code, docs, R18 or other research file is edited; no merge or
journal submission is performed. The original timing and welfare ownership
are preserved, including all documented corrections and failures.

| Preserved item | Exact correspondence / verification |
|---|---|
| Three countries; SU,SW,IS; post-policy private support | same 8 SU/64 SW/1 IS action profiles and per-standard fixed F |
| R9 demand and singleton-zero network | `gamma=1` with R13 homogeneous buyer ties and clearing gives original `p_i=1-Q+v*Cq`; no smooth-demand fiction |
| Consumer surplus | exactly `Q^2/2` in R9; `q'M0q/2` in differentiated FE buyer class |
| Original production and unsupported/support cost | 0,c,d unchanged; support changes both network and cost while residual comparison fixes post-support network |
| National welfare | home CS plus ONE home firm's worldwide net profit; symmetry only permits the m shortcut |
| Original partial quantities | T-R at gamma=1,ell=1-v gives `(1+d)/[4(1-v)]`, `(1-3d)/[4(1-v)]` |
| Residual function and cutoff | symbolic identity `R_gamma,v,ell(d)=d[(5-4v)d+2(1-4v)]/[32(1-v)^2]`; no replacement of R9 classification |
| R9 successful and unsuccessful examples | exact replay plus new zero-network investment-without-reversal example |
| Existing coalition stability | only original full-bypass strict-blocking/five-partition scope; no automatic positive-d or Bertrand extension |
| R10 correction | same-parameter full reversal stays RETRACTED; same-parameter partial residual slope contrast is explicitly a different statement |
| R13 expectation/strategy timing | individual buyer network expectation fixed; firm strategies anticipate fulfilled-network response |
| R15/R16 nonlinear evidence | all original calculations repeated, with numerical versus global theorem qualifications retained |

The analytical proof of R9 nesting is in T-R and the independent referee
expansion, not merely a successful numeric comparison. `verify_r19.py`
hashes every baseline Git blob from working files and rejects any mismatch.
The new CI also rejects changed/added paths outside its whitelist.

The proposed manuscript is built from the actual immutable PR34 source
with its original six-section body and then adds a separate audited R19
section. It does not include unverified R19 Main-Theorem claims, nor import
R12/R16 appended content as if certified R9 source. The helper records
snapshot SHA values; generated compilation files remain in the ignored
build directory. Source snapshots are build inputs, not edits to PR34.
