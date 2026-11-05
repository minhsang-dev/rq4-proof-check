# Báo cáo ghi nhận: HB2–TabFM (RQ2/H2), phiên FIX01

Nguồn số liệu: gói `sessions/55e5…/` (RESULTS.md, decision.json, root_results.json, paired_seed_results.json, identity_test.json, budget_arithmetic.json, final_state.json). Mọi số dưới đây đã được đối chiếu với các file này.

## 1. Kết luận một câu

Thí nghiệm **chạy đúng, đủ và tái lập được** (72/72 ô, 0 ô thiếu, kiểm danh tính điểm số PASS byte-for-byte). Kết quả khoa học: **HB2 cho M1 dương ở cả 3 root đánh giá được nhưng nhỏ hơn biên ε₂ = 0,03 khoảng 10 lần, và không nhất quán so với HB_RANDOM; do đó `HB2_TABFM_STATUS = NOT_SUPPORTED` và `H2 = NOT_ESTABLISHED`.** Đây là kết quả âm/chưa đủ bằng chứng được ghi nhận đúng quy tắc, không phải một lần chạy hỏng.

## 2. Vì sao đây không phải "thất bại thực hiện"

| Tiêu chí | Bằng chứng |
|---|---|
| Hoàn tất đầy đủ | `planned_cells = completed_cells = 72`, `missing_cells = 0`, `final_state.status = COMPLETE`, `error = null` |
| Tái lập | `identity_test`: PASS, `exact_score_bytes_equal = true`, 0 hàng lệch (SHA-256 khớp); không dùng dung sai xấp xỉ |
| Kỷ luật ngân sách | 177,44 + 18.825,13 = 19.002,57 s; còn 26.485,24 s (≈ 7 h 21 ph) trên trần 45.487,81 s; số học đã kiểm lại |
| Quy tắc quyết định có trước | trạng thái sinh ra từ `decision.json` theo quy tắc khóa, không chọn sau khi thấy số |
| Không có hại | cờ `harm = false` ở cả 3 root đánh giá được; `overall_delta` ≈ 0 (−1,3·10⁻⁴; +3,1·10⁻⁴; −2·10⁻⁵) |

## 3. Vì sao không lệch đề cương

1. **Đúng giả thuyết và biên đã đăng ký.** H2 (v14.3) yêu cầu hơn CURE và bộ đệm cân bằng lớp **ít nhất ε₂ = 0,03 AUPRC**, trên TabFM. Phép đo ở đây là HB2 − CBRS-family (một đối chứng trong H2) với cùng ε₂; `epsilon_2_vs_CBRS_FAMILY_observed = False`.
2. **Đề cương đã nói trước cách xử lý.** "Không nới biên"; nếu công suất thấp thì bổ sung ngày gốc, không giảm ε. Báo cáo này **không** hạ ε₂ để cho kết quả "đạt", và coi chuẩn mức trần (CEILING) là hạn chế của dữ liệu, không phải lý do đổi chuẩn.
3. **Đúng khung suy luận của đề cương.** Đề cương nêu cỡ mẫu hiệu dụng ≈ số ngày gốc, các tình huống cùng ngày gốc không độc lập. Báo cáo nói đúng điều đó: 7 root CIDDS là *một môi trường*, chỉ 3 root đánh giá được, 3 seed mỗi root; kết luận chỉ là mô tả.
4. **Phạm vi H2 giữ nguyên.** CURE chưa chạy (`untested_comparators`), nhiễu nhãn 10 % chưa kiểm (`NOT_TESTED`), kết quả TabPFN-2.5 là kiểm tra độ vững chưa báo cáo ở đây. Do đó H2 ở mức tối đa PARTIAL, khớp trạng thái `NOT_ESTABLISHED`.
5. **H2 không phụ thuộc kết quả này để đề cương đứng được.** Đề cương tách H1/H2/H3/H4 và cho phép từng giả thuyết được báo cáo riêng; một H2 âm không làm vô hiệu RQ3, RQ4. Kết quả LightGBM SUPPORTED_ONE (ngoài gói này, chưa kiểm) được giữ riêng.

## 4. Số liệu chính (CIDDS-001, 3 root đánh giá được)

