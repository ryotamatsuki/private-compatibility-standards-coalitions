"""Independent manuscript reconstruction; never imports production audit modules.

Inputs: the short paper's primitives and Appendix E's matrix demand systems.
First exposure to old R4/R5 code is disclosed in the audit report. Independence
comes from matrix inversion, a new triangular-domain Bernstein certificate for
S1, and finite normal-form reconstruction of adoption and coalition deviations.
Run from any directory; optional --json records exact rational certificates.
"""
from __future__ import annotations
import argparse
from functools import lru_cache
from itertools import product, combinations
from math import comb
import json
from pathlib import Path
import sympy as s

c, v, d, x, y = s.symbols("c v d x y", real=True)

@lru_cache(None)
def market(groups, costs, kind="canonical", competition="C", network=v):
    adjacency = s.zeros(3)
    for group in groups:
        if len(group) > 1 or kind == "singleton":
            for i in group:
                for j in group:
                    adjacency[i, j] = 1
    base = s.ones(3) if kind != "differentiated" else (s.eye(3)+s.ones(3))/2
    M = base-network*adjacency
    r, one = s.Matrix(costs), s.ones(3, 1)
    if competition == "C":
        q = (M+s.diag(*M.diagonal())).inv()*(one-r)
        p = one-M*q
        for i in range(3):
            assert s.simplify(p[i]-r[i]-M[i, i]*q[i]) == 0
    else:
        inverse = M.inv()
        diagonal = s.diag(*inverse.diagonal())
        p = (inverse+diagonal).inv()*(inverse*one+diagonal*r)
        q = inverse*(one-p)
        for i in range(3):
            assert s.simplify(q[i]-inverse[i, i]*(p[i]-r[i])) == 0
    q = q.applyfunc(s.factor)
    pi = s.Matrix([(p[i]-r[i])*q[i] for i in range(3)]).applyfunc(s.factor)
    cs = sum(q)**2/2 if kind != "differentiated" else (q.T*M*q)[0]/2
    return M, q, pi, s.factor(cs)

def blocks(kind="canonical", competition="C"):
    all_firms, pair = ((0, 1, 2),), ((0, 1), (2,))
    I = market(all_firms, (0, 0, 0), kind, competition)
    U = market(pair, (0, 0, c), kind, competition)
    O = market(pair, (c, c, 0), kind, competition)
    W = market(((0,), (1,), (2,)), (0, c, c), kind, competition)
    P, A, B, C, S = I[2][0], U[2][0], U[2][2], O[2][0], W[2][1]
    phi = s.factor(U[3]+2*A+C-I[3]-3*P)
    exclusion = s.factor(U[3]-I[3]+2*(A-P))
    disadvantage = s.factor(P-C)
    assert s.simplify(phi-exclusion+disadvantage) == 0
    return dict(I=I,U=U,O=O,W=W,P=P,A=A,B=B,C=C,S=S,
                phi=phi,E=exclusion,D=disadvantage,
                TA=s.factor(P-B),TU=s.factor(A-C),TW=s.factor(A-S))

def bernstein(poly, degree, zeros, minimum):
    """Exact power-to-Bernstein conversion from the manuscript formula."""
    p = s.Poly(s.expand(poly), x, y)
    n, m = degree
    assert (p.degree(x),p.degree(y)) == degree
    b = {}
    for i in range(n+1):
        for j in range(m+1):
            b[i,j] = s.factor(sum(
                p.coeff_monomial(x**k*y**l)*s.Rational(comb(i,k),comb(n,k))
                *s.Rational(comb(j,l),comb(m,l))
                for k in range(i+1) for l in range(j+1)))
    assert all(z >= 0 for z in b.values())
    assert {ij for ij,z in b.items() if z == 0} == set(zeros)
    assert min(z for z in b.values() if z > 0) == minimum
    # Reconstruct the polynomial from the basis; do not trust conversion alone.
    reconstructed = sum(z*comb(n,i)*x**i*(1-x)**(n-i)
                        *comb(m,j)*y**j*(1-y)**(m-j) for (i,j),z in b.items())
    assert s.expand(reconstructed-poly) == 0
    return dict(degree=list(degree),minimum=str(minimum),zeros=[list(z) for z in sorted(zeros)],
                coefficients={f"{i},{j}":str(z) for (i,j),z in b.items()})

