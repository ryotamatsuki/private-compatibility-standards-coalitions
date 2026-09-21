#!/usr/bin/env python3
"""R7 clean-room theory recertification.

Independent implementation: reconstructs market equilibria from primitives and does not
import code/canonical.py or any R2-R6 verification module.
"""
import sympy as sp

c, v, d, F, delta = sp.symbols("c v d F delta", real=True)

def simp(x):
    return sp.factor(sp.cancel(sp.simplify(x)))

def solve_cournot(groups, costs):
    q = sp.symbols("q0:3")
    Q = sum(q)
    network = []
    for i, grp in enumerate(groups):
        members = [j for j, h in enumerate(groups) if h == grp]
        network.append(v * sum(q[j] for j in members) if len(members) >= 2 else 0)
    price = [1 + network[i] - Q for i in range(3)]
    profit = [(price[i] - costs[i]) * q[i] for i in range(3)]
    foc = [sp.diff(profit[i], q[i]) for i in range(3)]
    sols = sp.solve(foc, q, dict=True)
    assert len(sols) == 1
    sol = sols[0]
    qs = [simp(sol[x]) for x in q]
    profits = [simp(profit[i].subs(sol)) for i in range(3)]
    cs = simp(sum(qs) ** 2 / 2)
    return qs, profits, cs

# --- Canonical primitives, rebuilt from first-order conditions ---
qI, piI, KI = solve_cournot([0, 0, 0], [0, 0, 0])
qM, piM, KM = solve_cournot([0, 0, 1], [0, 0, c])
qO, piO, KO = solve_cournot([0, 0, 1], [c, c, 0])
qW, piW, KW = solve_cournot([0, 1, 2], [0, c, c])
qR, piR, KR = solve_cournot([0, 0, 0], [0, 0, d])

P, A, B = piI[0], piM[0], piM[2]
C, D, H, S = piO[0], piO[2], piW[0], piW[1]

assert simp(qI[0] - 1 / (4 * (1 - v))) == 0
assert simp(qM[0] - (1 + c) / (2 * (2 - 3 * v))) == 0
assert simp(qM[2] - (1 - 3 * c - 3 * (1 - c) * v) / (2 * (2 - 3 * v))) == 0
assert simp(qO[0] - (1 - 2 * c) / (2 * (2 - 3 * v))) == 0
assert simp(qO[2] - (1 + 2 * c - 3 * v) / (2 * (2 - 3 * v))) == 0
assert simp(qW[0] - (1 + 2 * c) / 4) == 0
assert simp(qW[1] - (1 - 2 * c) / 4) == 0

WIS = simp(KI + 3 * P)
WMN = simp(KM + 2 * A + C)
E = simp((KM - KI) + 2 * (A - P))
Dgap = simp(P - C)
Phi = simp(WMN - WIS)
assert simp(Phi - (E - Dgap)) == 0

# --- R3: re-solve partial erosion from primitives ---
AR, BR = piR[0], piR[2]
WMO = simp(KR + 2 * AR + C)
R = simp(WMO - WIS + Dgap)
R_expected = d * ((5 - 4 * v) * d + 2 * (1 - 4 * v)) / (32 * (1 - v) ** 2)
assert simp(R - R_expected) == 0
assert simp(WMO - WIS - (-Dgap + R)) == 0

# Re-solve the relevant adoption deviations.
qUA, piUA, _ = solve_cournot([0, 0, 1], [0, d, c])
qAA, piAA, _ = solve_cournot([0, 0, 0], [0, d, d])
TO = simp(BR - B)
TUd = simp(piUA[1] - C)
TWd = simp(piUA[1] - S)
TAR = simp(piAA[1] - piUA[2])

r3w = {
    c: sp.Rational(1, 10),
    v: sp.Rational(6, 25),
    d: sp.Rational(1, 20),
    F: sp.Rational(9, 100),
}
assert Phi.subs(r3w) > 0
assert (WMO - WIS).subs(r3w) < 0
assert (2 * TO - F).subs(r3w) > 0
assert (F - TUd).subs(r3w) > 0
assert (F - TWd).subs(r3w) > 0
assert (F - TAR).subs(r3w) > 0

# --- R4: boundary and reciprocal-disadvantage identities ---
assert simp(Phi.subs(v, 0) - c * (13 * c - 6) / 32) == 0
positive_cofactor = 4 - 5 * v - 4 * c * (1 - v)
assert simp(
    Dgap
    - (4 * c * (1 - v) - v)
    * positive_cofactor
    / (16 * (1 - v) * (2 - 3 * v) ** 2)
) == 0

