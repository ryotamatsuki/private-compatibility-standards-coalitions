import sympy as sp
from math import comb

c, v = sp.symbols("c v", real=True)
gamma = sp.Rational(1, 2)
B0 = (1-gamma)*sp.eye(3) + gamma*sp.ones(3)

def eq(a, b=0):
    return sp.simplify(a-b) == 0

def cmat(groups):
    C = sp.zeros(3)
    for g in groups:
        if len(g) >= 2:
            for i in g:
                for j in g:
                    C[i,j] = 1
    return C

def cournot(groups, costs):
    M = B0 - v*cmat(groups)
    qs = sp.symbols("q0:3")
    q = sp.Matrix(qs)
    foc = [
        1-costs[i]-2*M[i,i]*q[i]
        -sum(M[i,j]*q[j] for j in range(3) if j != i)
        for i in range(3)
    ]
    sol = sp.solve(foc, qs, dict=True)[0]
    q = sp.Matrix([sp.factor(sol[z]) for z in qs])
    p = sp.simplify(sp.ones(3,1)-M*q)
    pi = sp.Matrix([sp.factor((p[i]-costs[i])*q[i]) for i in range(3)])
    cs = sp.factor(sp.Rational(1,2)*(q.T*M*q)[0])
    return M, q, p, pi, cs

def bertrand(groups, costs):
    M = B0 - v*cmat(groups)
    A = sp.simplify(M.inv())
    ps = sp.symbols("p0:3")
    p = sp.Matrix(ps)
    q = A*(sp.ones(3,1)-p)
    foc = [sp.expand(q[i]-A[i,i]*(p[i]-costs[i])) for i in range(3)]
    sol = sp.solve(foc, ps, dict=True)[0]
    p = sp.Matrix([sp.factor(sol[z]) for z in ps])
    q = sp.simplify(A*(sp.ones(3,1)-p))
    pi = sp.Matrix([sp.factor((p[i]-costs[i])*q[i]) for i in range(3)])
    cs = sp.factor(sp.Rational(1,2)*(q.T*M*q)[0])
    return M, A, q, p, pi, cs

configs = {
    "I": ([[0,1,2]],[0,0,0]),
    "M": ([[0,1],[2]],[0,0,c]),
    "O": ([[0,1],[2]],[c,c,0]),
    "W": ([[0],[1],[2]],[0,c,c]),
}

def blocks(fn, mode):
    out = {}
    for name, (groups, costs) in configs.items():
        r = fn(groups, costs)
        if mode == "C":
            M, q, p, pi, cs = r
        else:
            M, Ainv, q, p, pi, cs = r
        out[name] = (q, pi, cs)

    P = sp.factor(out["I"][1][0]); KI = sp.factor(out["I"][2])
    A = sp.factor(out["M"][1][0]); Bout = sp.factor(out["M"][1][2]); KM = sp.factor(out["M"][2])
    C = sp.factor(out["O"][1][0]); D = sp.factor(out["O"][1][2]); KO = sp.factor(out["O"][2])
    H = sp.factor(out["W"][1][0]); S = sp.factor(out["W"][1][1]); KW = sp.factor(out["W"][2])

    Phi = sp.factor(KM + 2*A + C - (KI + 3*P))
    Dis = sp.factor(P-C)
    E = sp.factor(Phi+Dis)
    TA = sp.factor(P-Bout)
    TU = sp.factor(A-C)
    TW = sp.factor(A-S)

    return dict(
        P=P, KI=KI, A=A, B=Bout, KM=KM, C=C, D=D, KO=KO,
        H=H, S=S, KW=KW, Phi=Phi, Dis=Dis, E=E,
        TA=TA, TU=TU, TW=TW, out=out
    )

BC = blocks(cournot, "C")
BB = blocks(bertrand, "B")

