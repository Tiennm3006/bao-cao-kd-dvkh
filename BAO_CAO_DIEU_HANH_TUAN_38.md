# BÁO CÁO ĐIỀU HÀNH KINH DOANH & DỊCH VỤ KHÁCH HÀNG

## PC Đồng Nai — Tuần 38/2026

**Kỳ báo cáo:** 14/09–18/09/2026  
**Kỳ đối chiếu:** Tuần 37/2026  
**Nguồn:** `data_history.json` (Tuần 38) và `KD-SO LIEU KD-DVKH TUAN 37.xlsx`/bản dữ liệu đã chuẩn hóa (Tuần 37)

## 1. Cảnh báo dữ liệu cần xử lý ngay

Không nên diễn giải việc “không biến động” từ kết quả so sánh máy móc. Kiểm tra nguồn cho thấy **11/12 chuyên đề của Tuần 38 có payload giống hệt Tuần 37**: cùng số liệu, cùng bảng xếp hạng, cùng nhận định và cùng kiến nghị. Riêng chuyên đề **Điện nhận tuần** của Tuần 38 vẫn chứa các trường `tuan36`, `tuan37`, tức là chưa có cặp `tuan37`, `tuan38` để so sánh đúng kỳ.

**Hệ quả điều hành:** các kết luận bên dưới phản ánh trạng thái dữ liệu đang có của Tuần 38; chưa đủ cơ sở xác nhận xu hướng tăng/giảm thực tế so với Tuần 37 ở 11 chuyên đề. Ưu tiên xác nhận lại pipeline nạp dữ liệu và phát hành `data_history.json` trước khi dùng báo cáo này làm căn cứ đánh giá xu hướng.

## 2. Tóm tắt điều hành

| Mức ưu tiên | Nội dung chính | Hành động đề nghị |
|---|---|---|
| **P0 — Dữ liệu** | 11/12 chuyên đề Tuần 38 trùng Tuần 37; Điện nhận tuần chưa có cặp 37–38 | Rà soát file nguồn Tuần 38, parser Excel, bước ghi đè `STORE[weekKey]` và quy trình xuất `data_history.json` |
| **P1 — Thiết bị** | 39.643 thiết bị đo đếm quá hạn; tập trung tại Trảng Bom, Trấn Biên, Long Khánh | Giao kế hoạch thay thế theo tuần, kiểm soát vật tư và nhân lực |
| **P1 — Công nợ** | Nợ NSNN tập trung tại Định Quán 2.234,6 triệu đồng, Trị An 1.083,8 triệu đồng, Bù Đăng 881,6 triệu đồng | Chốt danh sách công nợ, xác nhận nguồn ngân sách và lịch thanh toán |
| **P1 — Dịch vụ** | 20 lần mất điện lặp lại tại 7 trạm; Long Bình chiếm 16/20 lần | Phúc tra nguyên nhân gốc, đối chiếu CRM–OMS–đo xa |
| **P1 — Tiến độ** | ĐMTMN chỉ 3/10 Điện lực hoàn tất 100%; Xuân Lộc đạt 25% | Tập trung xử lý hồ sơ tồn, báo cáo tiến độ hàng tuần |
| **P2 — Đo xa/kiểm tra** | Đo xa đạt 11/22; kiểm tra SDĐ lũy kế đạt 7/22 | Lập danh sách đơn vị dưới chuẩn và kế hoạch bù tiến độ |

## 3. Phân tích 12 chuyên đề

### 3.1. Thu tiền điện — `4THUTD`

- **Kết quả:** 22/22 Điện lực đạt chỉ tiêu tỷ lệ thu **≥99,8%**; các đơn vị cao gồm Xuân Lộc 99,99%, Trị An và Long Khánh 99,98%.
- **Nhóm sát ngưỡng:** Lộc Ninh 99,80%, Bù Đăng 99,85%, Trảng Bom 99,86%.
- **Đánh giá:** Chỉ tiêu đang được kiểm soát tốt; tuy nhiên Lộc Ninh ở đúng ngưỡng nên cần theo dõi dư nợ phát sinh và dòng tiền cuối kỳ.
- **So sánh tuần:** Chưa xác nhận được biến động 38/37 do payload hai tuần trùng nhau.
- **Kiến nghị:** Duy trì đôn đốc thu trước hạn; lập danh sách khách hàng/nợ có nguy cơ làm tỷ lệ thu giảm dưới 99,8% tại các đơn vị sát ngưỡng.

