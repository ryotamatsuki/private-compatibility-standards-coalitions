# R19 endogenous adoption: what is derived and what remains missing

## 1. Technology and the exact investment lemma

One newly supported standard covers both member destinations and only
those destinations. No worldwide network/capacity spillovers are allowed.
Consequently the outsider's gross incremental gain after members choose
no support is the SUM of two equilibrium operating-profit increments.
A member's reverse standard improves one outsider destination. That is
a primitive technology, not a claim that per-market gains are ordered.

Let every member/SW incremental support edge (every rival profile AND
every own partial portfolio) have gross gain below F, and let the
outsider's two-market gain against nonadopting members exceed F.
Then the unique investment Nash, allowing mixed investment actions,
is outsider-only in SU and no investment in SW.

**Proof.** Repeatedly remove one interface from a nonnative member/SW
portfolio. Each removal strictly raises profit against every rival
profile; telescope the finite removals to show native support strictly
dominates every nonempty portfolio, even against mixed rivals. Eliminate
these actions. The outsider then strictly prefers its single additional
standard. No other mixed or pure investment Nash remains. QED.

This improves R18's unnecessary all-profile LOWER outsider bound: only
its gain after dominated member actions are eliminated is needed. The
all-profile UPPER bounds cannot generally be removed. The lemma is
standard dominance logic, not Level 4 novelty and not a primitive
ordering theorem for arbitrary demand. Equilibrium profit gains remain
derived objects until computed from a named game.

## 2. Derived outsider residual-cost threshold

For the fully compatible family T-R, let `B=pi_outsider^B(c)` be its
pre-adoption profit from the separately re-solved incompatible member
market. Its exact two-market benefit is

`G_o(d)=2*(ell*y(d)^2-B)`.

It falls strictly throughout `0<=d<dbar`. Conditional on members not
supporting, its unique best response is adoption precisely when

`d<d_A=dbar*[1-kappa*sqrt((B+F/2)/ell)]`,

provided `0<d_A<dbar`; if the bracket is nonpositive, no positive-gain
adoption region exists. Equality gives indifference, not strict selection.
This cutoff is distinct from the all-profile unique-investment threshold:
member/SW deviations must still be verified.

**Proof.** Substitute `y=(1-d/dbar)/kappa>0` into `G_o(d)>F`, divide
by positive ell and take the positive square root. Monotonicity gives
the unique cutoff. Its exact equality is independently verified by SymPy.
B is not an assumed free constant: the verifier derives it from
`M_B=M0-v*[[1,1,0],[1,1,0],[0,0,0]]`, costs `(0,0,c)` and the
actual Bertrand/Cournot equations. The full fixed-cost interval ordering
for an unrestricted primitive class nevertheless remains open.

At the R16 primitives, `d_A≈0.01058951937`, above actual `d=.002` but
below c=.016 and the residual quadratic minimum. Thus the unconstrained
quadratic's later rise cannot be advertised as a selected equilibrium
prediction at that example. Outsider-only adoption at actual d and d=0
is certified by complete investment and global pure-price checks.

## 3. Exact nonvacuity and failure

| Exact primitive instance | Outsider benefit vs competing gains | Government pre / post SU-minus-IS |
|---|---|---|
| R9 Cournot `(v,c,d,F)=(6/25,1/10,1/20,9/100)` | outsider `0.11800704153`, max member `0.06502431769`, max SW `0.06816794948`; F=.09 strict | `2408509/295731200>0`, `-1341/184832<0` |
| R16 Bertrand `(gamma,v,c,d,F)=(23/25,33/500,2/125,1/500,1/40)` | outsider `0.02981641506`, max member/SW `0.01515717180`; F=.025 strict | `+0.00277400733148`, `-0.000907433889334` |
| Zero-network Cournot `(0,1/10,1/20,1/50)` | `21/1280<F<93/3200`; all profiles strict | `-47/3200`, `-243/12800`; no initial SU advantage |

These are exact underlying rational comparisons, decimals only for
reading. The two positive examples have different primitives. The last
counterexample proves that access aggregation and unique private adoption
do not alone predict government reversal; strictness also permits small
positive-network perturbations, so the issue is not just a degenerate v=0
point. Complete data and commands are under replay_work.

## 4. Market count comparison, correctly limited

If adding a destination literally clones an independent market with
unchanged participants, costs and per-market gain, aggregated gain is
linear in its number, a known scope effect. Increasing coalition membership
in an n-country economic model also changes suppliers, network sizes,
owned profits and competition; that is a different experiment. R19 does
not add an unapproved n-country model to manufacture a monotonicity
result. No general size monotonicity or size reversal is certified here.
