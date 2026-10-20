# R19 Stage 0: why the R18 theorem is Level 2

**Target diagnosis completed; requested Level 3 reduction remains open.**
All nine requested R18 files were obtained at immutable head `6cd349d`.
PRs 34/41/42/43 and R18 Actions run 39409427371 were read from the GitHub
connector; that run's actual head equals the same SHA and both jobs passed.
The exact input records are in `R19_INPUT_PROVENANCE.json`. Relevant R9,
R12/R13/R15/R16/R17 source and proof logs were checked; the independent
18-command replay and complete detailed diagnosis are in
`replay_work/R19_REPLAY_AND_GAP_DIAGNOSIS.md`.

## Every material R18 assumption, classified

| R18 condition | Type | What weakening/removal loses |
|---|---|---|
| atomistic quasilinear buyer choice and fulfilled expectations | preference/network/timing primitive | justified CS and exact R9 nesting; R10 is a concrete counterexample to switching CS conventions |
| c,d,F; support one standard in two markets | cost/access primitives | the two-market vs one-market investment technology |
| nonreciprocal destination recognition | access/network primitive | invariance of members' outsider-market profit |
| destination separability/symmetry | structural market restriction | factor-two gain without cross-market feedback; ownership shortcut for m |
| unique regular continuation or all-selection uniform bounds | endogenous equilibrium restriction | well-defined investment payoffs and selection-free conclusions |
| b_L,r_U,e_L,e_U | endogenous derivative envelopes | corresponding integral sufficient bounds; actual ranking need not fail when a loose bound fails |
| H,J | endogenous cross-network contrasts | network offsets; neither has an assumed positive sign (J is negative at both witnesses) |
| alpha,beta,sigma | endogenous investment-response bounds | threshold ordering and all-profile domination |
| max(0,beta,sigma)<F<2alpha | primitive F plus endogenous thresholds | strict investment selection; equality may yield mixing/multiplicity |
| c(b_L-e_U)>H+J | endogenous sufficient initial-ranking condition | initial SU advantage is no longer guaranteed; it is not a utility/cost primitive |
| d*r_U<J+c*e_L | endogenous sufficient post-ranking condition | strict IS preference is no longer guaranteed |

The two welfare inequalities do not literally assume their endpoint
conclusions, but they already require the quantitative incidence ordering
that a Level 3 theorem must derive. Relabelling them as primitive would
not close the gap.

## Minimal unresolved lemma set

1. **E (continuation):** primitive conditions imply global buyer-consistent
   market equilibrium for every relevant portfolio/path, with uniqueness
   or selection-independent consequences. Separate quantity/price proofs
   are legitimate; a nonsingular FOC is insufficient.
2. **I (adoption order):** the SAME primitive domain implies the outsider's
   aggregate two-market gain exceeds every reverse/SW incremental gain,
   after all market reactions. A positive individual gain is insufficient.
3. **W (incidence order):** preferences/cost/network restrictions imply
   both initial protection exceeding export loss and residual component
   below export loss, without assuming welfare or response-envelope signs.
4. **C (coupling/nonvacuity):** these restrictions share an economic cause
   and include exact R9 and a valid price game; merely intersecting
   unrelated successful inequalities is not an explanatory theorem.

R19 closes part of E (fully compatible affine price games, and all R16
rational portfolio pure-price continuations via the new kink certificate)
and part of W (post-adoption residual slope). I and the initial part of W
remain unresolved in a common primitive class, so C is not proved.

## Removal/counterexample checks

- R9 at `v=0,c=.1` has initial gap `-47/3200`; concavity and positive
  market access gains alone do not give initial regional superiority.
- The exact quadratic counterexample in `incidence_work/exact_output.json`
  has SPD demand and a strictly diagonally dominant Cournot Jacobian,
  but reducing one firm's cost increases another firm's output. Negative
  utility cross-partials alone are not full Marshallian gross substitutes.
- The residual-incidence theorem proves opposite slopes in R9 Cournot
  and substitute Bertrand. A common positive `r` restriction would
  wrongly exclude the required Bertrand example.
- At `v=gamma>0` in differentiated Bertrand, the formal residual minimum
  lies beyond outsider exit; rho>0 does not imply an observable U-shape.
- At `gamma=.9,v=.8`, full-compatible demand is SPD but the incompatible
  2+1 demand is not. Checking only post-adoption demand is insufficient.

No negative search is presented as a general mathematical impossibility
proof. The stop is a justified failure to meet the requested criterion,
not a theorem that Level 3 cannot ever be reached.