### 3.2. Nợ ngân sách nhà nước — `41NONSNN`

- **Kết quả:** Chỉ **4/22** Điện lực không phát sinh nợ theo tiêu chí dữ liệu; nợ tập trung tại Định Quán **2.234,6 triệu đồng/116 hợp đồng**, Trị An **1.083,8 triệu đồng/180 hợp đồng**, Bù Đăng **881,6 triệu đồng/38 hợp đồng**.
- **Rủi ro:** Ba đơn vị trên chiếm phần lớn giá trị nợ; Trị An có số hợp đồng cao nhất, cho thấy rủi ro phân tán nhưng kéo dài.
- **So sánh tuần:** Chưa xác nhận được biến động 38/37.
- **Kiến nghị:** Phân loại nợ theo niên độ và tuổi nợ; làm việc với đơn vị sử dụng ngân sách để chốt biên bản xác nhận và lịch bố trí vốn; báo cáo riêng các khoản quá hạn dài ngày.

### 3.3. Điện mặt trời mái nhà — `5NLMT`

- **Kết quả:** **3/10** Điện lực hoàn tất 100% hồ sơ: Dầu Giây, Nhơn Trạch, Cẩm Mỹ.
- **Rủi ro:** Xuân Lộc chỉ **25% (1/4 hồ sơ)**; Trấn Biên **70,5% (31/44)**; Định Quán **72,7% (8/11)**.
- **Đánh giá:** Tồn đọng lớn nhất theo số lượng nằm tại Trấn Biên, còn điểm nghẽn theo tỷ lệ là Xuân Lộc.
- **So sánh tuần:** Chưa xác nhận được biến động 38/37.
- **Kiến nghị:** Giao mốc hoàn tất hồ sơ còn lại cho Xuân Lộc, Trấn Biên, Định Quán; phân loại hồ sơ thiếu pháp lý/khách hàng chưa phối hợp; cập nhật tiến độ theo tuần.

### 3.4. Thiết bị đo đếm quá hạn kiểm định — `6THAYDK`

- **Kết quả:** Không có Điện lực đạt mức tồn bằng 0; tổng tồn **39.643 thiết bị**.
- **Rủi ro trọng yếu:** Trảng Bom **5.281**, Long Khánh **4.699**, Trấn Biên **4.439** thiết bị; đây là nhóm cần ưu tiên nguồn lực.
- **Mức thấp:** Bù Đốp 3, Cẩm Mỹ 5, Long Thành 11.
- **So sánh tuần:** Chưa xác nhận được biến động 38/37; cần tránh coi số liệu hiện tại là số mới nếu chưa xác nhận file nguồn.
- **Kiến nghị:** Lập kế hoạch thay thế theo khu vực/sản lượng, kiểm soát tồn kho công tơ–TU–TI và điều phối đội hỗ trợ cho ba đơn vị tồn cao.

### 3.5. Công tác đo xa — `7DOXA`

- **Kết quả:** **11/22** Điện lực đạt tỷ lệ thu thập dữ liệu chung tối thiểu 99%.
- **Rủi ro:** Chơn Thành 96,9%, Hớn Quản 96,7%, Đồng Phú 96,5%; cả ba chưa đạt đo xa. Tỷ lệ khai thác công tơ điện tử tại các đơn vị này lần lượt 99,7%, 99,5%, 99,6%.
- **Đánh giá:** Điểm nghẽn chính là thu thập dữ liệu/modem/DCU, không phải khai thác công tơ ở phần lớn đơn vị.
- **So sánh tuần:** Chưa xác nhận được biến động 38/37.
- **Kiến nghị:** Lập danh sách điểm đo mất tín hiệu trên 7 ngày; phân loại lỗi modem, DCU, nguồn và sóng; phối hợp nhà mạng xử lý vùng tín hiệu yếu.

