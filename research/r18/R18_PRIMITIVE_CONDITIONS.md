# R18 — Primitive reduction and level audit (not simply G1 + G3)

## Candidate comparison (maximum three)
A. **Scope:** One outsider investment covers TWO member markets, versus members' reverse investment covering ONE outsider market. Under uniform positive per-market outsider operating-gain lower bound alpha and all-profile upper gain beta/sigma, 2alpha>max(beta,sigma) creates a nonempty F interval. This is not a fresh theorem of fixed-cost economies of scope; derivative-based payoff envelopes and all-profile checks are required. Outcome: useful bridge, substantial prior-art absorption.

B. **Rent/consumer incidence:** With buyers maximizing and fulfilled expectations, b=m_B' and r=m_C' can be expressed in quantities, markups, network gains and price pass-through; cost pressure e=-f_B' in outsider market measures persistent disadvantage. No universal signs; standard pass-through literature already studies most pieces. Outcome: diagnostic sufficient bounds, not a universal demand-curvature theorem.

C. **Asymmetric policy feedback (preferred):** The same outsider buys the member standard but DOES NOT remove members' foreign-market handicap. The initial SU advantage and post-adoption IS advantage are simultaneously certified by two independently measured cost/competition/network channels:
L0=c(bL-eU)-H-J>0, U1=d*rU-J-c*eL<0.
The key asymmetry is structural: only m_B(c) changes into m_C(d), while f_B(c) is literally unchanged. Do not assume D0>0 or D1<0; derive their bounds. The network contrasts H,J can be negative; neither is a free positive parameter. This is narrower than an arbitrary end-point welfare identity and portable across distinct product-market conducts **conditional on the response bounds**.

## Exact independent checks, dated 2026-10-20
R9 Cournot (v,c,d,F)=(6/25,1/10,1/20,9/100):
- bL=1501/4096, eL=95/256, eU=475/1024, rU=605/23104.
- H=67611/2957312, J=-2625/77824.
- L0=1041/924160 = +0.001126428324; U1=-3061/1478656 = -0.002070123139.
- True D0=2408509/295731200 = +0.008144250590; D1=-1341/184832 = -0.007255237188.
- Two-market outsider gross gain 0.11800704153; max SU member gain 0.06502431769, max SW one-addition gain 0.06816794948; F=0.09 lies strictly inside.

R16 Bertrand (gamma,v,c,d,F)=(23/25,33/500,2/125,1/500,1/40):
- bL≈0.5950838531; eL≈0.2681018570, eU≈0.3069192000; rU≈-0.1000955168.
- H≈+0.00719182662; J≈-0.00389819337.
- L0≈+0.001317001203; U1≈-0.0005916273735.
- True D0≈+0.00277400733148; D1≈-0.000907433889334.
- Two-market outsider gross gain≈0.02981641506; max SU member and SW increment≈0.01515717180; F=0.025 lies strictly inside.

These exact inequalities are checked by **SymPy rational** market equations and full investment-stage enumeration, not by rounded thresholds. Each m_B,m_C,f_B is quadratic in the scalar cost wedge z in the benchmark models, so b,e,r are affine: global extrema on the claimed closed intervals occur at endpoints. This observation is checked by symbolic third derivative =0. R16's global corner Nash and no-entry cases rely on prior R16 certified scripts; R18 does not independently rerun them.

## What is and is NOT primitive
The actual utility U or type distribution, technological compatibility groups, unit marginal costs (0,c,d), fixed F, and destination-count technology are primitives. In contrast **bL,rU,eL,eU,alpha,beta,sigma** are *endogenous response envelopes*. They can be derived exactly in the specified Cournot and Bertrand microfoundations, but the R18 main proposition assumes their sign/size for arbitrary E(r,s;theta). Establishing their bounds for a wide class directly from cross-partials, curvature, substitutability, diagonal dominance, network-feedback strength and equilibrium strategic response remains OPEN. It would be false to label these inequalities universally implied by consumer concavity. The new theorem is a genuine testable cross-market SU/IS *sufficient condition* and improves on G1+G3's single adoption-path accounting, but at referee-level **Level 2, not Level 3**.

## Falsifiers and sensitivity
v=0,c=0.1 Cournot gives D0=-47/3200. If the full network-compatible foreign expansion makes local CS dominate producer diversion, bL may be nonpositive and protection will not outweigh the foreign handicap. If d is too high and rU positive, the post bound may no longer force IS; if per-market gain alpha shrinks under rival retaliation, the access interval disappears. No "all Cournot and all Bertrand" conclusion.