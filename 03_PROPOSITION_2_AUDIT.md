STATUS: G2 DRAFT — phần độc lập DoP. `f*`, `β` ↔ công suất DoP = **HOLD_PROOF_SOURCE** (đặc tả DoP MISSING). Mọi chứng minh dưới đây là sơ cấp và tự chứa; cần người nghiên cứu hoặc agent độc lập kiểm lại trước khi trích.
SOURCE ANCHORS: v14.3 Nội dung 4 (Mệnh đề 2, (2-7), (2-8)), tr.~23; Định nghĩa 5; hồ sơ §3 (S1); `02_THREAT_AND_ATTACKS.md` §1, §4, §5 (DC-2); quyết định D8, D10 (`01_REQUIREMENT_TRACE.md` §E–F); [49] Jia et al. AAAI 2022 (chỉ qua `RQ4_PRIOR_ART` G2-8, `SECONDARY`).
ASSUMPTIONS: không có đặc tả DoP ⇒ DoP chỉ được mô hình như hộp đen với *tính chất phát hiện* ghi ở H-audit (§6); không giả định độc lập; mọi số ví dụ (K=5, f=0,2…) là **minh họa**, không phải giá trị khóa.
OPEN QUESTIONS: Q-G2-1 (cách đọc "tỷ lệ lật vượt f", §3); Q-G2-2 (DoP có cờ bền không, có xóa dòng cũ khi bị cờ không, §5.3); đặc tả DoP.
DECISION: **Mệnh đề 2 như phát biểu: `ASSUMPTION GAP / COUNTEREXAMPLE`** cho bước `m·s → m·f·s` ở cách đọc tự nhiên (R1). Chặn quota `min(k, m·s)` **PROVED**. Công thức `(1−β)^m` **không suy ra được** từ giả định biên; union bound `1−mβ` PROVED. Mệnh đề thay thế 2′ = `CANDIDATE / REQUIRES PROPOSAL APPROVAL`. Đề cương: NO CHANGE NOW.

Nhãn: `PROVED` (chứng minh trong tệp này) · `COUNTEREXAMPLE` (phản ví dụ tường minh) · `SL` suy luận · `CXM` chưa xác minh · `CANDIDATE`.

---

## 0. Bảng kết luận

| Mục | Khẳng định | Kết luận |
|---|---|---|
| Q | `#dòng nguồn bị chiếm trong C_t ≤ min(k, m·s)` | **PROVED** (Bổ đề 1) |
| F-R1 | `#dòng độc ≤ m·f·s`, khi "tỷ lệ lật" đo trên nhãn của nguồn trong ngày | **COUNTEREXAMPLE** (§4, C-A…C-D) |
| F-R2 | cùng khẳng định, khi "tỷ lệ lật" đo trên chính các dòng được nạp | PROVED nhưng **hầu như đồng nhất với kết luận**; đòi hỏi kiểm toán trên tập được nạp (§6, Định lý 1) |
| P | xác suất ≥ `(1−β)^{m_max}` | **không suy ra được** từ giả định biên (Bổ đề 2); union bound `≥ 1 − m_maxβ` PROVED; thêm lũy thừa theo ngày (§5) |
| K | bảo đảm kNN | PROVED dạng "tập dòng cố định, chỉ lật nhãn" (Bổ đề 3); **chân không về thực hành** ở k=2000 (§8); không áp dụng cho TabFM |
| C | "đúng khi phối hợp vì s áp cho từng nguồn" | đúng cho quota `m·s`, **không** cho `m·f·s` (§9) |
| f*, β ↔ power | — | **HOLD_PROOF_SOURCE** |
| 2′ | mệnh đề thay thế | `CANDIDATE / REQUIRES PROPOSAL APPROVAL` (§7) |

---

## 1. Phát biểu đang kiểm (rút từ v14.3, giữ nguyên ý)

Giả sử chính sách nạp giới hạn mỗi nguồn ≤ `s` dòng trong ngữ cảnh, và kiểm toán nguồn phát hiện nguồn có tỷ lệ lật nhãn vượt `f` với xác suất ≥ `1−β`. Khi đó với xác suất ≥ `(1−β)^{m_max}`, đối thủ muốn không bị phát hiện chỉ đưa được ≤ `m_max·f*·s` dòng độc, tức `ρ ≤ m_max f* s / k` (2-8). Với `s = k/K`: `ρ ≤ (m_max/K)·f < f*/2`.

