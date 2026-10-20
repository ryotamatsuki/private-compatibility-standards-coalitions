"""R19 exact necessary-inequality certificate excluding boundary price Nash.

Unlike checking restricted-active-set stationary candidates, this covers
arbitrary kink prices of inactive products. No inherited file is modified.
"""
from itertools import combinations, product
from pathlib import Path
import json
import sympy as s

R=s.Rational
G,V,C,D=R(23,25),R(33,500),R(2,125),R(1,500)
M0=(1-G)*s.eye(3)+G*s.ones(3)

def markets():
    out=set()
    for rho in [(0,0,1),(0,1,2),(0,0,0)]:
        choices=[]
        for i in range(3):
            foreign=sorted(set(rho)-{rho[i]})
            choices.append([frozenset((rho[i],)+t) for k in range(len(foreign)+1)
                            for t in combinations(foreign,k)])
        for actions in product(*choices):
            for dest in rho:
                used=tuple(dest if dest in actions[i] else rho[i] for i in range(3))
                cost=tuple(R(0) if rho[i]==dest else D if dest in actions[i] else C for i in range(3))
                out.add((used,cost))
    return sorted(out,key=str)

def vertices(A,b):
    """Vertices of {x>=0, A*x<=b}, dimensions 1 or 2, exact rationals."""
    n=A.cols
    I=s.eye(n)
    rows=[(A[i,:],b[i]) for i in range(A.rows)]+[(I[i,:],s.S(0)) for i in range(n)]
    found=set()
    for indices in combinations(range(len(rows)),n):
        B=s.Matrix.vstack(*(rows[i][0] for i in indices))
        if B.det()==0:continue
        point=B.inv()*s.Matrix([rows[i][1] for i in indices])
        if all(t>=0 for t in point) and all(t<=0 for t in A*point-b):
            found.add(tuple(point))
    assert found
    return [s.Matrix(t) for t in found]

def main():
    records=[]
    for used,cost in markets():
        K=s.Matrix(3,3,lambda i,j:int(used[i]==used[j] and used.count(used[i])>=2))
        M=M0-V*K
        assert all(M[:k,:k].det()>0 for k in (1,2,3))
        A=M.inv()
        H=s.diag(*[1/A[i,i] for i in range(3)])
        for n in (1,2):
            for B in combinations(range(3),n):
                T=(M+H).extract(B,B)
                b=s.Matrix([1-cost[i] for i in B])
                verts=vertices(T,b)
                for j in set(range(3))-set(B):
                    max_pressure=max((M.extract([j],B)*x)[0] for x in verts)
                    slack=s.factor(1-cost[j]-max_pressure)
                    assert slack>0,(used,cost,B,j,slack)
                    records.append({"used":used,"cost":list(map(str,cost)),"active":B,"omitted":j,
                                    "max_pressure":str(max_pressure),"strict_entry_slack":str(slack)})
    report={"markets":len(markets()),"proper_active_set_omitted_brand_checks":len(records),
            "minimum_strict_slack":str(min(s.Rational(r["strict_entry_slack"]) for r in records)),
            "status":"exact rational polytope proof, including inactive-at-choke kinks", "certificates":records}
    out=Path(__file__).resolve().parent/"bertrand_kink_certificate.json"
    out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:v for k,v in report.items() if k!="certificates"},indent=2))

if __name__=="__main__":
    main()
