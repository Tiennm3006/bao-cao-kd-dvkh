# Bộ Prompt Đánh giá/Nhận xét theo từng Sheet — Dashboard KD-DVKH

Mục tiêu: mỗi tuần, khi có file `KD-SO_LIEU_KD-DVKH_TUAN_xx.xlsx` mới, dùng đúng prompt tương ứng với từng sheet (dán kèm bảng số liệu của sheet đó, hoặc để AI tự đọc file) để tạo ra phần "Đánh giá/Nhận xét" **bám sát số liệu thật**, đúng văn phong báo cáo PKD, thay vì nhận xét chung chung.

## Cách dùng
1. Chọn prompt đúng với sheet đang cần đánh giá.
2. Dán bảng dữ liệu của sheet đó (copy từ Excel) vào chỗ `[DÁN DỮ LIỆU SHEET TẠI ĐÂY]`, hoặc đính kèm file Excel và ghi rõ "dùng sheet ...".
3. Nếu có số liệu tuần trước (để so sánh xu hướng), dán thêm vào `[DÁN SỐ LIỆU TUẦN TRƯỚC — nếu có]`.
4. Chạy prompt → dán kết quả vào ô "Đánh giá/Nhận xét" tương ứng trên Dashboard.

## Khung chung (nguyên tắc bắt buộc cho mọi prompt)
Mỗi đánh giá phải:
- Nêu **số liệu tổng hợp cụ thể** (tổng số, %, số tiền...), không nói chung chung kiểu "tình hình ổn định".
- **Chỉ đích danh đơn vị/Điện lực** có số liệu tốt nhất và kém nhất (kèm con số).
- **So sánh với kế hoạch/ngưỡng quy định/tuần trước** khi có cột tương ứng trong sheet.
- Nêu **nguyên nhân** (nếu sheet có cột nội dung/giải trình) và **đề xuất/kiến nghị** ngắn gọn.
- Độ dài 4–8 câu, văn phong báo cáo hành chính (không markdown, không bullet trừ khi có nhiều đơn vị cần liệt kê).

---

## Sheet 1 — `1CRM`: Phiếu yêu cầu gọi nhiều lần
**Cột dữ liệu:** STT, Mã phiếu, Điện lực, Loại yêu cầu, Ngày tạo, Nội dung giải trình các Điện lực, Đánh giá của PKD Cty (từng phiếu).

**Prompt:**
```
Bạn là chuyên viên Phòng Kinh doanh (PKD) Công ty Điện lực Đồng Nai. Dưới đây là danh sách các phiếu yêu cầu gọi nhiều lần (>=2 lần) phát sinh trong tuần, gồm các cột: Mã phiếu, Điện lực, Loại yêu cầu, Ngày tạo, Nội dung giải trình của Điện lực, Đánh giá của PKD cho từng phiếu.

[DÁN DỮ LIỆU SHEET 1CRM TẠI ĐÂY]

Hãy viết một đoạn ĐÁNH GIÁ TỔNG HỢP TUẦN (không liệt kê lại từng phiếu) gồm:
1. Tổng số phiếu gọi nhiều lần trong tuần, phân theo Điện lực (nêu tên Điện lực có số phiếu nhiều nhất).
2. Phân loại nguyên nhân chính gây phát sinh phiếu lần 2 trở lên (dựa trên cột "Đánh giá của PKD Cty" của từng phiếu — ví dụ: chậm liên hệ khách hàng, chưa cập nhật lịch sử xử lý, hiểu lầm giữa KH và Điện lực...), nêu số lượng phiếu ứng với mỗi nhóm nguyên nhân.
3. So sánh với tuần trước nếu có dữ liệu: [DÁN SỐ LIỆU TUẦN TRƯỚC — nếu có].
4. Kiến nghị cụ thể cho (các) Điện lực có số phiếu/nguyên nhân lặp lại nhiều nhất.
Không bịa số liệu ngoài dữ liệu đã cho.
```

---

## Sheet 2 — `2MATDIENTBACC`: Danh sách trạm mất điện tuần
**Cột dữ liệu:** Điện lực, Mã trạm, Tên trạm, số khách hàng gọi theo từng ngày (11–17/9), Tổng số lần mất điện trong tuần theo CRM, Đối chiếu đo xa (lần 1, 2), Đối chiếu OMS (lần 1, 2).