Tách thành năm khẳng định: **Q** (quota), **F** (hệ số `f`), **P** (xác suất), **K** (kNN), **C** (phối hợp).

Kiểm số học cuối: `ρ ≤ m f* (k/K)/k = (m/K) f*`; vì `m < K/2` ⇒ `< f*/2` (cần `f* > 0`). Đúng (SL, tính trực tiếp). Chỉ ghi: tử số dùng `f`, mẫu `f*` (N-1).

## 2. Q — chặn quota (PROVED)

**Bổ đề 1.** Gọi `C_t` là ngữ cảnh, `|C_t| ≤ k`; `C_{t,j}` các dòng của nguồn `j` trong `C_t` với `|C_{t,j}| ≤ s` mọi `j`, mọi `t`. Tập nguồn bị chiếm `A`, `|A| = m`. Tập dòng độc (nhãn trả về ≠ nhãn thật) `Π_t`. Khi đó `Π_t ⊆ ⋃_{j∈A} C_{t,j}` và `|Π_t| ≤ min(k, m s)`.

*Chứng minh.* Đối thủ chỉ đổi nhãn dòng được giao cho nguồn thuộc `A` (ĐN5). Dòng của nguồn không thuộc `A` có nhãn đúng (hoặc nhiễu trung thực, D9=0 mặc định) nên không thuộc `Π_t`. Do đó `Π_t ⊆ ⋃_{j∈A} C_{t,j}`, và `|⋃| ≤ Σ_{j∈A} |C_{t,j}| ≤ m s`. Mặt khác `Π_t ⊆ C_t` nên `|Π_t| ≤ k`. ∎

*Điều kiện thực thi:* quota phải **cưỡng chế trên toàn bộ ngữ cảnh hiện tại** ở mọi thời điểm, kể cả khi dòng cũ vẫn lưu từ ngày trước. v14.3 không nói cách cưỡng chế (dòng nào bị cắt). Đây là hệ quả cho thiết kế, không ảnh hưởng chứng minh.

*Hệ quả:* `ρ ≤ min(1, m s / k)`; với `s = k/K`: `ρ ≤ m/K < 1/2`. **Không có `f`.**

## 3. Hai cách đọc của "nguồn có tỷ lệ lật nhãn vượt f"

- **R1 (tự nhiên với DoP):** tỷ lệ lật = `#nhãn lật / #nhãn nguồn trả trong cùng ngày`. DoP kiểm toán "trong cùng ngày" theo so sánh ngang hàng (v14.3 Nội dung 4), nên mẫu số là nhãn đến trong ngày của nguồn. *Đây là cách đọc dùng cho kết luận chính của §4–§5.*
- **R2:** tỷ lệ lật = `#dòng lật / #dòng` **trong tập dòng của nguồn được nạp vào ngữ cảnh**. Cách đọc này làm `f·s` đúng theo định nghĩa nhưng đòi hỏi kiểm toán nhắm đúng tập đã nạp (kích thước ≤ `s`).

Cần NCS chốt (Q-G2-1). Kết luận của tôi không phụ thuộc chọn ngẫu nhiên: R1 sai (§4), R2 đúng (§6) nhưng là một mệnh đề khác về mặt thiết kế.

## 4. F — phản ví dụ cho bước `m·s → m·f·s` ở R1 (COUNTEREXAMPLE)

Giả định được giữ nguyên (đúng nghĩa của Mệnh đề 2): (a) quota `s`; (b) kiểm toán: với mọi nguồn có tỷ lệ lật **trong ngày** `> f`, bị phát hiện (và loại) với xác suất ≥ `1−β`; (c) nguồn bị cờ không được nạp. Kết luận cần phản bác: `|Π_t| ≤ m f s` (với xác suất cao).

**C-A (chọn lọc, một ngày).** Một nguồn có `n` nhãn trong ngày, lật `λ` dòng với `λ/n ≤ f`. Giả định (b) không áp đặt gì (tỷ lệ ≤ f). Chính sách nạp chọn **đúng** `λ` dòng lật (đủ nếu `λ ≤ s`). Khi đó `|Π_t ∩ C_{t,j}| = λ`. Với `λ = s`: `s > f s`. Vi phạm với xác suất 1 (không phải xác suất nhỏ).
*Ví dụ số hồ sơ:* `n = 1000`, `λ = s = 10`, `f = 0,2`: `10 > f s = 2`. Tôi kiểm lại: tỷ lệ 1% ≤ 20% nên không bắt buộc bị phát hiện; quota thỏa; kết luận sai. (Lưu ý `n = 1000/nguồn/ngày` lớn hơn `(1−η)b/K` của lưới D14, xem C-B cho tham số trong lưới.)

