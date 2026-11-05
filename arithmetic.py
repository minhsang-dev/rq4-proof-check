"""Recompute numbers used in 03_PROPOSITION_2_AUDIT.md and brute-force kNN threshold."""
import math, itertools

# C2: accumulation example
k, K, m, f, b, eta = 2000, 5, 2, 0.2, 1000, 0.2
s = k // K
print("s =", s, "| m*s =", m*s, "rho =", m*s/k, "| m*f*s =", m*f*s, "rho =", m*f*s/k)
for n in (round((1-eta)*b/K), round(b/K)):
    lam = math.floor(f*n + 1e-9) - 1
    print(f"n={n}: lambda_d={lam}, days={math.ceil(s/lam)}, daily rate={lam/n:.4f}")
# C-A
print("C-A: rate", 10/1000, "<= f", f, "; flips in context", 10, ">", f*10)
# C3
for beta in (0.1,):
    print("m=2 beta=.1: union", 1-2*beta, " indep", (1-beta)**2)
    print("multi-day m=2,W=13:", 1-2*13*beta, "; beta' for 0.9:", 0.1/(2*13))
# simulate the 2-source counterexample marginals/joint
import random
random.seed(1); beta=0.1; N=10**6; c1=c2=both=0
for _ in range(N):
    c=random.random()
    e1 = not (c<beta); e2 = not (beta<=c<2*beta)
    c1+=e1; c2+=e2; both+=(e1 and e2)
print("sim P(E1),P(E2),P(E1&E2) =", c1/N, c2/N, both/N)

# C4: kNN threshold, brute force. Convention T_big: ties -> larger label index (Jia). T_small: smaller index.
def predict(votes, tie):
    mx = max(votes)
    cands = [i for i,v in enumerate(votes) if v==mx]
    return max(cands) if tie=="big" else min(cands)
def robust_e(votes, tie):
    """largest e such that no relabelling of <=e neighbours changes prediction (brute force over vote shifts)"""
    a = predict(votes, tie); c=len(votes); best=-1
    for e in range(0, sum(votes)+1):
        ok=True
        for tgt in range(c):
            if tgt==a: continue
            # worst case: move e votes from a to tgt (only a-voters are useful)
            if e>votes[a]: continue
            v=list(votes); v[a]-=e; v[tgt]+=e
            if predict(v,tie)!=a: ok=False;break
        if ok: best=e
        else: break
    return best
bad=0
for sa in range(0,13):
  for sb in range(0,13):
    for a,b_ in ((0,1),(1,0)):
        v=[0,0]; v[a]=sa; v[b_]=sb
        if sa<sb: continue
        for tie in ("big","small"):
            if predict(v,tie)!=a: continue
            d=sa-sb
            ind = (a>b_) if tie=="big" else (a<b_)
            formula = math.ceil((d+int(ind))/2)-1
            if formula!=robust_e(v,tie): bad+=1
print("mismatches formula vs brute force (indicator matched to tie rule):", bad)
# audit formula with wrong indicator for Jia's rule would mismatch:
mis=0
for sa in range(0,13):
  for sb in range(0,sa+1):
    for a,b_ in ((0,1),(1,0)):
        v=[0,0]; v[a]=sa; v[b_]=sb
        if predict(v,"big")!=a: continue
        if math.ceil((sa-sb+int(a<b_))/2)-1!=robust_e(v,"big"): mis+=1
print("audit indicator 1[a<b] under Jia's larger-index tie rule mismatches:", mis)
# threshold for e=160
e=160
for I in (0,1):
    dmin=min(d for d in range(0,1000) if math.ceil((d+I)/2)-1>=e)
    print(f"I={I}: certified e=160 needs d>={dmin}")
