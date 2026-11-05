# PROOF_CHECK — independent check of 03_PROPOSITION_2_AUDIT.md (RQ4), v1

Inputs read in full: `03_PROPOSITION_2_AUDIT.md` (03), outline v14.3 excerpt (OUT), arXiv 2012.03765 (Jia et al., Thm 1 + Appendix A). Script: `arithmetic.py` (all numbers recomputed; run with `python3 -I`).
Labels: **CHECKED** (verified by me), **INFERENCE**, **UNSURE**.

## 1. Claim table

| # | Claim (03 section) | Verdict | One-line reason |
|---|---|---|---|
| C1 | Quota bound `|Π_t| ≤ min(k,m·s)` (§2, Lemma 1) | VERIFIED_WITH_FIX | Proof correct; must define Π_t as rows *flipped by sources in A* (not "any wrong label") and divide by k, not |C_t| |
| C2 | `m·s → m·f·s` fails under R1 (§4: C-A, C-B) | VERIFIED_WITH_FIX | Arithmetic right; but both examples need **label-dependent retention**; it is an assumption gap, not a refutation for every admissible implementation |
| C2′ | C-C (family-balanced buffer, "100 % of the family's rows poisoned") (§4) | GAP | Ignores that family rows also come from honest sources; 100 % only if the family is exclusive to the captured source |
| C2″ | C-D / §5.3 temporal (persistence, purge) (§4–5.3) | VERIFIED | Follows from definitions; 1−mWβ is union bound |
| C3 | Only `1−mβ` without independence; ex. 0.80 vs 0.81; multi-day `1−mWβ` (§5, Lemma 2) | VERIFIED | Union bound valid; counterexample valid (marginals 0.90/0.90, joint 0.80, simulated) |
| C4 | kNN certificate, fixed rows, label flips; margin ≥ 321; agreement with Jia Thm 1 (§8, Lemma 3) | VERIFIED_WITH_FIX | Lemma true under its own tie rule, but the indicator is `1[a<b]` vs Jia's `I(a>b)` — **not literally the same formula** (see §2) |
| C5 | Proposition 2′ (cap s on eligible pool; `1−|A_aud|β′`) (§7) | VERIFIED_WITH_FIX | Proof sound; add "whole batches, |B| ≤ s" and note it overrides RQ2's long-term compartment |
| C6 | Mode-B non-identifiability lemma (§9, citing `02` §4) | NOT_CHECKABLE | Lemma and proof live in `02`, not in my inputs; 03 only cites it |
| C7 | Collusion (vi) keeps quota bound, not the f factor (§9) | VERIFIED_WITH_FIX | Quota part true; wording "vacuous" is loose (see below) |
| C8 | Final arithmetic `ρ ≤ (m/K)f* < f*/2` (§1) | VERIFIED | Needs f*>0; note numerator uses f, formula (2-8) uses f* |
| C9 | R2 Theorem 1 (§6) | VERIFIED | Trivial summation; as 03 says, it just restates the assumption |
| — | §10 dependence loop V_t (items 1–5) | NOT_CHECKABLE | Labelled SL by 03 itself; relies on D4/D10/D17 not in my inputs |
| — | Absent from list? | — | All C1–C7 are present in 03. Extra claims found: C2′, C2″, C8, C9, §10 |

## 2. Details

**C1 (CHECKED).** `Π_t ⊆ ⋃_{j∈A} C_{t,j}` and `|⋃| ≤ Σ|C_{t,j}| ≤ m·s`; `Π_t ⊆ C_t` gives `≤ k`. With `s = k/K`: `m·s/k = m/K < 1/2` ✓.
Gaps: (i) 03 defines Π_t as rows whose returned label ≠ true label and then assumes honest rows are noise-free (D9=0). OUT does not say that, and RQ2/H2 explicitly add 10 % random label noise. Fix: define `Π_t := rows of A-sources whose label was flipped by the adversary`. (ii) `ρ`: OUT says "tỷ lệ dòng độc"; if the context is not full (e.g. honest sources flagged, §10 item 4) then `|Π_t|/|C_t|` can exceed `m·s/k`. Fix: define `ρ := |Π_t|/k` or assume `|C_t| = k`. (iii) The cap must be enforced per *identity* over the whole context including carried-over rows (03 notes this; also no sybil identities) — INFERENCE, not in OUT. (iv) Pseudo-label ablation rows (OUT, Nội dung 3, ≤10 % of context) have no source and can be wrong; they are outside Lemma 1 — UNSURE whether they matter; exclude them in the statement.