**C-B (tích lũy theo ngày, bám đúng kiểu tấn công (iv)).** Tham số trong lưới D14, minh họa: `K = 5`, `b = 1000`, `η = 0,2` ⇒ `n ≈ 160` nhãn/nguồn/ngày; `k = 2000`, `s = k/K = 400`; `f = 0,2`. Đối thủ (iv) mỗi ngày lật `λ_d = ⌊f n⌋ − δ ≈ 31` dòng họ mục tiêu — dưới ngưỡng mỗi ngày nên (b) không áp đặt. Giả sử chính sách **giữ lại ưu tiên dòng lật** (retention phụ thuộc nhãn; HB2 là ứng viên, §SL dưới). Sau `⌈s/λ_d⌉ = 13` ngày (**[ĐÍNH CHÍNH E1]** nếu kiểm toán thấy `n = b/K = 200` thì `λ_d ≈ 39` và `≈ 11` ngày — khớp "~10–13 ngày" của `THESIS_AUDIT_LOG` §3; kết luận định tính không đổi), tập dòng lật tích lũy ≥ `s`, nên `|Π_t ∩ C_{t,j}| = s = 400`, tức nguồn đó **chiếm 100% hạn mức `s`**, trong khi `m f s` cho `m=2`: `160`. Thực tế: `|Π_t| = m s = 800 = 40%` của `k`, so với `ρ ≤ 8%` theo (2-8).
*Chứng minh (tồn tại):* giả định Mệnh đề 2 chỉ ràng buộc quota và phát hiện; không ràng buộc *cách chọn dòng giữ lại*. Chọn chính sách "giữ lại dòng có cờ lật" thỏa mọi giả định (nó chỉ là một chính sách nạp hợp lệ theo quota) nhưng cho kết quả `|Π_t| = min(s, tích lũy)`. ∎ Chính sách này không thực thi được (cần oracle), vì vậy phần dưới nói về chính sách thực thi được.
**SL — chính sách thực thi được cũng vi phạm:** HB2 giữ nhãn benign có điểm tấn công cao (DC-2, S9 §8). Dòng bị lật bởi (ii)/(iv) có đặc trưng tấn công (đặc trưng không đổi) và nhãn benign; nếu mô hình chấm chúng cao thì chúng thuộc nhóm ưu tiên giữ. Mức vi phạm thực tế phụ thuộc điểm số — **chưa kiểm**, cần P4c/DEV; ở đây chỉ chứng minh rằng Mệnh đề 2 không loại trừ.

**C-C (chính sách cân bằng họ).** CBRS_FAMILY giữ họ hiếm vượt tỷ lệ của luồng (RQ2). Nếu họ mục tiêu chiếm 1% nhãn ngày của nguồn, lật 100% các dòng họ này cho tỷ lệ lật ngày 1% (< `f`), nhưng nếu bộ đệm giữ họ đó với hạn mức cố định `q`, thì **100%** dòng họ đó trong ngữ cảnh là độc. Cùng cấu trúc với C-A (mẫu số khác tập được nạp). *(SL; mức độ phụ thuộc cấu hình CBRS_FAMILY chưa kiểm.)*

**C-D (thời gian, bổ sung).** Xem §5.3: nếu cờ không bền hoặc dòng cũ của nguồn vừa bị cờ không bị xóa, cũng vi phạm.

**Kết luận F.** Với R1, Mệnh đề 2 như phát biểu **không suy ra** `m f s`; thiếu giả định về (i) mẫu số của audit = tập được nạp, hoặc (ii) retention không phụ thuộc nhãn/cờ lật, hoặc (iii) cap ở mức eligible-pool (xem 2′).

## 5. P — xác suất

### 5.1 Tích `(1−β)^m` cần độc lập

**Bổ đề 2 (union bound, PROVED).** Gọi `E_j` = "nguồn `j ∈ A` hoặc không vượt `f`, hoặc bị phát hiện", với `P(E_j) ≥ 1−β`. Khi đó `P(⋂_{j∈A} E_j) ≥ 1 − mβ ≥ 1 − m_maxβ`.
*Chứng minh.* `P(⋃ E_j^c) ≤ Σ P(E_j^c) ≤ mβ`. ∎ Không dùng độc lập.

