"""R6 coalition-stability robustness verification.

Exact symbolic identities and exhaustive deviation enumeration for:
- symmetric strict versus weak/Pareto blocking;
- market-size perturbation m1=m2=1, m3=1-delta;
- exact high-F and intermediate-F witnesses.

Production manuscript is intentionally untouched.
"""

from itertools import combinations
import sympy as sp

c, v, delta, F = sp.symbols("c v delta F", positive=True)

P = 1 / (16 * (1 - v))
A = (1 - v) * (1 + c) ** 2 / (4 * (2 - 3 * v) ** 2)
B = (1 - 3 * c - 3 * (1 - c) * v) ** 2 / (4 * (2 - 3 * v) ** 2)
C = (1 - v) * (1 - 2 * c) ** 2 / (4 * (2 - 3 * v) ** 2)
D = (1 + 2 * c - 3 * v) ** 2 / (4 * (2 - 3 * v) ** 2)
H = (1 + 2 * c) ** 2 / 16
S = (1 - 2 * c) ** 2 / 16

K_I = sp.Rational(9, 32) / (1 - v) ** 2
K_M = (3 - c - 3 * v + 3 * c * v) ** 2 / (8 * (2 - 3 * v) ** 2)
K_O = (3 - 2 * c - 3 * v) ** 2 / (8 * (2 - 3 * v) ** 2)
K_W = (3 - 2 * c) ** 2 / 32

T_A = sp.simplify(P - B)
T_U = sp.simplify(A - C)
T_W = sp.simplify(A - S)

W_IS_0 = sp.simplify(K_I + 3 * P)
W_M_0 = sp.simplify(K_M + 2 * A + C)
W_O_0 = sp.simplify(K_O + 2 * B + D)
W_SW_0 = sp.simplify(K_W + H + 2 * S)

Phi = sp.simplify(W_M_0 - W_IS_0)
Delta_MO = sp.simplify(W_M_0 - W_O_0)
G_MSW = sp.simplify(W_M_0 - W_SW_0)
G_ISW = sp.simplify(W_IS_0 - W_SW_0)
D_rec = sp.simplify(P - C)
J = sp.simplify(K_I + P - K_O - D)

# Canonical identity reused in the asymmetry proof.
assert sp.simplify((T_W - T_U) - (C - S)) == 0

# Market sizes.
m1 = sp.Integer(1)
m2 = sp.Integer(1)
m3 = 1 - delta
M = m1 + m2 + m3

# High-F no-bypass payoffs under SU12.
W1_12_N = sp.simplify(K_M + 2 * A + m3 * C)
W2_12_N = W1_12_N
W3_12_N = sp.simplify(m3 * K_O + 2 * B + m3 * D)

# High-F no-bypass payoffs under SU13.
W1_13_N = sp.simplify(K_M + (1 + m3) * A + C)
W2_13_N = sp.simplify(K_O + (1 + m3) * B + D)
W3_13_N = sp.simplify(m3 * K_M + (1 + m3) * A + C)

# International and SW payoffs for countries 1 and 3.
W1_IS = sp.simplify(K_I + M * P)
W3_IS = sp.simplify(m3 * K_I + M * P)
W1_SW = sp.simplify(K_W + H + (m2 + m3) * S)
W3_SW = sp.simplify(m3 * (K_W + H) + (m1 + m2) * S)

# Exact asymmetry identities.
assert sp.simplify((W1_12_N - W1_IS) - (Phi + delta * D_rec)) == 0
assert sp.simplify((W1_12_N - W1_SW) - (G_MSW - delta * (C - S))) == 0
assert sp.simplify((W1_12_N - W1_13_N) - delta * (A - C)) == 0
assert sp.simplify((W2_12_N - W2_13_N) - (Delta_MO + delta * (B - C))) == 0
assert sp.simplify((W1_IS - W1_SW) - (G_ISW - delta * (P - S))) == 0
assert sp.simplify(
    (W3_IS - W3_SW) - (G_ISW - delta * (K_I + P - K_W - H))
) == 0

# Intermediate-F outsider-only bypass identities for a generic SU.
mi, mj, mo = sp.symbols("mi mj mo", positive=True)
MC = mi + mj
MT = MC + mo
W_member_O = sp.simplify(mi * K_I + MC * P + mo * C)
W_outsider_O = sp.simplify(mo * K_O + MC * P + mo * D - F)
W_member_IS = sp.simplify(mi * K_I + MT * P)
W_outsider_IS = sp.simplify(mo * K_I + MT * P)
assert sp.simplify((W_member_IS - W_member_O) - mo * D_rec) == 0
assert sp.simplify((W_outsider_IS - W_outsider_O) - (mo * J + F)) == 0