**Prompt:**
```
Bạn là chuyên viên PKD Công ty Điện lực Đồng Nai. Dưới đây là danh sách trạm biến áp có khách hàng gọi báo mất điện trong tuần, gồm: Điện lực, Mã trạm, Tên trạm, số khách hàng gọi theo từng ngày, Tổng số lần mất điện trong tuần theo CRM, đối chiếu với dữ liệu đo xa và OMS.

[DÁN DỮ LIỆU SHEET 2MATDIENTBACC TẠI ĐÂY]

Viết ĐÁNH GIÁ TỔNG HỢP TUẦN gồm:
1. Tổng số trạm phát sinh khách hàng gọi mất điện, phân bổ theo Điện lực (nêu cụ thể Điện lực có nhiều trạm nhất).
2. Liệt kê các trạm có từ 2 lần mất điện trở lên trong tuần (nêu tên trạm, Điện lực, số lần) — đây là các trạm cần lưu ý theo dõi/kiểm tra kỹ thuật.
3. Đối chiếu tính nhất quán giữa số liệu CRM với đo xa/OMS: nêu rõ các trường hợp "Không có OMS" hoặc lệch thời gian giữa đo xa và OMS — đây là điểm cần làm rõ nguyên nhân kỹ thuật hoặc thiếu dữ liệu giám sát.
4. Kiến nghị: đơn vị nào cần rà soát lưới/chất lượng cung cấp điện do lặp lại sự cố.
Chỉ dùng đúng số liệu trong bảng, không suy diễn thêm.
```

---

## Sheet 3 — `3HAILONGKH`: Khách hàng đánh giá không hài lòng
**Cột dữ liệu:** Mã đơn vị, Điện lực, Mã phiếu, Nội dung ghi nhận, Không hài lòng.

**Prompt:**
```
Bạn là chuyên viên PKD Công ty Điện lực Đồng Nai. Dưới đây là danh sách các phiếu khách hàng đánh giá KHÔNG HÀI LÒNG trong tuần, gồm: Điện lực, Mã phiếu, Nội dung ghi nhận (lý do không hài lòng).

[DÁN DỮ LIỆU SHEET 3HAILONGKH TẠI ĐÂY]

Viết ĐÁNH GIÁ TỔNG HỢP TUẦN gồm:
1. Tổng số phiếu không hài lòng trong tuần, phân theo Điện lực (nêu Điện lực có số phiếu không hài lòng cao nhất và tỷ trọng % trên tổng số).
2. Nhóm các "Nội dung ghi nhận" theo chủ đề lặp lại (ví dụ: thái độ phục vụ, thời gian xử lý chậm, giải quyết chưa thỏa đáng...), nêu số phiếu mỗi nhóm.
3. So sánh với tuần trước nếu có: [DÁN SỐ LIỆU TUẦN TRƯỚC — nếu có], nêu xu hướng tăng/giảm bao nhiêu % hoặc phiếu.
4. Kiến nghị chấn chỉnh cụ thể cho Điện lực/nhóm nguyên nhân nổi cộm nhất.
Không thêm nhận định ngoài dữ liệu cung cấp.
```

---

## Sheet 4 — `4THUTD`: Tỷ lệ thu tiền điện
**Cột dữ liệu:** Tên đơn vị, Phải trả, Phải thu, Phát sinh trong kỳ, Số thu được trong kỳ, Tồn cuối kỳ, Dư nợ hóa đơn phát sinh lập 07 ngày, Dư nợ khách hàng NSNN, Tỷ lệ Thu/phải thu, Kế hoạch, Đánh giá (chênh lệch).