**Phản ví dụ cho `(1−β)^m` (COUNTEREXAMPLE).** Bernoulli: `(1−β)^m ≥ 1−mβ`, bằng nhau chỉ khi `m=1`. Xây dựng `m=2`, `β ≤ 1/2`: một bộ phát hiện tung đồng xu `c ~ U[0,1]`; nếu `c < β` bỏ sót nguồn 1; nếu `β ≤ c < 2β` bỏ sót nguồn 2; ngược lại bắt cả hai. Cận biên: `P(E_1) = P(E_2) = 1−β` — **thỏa giả định biên**. Nhưng `P(E_1 ∩ E_2) = 1 − 2β < (1−β)² = 1 − 2β + β²` (với `β > 0`). Ví dụ `β = 0,1`: `0,80 < 0,81`. Vậy **công thức `(1−β)^{m_max}` không suy ra được từ giả định biên**; nó đúng nếu thêm giả định độc lập (hoặc kết hợp dương). ∎ (Có thể DoP thỏa độc lập hoặc kết hợp dương; **không biết** vì DoP MISSING ⇒ HOLD.)

### 5.2 Phụ thuộc thực tế (SL)

Hai nguồn trong cùng ngày dùng **cùng tham chiếu ngang hàng** (đồng nghiệp trung thực chung) nên sự kiện phát hiện nhìn chung không độc lập; dưới đồng mưu (vi) thì phụ thuộc có chủ đích. Cũng tồn tại tình huống đối thủ thích nghi chọn `φ_j` sau khi quan sát kết quả cũ (F1) — bảo đảm phải ở dạng *có điều kiện trên lịch sử*.

### 5.3 Phạm vi thời gian (nhiều ngày)

Ngữ cảnh chứa dòng từ nhiều ngày; sự kiện phát hiện `1−β` là **mỗi lần kiểm toán**. Cần thêm:
- **Cờ bền + xóa dòng cũ khi bị cờ (persistence + purge).** Khi đó sự kiện xấu ⊆ "lô đầu tiên có tỷ lệ lật `> f` bị bỏ sót" ⇒ `P ≤ β` mỗi nguồn ⇒ tổng `≤ mβ` (union). Nhưng: cờ bền loại vĩnh viễn nguồn trung thực bị cờ oan, mâu thuẫn mục tiêu RQ4 ("không loại nhầm nguồn trung thực") nếu FPR > 0.
- **Cờ không bền (kiểm toán độc lập từng ngày).** Đối thủ gửi lô có `φ > f` mỗi ngày; mỗi lô bị bỏ sót với xác suất ~`β`. Số lô bị bỏ sót trong cửa sổ `W` ngày: kỳ vọng `Wβ`. Xác suất không có lô xấu nào lọt: `≥ 1 − mWβ` (union), hoặc `(1−β)^{mW}` nếu độc lập — **không phải** `(1−β)^m`. Ví dụ `m = 2, W = 13, β = 0,1`: `1 − 2·13·0,1 < 0` ⇒ vô nghĩa; để đạt xác suất `0,9` cần `β' ≤ 0,1/26 ≈ 0,0038` cho từng lô.
- **Không xóa dòng cũ khi nguồn bị cờ:** dòng nạp trước đó vẫn ở trong ngữ cảnh; bảo đảm mất hiệu lực với phần đó.

Câu hỏi Q-G2-2: DoP/ pipeline có cờ bền và có xóa dòng cũ không? v14.3 không nói.

## 6. Định lý 1 (cách đọc R2, giả định gốc được làm chính xác) — PROVED

**Giả định H-R2.** Với mọi nguồn `j` và ngày `t`, trên sự kiện `E` (xác suất ≥ `1 − mβ`, §5): nếu `j` không bị cờ thì tập dòng của `j` đang trong ngữ cảnh có tỷ lệ lật `≤ f`: `|Π_t ∩ C_{t,j}| ≤ f |C_{t,j}|`.
**Kết luận.** Trên `E`: `|Π_t| ≤ Σ_{j∈A, chưa cờ} f|C_{t,j}| ≤ m f s`, và `ρ ≤ m f s / k`.
*Chứng minh.* Nguồn bị cờ không đóng góp (không được nạp, và dòng cũ bị xóa — xem §5.3). Cộng theo `j ∈ A` và dùng `|C_{t,j}| ≤ s`. ∎

