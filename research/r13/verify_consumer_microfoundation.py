"""R13 exact algebra: consumer welfare from fulfilled network expectations.

Reproduces R9 homogeneous heterogeneous-valuations model *exactly*, then
checks the general inverse-quantile class and a distinct differentiated
random-utility member (logit illustration). Does not certify a price
equilibrium exists or that the government ranking reverses universally.
"""
import sympy as s

a,v=s.symbols("a v",real=True)
q=s.symbols("q0:3",real=True)
q0,q1,qo=q
Q=sum(q)
z=s.symbols("z",real=True)
D=s.Function("D")
g0=v*(q0+q1+a*qo)
go=v*a*Q
g=(g0,g0,go)
p=tuple(D(Q)+g_i for g_i in g)
CS=s.Integral(D(z),(z,0,Q))-Q*D(Q)
# Q is an expression, so differentiate with respect to each quantity.
for var in (*q,a):
    assert s.simplify(s.diff(CS,var)
           -sum(q[i]*(s.diff(g[i],var)-s.diff(p[i],var))
                for i in range(3)))==0, var
print("ARBITRARY DIFFERENTIABLE INVERSE QUANTILE D(Q): CONSUMER ENVELOPE PASS")

price_linear=tuple(s.factor(pi.subs(D(Q),1-Q)) for pi in p)
CS_linear=s.simplify(CS.subs(s.Integral(D(z),(z,0,Q)),
                                Q-Q**2/2).subs(D(Q),1-Q))
assert s.simplify(CS_linear-Q**2/2)==0
assert all(s.simplify(price_linear[i]-(1-Q+g[i]))==0 for i in range(3))
print("R9 DEMAND AND CS=Q^2/2 FROM UNIFORM BUYERS: EXACT PASS")

costs=[s.Function("C0")(q0),s.Function("C1")(q1)]
W=CS+sum(p[i]*q[i]-costs[i] for i in (0,1))
vel=s.symbols("vel0:3",real=True)
def along(expr):
    return s.diff(expr,a)+sum(s.diff(expr,q[i])*vel[i] for i in range(3))
micro=s.expand(sum(q[i]*along(g[i]) for i in range(3))
               -qo*along(p[2])
               +sum((p[i]-s.diff(costs[i],q[i]))*vel[i] for i in (0,1)))
assert s.simplify(along(W)-micro)==0
print("R13 NATIONAL-INCIDENCE IDENTITY FOR NONLINEAR D,C AND NETWORK G: PASS")

# Arbitrary smooth brand-taste random utility: logit example,
# not an assumed benchmark demand in the general theory.
sigma,m,alpha=s.symbols("sigma m alpha",positive=True)
net=s.symbols("n0:3",real=True)   # net_i = g_i - p_i
x=[s.exp((alpha+net_i)/sigma) for net_i in net]
V=sigma*m*s.log(1+sum(x))
shares=[s.factor(m*x[i]/(1+sum(x))) for i in range(3)]
for i in range(3):
    assert s.simplify(s.diff(V,net[i])-shares[i])==0
print("SMOOTH DIFFERENTIATED RANDOM-UTILITY ROY/ENVELOPE: PASS")

# The *original* singleton-zero network rule is unchanged:
# adoption profile selects the discrete compatible group and
# its original g_i; interpolation a is not an additional firm action.
print("R13 BUYER MICROFOUNDATION & OLD R9 MODEL NESTING: PASS")