**Prompt:**
```
Bạn là chuyên viên PKD Công ty Điện lực Đồng Nai. Dưới đây là bảng tỷ lệ thu tiền điện theo từng đơn vị, gồm: Tên đơn vị, Phải thu, Phát sinh trong kỳ, Số thu được, Tồn cuối kỳ, Dư nợ hóa đơn ≤7 ngày, Dư nợ khách hàng ngân sách nhà nước, Tỷ lệ Thu/phải thu, Kế hoạch, chênh lệch Đánh giá.

[DÁN DỮ LIỆU SHEET 4THUTD TẠI ĐÂY]

Viết ĐÁNH GIÁ TỔNG HỢP TUẦN/THÁNG gồm:
1. Tỷ lệ thu bình quân toàn Công ty so với kế hoạch chung (nêu % cụ thể, đạt/vượt/chưa đạt bao nhiêu điểm % so với kế hoạch).
2. Nêu đích danh đơn vị có tỷ lệ thu THẤP NHẤT so với kế hoạch (số liệu cụ thể, mức chênh lệch âm) và đơn vị cao nhất.
3. Phân tích cơ cấu tồn cuối kỳ: đơn vị nào có dư nợ hóa đơn mới phát sinh (≤7 ngày) và dư nợ khách hàng ngân sách nhà nước cao bất thường so với tồn cuối kỳ.
4. Kiến nghị đôn đốc thu nợ cho các đơn vị chưa đạt kế hoạch.
Chỉ dùng số liệu trong bảng, trình bày số liệu dưới dạng %, không làm tròn quá mức gây sai lệch.
```

---

## Sheet 5 — `5NONSNN`: Nợ ngân sách nhà nước
**Cột dữ liệu:** Điện lực, HĐ nợ 2025 & số tiền, HĐ T1–T5/2026 & số tiền, HĐ T6/2026 & số tiền, HĐ T7/2026 & số tiền, Tổng HĐ nợ, Tổng tiền nợ.

**Prompt:**
```
Bạn là chuyên viên PKD Công ty Điện lực Đồng Nai. Dưới đây là bảng nợ ngân sách nhà nước theo từng Điện lực, phân theo thời gian phát sinh nợ (2025, T1-T5/2026, T6/2026, T7/2026), kèm tổng số hóa đơn nợ và tổng tiền nợ.

[DÁN DỮ LIỆU SHEET 5NONSNN TẠI ĐÂY]

Viết ĐÁNH GIÁ TỔNG HỢP gồm:
1. Tổng số hóa đơn nợ và tổng số tiền nợ ngân sách nhà nước toàn Công ty tính đến thời điểm báo cáo.
2. Nêu đích danh 2–3 Điện lực có tổng tiền nợ cao nhất (số liệu cụ thể, tỷ trọng % trên tổng nợ toàn Công ty).
3. Phân tích cơ cấu tuổi nợ: nợ tồn từ 2025 (nợ cũ, khó đòi) so với nợ mới phát sinh trong các tháng gần đây (T6, T7/2026) — nêu rõ đơn vị nào có nợ cũ chiếm tỷ trọng lớn cần xử lý dứt điểm.
4. Kiến nghị làm việc với đơn vị sử dụng ngân sách để thu hồi nợ, ưu tiên các khoản nợ cũ.
Chỉ dùng số liệu có trong bảng.
```

---

## Sheet 6 — `6NLMT`: Tiến độ xử lý tồn tại điện mặt trời mái nhà
**Cột dữ liệu:** Điện lực, Số lượng cần xử lý tính đến hết T7-2026, Tiến trình xử lý, Kết quả, Ghi chú.

**Prompt:**
```
Bạn là chuyên viên PKD Công ty Điện lực Đồng Nai. Dưới đây là bảng tiến độ xử lý tồn tại hồ sơ pháp lý điện mặt trời mái nhà (ĐMTMN) theo từng Điện lực: Số lượng cần xử lý, Tiến trình xử lý, Kết quả, Ghi chú.

[DÁN DỮ LIỆU SHEET 6NLMT TẠI ĐÂY]

Viết ĐÁNH GIÁ TỔNG HỢP gồm:
1. Tổng số hồ sơ ĐMTMN còn tồn cần xử lý toàn Công ty, và số hồ sơ đã xử lý xong (theo cột Kết quả) — tính tỷ lệ % hoàn thành.
2. Nêu đích danh Điện lực có số lượng tồn nhiều nhất và Điện lực có tiến độ xử lý chậm nhất (dựa vào cột Tiến trình xử lý/Kết quả/Ghi chú).
3. Tổng hợp nguyên nhân chậm trễ phổ biến từ cột Ghi chú (nếu có).
4. Kiến nghị đôn đốc các Điện lực còn tồn nhiều, gắn mốc thời gian xử lý dứt điểm.
Không suy diễn ngoài dữ liệu, nếu cột Ghi chú trống thì không tự thêm nguyên nhân.
```