Nhận xét: Định lý 1 chỉ đẹp nếu H-R2 được *bảo đảm bởi kiểm toán nhắm vào tập được nạp*; cái bảo đảm đó chính là điều kiện cần của kết luận, nên Mệnh đề 2 theo R2 là một cách gói gọn giả định chứ không phải sự suy ra.

## 7. Mệnh đề thay thế 2′ — `CANDIDATE / REQUIRES PROPOSAL APPROVAL`

Mục tiêu: đưa `f` vào bằng giả định **kiểm tra được ở mức thiết kế**, tách khỏi retention.

**Cấu trúc (giả định thiết kế, M1–M4).**
- **M1 (cap ở tầng eligible).** Mỗi nguồn `j` có *tập đủ điều kiện* `P_{t,j}`: gộp các lô nguyên vẹn gần nhất của `j` đã được chấp nhận, tổng `|P_{t,j}| ≤ s` (đuổi lô cũ theo tuổi, không theo nhãn). Ngữ cảnh `C_t ⊆ ⋃_j P_{t,j} ∪ (nguồn khác, §Hệ quả b)`. Retention (HB2, v.v.) **được phép phụ thuộc nhãn và điểm số**.
- **M2 (kiểm toán lô).** Với mỗi lô `B_{j,d}` (nhãn đến của `j` ngày `d`), tồn tại sự kiện chấp nhận/loại. Giả định audit (H-audit): với mọi chiến lược (có thể thích nghi) của đối thủ, xác suất (có điều kiện trên lịch sử) lô đầu tiên có số nhãn lật `> f|B_{j,d}|` được **chấp nhận** `≤ β'`.
- **M3 (cờ bền + xóa).** Một lô bị loại do audit ⇒ `j` bị cờ. Khi `j` bị cờ: `P_{t,j} = ∅` cho mọi `t` sau, kể cả dòng cũ.
- **M4 (không phụ thuộc đặc biệt giữa các nguồn).** Chỉ dùng union bound.

**Mệnh đề 2′.** Gọi `A_aud` các nguồn bị chiếm mà lô được kiểm toán đủ điều kiện M2, `A_unc = A ∖ A_aud` (ví dụ nguồn `UNCERTAIN` dưới U1 hoặc mẫu quá nhỏ để audit). Khi đó
(a) Với mọi `t`, mọi chính sách: `|Π_t| ≤ min(k, m s)` (Bổ đề 1).
(b) Với xác suất ≥ `1 − |A_aud| β'`, đồng thời mọi `t`: `|Π_t| ≤ |A_aud|·⌊f s⌋ + |A_unc|·s`; `ρ ≤ (|A_aud| f s + |A_unc| s)/k`.

*Chứng minh.* Trên sự kiện `E` = "mọi nguồn `j ∈ A_aud` không có lô xấu nào được chấp nhận": vì M3, `E^c ⊆ ⋃_j {lô xấu đầu tiên của j được chấp nhận}`; mỗi sự kiện có xác suất ≤ `β'` (M2) ⇒ `P(E^c) ≤ |A_aud| β'` (union). Trên `E` mọi lô trong `P_{t,j}` có số lật `≤ f |B|`; cộng: `flips(P_{t,j}) ≤ f Σ|B| ≤ f s`, nguyên ⇒ `≤ ⌊f s⌋`. Dòng lật trong `C_t` thuộc `⋃ P_{t,j}`, bất kể retention (retention chỉ chọn tập con) ⇒ `|Π_t ∩ C_{t,j}| ≤ flips(P_{t,j})`. Với `A_unc`, chỉ còn Bổ đề 1: `≤ s` mỗi nguồn. Cộng lại. ∎ (E không phụ thuộc `t` ⇒ đồng thời mọi `t`.)

**Hệ quả 2′-b (rất quan trọng với D8).** Dưới U1, nguồn `UNCERTAIN` (chế độ B) **không có bảo đảm `f`**: mỗi nguồn bị chiếm mà `UNCERTAIN` đóng góp tới `s` dòng. Mệnh đề thu về chặn quota `m s` ở chế độ B nếu mọi nguồn bị chiếm rơi vào `UNCERTAIN`. Kết quả đối nghịch (U2: giữ dòng của nguồn `UNCERTAIN`) làm `A_unc` rỗng nhưng loại luôn dòng sạch của nguồn trung thực khác phân phối (coverage thấp).