# Demand regularity on 0 <= v < 1/4.
MI = B0-v*cmat([[0,1,2]])
MP = B0-v*cmat([[0,1],[2]])
assert eq(MI[0,0], 1-v)
assert eq(MI[:2,:2].det(), sp.Rational(3,4)-v)
assert eq(MI.det(), sp.Rational(1,4)*(2-3*v))
assert eq(MP[0,0], 1-v)
assert eq(MP[:2,:2].det(), sp.Rational(3,4)-v)
assert eq(MP.det(), (1-2*v)/2)

# R5-C quantities; all are strictly positive on 0<c<1/3, 0<=v<1/4.
qI = BC["out"]["I"][0]; qM = BC["out"]["M"][0]
qO = BC["out"]["O"][0]; qW = BC["out"]["W"][0]
assert eq(qI[0], 1/(3-4*v))
assert eq(qM[0], (c+3)/(3*(3-4*v)))
assert eq(qM[2], (3-6*v-c*(5-6*v))/(3*(3-4*v)))
assert eq(qO[0], (3-4*c)/(3*(3-4*v)))
assert eq(qO[2], (3+2*c-6*v)/(3*(3-4*v)))
assert eq(qW[0], (2*c+3)/9)
assert eq(qW[1], (3-4*c)/9)
assert eq((3-6*v-c*(5-6*v)).subs(c,sp.Rational(1,3)), sp.Rational(4,3)-4*v)
assert sp.Rational(4,3)-4*sp.Rational(1,4) > 0

# R5-B quantities in positive-denominator form.
Hpoly = 8*v**2-16*v+7
L = (1-2*v)*Hpoly
r = 3-4*v
qI = BB["out"]["I"][0]; qM = BB["out"]["M"][0]
qO = BB["out"]["O"][0]; qW = BB["out"]["W"][0]
LM = 7-12*v+c*(3-4*v)
LB = 16*v**2-24*v+7-c*(16*v**2-32*v+13)
LC = 7-12*v+c*(16*v-10)
LD = 16*v**2-24*v+7+c*(6-8*v)
assert eq(qI[0], r/(4*(1-v)*(2-3*v)))
assert eq(qM[0], r*LM/(8*L))
assert eq(qM[2], r*LB/(8*L))
assert eq(qO[0], r*LC/(8*L))
assert eq(qO[2], r*LD/(8*L))
assert eq(qW[0], 3*(6*c+7)/56)
assert eq(qW[1], 3*(7-10*c)/56)
assert 7-12*sp.Rational(1,4) > 0
assert eq(LB.subs(c,sp.Rational(1,3)), sp.Rational(8,3)*(4*v-1)*(v-1))
assert LC.subs(c,sp.Rational(1,3)).subs(v,sp.Rational(1,4)) == 2
assert LD.subs(c,0).subs(v,sp.Rational(1,4)) == 2
assert Hpoly.subs(v,sp.Rational(1,4)) > 0

# R5-C political signs.
NC = sp.factor(sp.fraction(BC["Phi"])[0])
EC = sp.factor(sp.fraction(BC["E"])[0])
assert eq(BC["Phi"], NC/(18*(3-4*v)**2))
assert eq(BC["Dis"], 8*c*(3-2*c)*(1-v)/(9*(3-4*v)**2))
assert eq(BC["E"], EC/(18*(3-4*v)**2))
assert eq(sp.Poly(NC,c).coeff_monomial(c**2), 2*(18*v**2-44*v+27))
assert eq(sp.Poly(EC,c).coeff_monomial(c**2), 2*(18*v**2-28*v+11))
assert eq(NC.subs(c,0), 9*v*(4*v-3))
assert eq(NC.subs(c,sp.Rational(1,3)), (144*v**2+29*v-126)/9)
assert eq(EC.subs(c,0), 9*v*(4*v-3))
assert eq(EC.subs(c,sp.Rational(1,3)), (144*v**2-83*v-14)/9)
for poly in [144*v**2+29*v-126, 144*v**2-83*v-14]:
    assert poly.subs(v,0) < 0
    assert poly.subs(v,sp.Rational(1,4)) < 0