### 3.6. Truy thu hư cháy, sai lệch đo đếm và trộm cắp — `8TRUYTHU`

- **Kết quả:** 8/22 Điện lực đạt/vượt tiến độ; bình quân dữ liệu hiện có khoảng **58,9% kế hoạch**.
- **Nhóm tốt:** Đồng Phú 161,6%, Chơn Thành 126,3%, Hớn Quản 118,5%.
- **Rủi ro:** Trấn Biên 12,7%, Long Khánh 14,8%, Bù Gia Mập 16,4%.
- **Trộm cắp điện:** Trấn Biên 4 vụ; Lộc Ninh và Trảng Bom 2 vụ/đơn vị.
- **So sánh tuần:** Chưa xác nhận được biến động 38/37.
- **Kiến nghị:** Đẩy nhanh hồ sơ điều chỉnh có thời gian tồn dài; lập kế hoạch truy thu riêng cho ba đơn vị dưới 20%; tăng phúc tra tại khu vực có lịch sử trộm cắp.

### 3.7. Kiểm tra sử dụng điện định kỳ — `9KTSDĐ`

- **Kết quả:** Chỉ **7/22** Điện lực đạt/vượt 100% kế hoạch lũy kế.
- **Nhóm vượt:** Bù Đăng 117,5%, Định Quán 114,2%, Hớn Quản 105,4%.
- **Rủi ro tiến độ:** Nhơn Trạch 64,9%, Xuân Lộc 76,2%, Trảng Bom 79,7%.
- **So sánh tuần:** Chưa xác nhận được biến động 38/37.
- **Kiến nghị:** Bù khối lượng tại nhóm dưới 80%; ưu tiên khách hàng sản lượng lớn và khu vực nguy cơ tổn thất; theo dõi năng suất kiểm tra theo người/ca.

### 3.8. Dự báo phụ tải/điện thương phẩm — `9DUBAOPHUTAI`

- **Kết quả:** Chỉ tiêu được biểu diễn theo số tháng đạt đủ hai tiêu chí trên 16 tháng-tiêu chí; nhóm cao gồm Bù Gia Mập 11, Lộc Ninh 10, Định Quán 10.
- **Rủi ro:** Long Bình và Nhơn Trạch chỉ 5 tháng đạt; Long Khánh 6 tháng. Đây là nhóm cần rà soát phương pháp dự báo và sai số theo từng tiêu chí.
- **So sánh tuần:** Chưa xác nhận được biến động 38/37; bản chất chỉ tiêu là lũy kế năm nên cần so sánh thêm theo tháng cập nhật.
- **Kiến nghị:** Đối chiếu sai số với thời tiết, mùa vụ, khách hàng lớn và phụ tải thực tế; tổ chức rút kinh nghiệm giữa nhóm đạt cao và nhóm thấp.

### 3.9. Khách hàng đánh giá không hài lòng — `3HAILONGKH`

- **Kết quả:** 3 phản ánh, tại Đồng Xoài, Định Quán và Trảng Bom.
- **Nội dung rủi ro:** Chậm hỗ trợ sự cố/mất điện, thông tin hẹn xử lý chưa rõ, xử lý cắt điện không đúng lịch và vấn đề nhận diện đồng phục/trao đổi với khách hàng.
- **So sánh tuần:** Chưa xác nhận được biến động 38/37.
- **Kiến nghị:** Rà soát SLA phản hồi ngoài giờ; bắt buộc cập nhật tiến độ khi trễ hẹn; chấn chỉnh nhận diện nhân viên và thông báo lịch cắt điện.

### 3.10. Phiếu yêu cầu gọi nhiều lần trên CRM — `1CRM`