**Giả định tối thiểu và giới hạn (không ẩn).**
1. M1 yêu cầu đổi thiết kế nạp (tầng eligible, đuổi theo tuổi, không theo nhãn). Đây là **thay đổi so với v14.3** ("chính sách nạp giới hạn s") — ĐX, chưa duyệt.
2. M2 là điều kiện lên DoP (HOLD): audit phải có công suất ở cỡ lô `n ≈ b/K` (**[ĐÍNH CHÍNH E1]**; ≈20 khi `b=100, K=5`; ≈200 khi `b=1000`; bản đầu ghi `(1−η)b/K`: 16 và 160). Ở lô nhỏ, ngưỡng `f` thấp hơn độ phân giải thống kê là không phát hiện được ⇒ `f` phải ≥ `f_min(n, β')` (đây chính là việc `f*` phụ thuộc `n`; HOLD).
3. M3 mâu thuẫn một phần mục tiêu "không loại nhầm" (cờ bền).
4. Xác suất `1 − |A_aud|β'` (không phải `(1−β)^m`) và `β'` là của *lô*.
5. Hiệu lực với đối thủ (iv): chặn `f s` mỗi nguồn là **kết quả đúng** cho (iv) (đối thủ ở ngay dưới ngưỡng); không phải bảo đảm tổn hại nhỏ — `ρ ≤ (m/K) f` có thể vẫn lớn (ví dụ `K=5,m=2,f=0,2`: `ρ ≤ 0,08`).

**Ảnh hưởng đến H4b (SL).** H4b không đòi hỏi Mệnh đề 2; 2′ chỉ là bảo đảm lý thuyết phụ trợ. Nếu 2′ không được duyệt, H4a/H4b vẫn kiểm định thực nghiệm; Mệnh đề 2 trở thành chỉ chặn quota (Bổ đề 1).

**Novelty check sơ bộ (không phải kết luận).** 2′ là lập luận đếm (counting) kèm union bound. Rất ít giá trị toán mới; giá trị nếu có nằm ở yêu cầu thiết kế (audit tập được nạp, cap eligible-pool, retention không giảm bảo đảm). Cần G3 đối chiếu với tài liệu Byzantine-robust và "poisoning with bounded sources". `đúng toán học` ≠ `mới` ≠ `đủ chuẩn đóng góp luận án`.

## 8. K — bảo đảm kNN

**Bổ đề 3 (PROVED, dạng tập dòng cố định).** Cho tập láng giềng `N(x)` gồm `κ` dòng, xác định chỉ bởi đặc trưng (không đổi dưới ĐN5), phiếu `v_c` = số láng giềng nhãn `c` (nhãn trả về). Quy tắc dự đoán: lớp có phiếu cao nhất; hòa thì lớp chỉ số nhỏ hơn. Dự đoán sạch là `a`, đối thủ lật nhãn `e` láng giềng. Với lớp cạnh tranh `b ≠ a`, chênh `d = v_a − v_b`. Dự đoán vẫn là `a` với mọi cách lật `e` nếu và chỉ nếu với mọi `b`: `2e < d` hoặc (`2e = d` và `a < b`), tức `e ≤ ⌈(d + 𝟙[a<b])/2⌉ − 1`.
*Chứng minh.* Mỗi nhãn lật chuyển nhiều nhất một phiếu từ `a` sang một lớp khác: đổi `d` đi tối đa 2 cho mỗi dòng lật; tệ nhất chuyển hết sang lớp `b` có `v_b` cao nhất. Sau `e` lần: `v_a − e` và `v_b + e`; `a` thắng nếu `v_a − e > v_b + e` hoặc bằng và `a<b`. Biến đổi cho điều kiện trên. ∎ (Khớp với dạng công thức của [49] theo `SECONDARY`; **quy ước tie-break và chỉ số `I(a>b)` của [49] phải kiểm ở G3.**)

Lưu ý cho v14.3: câu "`m_max f* s` < một nửa chênh lệch phiếu" là **điều kiện đủ** hợp lệ: số dòng lật nằm trong `N(x)` thỏa `e_N ≤ min(κ, |Π_t|)`, nên nếu `|Π_t| ≤ m_max f* s` (cần Mệnh đề 2, vốn chưa được chứng minh ở R1) thì Bổ đề 3 áp dụng với `e = m_max f* s`. Các hạn chế:

