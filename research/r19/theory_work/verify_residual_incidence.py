"""Exact symbolic/rational checks for the proved R19 partial residual theorem.

This is NOT a numerical proof of the full R19 main theorem, investment-game
selection over a parameter interval, or general Bertrand global uniqueness.
"""
import json
import sympy as s

g, v, ell, d = s.symbols("gamma v ell d", real=True)
b = g-v
tau = 1-g+ell
kappa = 1+2*g-3*v+ell
x = (tau+b*d)/(tau*kappa)
y = (tau-(tau+2*b)*d)/(tau*kappa)
m = (1+g+2*ell)*x**2+2*g*x*y+y**2/2
rho = 1+2*g-4*ell*b/tau
A = tau**2+4*(1-g)*tau*b+(6*(1-g)+4*ell)*b**2
R = (-rho*d+A*d**2/(2*tau**2))/kappa**2
assert s.factor(m-m.subs(d,0)-R)==0
assert s.factor(s.diff(R,d,2)-A/(tau**2*kappa**2))==0
assert s.factor(s.diff(2*ell*y**2,d)+4*ell*(tau+2*b)*y/(tau*kappa))==0

# Exact original R9 nesting, including its residual-rent coefficient.
r9 = s.factor(R.subs({g:1,ell:1-v}))
r9_original = d*((5-4*v)*d+2*(1-4*v))/(32*(1-v)**2)
assert s.factor(r9-r9_original)==0
assert s.factor(rho.subs({g:1,ell:1-v})-(4*v-1))==0

# Separate Bertrand FOC derivation, not mechanical Cournot substitution.
M0 = (1-g)*s.eye(3)+g*s.ones(3)
M = M0-v*s.ones(3)
ell_b = (1-g)*(1+2*g-3*v)/(1+g-2*v)
assert s.factor(1/M.inv()[0,0]-ell_b)==0
N = 2*g**2-10*g*v-3*g+12*v**2+v-2
rho_b = s.factor(rho.subs(ell,ell_b))
assert s.factor(rho_b-N/(-3*g+5*v-2))==0
assert s.factor(N.subs(v,0)-(2*g+1)*(g-2))==0
assert s.factor(N.subs(v,g)-2*(g-1)*(2*g+1))==0
assert s.diff(N,v,2)==24

# Differentiated Cournot's substitution boundary; monotone numerator is
# proved in the note, rather than inferred from a numeric plot.
rho_c = s.factor(rho.subs(ell,1-v))
Nc = 2*g**2-2*g*v+g+4*v**2-3*v-2
g_star = (2*v-1+s.sqrt(17+20*v-28*v**2))/4
assert s.factor(rho_c-Nc/(g+v-2))==0
assert s.factor(Nc.subs(g,g_star))==0
assert s.factor(Nc.subs(g,v)-2*(2*v+1)*(v-1))==0
assert s.factor(Nc.subs(g,1)-(4*v-1)*(v-1))==0
assert s.diff(Nc,g)==4*g-2*v+1

# Global-BR demand-slope ordering for the fully compatible price family.
t, bb = s.symbols("t bb", positive=True)
hn = lambda n:(t+(n-1)*bb)/(t*(t+n*bb))
for n in (1,2):
    assert s.factor(hn(n+1)-hn(n)-bb**2/((t+n*bb)*(t+(n+1)*bb)*t))==0
assert s.factor(hn(3).subs({t:1-g,bb:g-v})-1/ell_b)==0

# Exact R16 instance. Full game price deviations are a separate R16 check.
params = {g:s.Rational(23,25),v:s.Rational(33,500)}
ell_val = s.factor(ell_b.subs(params))
params[ell] = ell_val
get = lambda expr:s.factor(expr.subs(params))
tau_val,kappa_val,rho_val,A_val = map(get,(tau,kappa,rho,A))
d_min = s.factor(rho_val*tau_val**2/A_val)
d_bar = get(tau/(tau+2*b))
c0,d0 = s.Rational(2,125),s.Rational(1,500)
assert 0<d0<c0<d_min<d_bar
assert get(R).subs(d,d0)<0
assert get(s.diff(R,d)).subs(d,c0)<0
assert get(s.diff(2*ell*y**2,d)).subs(d,d0)<0

# Exact outsider best-response adoption cutoff against inactive members.
# B-state is independently solved; its network matrix still uses R9's
# singleton-zero outsider convention.
C_B = s.Matrix([[1,1,0],[1,1,0],[0,0,0]])
M_B = M0-v*C_B
own_B = s.diag(*[1/M_B.inv()[i,i] for i in range(3)])
q_B = (M_B+own_B).inv()*(s.ones(3,1)-s.Matrix([0,0,c0]))
Bpre = s.factor((own_B[2,2]*q_B[2]**2).subs(params))
F0 = s.Rational(1,40)
d_A = d_bar*(1-kappa_val*s.sqrt((Bpre+F0/2)/ell_val))
gross_gain = 2*(ell_val*get(y)**2-Bpre)
assert s.factor(gross_gain.subs(d,d_A)-F0)==0
assert gross_gain.subs(d,d0)>F0
assert gross_gain.subs(d,c0)<F0

# A two-sided exact check of the quadratic minimum and zero (interior).
assert get(s.diff(R,d)).subs(d,d_min)==0
assert get(R).subs(d,2*d_min)==0
assert 2*d_min<d_bar

report = {
 "status":"PROVED_PARTIAL_THEOREM_NOT_FULL_LEVEL_3",
 "symbolic_identity":"PASS",
 "original_R9_residual_identity":"PASS",
 "Bertrand_rho_sign":"analytic convex numerator and negative denominator",
 "R16":{k:{"exact":str(value),"decimal":float(value)} for k,value in
   {"ell":ell_val,"tau":tau_val,"kappa":kappa_val,"rho":rho_val,
    "A":A_val,"d_min":d_min,"d_zero_again":2*d_min,
    "d_exit":d_bar,"R_at_d":get(R).subs(d,d0),
    "R_slope_at_d":get(s.diff(R,d)).subs(d,d0),
    "outsider_pre_profit":Bpre,"outsider_adoption_cutoff":d_A}.items()},
 "not_proved":["initial SU rank from primitives",
   "all-stage investment selection over an interval",
   "global price uniqueness for arbitrary demand",
   "scholarly priority"]}
print(json.dumps(report,indent=2))