assert eq(NC.subs(v,0), 6*c*(9*c-10))
assert eq(EC.subs(v,0), 2*c*(11*c-6))

# R5-C adoption interval.
MTA = sp.factor(-BC["TA"]*9*(3-4*v)**2)
assert eq(sp.Poly(MTA,c).coeff_monomial(c**2), (6*v-5)**2)
assert eq(MTA.subs(c,0), 9*v*(4*v-3))
assert eq(MTA.subs(c,sp.Rational(1,3)), (144*v**2-15*v-65)/9)
assert eq(MTA.subs(v,0), c*(25*c-30))
assert eq(BC["TU"], 5*c*(2-c)*(1-v)/(3*(3-4*v)**2))
assert eq(BC["TW"]-BC["TU"], v*(3-4*c)**2*(15-16*v)/(81*(3-4*v)**2))
gapC = sp.factor(2*BC["TA"]-BC["TW"])
MCgap = sp.factor(-gapC*81*(3-4*v)**2)
assert sp.Poly(MCgap,c).coeff_monomial(c**2).subs(v,sp.Rational(1,4)) > 0
assert eq(MCgap.subs(c,0), 9*v*(56*v-39))
assert eq(MCgap.subs(c,sp.Rational(1,3)), (2192*v**2-570*v-495)/9)
assert eq(MCgap.subs(v,0), c*(315*c-270))

# Exact Bernstein certificates on [0,1/3] x [0,1/4].
x, y = sp.symbols("x y")
def bernstein_coeffs(poly):
    p = sp.Poly(sp.expand(poly.subs({c:sp.Rational(1,3)*x, v:sp.Rational(1,4)*y})), x, y)
    nx, ny = p.degree(x), p.degree(y)
    a = {(k,l): p.coeff_monomial(x**k*y**l)
         for k in range(nx+1) for l in range(ny+1)}
    out = {}
    for i in range(nx+1):
        for j in range(ny+1):
            z = sp.Rational(0)
            for k in range(i+1):
                for l in range(j+1):
                    z += a[(k,l)] * sp.Rational(comb(i,k),comb(nx,k)) * sp.Rational(comb(j,l),comb(ny,l))
            out[(i,j)] = sp.factor(z)
    return nx, ny, out

def cert(poly, zeros, min_positive):
    nx, ny, b = bernstein_coeffs(poly)
    assert all(z >= 0 for z in b.values())
    assert {ij for ij,z in b.items() if z == 0} == set(zeros)
    assert min(z for z in b.values() if z > 0) == min_positive
    return nx, ny

phi_n, _ = sp.fraction(sp.factor(BB["Phi"]))
E_n, _ = sp.fraction(sp.factor(BB["E"]))
D_n, _ = sp.fraction(sp.factor(BB["Dis"]))
TA_n, _ = sp.fraction(sp.factor(BB["TA"]))
Qphi = sp.factor(phi_n/(4*v-3))
QE = sp.factor(E_n/(4*v-3))
QD = sp.factor(D_n/(-(4*v-3)))
QTA = sp.factor(TA_n/(-(4*v-3)))

gTW = sp.factor(2*BB["TA"]-BB["TW"]); gTW_n, _ = sp.fraction(gTW)
gTU = sp.factor(2*BB["TA"]-BB["TU"]); gTU_n, _ = sp.fraction(gTU)
dWU = sp.factor(BB["TW"]-BB["TU"]); dWU_n, _ = sp.fraction(dWU)
QgapTW = sp.factor(gTW_n)
QgapTU = sp.factor(gTU_n/(-(4*v-3)))
Qdiff = sp.factor(dWU_n/(-v))