1. **Hiệu lực chỉ khi tập dòng cố định.** Trong pipeline, ngữ cảnh `C_t` phụ thuộc nhãn (HB2 chọn theo điểm; tầng dòng lọc theo `I_i`; điểm số phụ thuộc ngữ cảnh trước). Do đó dòng độc có thể *thay thế* dòng sạch, ảnh hưởng ngoài "lật nhãn trên cùng tập". Bổ đề 3 là cho tập cố định; phiên bản động cần đếm khoảng cách giữa `C_t` thật và `C_t` sạch (bao gồm hiệu ứng dây chuyền) — **OPEN**.
2. **Chân không về số học (SL, tính tay).** `k = 2000, K = 5, m = 2, s = 400, f = 0,2` ⇒ `m f s = 160`. Muốn đảm bảo cần `2·160 = 320 < d ≤ κ` ⇒ `κ ≥ 321` láng giềng. Với `κ` điển hình nhỏ (≈ vài chục) chứng nhận **không bao giờ kích hoạt** nếu dùng cận toàn cục `m f s`; muốn có ý nghĩa cần cận *cục bộ* theo vùng của `x`, mà cận toàn cục không cung cấp. Họ mục tiêu thường tụ thành cụm nên chính các dòng độc dồn trong `N(x)` của dòng thuộc họ mục tiêu.
3. **TFM/LoCalPFN không được chứng nhận.** Chứng nhận áp dụng cho bộ dự đoán kNN thay thế. LoCalPFN truy hồi láng giềng theo đặc trưng (label-independent retrieval — không kiểm lại ở đây, `CXM`), nhưng dự đoán cuối do TabPFN trên tập truy hồi, không phải đa số phiếu. v14.3 đã nói TFM không có bảo đảm tương tự (đúng).
4. Đây là ngoài lề của f*, β: kNN phần chỉ phụ thuộc kết quả Mệnh đề 2 qua `e`.

## 9. C — phối hợp (vi) và chế độ B

- "Chặn trên `m_max f* s` vẫn đúng khi phối hợp vì `s` áp cho từng nguồn": **đúng cho Bổ đề 1** (quota `m s`, không đổi). Phần `f*` không còn bảo đảm: v14.3 tự thừa nhận `f*`, `β` có thể xấu đi. Khi `f*, β` xấu đi, câu "vẫn đúng" trở nên vô nghĩa (đúng với giá trị tồi tùy ý). **Cần tách:** quota (xác định) | phát hiện (xác suất, mất hiệu lực khi phối hợp hoặc khi `m ≥ K/2`).
- Chế độ B + bổ đề không nhận dạng (`02` §4): nguồn có vùng đặc trưng rời nhau không thể phát hiện; M2 không khả thi cho những nguồn đó ⇒ chúng thuộc `A_unc` ⇒ chỉ còn `m s`.
- Union bound (Bổ đề 2) là phù hợp cho phối hợp; không cần giả định nào về phụ thuộc.

## 10. Vòng lặp phụ thuộc `V_t` (D10) — kiểm toán

Theo D10: `V_t`, `D_cal` ← nhãn η·b của **nguồn không bị gắn cờ**; tầng dòng dùng `I_i` trên `V_t`; tầng nguồn quyết định ai được tính.

Phụ thuộc: `tầng nguồn → V_t → I_i → ACCEPT/HOLD → C_t → mô hình → điểm → (D_cal, λ_t)`. Hệ quả (đều SL):

