# R19 comparative statics: actual signs and sharp limits

## 1. Why inverse-Jacobian notation does not solve the research problem

On a regular interior branch `Phi(x,z)=0`, `x_z=-Phi_x^{-1}Phi_z` is
classical. P-matrix, positive-definite or strong-monotone conditions
can ensure local/global uniqueness without fixing every entry of this
inverse. For a three-player complete strategic-substitutes graph, a sign
signature cannot turn every positive off-diagonal Jacobian entry negative:
`s1*s2<0` and `s1*s3<0` imply `s2*s3>0`. Direct M-matrix arguments
therefore require a suitable reduced system or additional structure.

Exact consumer-primitive counterexample without networks:

`U=1'q-q'Mq/2`,
`M=[[3/2,1,1/10],[1,3/2,1],[1/10,1,3/2]]`.

Leading minors are `3/2,5/4,14/25>0`, so utility is strongly concave
and all inverse-demand cross-effects are strictly negative. Cournot's
negative FOC Jacobian `J=M+diag(Mii)` is SPD and strictly diagonally
dominant. At zero costs, `q=(20/73,11/73,20/73)>0`; exactly,

`dq/dc3=(-70/2117,10/73,-800/2117)`.

A reduction in firm 3's cost increases firm 1's output. This refutes an
inference from those restrictions alone to loss of every rival. It does
not refute a theorem assuming full gross substitutes in Marshallian
demand, which this example does not satisfy. See the exact standalone
verifier; no floating-point sign test is used.

## 2. Signed two-group Schur reduction

For a fixed affine network state let

`M=[[a,b,t],[b,a,t],[t,t,s]]`,
with derived own markup coefficients h for members and k for outsider.
Set `L=a+b+h`, `T=s+k`, `K=L*T-2*t^2`. On a valid interior branch,

`x=(T-t+t*z)/K`, `y=(L-2*t-L*z)/K`.

If `t,L,K,h,k>0`,

`x_z=t/K>0`, `y_z=-L/K<0`,
`(pi_member)_z=2*h*x*t/K>0`,
`(pi_outsider)_z=-2*k*L*y/K<0`.

Thus cost relief increases outsider sales/profit and displaces both
members in this SYMMETRIC reduced class. These signs follow from
coefficients, not assumed response-envelope constants. For Cournot
`h=a,k=s`. For Bertrand, derive `h=1/(M^-1)hh`,
`k=1/(M^-1)oo`, and independently verify global price Nash. The reduction
itself does not certify arbitrary market conduct.

## 3. Private-profit/national-incidence ratio lemma

Let baseline CS use gamma, so
`m(z)=P*x^2+2*gamma*x*y+y^2/2`, `P=1+gamma+2h`.
The national welfare loss per unit outsider gain when its cost falls is

`eta=m_z/(-pi_outsider,z)`
`=(P*t-gamma*L)/(k*L)*(x/y)+(2*gamma*t-L)/(2*k*L)`.

Exactly,

`eta_z=(P*t-gamma*L)*K/[k*L*(L-2t-Lz)^2]`.

**Proof.** Differentiate the affine x,y and the quadratic m and pi;
use `(x/y)_z=K/(L-2t-Lz)^2`, then cancel common factors. All identities
are verified symbolically in `incidence_work/verify_incidence.py`.

The sign of outsider profit growth is insufficient for the sign of m.
The coefficient `P*t-gamma*L` measures producer diversion relative to
consumer substitution. It is a demand/conduct expression, not a new
independent welfare function. This lemma is an affine specialization of
known pass-through/incidence techniques, not certified Level 4 novelty.

## 4. Fully compatible primitive theorem

The strongest new result is T-R in `R19_MAIN_THEOREM_AND_PROOFS.md`:
it derives the entire residual quadratic and its slope from gamma,v,
and separately derived conduct. For R9 its slope is positive; for the
whole stated substitute Bertrand family its slope at zero is negative.
No universal common sign or comparative static in all c,d,v follows.
Network improvement and cost relief are distinct paths; a cost-only
lemma is not the complete binary standard-support investment theorem.