PARTITIONS = (((0,),(1,),(2,)), ((0,1),(2,)), ((0,2),(1,)), ((0,),(1,2)), ((0,1,2),))

def adoption_game(partition, cc, vv, dd, ff, kind="canonical", competition="C", masses=(1,1,1)):
    native = [next(k for k,g in enumerate(partition) if i in g) for i in range(3)]
    choices = []
    for i in range(3):
        extra = [k for k in range(len(partition)) if k != native[i]]
        choices.append([frozenset(a) for size in range(len(extra)+1) for a in combinations(extra,size)])
    profiles = list(product(*choices)); payoffs = {}; welfares = {}
    for profile in profiles:
        profit = [-ff*len(profile[i]) for i in range(3)]; consumer=[]
        for destination in range(3):
            target = native[destination]
            used = [target if target == native[i] or target in profile[i] else native[i] for i in range(3)]
            groups = tuple(tuple(i for i in range(3) if used[i] == g) for g in sorted(set(used)))
            costs = tuple(0 if native[i] == target else dd if target in profile[i] else cc for i in range(3))
            _, q, pi, cs = market(groups,costs,kind,competition,vv)
            assert all(z > 0 for z in q)
            if kind != "differentiated": assert 0 < sum(q) < 1
            consumer.append(masses[destination]*cs)
            for i in range(3):profit[i] += masses[destination]*pi[i]
        payoffs[profile] = tuple(map(s.factor,profit))
        welfares[profile] = tuple(s.factor(profit[i]+consumer[i]) for i in range(3))
    equilibria=[]
    for profile in profiles:
        if all(payoffs[profile][i] >= payoffs[profile[:i]+(a,)+profile[i+1:]][i]
               for i in range(3) for a in choices[i]):equilibria.append(profile)
    assert len(equilibria) == 1
    equilibrium = equilibria[0]
    # Strict-dominance check rules out omitted mixed equilibria at these witnesses.
    for i in range(3):
        for profile in profiles:
            preferred = profile[:i]+(equilibrium[i],)+profile[i+1:]
            for a in choices[i]:
                if a != equilibrium[i]:
                    alternative = profile[:i]+(a,)+profile[i+1:]
                    assert payoffs[preferred][i] > payoffs[alternative][i]
    return equilibrium,welfares[equilibrium]

def stable_sets(cc,vv,ff,masses=(1,1,1)):
    welfare={rho:adoption_game(rho,cc,vv,0,ff,masses=masses)[1] for rho in PARTITIONS}
    strict=[];weak=[]
    for rho in PARTITIONS:
        sb=wb=False
        for size in range(1,4):
            for deviators in combinations(range(3),size):
                D=set(deviators)
                following=[tuple(deviators)]+[tuple(i for i in group if i not in D) for group in rho]
                following=tuple(sorted(g for g in following if g))
                gap=[welfare[following][i]-welfare[rho][i] for i in deviators]
                sb |= all(z>0 for z in gap)
                wb |= all(z>=0 for z in gap) and any(z>0 for z in gap)
        if not sb:strict.append(rho)
        if not wb:weak.append(rho)
    return strict,weak