1. **Nguồn bị chiếm lọt vào V_t.** Một nguồn bị chiếm không bị cờ (bị sót với xác suất ≤ `β'`, hoặc `UNCERTAIN` dưới U1) đóng góp nhãn lật vào `V_t` (nếu đối thủ không phân biệt được dòng dành riêng; điều này phụ thuộc giao diện — chưa quy định).
2. **Tín hiệu `I_i` yếu đi theo m/K.** Nếu họ mục tiêu trong `V_t` có tỷ lệ nhãn đúng `q ≈ 1 − m/K` (đối thủ lật 100% họ) thì kỳ vọng ảnh hưởng của dòng độc lên loss tập kiểm ∝ `q·(hại) − (1−q)·(lợi)`, đổi dấu tại `q = 1/2` ⇔ `m = K/2`. Dưới `m < K/2` dấu đúng nhưng độ lớn co lại theo `(1 − 2m/K)`. *(Phỏng đoán đối xứng; cần kiểm bằng DEV, không chứng minh ở đây.)*
3. **D_cal ↔ λ_t.** Nhãn lật attack→benign trong `D_cal` làm đuôi phân phối điểm "benign" nặng hơn ⇒ `λ_t` tăng ⇒ FNR toàn cục tăng, **ngay cả khi ngữ cảnh được lọc sạch**. Vì `ASR_raw` đo ở `λ_t`, kênh này tác động độc lập với ngữ cảnh. Phòng thủ tầng nguồn phải bảo vệ `D_cal` (không chỉ `C_t`).
4. **FPR nguồn giảm kích thước V_t.** Nguồn trung thực bị cờ oan bị loại khỏi `V_t`, `V_t` nhỏ, ước lượng `I_i` nhiễu hơn; không tuyến tính theo nhiễu. Vòng phản hồi: `V_t` nghèo ⇒ `I_i` kém ⇒ nhiều dòng sạch bị giữ.
5. **Chưa rõ:** v14.3 viết V_t từ "chuyên viên" (Nội dung 3) lẫn "nguồn không gắn cờ"; D4 đã làm cho "mỗi nguồn = một chuyên viên", nên nhất quán với D10. Nhưng đây là điều kiện mô phỏng chứ không phải dữ kiện nào chống lại việc đối thủ lật nhãn trong tập dành riêng. **Cần NCS quyết (Q-G2-3):** có giả định nhãn dành riêng η·b của nguồn bị chiếm cũng bị lật (bảo thủ) hay không bị lật (tập dành riêng độc lập)? D10 hàm ý có thể bị lật (nguồn bị chiếm lật mọi dòng thuộc họ mục tiêu mà nó nhìn thấy).

## 11. Đầu ra bắt buộc của G2 (hồ sơ §3.4)

- (B) **Phản ví dụ + mệnh đề thay thế:** C-A…C-D (§4); 2′ = `CANDIDATE / REQUIRES PROPOSAL APPROVAL` (§7) với proof, giả định tối thiểu, giới hạn và novelty check sơ bộ.
- Chặn quota (A) PROVED cho phần không phụ thuộc DoP.
- `HOLD_PROOF_SOURCE`: liên hệ `f*`, `β` với công suất của DoP; độc lập/phụ thuộc của các sự kiện phát hiện; cờ bền hay không.

| Item | Trạng thái |
|---|---|
| Proposition 2 | `COUNTEREXAMPLE/ASSUMPTION GAP/HOLD` (R1); quota PROVED |
| H4a, H4b | NO CONCLUSION |
| Đề cương | NO CHANGE NOW; 2′ chỉ là phương án |

## 12. Việc cần NCS quyết trước G3/G4

- **Q-G2-1** Cách đọc "tỷ lệ lật vượt f": R1 hay R2?
- **Q-G2-2** Cờ có bền và có xóa dòng cũ khi nguồn bị cờ không?
- **Q-G2-3** Nhãn η·b dành riêng của nguồn bị chiếm có bị lật không (vai trò V_t, D_cal)?
- Đặc tả DoP (để mở HOLD).

---

## 13. Giải quyết sau duyệt G2 (D15–D17, `01_REQUIREMENT_TRACE.md` §G)

- Q-G2-1 → **R1**. Hệ quả: kết luận `ASSUMPTION GAP / COUNTEREXAMPLE` giữ nguyên; §6 (R2) chỉ là đối chiếu.
- Q-G2-2 → cờ bền + giữ hồi tố là **PROPOSAL** chính (khớp M3 của 2′). Hệ quả đã ghi: ràng buộc FPR nguồn nặng hơn vì cờ oan loại vĩnh viễn một nguồn trung thực; cần khóa quy tắc "xác minh" trong prereg. Xung đột với A4 của Mệnh đề 1 (RQ2): hồi tố nghĩa là gỡ dòng đã nạp khỏi ngữ cảnh RQ2; giữ `OPEN` theo T2.
- Q-G2-3 → bảo thủ (D17): `V_t`, `D_cal` bao gồm nhãn lật của nguồn bị chiếm chưa bị cờ. Phân tích §10 mục 1–3 áp dụng ở dạng xấu nhất.