---

## Sheet 7 — `7THAYDK`: Thiết bị đo đếm quá hạn
**Cột dữ liệu:** Điện lực, Công tơ 1 pha HKĐ quá hạn, Công tơ 3 pha HKĐ quá hạn, Số trường hợp trở ngại, Tổng cộng công tơ quá hạn, TU HKĐ quá hạn, TI HKĐ quá hạn.

**Prompt:**
```
Bạn là chuyên viên PKD Công ty Điện lực Đồng Nai. Dưới đây là bảng thiết bị đo đếm (công tơ 1 pha, 3 pha, TU, TI) quá hạn hiệu chuẩn/kiểm định (HKĐ) theo từng Điện lực.

[DÁN DỮ LIỆU SHEET 7THAYDK TẠI ĐÂY]

Viết ĐÁNH GIÁ TỔNG HỢP gồm:
1. Tổng số công tơ quá hạn HKĐ toàn Công ty (tách riêng 1 pha và 3 pha), tổng số TU/TI quá hạn.
2. Nêu đích danh Điện lực có số lượng thiết bị quá hạn nhiều nhất (cả về số tuyệt đối), đặc biệt lưu ý công tơ 3 pha và TU/TI vì ảnh hưởng đến khách hàng lớn.
3. Nêu số trường hợp trở ngại (không thay được) và Điện lực có trở ngại nhiều nhất — đây là rủi ro cần theo dõi riêng.
4. Kiến nghị kế hoạch thay thế ưu tiên cho các Điện lực có tồn đọng lớn, đặc biệt nhóm 3 pha/TU/TI (ảnh hưởng doanh thu, tổn thất điện năng).
Chỉ dùng số liệu trong bảng.
```

---

## Sheet 8 — `8DOXA`: Số liệu công tác đo xa
**Cột dữ liệu:** Tên đơn vị, Tỷ lệ thu thập dữ liệu chung (Modem+DCU), Tỷ lệ khai thác công tơ điện tử trên đo xa, Đánh giá tỷ lệ đo xa (ngưỡng tối thiểu 99%), Đánh giá tỷ lệ khai thác CTĐT (ngưỡng tối thiểu 99,5%).

**Prompt:**
```
Bạn là chuyên viên PKD Công ty Điện lực Đồng Nai. Dưới đây là bảng tỷ lệ đo xa theo từng đơn vị: Tỷ lệ thu thập dữ liệu chung (Modem+DCU), Tỷ lệ khai thác công tơ điện tử (CTĐT) trên đo xa, và đánh giá Đạt/Không đạt theo ngưỡng quy định (đo xa ≥99%, khai thác CTĐT ≥99,5%).

[DÁN DỮ LIỆU SHEET 8DOXA TẠI ĐÂY]

Viết ĐÁNH GIÁ TỔNG HỢP gồm:
1. Tỷ lệ đo xa và tỷ lệ khai thác CTĐT bình quân toàn Công ty, so với ngưỡng quy định (99% và 99,5%).
2. Liệt kê đích danh các đơn vị KHÔNG ĐẠT ngưỡng (nêu rõ tỷ lệ thực tế và mức thiếu hụt so với ngưỡng) — đây là phần bắt buộc phải nêu cụ thể tên và số liệu.
3. Nêu đơn vị có tỷ lệ tốt nhất để làm điển hình.
4. Kiến nghị khắc phục cho các đơn vị chưa đạt (kiểm tra hạ tầng thu thập, xử lý sự cố modem/DCU).
Chỉ dùng số liệu trong bảng, không làm tròn sai lệch bản chất Đạt/Không đạt.
```

---

## Sheet 9 — `9TRUYTHU`: Truy thu hư hỏng cháy nổ, trộm cắp điện
**Cột dữ liệu:** Tên đơn vị, Kế hoạch truy thu năm 2026 (sản lượng, thành tiền), Số hóa đơn điều chỉnh truy thu theo độ trễ (≤31 ngày, 32–61 ngày, >62 ngày), Sản lượng/số tiền truy thu thực hiện tuần, So sánh kế hoạch (%) sản lượng và thành tiền.