- **Kết quả:** 7 phiếu gọi nhiều lần.
- **Phân bố:** Định Quán 2, Lộc Ninh 2, Đồng Xoài 1, Trảng Bom 1, Dầu Giây 1.
- **Rủi ro:** Định Quán và Lộc Ninh cần phân tích nguyên nhân gốc để tránh khách hàng phải gọi lại cùng nội dung.
- **So sánh tuần:** Chưa xác nhận được biến động 38/37.
- **Kiến nghị:** Kiểm tra các phiếu lặp theo loại yêu cầu, thời gian xử lý và đơn vị thực hiện; theo dõi tỷ lệ xử lý dứt điểm ngay lần đầu.

### 3.11. Trạm mất điện lặp lại — `2MATDIENTBACC`

- **Kết quả:** 7 trạm/nhóm trạm, tổng **20 lần mất điện lặp lại**.
- **Rủi ro trọng yếu:** Long Bình có **8 trạm, 16 lần**, chiếm 80% tổng số lần; các đơn vị còn lại trong dữ liệu có 2 trạm/4 lần.
- **So sánh tuần:** Chưa xác nhận được biến động 38/37.
- **Kiến nghị:** Phúc tra ngay nhóm trạm Long Bình; đối chiếu lịch sử sự cố, tải, bảo vệ và chất lượng thiết bị; lập kế hoạch bảo trì/sửa chữa ưu tiên.

### 3.12. Điện nhận tuần — `10DIENNHANTUAN`

- **Dữ liệu hiện có:** Tổng Tuần 37 là **434.749.998 kWh**, tăng **17,7%** so với Tuần 36 là 369.341.691 kWh.
- **Ngày biến động mạnh:** Thứ 4 đạt 168,6% so với cùng ngày Tuần 36; Thứ 3 đạt 147,3%.
- **Ngày giảm:** Thứ 7 đạt 97,9%, Chủ nhật 98,5%.
- **Cảnh báo:** Bản ghi gắn nhãn Tuần 38 nhưng vẫn dùng trường `tuan36` và `tuan37`; chưa có số liệu `tuan38`. Vì vậy **chưa thể kết luận điện nhận Tuần 38 tăng/giảm so với Tuần 37**.
- **Kiến nghị:** Bổ sung dữ liệu Tuần 38, sau đó đối chiếu với dự báo phụ tải và các ngày tăng đột biến để cảnh báo nguy cơ quá tải cục bộ.

## 4. Danh sách hành động ưu tiên

1. **Khắc phục dữ liệu:** xác minh file nguồn Tuần 38 và tái sinh `data_history.json`; kiểm tra riêng 11 chuyên đề bị trùng và sheet Điện nhận tuần.
2. **Thiết bị đo đếm:** yêu cầu Trảng Bom, Long Khánh, Trấn Biên trình kế hoạch giảm tồn 39.643 thiết bị theo tuần.
3. **Công nợ NSNN:** Định Quán, Trị An, Bù Đăng lập bảng tuổi nợ, hồ sơ xác nhận và lịch thu hồi.
4. **Mất điện lặp lại:** phúc tra 8 trạm/16 lần tại Long Bình; báo cáo nguyên nhân gốc và phương án xử lý.
5. **Tiến độ ĐMTMN và kiểm tra SDĐ:** giao chỉ tiêu bù tiến độ cho nhóm thấp, đặc biệt Xuân Lộc, Trấn Biên, Nhơn Trạch, Trảng Bom.
6. **Dịch vụ khách hàng:** rà soát 3 phản ánh không hài lòng và 7 phiếu CRM gọi nhiều lần, gắn trách nhiệm xử lý đến từng Điện lực.

## 5. Kết luận

Về vận hành, các rủi ro lớn nhất hiện nằm ở **thiết bị đo đếm quá hạn, công nợ NSNN, mất điện lặp lại, tiến độ ĐMTMN và tiến độ kiểm tra sử dụng điện**. Tuy nhiên, về mặt quản trị dữ liệu, rủi ro cấp cao hơn là **chưa chứng minh được dữ liệu Tuần 38 đã được cập nhật đầy đủ**. Báo cáo chính thức phục vụ lãnh đạo nên được phát hành lại sau khi hoàn tất bước xác minh và đồng bộ dữ liệu Tuần 38.

