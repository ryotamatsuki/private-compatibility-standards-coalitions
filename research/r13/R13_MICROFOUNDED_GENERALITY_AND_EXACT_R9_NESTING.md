# R13 — Fulfilled-expectations consumer microfoundation for R9 ⊂ R12

**As of 2026-10-20. Research revision base only, not a journal-submission package.** Direct predecessor: R12 [draft PR #37], itself based on unchanged R9/JICT [draft PR #34] commit \`08d6e6adb1a90bdf03fa223c0961ac04620f0fa2\`. All previously established R9 equations, propositions, theorem, Appendix proof certificates, numerical witness and negative scope tests remain byte-for-byte unchanged.

## Main correction to R12: consumer-welfare and price schedules cannot be arbitrary independent functions

R12 first wrote inverse demand \(p(q,a)\) and consumer surplus \(S(q,a)\) as separate smooth objects, and verified a chain-rule identity. That identity is mathematically true even when the pair has **no consistent optimizing-consumer representation**. Such an unconstrained pair is not sufficient as a micro-founded IO theory.

R13 imposes a *consumer-choice and fulfilled-expectations envelope* restriction **without** imposing linear inverse demand, differentiated Bertrand or Cournot, and without imposing \(p_i=\partial U(q)/\partial q_i\). In particular, the R9 model has **network externality effects taken as given by an atomistic purchaser but affected by the actions of oligopolistic suppliers**. It would be incorrect to require each firm's observed inverse price to be the marginal derivative of a single static representative-consumer quantity potential. R13 preserves that distinction.

## Consumer primitives — general non-atomic buyer choices

Each destination has a continuum of total mass \(M\) of atomistic consumers, quasilinear transferable numeraire utility, one-unit demand, an outside option of utility zero, and heterogeneous type \(t\). Conditional on fulfilled expected network access \(g_i^e\), a consumer chooses \(i\) to maximize
\[
u_i(t;p,g^e)=\theta(t)+\epsilon_i(t)+g_i^e-p_i,
\qquad u_0=0.
\]
The network state is a technological compatibility mapping \(G_i(q,s)\) of quantities and **discrete** adoption/standards state \(s\), including exactly the R9 singleton-zero convention: \(G_i=0\) for the isolated/unsupported compatible group. Atomistic consumers individually **take** \(g_i^e\) as fixed in their own decision; at market clearing their shared expectations are **fulfilled**, \(g_i^e=G_i(q,s)\).

There is an economically essential timing/commitment qualification: **the original R9 Cournot first-order conditions use \(\partial G_i/\partial q_i\)**. To reproduce them while maintaining buyer atomism, firms must anticipate that their quantity commitment changes *fulfilled buyer expectations*, e.g. firms commit simultaneous quantities, then those quantities become observable and buyers form correct network expectations before consuming. Treating *firms too* as taking \(g^e\) as fixed when deviating (the other possible fulfilled-expectations Cournot concept) would yield **different** FOCs. Thus R13 is not asserting equivalence of all timing interpretations of the 1985 Katz–Shapiro model; it names the precise original reduced-form timing needed for exact nesting.

For no ties almost everywhere, define the consumer surplus
\[
V(p,g)=\int\max\{0,\max_i[\theta(t)+\epsilon_i(t)+g_i-p_i]\}d\mu(t).
\]
Consumer maximization (Roy/envelope) gives \(V_{g_i}=q_i\), \(V_{p_i}=-q_i\) at differentiable points, and hence **along a regular fulfilled-expectations equilibrium path**
\[
\boxed{\frac{d CS}{da}=\sum_i q_i(a)\left(\frac{dG_i}{da}
 -\frac{dp_i}{da}\right).}
\tag{R13.1}
\]
This is a directional *total* derivative including the endogenous quantity dependence of \(G_i\), not a claim that buyer-specific network expectations stay fixed across equilibria. A continuum of tied consumers requires a compatible equilibrium allocation and a pathwise proof instead of naively applying pointwise derivatives of a nonsmooth maximum. The R9 homogeneous case has exactly such ties and is proved directly below.

## Exact nesting of original R9 (not merely in a limit)

Choose \(\epsilon_i=0\), valuation \(\theta\sim U[0,1]\), \(M=1\), and original group-network mapping \(G_i\). Interior firms' supplied quantities \(q_i>0\) are cleared with equal quality-adjusted prices \(z=p_i-G_i=1-Q\). Each buyer buys if \(\theta\ge z\); allocation among active firms is indeterminate from buyer preferences but clearing of quantities supplied by firms selects that allocation. The same buyers' quasilinear welfare implies
\[
p_i=1-Q+G_i(q,s),\qquad
CS=\int_{1-Q}^{1}(\theta-(1-Q))d\theta=Q^2/2.
\tag{R13.2}
\]
This is **exactly** R9's demand and consumer-surplus formula, including the group-specific network benefit and singleton-zero treatment, rather than a substituted new market model. R13 does not change or recalibrate any Cournot FOC, \(c,d,F,v\), market size, quantity, or coalition payoff.

For an arbitrary differentiable, decreasing inverse survival quantile \(D(Q)=F_\theta^{-1}(1-Q/M)\) (on an interior interval with supported buyer mass), identical reasoning gives
\[
p_i=D(Q)+G_i(q,s),\qquad
CS(Q)=\int_0^Q D(z)\,dz-QD(Q).
\tag{R13.3}
\]
The standard \(D(Q)=1-Q\) case nests R9. Conditional regularity and interiority are required; convex/concave \(D\) alone does not assure market existence. Every supported seller faces the common **net** price \(D(Q)\), so the homogeneous choice case is a natural Cournot **quantity-clearing** representation; it does **not** automatically admit smooth, interior pure-strategy *Bertrand* pricing equilibria.

For differentiated brand tastes \(\epsilon_i(t)\), the same general optimization and envelope formula hold without consumers being indifferent, given unique selections almost surely. For example an additive i.i.d. extreme-value shock produces the logsum surplus and smooth probabilistic product shares when the shock scale is positive; this is an **illustrative consumer foundation**, not a new R13 Bertrand result or a changed R9 assumption. Price equilibrium conditions and existence must be proved in any such application.

## National welfare, common mechanism and exact conduct-neutral identity

A representative member government's welfare is consumer surplus in its local market plus **its single home firm's worldwide operating profit**, not regional aggregate profits. Because the two member destinations and domestic firms are symmetric, the latter's profits in those two destinations equal the sum of two *different* member firms' profits in the representative member destination, which is the useful equality in R12. The home firm's outsider-destination profits are invariant to outsider-only adoption. Only the outsider pays extra foreign-standard investment \(F\); no new home firm fixed cost enters the selected SU continuation.

Let \(\mu_h=p_h-C'_h(q_h)\). Combining (R13.1) with producer-profit accounting yields
\[
\boxed{
W_M'(a)
=\underbrace{\sum_i q_i G_i'}_{\text{consumer network gain}}
-\underbrace{q_O p_O'}_{\text{foreign-price/terms-of-trade incidence}}
+\underbrace{\sum_{h\in H}\mu_h q_h'}_{\text{domestic markup-rent displacement}} .
}\tag{R13.4}
\]
There is no Cournot or Bertrand FOC in the proof. Network \(G_i'\), outsider price \(p_O'\), home markup \(\mu_h\) and home quantity change \(q_h'\) can come from any *regular, specified* product-market game, and all terms are **market responses**, not arbitrary ex-post national welfare functions. The identity is not a sign theorem or independent original economic novelty; relative to Gandal–Shy, it is the **connection** to asymmetric privately chosen compatibility across policy partitions that matters.

For original R9, set \(D(Q)=1-Q\), \(CS=Q^2/2\), \(p_i=1-Q+G_i\), and the original compatible groups. Then (R13.1) follows directly because
\[
\sum_i q_i(G_i'-p_i')=-Q[D'(Q)Q']=QQ'
=(Q^2/2)'.
\]
This was verified symbolically for arbitrary differentiable \(D\) and for the original uniform R9 specification, for **every** equilibrium-path differential in \(q_1,q_2,q_O,a\), not only a numerical example. This also certifies the equivalence of the old R12 incidence coefficients \(A,H_j\) with the microfounded R13 envelope decomposition on the restricted admissible class.

## Existing R12 mechanism conditions unaffected

- **G1 firm selection:** \(\max\{0,\bar g_H,\bar g_{SW}\}<F<g_O^0\) remains a strictly sufficient firm-investment condition. Its exact certified R9 numeric example and complete adoption deviation table are unmodified.
- **G2 market-incidence sufficiency:** the positive-pointwise loss bound is valid but **not necessary**. Keep its original limitations.
- **G3 non-monotone integrated criterion:** \(I(a)\) nondecreasing and a finite right-Riemann upper bound smaller than \(-G_0\), with \(I(a)=\sum q_i G_i'-q_Op_O'+\sum\mu_hq_h'\) on the microfounded class. Its exact R9 witness passing the independent 16-cell upper-bound audit is preserved.
- **R9 originals:** Cournot propositions, \(R(d,v)\), exact network thresholds, partial residual costs, original joint witness, Appendix E negatives (including \(\gamma=1/2\) differentiated Bertrand/Cournot), and coalition-stability theorem all unchanged.
- **Existence:** Neither G1–G3 nor buyer-envelope restrictions guarantees existence/uniqueness of a pure Bertrand equilibrium in the homogeneous limit. Claim only conditional applicability **to regular equilibria**.
- **Network welfare:** social net network effects are accounted for in \(V\) via \(g\), even though the *specialized* R9 CS simplifies to \(Q^2/2\); the network benefit is already capitalized into the quality-adjusted prices.

## Scholarly baseline / closest overlap

- Katz & Shapiro (1985), *Network Externalities, Competition, and Compatibility*, **AER 75(3):424–440**. Classical framework of buyer valuations involving expected network size, endogenous compatibility, fulfilled expectations; **not** new for this manuscript. See [original citation](https://ideas.repec.org/a/aea/aecrev/v75y1985i3p424-40.html) and [author-deposited scan](https://www.researchgate.net/publication/4723878_Network_Externalities_Competition_and_Compatibility). Their firm reaction timing may differ; see above.
- Gandal & Shy (2001), *Standardization Policy and International Trade*, **JIE 53**, DOI 10.1016/S0022-1996(00)00067-2. Closest older government standardization-choice setting.
- Weyl & Fabinger (2013), *Pass-Through as an Economic Tool*, **JPE 121:528–583**, DOI 10.1086/670401. General surplus-incidence accounting; do not claim (R13.4) is a fresh general pass-through theorem.
- Buccella, Fanti & Gori (2026), *The Compatibility Decision Game*, **Economics of Innovation and New Technology 35(2)**, DOI 10.1080/10438599.2025.2478583. Closest endogenous compatibility and competition-mode overlap, full paper proposition-by-proposition comparison pending.

## Referee and workflow gate

**Mathematical status after standalone symbolic CI:**
- Arbitrary nonlinear \(D\), original R9 uniform specialization, and regular differentiated logsum buyer envelope: **verify with new R13 CI**.
- Existing R12 strict adoption-gain and integrated reversal certificates: unchanged, already PASS in R12 CI.
- Original R9 scientific source should be byte-for-byte identical to PR #34 base and included old Section 4 bytes a preserved prefix.

**Editorial status:** This is a meaningful economic microfoundation that fixes a **real** weakness in R12's arbitrary independent \(p,S\) formulation and may strengthen the response to IJIO's generality objection. It does **not** turn the conditional reversal into a universal result; it does not make novelty automatic, nor does it remove the JICT 19-page short-format packaging blocker.

**Next eventual gate:** Independent hostile scrutiny of the network-fulfillment timing and observationally meaningful restrictions on market-response terms; verify one genuinely price-setting regular equilibrium if asserting Bertrand portability. Do not make new generalization mandatory for the already certified R9 conclusion. Do not silently merge any PR.