**Prompt:**
```
Bạn là chuyên viên PKD Công ty Điện lực Đồng Nai. Dưới đây là bảng theo dõi truy thu hư hỏng cháy hỏng và trộm cắp điện tuần, gồm: Kế hoạch truy thu năm 2026, số hóa đơn điều chỉnh (HĐĐC) theo các mốc thời gian trễ (≤31 ngày, 32-61 ngày, >62 ngày), sản lượng/số tiền truy thu thực hiện trong tuần, so sánh % với kế hoạch.

[DÁN DỮ LIỆU SHEET 9TRUYTHU TẠI ĐÂY]

Viết ĐÁNH GIÁ TỔNG HỢP TUẦN gồm:
1. Tổng sản lượng và số tiền truy thu thực hiện trong tuần, tỷ lệ % lũy kế so với kế hoạch năm 2026 toàn Công ty.
2. Nêu đích danh đơn vị có tiến độ truy thu đạt thấp nhất so với kế hoạch (theo %).
3. CẢNH BÁO các đơn vị có số HĐĐC quá hạn xử lý trên 62 ngày (nêu số lượng cụ thể) — đây là chỉ số vi phạm quy định thời gian xử lý, cần nêu rõ.
4. Kiến nghị đẩy nhanh xử lý các hóa đơn tồn đọng quá 62 ngày và đôn đốc đơn vị chưa đạt kế hoạch.
Chỉ dùng số liệu trong bảng.
```

---

## Sheet 10 — `10KTSDĐ`: Kiểm tra sử dụng điện định kỳ
**Cột dữ liệu:** Đơn vị, KH (kế hoạch), Thực hiện tuần, TH lũy kế, Thời gian trung bình thực hiện (phút/công tơ), So sánh TH/KH.

**Prompt:**
```
Bạn là chuyên viên PKD Công ty Điện lực Đồng Nai. Dưới đây là bảng kết quả kiểm tra hệ thống đo đếm (HTĐĐ) định kỳ 1 pha trực tiếp theo từng đơn vị: Kế hoạch (KH), Thực hiện trong tuần, Thực hiện lũy kế, Thời gian trung bình thực hiện (phút/công tơ), tỷ lệ So sánh TH/KH.

[DÁN DỮ LIỆU SHEET 10KTSDĐ TẠI ĐÂY]

Viết ĐÁNH GIÁ TỔNG HỢP TUẦN gồm:
1. Tổng số công tơ đã kiểm tra trong tuần và lũy kế toàn Công ty, tỷ lệ % lũy kế so với kế hoạch (KH).
2. Nêu đích danh đơn vị có tỷ lệ TH/KH THẤP NHẤT (kể cả các đơn vị thực hiện 0 trong tuần) — cần chỉ rõ số liệu 0 hoặc gần 0 nếu có.
3. Nhận xét về thời gian trung bình thực hiện (phút/công tơ) — đơn vị nào có thời gian cao bất thường so với mặt bằng chung (ảnh hưởng năng suất).
4. Kiến nghị đẩy nhanh tiến độ cho đơn vị chậm, đảm bảo hoàn thành kế hoạch kiểm tra định kỳ.
Chỉ dùng số liệu trong bảng.
```

---

## Sheet 11 — `11DUBAOPHUTAI`: Dự báo điện thương phẩm
**Cột dữ liệu:** Đơn vị, theo từng tháng: Sai số (%) nhóm khách hàng >1 triệu kWh và ĐTP tổng, So sánh với kế hoạch.

**Prompt:**
```
Bạn là chuyên viên PKD Công ty Điện lực Đồng Nai. Dưới đây là bảng tổng hợp công tác dự báo điện thương phẩm (ĐTP) năm 2026 theo từng đơn vị, với sai số dự báo (%) của nhóm khách hàng >1 triệu kWh và ĐTP tổng theo từng tháng, so sánh với kế hoạch.

[DÁN DỮ LIỆU SHEET 11DUBAOPHUTAI TẠI ĐÂY — nêu rõ đang đánh giá tháng nào]

Viết ĐÁNH GIÁ TỔNG HỢP THÁNG gồm:
1. Sai số dự báo bình quân toàn Công ty của tháng đang xét (cả nhóm >1 triệu kWh và ĐTP tổng), xu hướng so với các tháng trước đó trong bảng (sai số tăng hay giảm).
2. Nêu đích danh đơn vị có sai số dự báo LỚN NHẤT trong tháng (kèm % cụ thể), đây là đơn vị cần rà soát lại phương pháp dự báo.
3. So sánh kết quả thực hiện với kế hoạch điện thương phẩm — đơn vị nào chênh lệch lớn giữa thực hiện và kế hoạch.
4. Kiến nghị cải thiện độ chính xác dự báo cho đơn vị có sai số cao và bất thường.
Chỉ dùng số liệu trong bảng, không suy đoán nguyên nhân nếu không có dữ liệu hỗ trợ.
```

