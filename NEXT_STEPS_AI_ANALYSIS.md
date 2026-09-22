# Ghi chú tiếp tục triển khai phân tích AI

Ngày ghi chú: 2026-09-21

## Đã thống nhất

- Mục tiêu: mỗi tuần người dùng upload file Excel báo cáo vào Dashboard.
- Hệ thống cần tự động:
  1. Đọc từng sheet Excel.
  2. Nhận diện sheet theo tên/mẫu nội dung, không phụ thuộc cứng vào mã sheet.
  3. Chèn bảng dữ liệu của sheet vào đúng prompt tương ứng.
  4. So sánh với tuần trước.
  5. Sinh đánh giá, rủi ro, nguyên nhân và kiến nghị.
  6. Lưu dữ liệu tuần mới và đồng bộ cho tất cả người dùng.
- Báo cáo đầu ra cần phục vụ lãnh đạo, gồm đầy đủ các chuyên đề; chuyên đề rủi ro phải chi tiết, chuyên đề ổn định tóm tắt.
- So sánh kết hợp với chỉ tiêu/kế hoạch và tuần trước.
- Đã tích hợp tab `Báo cáo điều hành` vào Dashboard và đã push commit `837b173` lên GitHub.

## Nguồn prompt

File: `Prompt-danh-gia-theo-sheet.md`

File hiện có 13 prompt tương ứng với 13 nhóm phân tích:

1. `1CRM`
2. `2MATDIENTBACC`
3. `3HAILONGKH`
4. `4THUTD`
5. `5NONSNN` (ánh xạ Excel hiện tại: `41NONSNN`)
6. `6NLMT` (ánh xạ Excel hiện tại: `5NLMT`)
7. `7THAYDK` (ánh xạ Excel hiện tại: `6THAYDK`)
8. `8DOXA` (ánh xạ Excel hiện tại: `7DOXA`)
9. `9TRUYTHU` (ánh xạ Excel hiện tại: `8TRUYTHU`)
10. `10KTSDĐ` (ánh xạ Excel hiện tại: `9KTSDĐ`)
11. `11DUBAOPHUTAI` (ánh xạ Excel hiện tại: `9DUBAOPHUTAI`)
12. `12DIENNHANTUAN` (ánh xạ Excel hiện tại: `10DIENNHANTUAN`)
13. `13LAPDATTBDD` (sheet mới trong Excel Tuần 38)

## Dữ liệu hiện có

- Excel Tuần 37: 12 sheet.
- Excel Tuần 38: 13 sheet, có thêm `11LAPDATTBDD`.
- `data_history.json` đang chứa lịch sử các tuần và dữ liệu chuẩn hóa cũ.
- `index.html` và `Dashboard_KinhDoanh_PCDongNai_HangTuan_Final.html` đã có tab báo cáo điều hành.

## Kiến trúc dự kiến

```text
Upload Excel
  -> đọc workbook ở client hoặc backend
  -> nhận diện sheet theo tên/mẫu nội dung
  -> chuẩn hóa bảng dữ liệu
  -> lấy prompt tương ứng từ Prompt-danh-gia-theo-sheet.md
  -> chèn dữ liệu tuần hiện tại + dữ liệu tuần trước
  -> gọi AI API ở backend/GitHub Actions
  -> kiểm tra JSON/schema kết quả
  -> cập nhật data_history.json
  -> sinh báo cáo điều hành Markdown/HTML
  -> deploy GitHub Pages
```

## Quyết định còn chờ

- Nhà cung cấp AI dự kiến: **Google Gemini API**.
- Không được đặt API key trong `index.html` hoặc mã JavaScript client-side.
- Cần chọn cách lưu secret: GitHub Actions Secrets hoặc một backend trung gian.
- Cần xác định cách kích hoạt đồng bộ: upload qua Dashboard, upload file vào repository, hay workflow kết hợp.

## Việc cần làm tiếp theo

1. Chốt model Gemini, giới hạn token và định dạng JSON đầu ra.
2. Tách 13 prompt thành cấu hình có thể đọc tự động, hoặc parser các block trong file Markdown.
3. Xây dựng schema kết quả phân tích cho từng sheet.
4. Bổ sung parser cho `11LAPDATTBDD`.
5. Tạo backend/workflow gọi AI bằng secret an toàn.
6. Tự động so sánh tuần mới với tuần liền trước.
7. Cập nhật `data_history.json`, báo cáo Markdown/HTML và GitHub Pages.
8. Kiểm thử với file `KD-SO LIEU KD-DVKH TUAN 38.xlsx`.

## Lưu ý dữ liệu

- Không kết luận “không có biến động” chỉ vì hai payload giống nhau; phải kiểm tra kỳ báo cáo và nguồn file.
- Sheet Điện nhận tuần phải có cặp cột tuần hiện tại và tuần trước đúng kỳ.
- Kết quả AI phải bị ràng buộc chỉ sử dụng số liệu trong bảng, không bịa số liệu.
- Cần lưu cả dữ liệu đầu vào đã chuẩn hóa và kết quả phân tích để có thể kiểm tra/audit.