def main():
    report={}
    Z=blocks()
    all_firms=((0,1,2),)
    Rmarket=market(all_firms,(0,0,d))
    rent=s.factor(Rmarket[3]-Z['I'][3]+2*(Rmarket[2][0]-Z['P']))
    target=d*((5-4*v)*d+2*(1-4*v))/(32*(1-v)**2)
    assert s.simplify(rent-target)==0
    assert s.simplify((Rmarket[3]+2*Rmarket[2][0]+Z['C']-Z['I'][3]-3*Z['P'])-rent+Z['D'])==0
    assert s.factor(Z['phi'].subs(v,0))==c*(13*c-6)/32
    cw,vw=s.Rational(1,10),s.Rational(6,25)
    w={c:cw,v:vw}
    pre=s.factor(Z['phi'].subs(w))
    post=s.factor((rent-Z['D']).subs(w).subs(d,s.Rational(1,20)))
    assert pre==s.Rational(2408509,295731200) and post==-s.Rational(1341,184832)
    for rho in PARTITIONS:
        profile,_=adoption_game(rho,cw,vw,s.Rational(1,20),s.Rational(9,100))
        if len(rho)==2:
            outsider=next(g[0] for g in rho if len(g)==1)
            assert [len(a) for a in profile]==[int(i==outsider) for i in range(3)]
        else:assert all(not a for a in profile)
    report['core']=dict(residual_rent=str(rent),pre_gap=str(pre),post_gap=str(post),strict_dominance='PASS')
    S1=blocks('singleton'); K=3*v*v-6*v+2
    M1=s.cancel(S1['phi']*32*(1-v)**2*K**2)
    Q1=s.cancel(-9*M1.subs(c,x*(1-3*v)/(3*(1-v))))
    report['S1']=bernstein(Q1.subs(v,y/4),(2,5),{(0,0)},s.Rational(571,512))
    for mode in ('C','B'):
        z=blocks('differentiated',mode)
        if mode=='C':
            targets=[('Phi',s.cancel(-18*(3-4*v)**2*z['phi']), (2,2),{(0,0)},s.Rational(27,8)),
                     ('E',s.cancel(-18*(3-4*v)**2*z['E']), (2,2),{(0,0)},s.Rational(14,9))]
        else:
            positive_den=(1-v)**2*(1-2*v)*(2-3*v)*(8*v*v-16*v+7)**2
            targets=[('Phi',s.cancel(64*positive_den*z['phi']/(4*v-3)),(2,7),{(0,0)},s.Rational(51,8)),
                     ('E',s.cancel(64*positive_den*z['E']/(4*v-3)),(2,7),{(0,0),(2,7)},s.Rational(11,6)),
                     ('D',s.cancel(32*positive_den*z['D']/(3-4*v)),(2,5),{(0,0)},s.Integer(1))]
        for label,poly,degree,zeros,minimum in targets:
            report[f'{mode}:{label}']=bernstein(poly.subs({c:x/3,v:y/4}),degree,zeros,minimum)
        for rho in PARTITIONS:
            adoption_game(rho,cw,vw,0,s.Rational(1,5),'differentiated',mode)
        assert max(z[t].subs(w) for t in ('TA','TU','TW'))<s.Rational(1,5)<2*z['TA'].subs(w)
    for rho in PARTITIONS:adoption_game(rho,cw,vw,0,s.Rational(3,25),'singleton')
    assert stable_sets(cw,vw,s.Rational(1,5))==(list(PARTITIONS[1:4]),[])
    assert stable_sets(cw,vw,s.Rational(3,25))==([PARTITIONS[4]],[PARTITIONS[4]])
    assert stable_sets(cw,vw,s.Rational(1,5),(1,1,s.Rational(3,4)))==([PARTITIONS[1]],[PARTITIONS[1]])
    assert stable_sets(cw,vw,s.Rational(3,25),(1,1,s.Rational(1,2)))==([PARTITIONS[4]],[PARTITIONS[4]])
    report['coalition_witnesses']='All five partitions and seven nonempty coalitions re-solved: PASS'
    parser=argparse.ArgumentParser();parser.add_argument('--json',type=Path);args=parser.parse_args()
    if args.json:
        args.json.parent.mkdir(parents=True,exist_ok=True)
        args.json.write_text(json.dumps(report,indent=2)+'\n')
    print('JICT SHORT INDEPENDENT RECONSTRUCTION: PASS (primitives, exact signs, adoption and deviations)')

if __name__=='__main__':main()