---

## Sheet 12 — `12DIENNHANTUAN`: Điện nhận tuần
**Cột dữ liệu:** Ngày (Thứ 2 → Chủ nhật), Tuần 37, Tuần 38, So sánh tuần trước (tỷ lệ).

**Prompt:**
```
Bạn là chuyên viên PKD Công ty Điện lực Đồng Nai. Dưới đây là bảng điện nhận theo từng ngày trong tuần, so sánh với tuần trước liền kề (tỷ lệ so sánh).

[DÁN DỮ LIỆU SHEET 12DIENNHANTUAN TẠI ĐÂY]

Viết ĐÁNH GIÁ TỔNG HỢP TUẦN gồm:
1. Tổng điện nhận trong tuần hiện tại so với tuần trước (tăng/giảm bao nhiêu %, quy đổi kWh nếu tính được từ dữ liệu).
2. Nêu ngày có mức tăng/giảm bất thường nhất so với cùng ngày tuần trước (kèm tỷ lệ %) và nhận định sơ bộ nguyên nhân nếu suy luận được từ xu hướng chung (thời tiết, ngày lễ, cuối tuần...) — chỉ nêu nếu hợp lý, không bịa.
3. Nhận xét xu hướng chung cả tuần (tăng dần, giảm dần, hay dao động).
Chỉ dùng số liệu trong bảng.
```

---

## Sheet 13 — `13LAPDATTBDD`: Tiến độ lắp đặt công tơ (đo xa)
**Cột dữ liệu:** Điện lực, Số lượng đã phân bổ (theo loại CTĐT/DCU/Modem), Số lượng lũy kế lắp đặt, Số lượng còn lại chưa lắp, Tỷ lệ lắp đặt/số lượng đã phân bổ (theo từng loại thiết bị).

**Prompt:**
```
Bạn là chuyên viên PKD Công ty Điện lực Đồng Nai. Dưới đây là bảng tiến độ lắp đặt công tơ điện tử (CTĐT 1 pha, 3 pha), DCU, Modem theo từng Điện lực: số lượng đã phân bổ, lũy kế đã lắp, còn lại chưa lắp, tỷ lệ lắp đặt/phân bổ.

[DÁN DỮ LIỆU SHEET 13LAPDATTBDD TẠI ĐÂY]

Viết ĐÁNH GIÁ TỔNG HỢP gồm:
1. Tỷ lệ lắp đặt bình quân toàn Công ty theo từng nhóm thiết bị (CTĐT 1 pha, CTĐT 3 pha, DCU, Modem) so với khối lượng đã phân bổ.
2. Nêu đích danh Điện lực có tỷ lệ lắp đặt THẤP NHẤT ở từng nhóm thiết bị (đặc biệt nếu tỷ lệ = 0% ở nhóm nào, phải nêu rõ) và số lượng còn lại chưa lắp cụ thể.
3. Nêu Điện lực có tiến độ tốt nhất để làm điển hình.
4. Kiến nghị đẩy nhanh tiến độ cho các đơn vị chậm, ưu tiên nhóm thiết bị có tỷ lệ thấp nhất.
Chỉ dùng số liệu trong bảng.
```

---

## Ghi chú triển khai trên Dashboard
- Có thể tạo 1 nút "Tạo đánh giá tự động" cho mỗi tab/sheet, gọi API (Claude/GPT) với đúng prompt tương ứng ở trên + dữ liệu sheet đó (đọc trực tiếp từ file Excel đang tải lên), rồi đổ kết quả vào ô nhận xét — giảm thao tác copy/dán thủ công mỗi tuần.
- Nên lưu lại 2–3 tuần gần nhất của mỗi sheet để prompt có thể so sánh xu hướng (phần "so sánh tuần trước" ở các prompt trên).