# --- R5: independently reconstruct the frozen differentiated demand ---
gamma = sp.Rational(1, 2)
I3 = sp.eye(3)
one = sp.ones(3, 1)
Bmat = (1 - gamma) * I3 + gamma * (one * one.T)

def compatibility_matrix(groups):
    out = sp.zeros(3)
    for i, grp in enumerate(groups):
        members = [j for j, h in enumerate(groups) if h == grp]
        if len(members) >= 2:
            for j in members:
                out[i, j] = 1
    return out

def r5_M(groups):
    return Bmat - v * compatibility_matrix(groups)

def r5_cournot(groups, costs):
    M = r5_M(groups)
    q = sp.symbols("x0:3")
    qv = sp.Matrix(q)
    price = one - M * qv
    profit = [(price[i] - costs[i]) * q[i] for i in range(3)]
    sol = sp.solve([sp.diff(profit[i], q[i]) for i in range(3)], q, dict=True)[0]
    qs = sp.Matrix([simp(sol[x]) for x in q])
    profits = [simp(profit[i].subs(sol)) for i in range(3)]
    cs = simp((qs.T * M * qs)[0] / 2)
    return qs, profits, cs

def r5_bertrand(groups, costs):
    M = r5_M(groups)
    Minv = M.inv()
    pvars = sp.symbols("p0:3")
    pv = sp.Matrix(pvars)
    qv = Minv * (one - pv)
    profit = [(pvars[i] - costs[i]) * qv[i] for i in range(3)]
    sol = sp.solve([sp.diff(profit[i], pvars[i]) for i in range(3)], pvars, dict=True)[0]
    qs = sp.Matrix([simp(qv[i].subs(sol)) for i in range(3)])
    profits = [simp(profit[i].subs(sol)) for i in range(3)]
    cs = simp((qs.T * M * qs)[0] / 2)
    return qs, profits, cs

def r5_blocks(solver):
    _, pii, ki = solver([0, 0, 0], [0, 0, 0])
    _, pim, km = solver([0, 0, 1], [0, 0, c])
    _, pio, ko = solver([0, 0, 1], [c, c, 0])
    _, piw, kw = solver([0, 1, 2], [0, c, c])
    return dict(
        P=pii[0], A=pim[0], B=pim[2], C=pio[0], D=pio[2],
        H=piw[0], S=piw[1], KI=ki, KM=km, KO=ko, KW=kw
    )

for mode, solver in [("C", r5_cournot), ("B", r5_bertrand)]:
    z = r5_blocks(solver)
    ph = simp(z["KM"] + 2 * z["A"] + z["C"] - (z["KI"] + 3 * z["P"]))
    e = simp((z["KM"] - z["KI"]) + 2 * (z["A"] - z["P"]))
    dg = simp(z["P"] - z["C"])
    ta = simp(z["P"] - z["B"])
    tu = simp(z["A"] - z["C"])
    tw = simp(z["A"] - z["S"])
    rw = {c: sp.Rational(1, 10), v: sp.Rational(6, 25)}
    assert ph.subs(rw) < 0, mode
    assert e.subs(rw) < 0, mode
    assert dg.subs(rw) > 0, mode
    assert ta.subs(rw) > 0, mode
    assert ta.subs(rw) < sp.Rational(1, 5) < 2 * ta.subs(rw), mode
    assert sp.Rational(1, 5) > tu.subs(rw), mode
    assert sp.Rational(1, 5) > tw.subs(rw), mode

# --- R6: independently reconstruct the deviation-relevant payoffs ---
def payoffs_no_bypass(m1, m2, m3, pair):
    ms = [m1, m2, m3]
    i, j = pair
    outsider = ({0, 1, 2} - {i, j}).pop()
    coalition_mass = ms[i] + ms[j]
    out = {}
    for k in (i, j):
        out[k] = simp(ms[k] * KM + coalition_mass * A + ms[outsider] * C)
    out[outsider] = simp(ms[outsider] * KO + coalition_mass * B + ms[outsider] * D)
    return out

r6w = {c: sp.Rational(1, 10), v: sp.Rational(6, 25)}
sym12 = payoffs_no_bypass(1, 1, 1, (0, 1))
sym13 = payoffs_no_bypass(1, 1, 1, (0, 2))
assert simp(sym13[0] - sym12[0]) == 0
assert (sym13[2] - sym12[2]).subs(r6w) > 0

m = [sp.Integer(1), sp.Integer(1), 1 - delta]
p12 = payoffs_no_bypass(*m, (0, 1))
p13 = payoffs_no_bypass(*m, (0, 2))
assert simp(p12[0] - p13[0] - delta * (A - C)) == 0
assert (A - C).subs(r6w) > 0

print("R7 CLEAN-ROOM THEORY RECERTIFICATION: PASS")
