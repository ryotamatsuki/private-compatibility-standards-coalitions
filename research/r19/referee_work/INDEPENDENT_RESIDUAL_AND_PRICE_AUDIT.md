# Independent adversarial audit: residual theorem and global price continuation

Date: 2026-10-20. This is an independent agent's derivation, not an external journal review. No inherited file was edited.

## 1. Algebra independently reproduced

Let `gamma in [0,1]`, `0<=v<=gamma`, `b=gamma-v>=0`, `ell>0`, `tau=1-gamma+ell>0`, and `kappa=tau+3b>0`. In a fully compatible affine market the two zero-cost member quantities and cost-d outsider quantity are

`x=(tau+b*d)/(tau*kappa)`,
`y=(tau-(tau+2*b)*d)/(tau*kappa)`.

The positive-output interval is `0<=d<dbar=tau/(tau+2*b)`. With consumer-optimized FE surplus, the member's two-destination national component is

`mC(d)=(1+gamma+2*ell)*x^2+2*gamma*x*y+y^2/2`.

Direct expansion gives

`mC(d)-mC(0)=[-rho*d+A*d^2/(2*tau^2)]/kappa^2`,

where

`rho=1+2*gamma-4*ell*b/tau`,
`A=tau^2+4*(1-gamma)*tau*b+[6*(1-gamma)+4*ell]*b^2>0`.

Thus the strict convexity and the turning point are actual theorems, not numerical graphs. For `rho>0`, the minimum is at `d_min=rho*tau^2/A`; the minimum lies in the positive-output interval only if `d_min<dbar`, an extra condition that must be checked. `rho>0` alone does NOT prove an interior U-shape over every admissible interval.

For homogeneous R9 Cournot, `gamma=1, ell=1-v` gives `rho=4v-1<0` on the inherited `v<1/4` domain: the residual component increases throughout `d>=0`.

For differentiated Bertrand,

`ell=(1-gamma)*(1+2*gamma-3*v)/(1+gamma-2*v)`.

For `0<=v<=gamma<1`,

`rho=(2*gamma^2-10*gamma*v-3*gamma+12*v^2+v-2)/(-3*gamma+5*v-2)>0`.

Proof: the denominator is at most `2*gamma-2<0`; its numerator is strictly convex in v, and at v=0 equals `(gamma-2)*(2*gamma+1)<0`, while at v=gamma equals `2*(gamma-1)*(2*gamma+1)<0`. A convex function is no greater than its endpoint chord, hence the numerator is negative throughout. This gives the sign. The endpoint argument is a genuine analytic inequality, not sample checking.

Outsider operating profit is `ell*y(d)^2`, and its derivative is strictly negative on `0<=d<dbar`. Holding the pre-adoption market unchanged, the privately funded outsider's adaptation gain falls with d. At the same time, when `rho>0` and `d<d_min`, the member component falls with d. The member's IS-minus-SU advantage therefore grows while private adaptation becomes less attractive, conditional on continued outsider-only adoption. It is essential to state the last qualification: when d exits the firm investment region, the selected continuation can change.

## 2. Global price Nash for the fully compatible residual market

This subsection establishes the global price continuation for the fully compatible affine Bertrand family only; it does not cover every pre-adoption compatibility matrix.

Set `a0=1-gamma>0`, so `M=a0*I+b*J` with `b>=0`. For any nonnegative price vector, FE demand is the unique LCP allocation because M is positive definite. In each active set S,

`q_j=[1-p_j-b*Q]/a0`,
`Q=sum_{j in S}(1-p_j)/(a0+|S|*b)`.

Fix rivals' prices and vary the active firm's own price. While it has positive demand, raising its price decreases total Q and increases every rival's candidate demand. Consequently rival products only enter as the own price increases; they do not leave. Its own demand slope in an n-product active set is

`-Aii(n)=-(a0+(n-1)*b)/(a0*(a0+n*b))`.

The magnitude increases weakly with n. Thus each entry of a rival creates a downward jump in the own-price derivative of profit on `p_i>=c_i`. Inside every active-set interval that profit is a strictly concave quadratic. A positive interior stationary point is therefore a global best response among all positive-sales prices. Prices below c cannot improve on a positive profit, and no-sale prices earn zero. This certifies the displayed positive FOC profile against all unilateral price deviations, including rival exits.

Uniqueness also requires ruling out inactive-product Nash equilibria. Any inactive zero-cost member can enter profitably: if another product is sold at a positive margin, `1-b*Q>0`; if no product sells, reservation value is one. So both zero-cost members must be active. Suppose instead only the outsider is inactive, including at its choke-price kink. At any putative Nash, increasing a positive-demand member's price gives a right derivative at most as steep in magnitude as the full active demand derivative. A necessary inequality is

`p_i-c_i >= ell*q_i`.

Indeed its right derivative cannot be positive, and the demand slope of any active set has magnitude at most full `(M^-1)ii=1/ell`. With p_i=`1-a0*q_i-b*Q`, summing both member inequalities yields

`Q<=2/(a0+ell+2*b)`.

The outsider's reservation price is therefore at least

`1-b*Q >= (a0+ell)/(a0+ell+2*b)=dbar`.

For `d<dbar`, the outsider can enter strictly above its cost. This excludes every inactive-outsider equilibrium including at-choke kinks. All equilibria must be interior, and the linear full-active FOC has a unique solution. Hence the displayed fully compatible price equilibrium is globally Nash and unique for every `0<=d<dbar`.

The necessary markup inequality is deliberately weak: using the restricted-active-set FOC at an inactive-product kink would be invalid. This argument does not make that substitution.

## 3. Decisive limits for R19's Level classification

1. `rho>0` for fully compatible Bertrand does NOT imply positive definiteness of the incompatible 2+1 network configuration. For example `gamma=9/10,v=4/5` makes full-compatible M positive definite but the two-member/one-outsider block determinant negative. Full-game existence must be separately certified.
2. The residual theorem supplies no primitive sufficient condition for the initial member SU advantage.
3. It does not rank all-profile SU member and SW adaptation gains against the outsider two-market gain. All-profile strict fee intervals remain necessary to endogenize continuation.
4. It does not supply a general primitive relation between outsider gain from the simultaneous cost-and-network switch and the government's initial protection surplus. A derivative with respect to post-adoption residual d holds the network matrix fixed; it is not the binary B-to-C investment comparison.
5. The same two-market national component can be represented by two local firms' profit only under the inherited symmetric-destination ownership accounting. It is not regional aggregate welfare.
6. The case d=0 has unchanged member-market allocation relative to IS, so the export-disadvantage comparison is particularly transparent. Positive d preserves a separate market wedge; its residual theorem can have opposite slopes under the two conducts.

Verdict: **new primitive subtheorem PASS; requested full primitive Main Theorem NOT ESTABLISHED; highest joint mechanism grade remains Level 2**. Level 4 is not attained under the user's cumulative definition. The residual counterdirection is a potentially interesting application, but general tax/foreign-cost pass-through theory may absorb its economic core; priority remains open.
