"""R19 exact counterfactuals beyond inherited success-only assertions.

The finite investment evaluator below is independently written from
consumer/network/cost primitives; R18's assertion pre>0 is not removed
or bypassed. The inherited global-price algorithm is imported unchanged
and reused at newly supplied exact market configurations with d=0.
"""
from contextlib import redirect_stdout
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import importlib.util
import io
import json
import sys
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
R=s.Rational

def load_module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def evaluate(mode,v,c,d,F,gamma=None):
    M0=s.ones(3) if mode=="cournot" else (1-gamma)*s.eye(3)+gamma*s.ones(3)
    @lru_cache(None)
    def market(used,cost):
        C=s.Matrix(3,3,lambda i,j:int(used[i]==used[j] and used.count(used[i])>=2))
        M=M0-v*C
        H=s.diag(*([M[i,i] for i in range(3)] if mode=="cournot"
                   else [1/M.inv()[i,i] for i in range(3)]))
        q=(M+H).inv()*(s.ones(3,1)-s.Matrix(cost))
        p=s.ones(3,1)-M*q
        assert all(x>0 for x in q) and all(p[i]>cost[i] for i in range(3))
        pi=tuple(s.factor((p[i]-cost[i])*q[i]) for i in range(3))
        cs=s.factor((q.T*M0*q)[0]/2)
        return pi,cs
    games={}
    for label,rho in [("SU",(0,0,2)),("SW",(0,1,2)),("IS",(0,0,0))]:
        choices=[]
        for i in range(3):
            foreign=sorted(set(rho)-{rho[i]})
            choices.append([tuple(t) for n in range(len(foreign)+1) for t in combinations(foreign,n)])
        tables={}
        for actions in product(*choices):
            profit=[s.S(0)]*3; cs=[]
            for dest in rho:
                used=tuple(dest if dest in actions[i] else rho[i] for i in range(3))
                cost=tuple(s.S(0) if rho[i]==dest else d if dest in actions[i] else c for i in range(3))
                pi,consumer=market(used,cost)
                profit=[profit[i]+pi[i] for i in range(3)]; cs.append(consumer)
            net=tuple(s.factor(profit[i]-F*len(actions[i])) for i in range(3))
            welfare=tuple(s.factor(cs[i]+net[i]) for i in range(3))
            tables[actions]=(tuple(profit),net,welfare)
        ne=[]
        for actions,(op,net,welfare) in tables.items():
            gaps=[s.factor(net[i]-tables[actions[:i]+(other,)+actions[i+1:]][1][i])
                  for i in range(3) for other in choices[i] if other!=actions[i]]
            if all(g>=0 for g in gaps):ne.append((actions,min(gaps) if gaps else s.oo))
        games[label]=(tables,ne,choices)
    nil=((),(),()); outsider=((),(),(0,))
    su,sw,is_=[games[k][0] for k in ("SU","SW","IS")]
    assert [a for a,m in games["SU"][1]]==[outsider]
    assert [a for a,m in games["SW"][1]]==[nil]
    member=[];sw_edges=[]
    for a,(op,net,welfare) in su.items():
        for i in (0,1):
            if not a[i]:
                alt=a[:i]+((2,),)+a[i+1:]
                member.append(s.factor(su[alt][0][i]-op[i]))
    for a,(op,net,welfare) in sw.items():
        for i in range(3):
            for extra in set(range(3))-{i}-set(a[i]):
                alt=a[:i]+(tuple(sorted(a[i]+(extra,))),)+a[i+1:]
                sw_edges.append(s.factor(sw[alt][0][i]-op[i]))
    gross=s.factor(su[outsider][0][2]-su[nil][0][2])
    upper=max([s.S(0)]+member+sw_edges)
    assert upper<F<gross
    pre=s.factor(su[nil][2][0]-is_[nil][2][0])
    post=s.factor(su[outsider][2][0]-is_[nil][2][0])
    return {"mode":mode,"v":str(v),"c":str(c),"d":str(d),"F":str(F),"gamma":str(gamma),
            "profiles":{name:len(g[0]) for name,g in games.items()},
            "unique_pure_investment_NE":{name:str(g[1]) for name,g in games.items()},
            "max_SU_member_increment":str(max(member)),"max_SW_increment":str(max(sw_edges)),
            "outsider_two_market_gross":str(gross),"fee_lower":str(upper),"fee_upper":str(gross),
            "pre_gap":str(pre),"post_gap":str(post),"pre_decimal":float(pre),"post_decimal":float(post),
            "all_mixed_investment_NE":"unique by all-profile strict removal dominance and outsider strict adoption",
            "market_configurations":market.cache_info().currsize}

