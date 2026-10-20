"""R11 exact symbolic incidence identity for arbitrary integrable demand.

This is a welfare-accounting identity, not new economics or a journal-theorem
certificate. No Cournot/Bertrand FOCs or demand functional form assumed.
"""
import sympy as sp

def check(k):
    q = sp.symbols("q0:" + str(k+1), real=True)
    a = sp.symbols("a", real=True)
    velocity = sp.symbols("v0:" + str(k+1), real=True)
    U = sp.Function("U")(*q,a)
    cost = [sp.Function("C" + str(i))(q[i]) for i in range(k)]
    prices = [sp.diff(U,qi) for qi in q]
    cs = U - sum(prices[i]*q[i] for i in range(k+1))
    W = cs + sum(prices[i]*q[i]-cost[i] for i in range(k))
    total = lambda h: sp.diff(h,a) + sum(sp.diff(h,qi)*velocity[i] for i,qi in enumerate(q))
    lhs = total(W)
    rhs = sp.diff(U,a) - q[k]*total(prices[k]) + sum(
        (prices[i]-sp.diff(cost[i],q[i]))*velocity[i] for i in range(k))
    assert sp.simplify(lhs-rhs)==0
    print("k",k,": general differentiable-utility identity PASS")

for k in (2,3,4):
    check(k)
print("R11 EXACT SYMBOLIC IDENTITY: PASS (not a novelty or general-sign certificate)")