# ---------------------------------------------------------------------------
# Exhaustive deviation enumeration on the five-partition institutional menu.
# ---------------------------------------------------------------------------

PLAYERS = (1, 2, 3)


def canon(blocks):
    return tuple(sorted((frozenset(b) for b in blocks), key=lambda b: (len(b), tuple(sorted(b)))))


SW = canon(({1}, {2}, {3}))
SU12 = canon(({1, 2}, {3}))
SU13 = canon(({1, 3}, {2}))
SU23 = canon(({2, 3}, {1}))
IS = canon(({1, 2, 3},))
PARTITIONS = (SW, SU12, SU13, SU23, IS)
COALITIONS = tuple(
    frozenset(s)
    for r in range(1, 4)
    for s in combinations(PLAYERS, r)
)


def deviate(partition, coalition):
    """Deviators form one coalition; residual members of old blocks stay together."""
    coalition = frozenset(coalition)
    new_blocks = []
    for block in partition:
        residual = block - coalition
        if residual:
            new_blocks.append(residual)
    new_blocks.append(coalition)
    return canon(new_blocks)


def is_su(partition):
    return len(partition) == 2 and sorted(len(b) for b in partition) == [1, 2]


def su_pair_outsider(partition):
    pair = next(b for b in partition if len(b) == 2)
    outsider = next(iter(set(PLAYERS) - set(pair)))
    return pair, outsider


def payoff_table(masses, fixed_cost, regime):
    total_mass = sum(masses.values())
    table = {}
    for part in PARTITIONS:
        if part == IS:
            table[part] = {
                i: sp.simplify(masses[i] * K_I + total_mass * P)
                for i in PLAYERS
            }
        elif part == SW:
            table[part] = {
                i: sp.simplify(
                    masses[i] * K_W
                    + masses[i] * H
                    + sum(masses[k] for k in PLAYERS if k != i) * S
                )
                for i in PLAYERS
            }
        else:
            assert is_su(part)
            pair, outsider = su_pair_outsider(part)
            coalition_mass = sum(masses[i] for i in pair)
            if regime == "high":
                pay = {
                    i: sp.simplify(
                        masses[i] * K_M + coalition_mass * A + masses[outsider] * C
                    )
                    for i in pair
                }
                pay[outsider] = sp.simplify(
                    masses[outsider] * K_O
                    + coalition_mass * B
                    + masses[outsider] * D
                )
            elif regime == "intermediate":
                pay = {
                    i: sp.simplify(
                        masses[i] * K_I + coalition_mass * P + masses[outsider] * C
                    )
                    for i in pair
                }
                pay[outsider] = sp.simplify(
                    masses[outsider] * K_O
                    + coalition_mass * P
                    + masses[outsider] * D
                    - fixed_cost
                )
            else:
                raise ValueError(regime)
            table[part] = pay
    return table


def blocks(part, coalition, table, concept):
    new_part = deviate(part, coalition)
    if new_part == part:
        return False
    diffs = [sp.simplify(table[new_part][i] - table[part][i]) for i in coalition]
    if concept == "strict":
        return all(x > 0 for x in diffs)
    if concept == "weak":
        return all(x >= 0 for x in diffs) and any(x > 0 for x in diffs)
    raise ValueError(concept)


def stable_set(table, concept):
    return tuple(
        part
        for part in PARTITIONS
        if not any(blocks(part, coalition, table, concept) for coalition in COALITIONS)
    )


# Exact witness point.
cw = sp.Rational(1, 10)
vw = sp.Rational(6, 25)
FH = sp.Rational(1, 5)
FI = sp.Rational(3, 25)
dw = sp.Rational(1, 100)

witness_subs = {c: cw, v: vw}

Pw = sp.simplify(P.subs(witness_subs))
Aw = sp.simplify(A.subs(witness_subs))
Bw = sp.simplify(B.subs(witness_subs))
Cw = sp.simplify(C.subs(witness_subs))
Sw = sp.simplify(S.subs(witness_subs))
TAw = sp.simplify(T_A.subs(witness_subs))
TUw = sp.simplify(T_U.subs(witness_subs))
TWw = sp.simplify(T_W.subs(witness_subs))