| Root | M1 = HB2 − CBRS-family | A1 = HB2 − HB_RANDOM | Ghi chú |
|---|---|---|---|
| 03-15 | +0,00301 (3/3 seed dương) | −0,00165 (0/3 dương) | HB_RANDOM cao hơn HB2 |
| 03-20 | +0,00405 (3/3) | +0,00272 (3/3) | tốt nhất |
| 03-24 | +0,00269 (2/3) | −0,00032 (1/3) | HB_RANDOM cao hơn HB2 |
| Trung vị M1 | **+0,00301** | không nhất quán | ε₂ = 0,03 |

4/7 root CIDDS (03-16, 03-17, 03-21, 03-23) và UNSW (01-22) ở mức trần: AP đã ≥ 0,99, không còn khoảng để phân biệt; chúng **không** là bằng chứng hỗ trợ cũng **không** là bằng chứng chống.

## 5. Câu nên và không nên viết trong luận án

**Nên viết**
- "Trên TabFM, HB2 cho cải thiện nhỏ nhưng cùng chiều so với CBRS-family ở cả 3 root đánh giá được (trung vị +0,0030 AUPRC), thấp hơn nhiều so với biên ε₂ = 0,03; do đó H2 chưa được xác lập."
- "Hầu hết các root nằm ở mức trần nên thí nghiệm này có công suất hạn chế để phân biệt các chính sách; các root đó không được tính là bằng chứng."
- "So với chọn ngẫu nhiên trong ngăn (HB_RANDOM), lợi ích của HB2 không nhất quán."
- "Kết quả mô tả, trên một môi trường (CIDDS-001); CURE và nhiễu nhãn 10 % chưa được kiểm, nên phát biểu đầy đủ của H2 chưa được đánh giá."
- Định hướng tiếp theo, đúng quy tắc đề cương: thêm ngày gốc/bộ dữ liệu có khoảng cải thiện (không trần) và chạy CURE + nhiễu 10 %, không đổi ε₂.

**Không nên viết**
- "HB2 không chuyển sang TabFM" hoặc "HB2 vô dụng trên TabFM" (4/7 root không có thông tin; chỉ 3 root, 3 seed).
- "Cải thiện có ý nghĩa" hoặc "xu hướng tích cực đã được xác nhận" (không có kiểm định, 3/3 là đếm dấu trên 3 root tương quan).
- "7 root xác nhận…" (một môi trường).
- Bất kỳ so sánh vượt CURE hoặc chính sách chưa chạy.
- Hạ ε₂ hoặc đổi định nghĩa M1/trần sau khi thấy kết quả để chuyển trạng thái thành SUPPORTED.

## 6. Tác động tới phần còn lại của đề cương

- **Giữ nguyên:** hướng nghiên cứu RQ2 (chính sách ba ngăn), vì kết quả âm ở H2/TabFM không phủ định HB2 trên LightGBM, và nó chỉ ra giới hạn cụ thể: khoảng cải thiện bị chặn bởi mức trần của dữ liệu.
- **Giá trị khoa học được ghi nhận:** (i) một đánh giá phản chứng công khai có quy tắc quyết định khóa trước; (ii) bằng chứng rằng lợi ích đo trên LightGBM chưa chuyển sang TabFM ở biên 0,03; (iii) chỉ ra cần bộ dữ liệu/tình huống ít bão hòa hơn để đủ công suất.
- **Việc còn lại, theo thứ tự ưu tiên:** CURE; nhiễu nhãn 10 %; thêm ngày gốc không bão hòa; TabPFN-2.5 như kiểm tra độ vững. Ngân sách còn 26.485,24 s theo sổ ngân sách dự án (không phải CU Google trừ).

## 7. Hạn chế của chính báo cáo này

Tôi chỉ kiểm lại các file trong gói đã nhận: bảng kết quả, số học ngân sách, kiểm danh tính. Chưa kiểm `OUTPUT_SHA256.json` với từng file, không chạy lại thí nghiệm, không có kết quả LightGBM SUPPORTED_ONE và không có quy tắc quyết định gốc; khẳng định "quy tắc có trước" dựa vào nội dung `decision.json` và `identity_rule`, chưa đối chiếu bản đăng ký.