assert cert(Qphi,{(0,0)},sp.Rational(51,8)) == (2,7)
assert cert(QE,{(0,0),(2,7)},sp.Rational(11,6)) == (2,7)
assert cert(QD,{(0,0)},sp.Integer(1)) == (2,5)
assert cert(QTA,{(0,0)},sp.Rational(151,16)) == (2,7)
assert cert(QgapTW,{(0,0)},sp.Rational(549927,512)) == (2,8)
assert cert(QgapTU,{(0,0)},sp.Integer(12)) == (2,7)
assert cert(Qdiff,set(),sp.Rational(3479,12)) == (2,4)

Dpos = (1-v)**2*(1-2*v)*(2-3*v)*Hpoly**2
assert eq(BB["Phi"], (4*v-3)*Qphi/(64*Dpos))
assert eq(BB["E"], (4*v-3)*QE/(64*Dpos))
assert eq(BB["Dis"], (3-4*v)*QD/(32*Dpos))
assert eq(BB["TA"], (3-4*v)*QTA/(32*Dpos))
assert eq(Qphi.subs(v,0), 14*c*(58-59*c))
assert eq(QE.subs(v,0), 6*c*(42-71*c))
assert eq(QD.subs(v,0), 40*c*(7-5*c))
assert eq(QTA.subs(v,0), 26*c*(14-13*c))
assert eq(BB["TU"], -c*(c-2)*(4*v-3)*(12*v-7)*(20*v-13)/(32*(2*v-1)*Hpoly**2))
assert eq(gTW, QgapTW/(1568*(1-v)**2*(1-2*v)*(2-3*v)*Hpoly**2))
assert eq(gTU, (3-4*v)*QgapTU/(32*(1-v)**2*(1-2*v)*(2-3*v)*Hpoly**2))
assert eq(dWU, v*Qdiff/(784*(1-2*v)*Hpoly**2))

# Full-bypass post-adoption identity.
for X in [BC, BB]:
    assert eq((X["KI"]+2*X["P"]+X["C"])-(X["KI"]+3*X["P"]), -X["Dis"])
    assert eq(X["Phi"], X["E"]-X["Dis"])

# Exact witness: adoption interval survives but political reversal does not.
w = {c:sp.Rational(1,10), v:sp.Rational(6,25)}
expected = {
    "C": {
        "Phi":-sp.Rational(79079,780300),
        "Dis":sp.Rational(1064,23409),
        "E":-sp.Rational(130837,2340900),
        "TA":sp.Rational(336899,2340900),
        "TU":sp.Rational(1805,31212),
        "TW":sp.Rational(87037,780300),
    },
    "B": {
        "Phi":-sp.Rational(53617141587261,615261340595200),
        "Dis":sp.Rational(133095975,2309106176),
        "E":-sp.Rational(18153719048511,615261340595200),
        "TA":sp.Rational(46252347421011,307630670297600),
        "TU":sp.Rational(511510875,8521625216),
        "TW":sp.Rational(44245363371,417559635584),
    }
}
for label, X in [("C",BC),("B",BB)]:
    for k,z in expected[label].items():
        assert eq(X[k].subs(w), z)
    FL = max(expected[label]["TA"], expected[label]["TU"], expected[label]["TW"])
    assert FL < 2*expected[label]["TA"]
    assert expected[label]["Phi"] < 0
    assert expected[label]["Dis"] > 0
    assert expected[label]["E"] < 0

print("R5 design freeze: gamma=1/2 differentiated demand")
print("R5-C pre-adoption SU advantage: FAILS on full audit box")
print("R5-B pre-adoption SU advantage: FAILS on full audit box")
print("R5-C/B outsider-only selection-free adoption interval: EXISTS on full audit box")
print("R5-C/B adoption effect on relative IS incentive: WEAKENS (E<0)")
print("R5-C/B SU->IS preference reversal: IMPOSSIBLE because initial SU preference fails")
print("R5 competition portability verification: PASS")