**C2 (CHECKED arithmetic; INFERENCE on scope).** Recomputed: k=2000, K=5 → s=400; m·s=800 → 40 %; m·f·s=160 → 8 % ✓. With n=b/K=200: λ_d=⌊40⌋−1=39 (19.5 %/day < f), ⌈400/39⌉=**11 days** ✓. With n=160: λ_d=31, **13 days** ✓ (E1 correction is right). C-A: 10/1000 = 1 % ≤ 20 %, 10 > f·s = 2 ✓.
*Scope problem.* In C-A and C-B the context must contain the flipped rows *preferentially*, i.e. the retention rule looks at labels (or scores that depend on them). If retention is independent of labels and of the flip pattern (uniform sampling from the day's batch, or age-based FIFO of whole daily batches), then each day's flipped fraction ≤ f carries into the context: in expectation (uniform) or exactly (age-based) `flips ≤ f·s` per source. So the proposition is false **only because its hypotheses ("cap s" + "audit with 1−β") do not restrict retention**; this is what 03 §4 "Kết luận F" says, but §0 labels it simply COUNTEREXAMPLE and C-A calls the violation "probability 1". Correct label: **ASSUMPTION GAP with an explicit (oracle-like or HB2-like) counter-policy**. 03 already concedes the oracle is not implementable and marks HB2 as unchecked (CXM) — that concession is correct and should stay in the headline. INFERENCE: this scope statement holds under reading R1 and also under a cumulative-rate reading (R3: rate over a source's whole history, not considered in 03); it fails only under R2 (audit on the loaded rows), as 03 says. Note NCS has fixed R1 (D15), so R1 counterexample is relevant.
Also under uniform retention `m·f·s` is only an *expectation* bound (hypergeometric fluctuation), so even then "≤ m f s with probability (1−β)^m" is not a hard bound — INFERENCE.

**C2′ (INFERENCE).** If the targeted family's rows are spread over K sources (mode a), only the ≤ m·s flipped rows of captured sources are poison, so "100 % of the family's rows in context" is wrong unless honest sources never see that family. Under quota the cap `m·s` still holds. The example needs "family exclusive to captured source" (e.g. mode b). Verdict GAP; 03 tags it SL, so impact is small.

**C3 (CHECKED).** `P(⋂E_j) ≥ 1 − Σ P(E_j^c) ≥ 1 − mβ` ✓ (no independence). Construction: c~U[0,1]; miss source 1 if c<β, source 2 if β≤c<2β: P(E_1)=P(E_2)=1−β, P(E_1∩E_2)=1−2β=0.80 < (1−β)²=0.81 (β=0.1; needs 2β≤1) ✓, simulation 0.7997. It is a valid instance: the outline only gives a marginal guarantee per source. Multi-day: m=2, W=13, β=0.1 → 1−2.6 = −1.6 (vacuous) ✓; β′ ≤ 0.1/26 ≈ 0.0038 for 0.9 ✓. With adaptive adversary the per-batch β must be conditional on history (03 §7 M2 does this) — fine. Note: this refutes only the *derivation* of (1−β)^m; the formula can still be true if DoP is independent/positively associated — 03 says so.

**C4 (CHECKED by brute force).** Jia et al.: ties among labels go to the **larger** label index (“take the label with the largest rank”), and the certificate is `e ≤ ⌈(s_a−s_b+I(a>b))/2⌉ − 1` (Thm 1; proof Appendix A: a wins if `s_a−s_b−2e ≥ 0` when a>b, `>0` when a<b). 03 Lemma 3 uses the **smaller** index rule and `1[a<b]`. Brute force over vote vectors: formula with indicator matched to the tie rule has 0 mismatches for both conventions; using 03's `1[a<b]` with Jia's tie rule mismatches (85 cases). So Lemma 3 is correct, equals Jia's after relabeling, but "khớp [49]" is true only up to tie-convention; state the convention explicitly. Jia's setting also allows added/removed rows (poisoning size = max(|D*|,|D|)−|D∩D*|), a superset of fixed-row label flips ✓.
Numbers: e=m·f·s=160. Need `⌈(d+I)/2⌉−1 ≥ 160` ⇒ d ≥ 321 (I=0) or d ≥ 320 (I=1); 03's “2·160=320<d ⇒ d ≥ 321” is the conservative sufficient version ✓. Since d ≤ v_a ≤ κ (neighbours), κ ≥ 321 is necessary ⇒ certificate inactive for κ of a few dozen ✓ (INFERENCE for “typical κ”). The dynamic case (context depends on labels) remains OPEN, correctly. OUT's sentence “nhỏ hơn một nửa chênh lệch” matches the strict version `2e<d`.

**C5 (CHECKED).** Event E = “no bad batch (flips > f|B|) is ever accepted for j∈A_aud”. With persistence (M3), “some bad batch accepted” ⊆ “first bad batch accepted”, probability ≤ β′ (conditional, so adaptive OK) ⇒ P(E^c) ≤ |A_aud|β′ ✓. On E, flips(P_{t,j}) ≤ f·Σ|B| ≤ f·s, integer ⇒ ⌊f s⌋ ✓; retention only picks a subset ✓; A_unc get ≤ s by Lemma 1 ✓; E does not depend on t ⇒ simultaneous in t ✓. Fixes: (a) requires every batch |B| ≤ s (OUT: n=b/K=200 ≤ 400 OK; else split/sample); (b) requires `C_t ⊆ ⋃P_{t,j}` — i.e. rows leave the context when they leave the pool; this conflicts with RQ2's long-lived rare-family compartment (03 says “design change”, agreed); (c) M2 is a *hypothesis* on DoP, not derived — the proposition is conditional, as 03 states.

**C6 (NOT_CHECKABLE).** Needed: `02_THREAT_AND_ATTACKS.md` §4. What 03 §9/§7 itself derives from it (UNCERTAIN sources only get the quota bound) is trivially consistent with Lemma 1 ✓.

**C7 (CHECKED/INFERENCE).** Lemma 1 holds for any joint behaviour of A ✓; union bound needs no independence ✓. 03's remark that under collusion the “still holds” sentence in OUT is “vacuous for arbitrarily bad f*, β” is loose: OUT's sentence is a true conditional statement if f*, β denote the degraded values; the real point is that no *a-priori* value of f*, β is guaranteed under (vi), and honest majority (m<K/2) is what the audit needs. Fix: reword as “quota bound unconditional; f*, β bound holds only with the post-collusion f*, β, which are not controlled”.

## 3. Overall verdict

**STANDS_WITH_CHANGES.** CHECKED: the quota bound `m·s` is correct and is the only part of Proposition 2 that follows from the hypotheses as written in OUT; `(1−β)^m` does not follow from per-source marginals (valid counterexample), and `1−mβ` is the correct independence-free bound (with `1−mWβ`-type loss over days). The step `m·s → m·f·s` is not implied by the stated hypotheses: the cap and the audit say nothing about which rows are retained, and a label-dependent retention rule with per-day rate just under f reaches `m·s` (40 % vs 8 %; arithmetic verified, E1 correction 11 days correct). The changes needed to 03's conclusion: (1) call C2 an *assumption gap shown by a label-dependent retention policy*, not a counterexample for all implementations (label-independent/age-based retention restores `f·s` per source); (2) fix Π_t/ρ definitions in Lemma 1; (3) fix the kNN tie-convention statement; (4) drop or qualify C-C. Proposition 2′ is sound as a conditional statement.

## 4. Fix list (minimal)

1. Lemma 1: `Π_t` = adversary-flipped rows of A-sources; `ρ := |Π_t|/k` (or assume full context); state no-sybil/per-identity cap; exclude pseudo-labels.
2. §0/§4: relabel F-R1 as “ASSUMPTION GAP (counter-policy: label-dependent retention)”; add the one-line positive result: label-independent age-based retention of whole daily batches gives `≤ ⌊f s⌋` per source.
3. §4 C-A: remove “xác suất 1” without stating that the policy is an oracle.
4. C-C: require the family to be exclusive to the captured source or delete.
5. Lemma 3: state tie rule; either use Jia's (larger index wins, `I(a>b)`) or keep smaller-index with `1[a<b]` and say “equivalent after relabeling”. Threshold: d ≥ 320 or 321 depending on tie.
6. 2′: add `|B| ≤ s`; state that `C_t ⊆ ⋃P_{t,j}` forbids RQ2 long-term retention of captured-source rows.
7. §9 collusion wording as in C7.
8. C6 and §10 not verified (inputs missing).