assert FH > 2 * TAw
assert FI > max(TWw, TAw, TUw)
assert FI < 2 * TAw

# Intermediate continuation is selection-free for every SU at delta=1/100.
masses_asym = {1: sp.Integer(1), 2: sp.Integer(1), 3: 1 - dw}
for part in (SU12, SU13, SU23):
    pair, outsider = su_pair_outsider(part)
    coalition_mass = sum(masses_asym[i] for i in pair)
    outsider_mass = masses_asym[outsider]
    assert FI < coalition_mass * TAw
    assert FI > outsider_mass * TUw
    assert FI > outsider_mass * TAw

# SW no-adoption conditions.
for mk in masses_asym.values():
    assert FI > mk * TWw
    assert FI > mk * TAw

# Stronger interval certificate: for 0 < delta <= 1/2, even the smallest
# two-country coalition mass is at least 3/2.
assert sp.Rational(3, 2) * TAw > FI

# High-F no adoption remains selection-free for all 0 < delta < 1.
assert FH > 2 * TAw
assert FH > TWw
assert FH > TAw
assert FH > TUw

# At the witness, the high-F asymmetry inequalities remain positive even at
# delta=1, so they hold throughout 0<delta<1 by linearity.
G_MSW_w = sp.simplify(G_MSW.subs(witness_subs))
Delta_MO_w = sp.simplify(Delta_MO.subs(witness_subs))
Phi_w = sp.simplify(Phi.subs(witness_subs))
Drec_w = sp.simplify(D_rec.subs(witness_subs))
assert sp.simplify(G_MSW_w - (Cw - Sw)) > 0
assert sp.simplify(Delta_MO_w + (Bw - Cw)) > 0
assert Phi_w > 0
assert Drec_w > 0
assert sp.simplify((A - C).subs(witness_subs)) > 0

# IS dominates SW at the witness throughout 0<=delta<=1 (linear endpoint check).
G_ISW_w = sp.simplify(G_ISW.subs(witness_subs))
assert G_ISW_w > 0
assert sp.simplify(G_ISW_w - (Pw - Sw)) > 0
assert sp.simplify(
    G_ISW_w - (K_I + P - K_W - H).subs(witness_subs)
) > 0

# Substitute the exact product-market witness before stable-set enumeration.
def substitute_table(table):
    return {
        part: {i: sp.simplify(pay.subs(witness_subs)) for i, pay in row.items()}
        for part, row in table.items()
    }


masses_sym = {1: sp.Integer(1), 2: sp.Integer(1), 3: sp.Integer(1)}

high_sym = substitute_table(payoff_table(masses_sym, FH, "high"))
inter_sym = substitute_table(payoff_table(masses_sym, FI, "intermediate"))
high_asym = substitute_table(payoff_table(masses_asym, FH, "high"))
inter_asym = substitute_table(payoff_table(masses_asym, FI, "intermediate"))

assert stable_set(high_sym, "strict") == (SU12, SU13, SU23)
assert stable_set(high_sym, "weak") == ()
assert stable_set(inter_sym, "strict") == (IS,)
assert stable_set(inter_sym, "weak") == (IS,)
assert stable_set(high_asym, "strict") == (SU12,)
assert stable_set(high_asym, "weak") == (SU12,)
assert stable_set(inter_asym, "strict") == (IS,)
assert stable_set(inter_asym, "weak") == (IS,)

# Symmetric high-F weak blocking: explicitly certify one alternative-SU block.
# From SU12, coalition {1,3} induces SU13. Country 1 is indifferent and
# country 3 moves from outsider to member and strictly gains.
diff_common = sp.simplify(high_sym[SU13][1] - high_sym[SU12][1])
diff_former_outsider = sp.simplify(high_sym[SU13][3] - high_sym[SU12][3])
assert diff_common == 0
assert diff_former_outsider > 0

print("R6 coalition-stability robustness verification: PASS")
print("symmetric high-F strict:", stable_set(high_sym, "strict"))
print("symmetric high-F weak:", stable_set(high_sym, "weak"))
print("symmetric intermediate strict/weak:", stable_set(inter_sym, "strict"))
print("asymmetric high-F strict/weak:", stable_set(high_asym, "strict"))
print("asymmetric intermediate strict/weak:", stable_set(inter_asym, "strict"))
print("exact witness adoption margin (3/2*T_A-F_I):", sp.simplify(sp.Rational(3, 2) * TAw - FI))