def d0_price_audit():
    capture=io.StringIO()
    with redirect_stdout(capture):
        global_audit=load_module(ROOT/"research/r16/verify_global_bertrand_price_deviations.py","r19_extra_global")
        global_audit.d=s.S(0)
        global_audit.verify_market.cache_clear()
        global_audit.TOTAL_CHECKS=0
        markets=global_audit.gather_markets()
        for used,cost in markets:assert global_audit.verify_market(used,cost)
    (OUT/"d0_global_price_reuse.stdout.txt").write_text(
        "The following 19-market output is the unchanged module's baseline import-time replay.\n"
        +capture.getvalue()+"\nNew d=0 replay completed separately: "
        +str(len(markets))+" labeled markets, "+str(global_audit.TOTAL_CHECKS)
        +" feasible global price candidates. All assertions passed.\n")
    kink=load_module(OUT/"verify_bertrand_boundary_kinks.py","r19_extra_kink")
    records=[]
    for used,cost in markets:
        K=s.Matrix(3,3,lambda i,j:int(used[i]==used[j] and used.count(used[i])>=2))
        M=kink.M0-kink.V*K
        assert all(M[:k,:k].det()>0 for k in (1,2,3))
        A=M.inv();H=s.diag(*[1/A[i,i] for i in range(3)])
        for n in (1,2):
            for B in combinations(range(3),n):
                verts=kink.vertices((M+H).extract(B,B),s.Matrix([1-cost[i] for i in B]))
                for j in set(range(3))-set(B):
                    pressure=max((M.extract([j],B)*x)[0] for x in verts)
                    slack=s.factor(1-cost[j]-pressure)
                    assert slack>0,(used,cost,B,j,slack)
                    records.append({"used":used,"cost":list(map(str,cost)),"active":B,"omitted":j,"slack":str(slack)})
    (OUT/"d0_kink_certificate.json").write_text(json.dumps(records,indent=2)+"\n")
    return {"d":"0","market_configurations":len(markets),
            "global_price_candidate_checks":global_audit.TOTAL_CHECKS,
            "kink_entry_checks":len(records),"minimum_kink_entry_slack":str(min(s.Rational(r["slack"]) for r in records)),
            "conclusion":"unique pure-price Nash in each d=0 market; no mixed-price uniqueness claim"}

def residual_derivative():
    gamma,v=R(23,25),R(33,500)
    M0=(1-gamma)*s.eye(3)+gamma*s.ones(3);M=M0-v*s.ones(3)
    A=M.inv();H=s.diag(*[1/A[i,i] for i in range(3)])
    z=s.symbols("z",real=True)
    q=(M+H).inv()*(s.ones(3,1)-s.Matrix([0,0,z]))
    p=s.ones(3,1)-M*q
    m=s.factor((q.T*M0*q)[0]/2+sum(p[i]*q[i] for i in (0,1)))
    r0=s.factor(s.diff(m,z).subs(z,0)); r1=s.factor(s.diff(m,z,2))
    assert r0<0
    vc=R(6,25)
    cournot_r0=s.factor((1-4*vc)/(16*(1-vc)**2))
    assert cournot_r0>0
    return {"government_post_gap_derivative_at_d0":str(r0),"derivative_decimal":float(r0),
            "second_derivative":str(r1),"original_Cournot_v6_25_d0_derivative":str(cournot_r0),
            "interpretation":"cost-only rise in residual d locally lowers SU-minus-IS welfare at Bertrand d=0; original Cournot derivative is positive; export term fixed"}

def main():
    zero=evaluate("cournot",s.S(0),R(1,10),R(1,20),R(1,50))
    assert s.Rational(zero["pre_gap"])==-R(47,3200)
    assert s.Rational(zero["pre_gap"])<0 and s.Rational(zero["post_gap"])<0
    complete=evaluate("bertrand",R(33,500),R(2,125),s.S(0),R(1,40),R(23,25))
    assert s.Rational(complete["pre_gap"])>0>s.Rational(complete["post_gap"])
    report={"zero_network_private_adoption_without_reversal":zero,
            "bertrand_complete_compatibility":complete,"bertrand_d0_price_audit":d0_price_audit(),
            "bertrand_local_residual_comparative_static":residual_derivative(),
            "epistemic_status":"exact rational finite games and exact candidate/vertex proof; local derivative at d=0, not a universal comparative-static theorem"}
    (OUT/"extra_counterfactuals.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))

if __name__=="__main__":main()
