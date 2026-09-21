# R4 Precheck — Zero Network Effect in the Submitted Cournot Model

## Status

**PRECHECK PROVED — R4 NOT YET CLOSED**

This is the R1-authorized baseline check requested before full R4.

## Claim

In the submitted symmetric Cournot model, extend the canonical welfare expressions continuously to the boundary \(v=0\). Then

\[
\left.
\left(W_M^{SU,N}-W^{IS}\right)
\right|_{v=0}
=
\frac{c(13c-6)}{32}.
\]

The \(v=0\) analogue of the interior feasibility restriction is

\[
0<c<\frac13.
\]

For every such \(c\),

\[
13c-6
<
\frac{13}{3}-6
=
-\frac53<0,
\]

and therefore

\[
\boxed{
\left.
\left(W_M^{SU,N}-W^{IS}\right)
\right|_{v=0}<0.
}
\]

## Interpretation

This proves only:

> In the current symmetric Cournot microfoundation, on the corresponding interior \(c\)-range, eliminating the network effect removes the pre-adoption regional-union advantage required by the headline SU→IS preference-reversal path.

It does **not** prove that network effects are necessary for every possible selective-erosion model.

At the same time, the revision should no longer use a broad "network effects are unnecessary" statement as if a non-network microfoundation had already been constructed. The correct distinction is:

- the abstract accounting decomposition can be written without \(v\);
- the submitted symmetric Cournot model's initial-SU-preference region does depend on positive network effects.

## Next R4 tasks

Full R4 must still:

1. characterize \(\mathcal V_{SU}(c)=\{v:\text{feasible and }W_M^{SU,N}>W^{IS}\}\);
2. test whether it is a single interval, empty, multi-interval, or non-monotone before introducing any \(v_{\min}(c)\);
3. audit the assumption that singleton firms receive zero network benefit;
4. separate any alternative network specification from verification of the old model.

Reproducible symbolic check: \`code/revision/check_network_zero.py\`.
