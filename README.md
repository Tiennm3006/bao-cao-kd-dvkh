# ⚡ Dashboard Kinh Doanh & Dịch Vụ Khách Hàng — PC Đồng Nai (Bản Đóng Gói Phê Duyệt v1.0.0)

Ứng dụng web báo cáo điều hành Kinh doanh & Dịch vụ khách hàng hàng tuần dành cho Công ty Điện lực Đồng Nai, hỗ trợ xem 24/7 từ xa trên máy tính và điện thoại di động.

---

## 🌐 Đường Dẫn Web Live
- **GitHub Pages**: [https://tiennm3006.github.io/bao-cao-kd-dvkh/](https://tiennm3006.github.io/bao-cao-kd-dvkh/)
- **Repository**: [https://github.com/Tiennm3006/bao-cao-kd-dvkh](https://github.com/Tiennm3006/bao-cao-kd-dvkh)

---

## 🔥 Các Tính Năng Nổi Bật

1. **Xác thực JWT & Phân quyền RBAC**:
   - 👔 **Phó Giám đốc**: Xem bức tranh tổng thể, nhận định báo cáo, biểu đồ xếp hạng 22 Điện lực và tải Excel.
   - 📋 **Trưởng phòng / 📝 Phó phòng**: Rà soát, duyệt số liệu và cập nhật file Excel báo cáo tuần mới.
   - 👑 **Quản trị viên (Admin)**: Toàn quyền quản trị và nạp dữ liệu lịch sử.

2. **So Sánh Biến Động Qua Các Tuần (Multi-Week Compare)**:
   - Cho phép chọn nhiều tuần (Tuần 32, 33, 34, 35, 37, 38...) để so sánh xu hướng trung bình toàn Công ty và biến động chỉ tiêu từng Điện lực.

3. **Đồng Bộ Dữ Liệu Tập Trung (Auto Central Sync)**:
   - Khi Admin/Phó phòng nạp dữ liệu tuần mới (như Tuần 38, 39...), hệ thống tự động đồng bộ trung tâm để **tất cả người dùng (bao gồm Lãnh đạo)** mở web lên là xem được báo cáo mới nhất ngay lập tức mà không cần tự nạp thủ công.

4. **Xuất & Nạp File Excel Thông Minh (Multi-CDN Fallback)**:
   - Xuất báo cáo tuần sang định dạng Excel đầy đủ 12 chuyên đề và nhận định chỉ đạo.
   - Trình nạp Excel trực tiếp từ file gốc `KD-SO LIEU KD-DVKH TUAN XX.xlsx` với 3 đường CDN dự phòng (`jsDelivr`, `cdnjs`, `unpkg`).

---

## 📦 Cấu Trúc Đóng Gói Đóng Băng Mã Nguồn (Release v1.0.0)

```
d:\1. Bao cao KD-DVKH hang tuan\
├── index.html                                 # Single-Page App chính chạy trực tiếp trên GitHub Pages
├── Dashboard_KinhDoanh_PCDongNai_HangTuan_Final.html # Tệp ứng dụng HTML đầy đủ dự phòng
├── data_history.json                          # Cơ sở dữ liệu lịch sử tuần (Tích hợp sẵn Tuần 32-38)
├── BaoCao_KD_DVKH_PC_DongNai_Final_Release.zip# Tệp nén đóng gói mã nguồn an toàn v1.0.0
├── README.md                                  # Hướng dẫn vận hành & đóng gói
└── scratch/
    ├── build_app.js                           # Kịch bản đóng gói & build bộ mã nguồn
    └── excel_parser_helpers.js                # Bộ engine phân tích file Excel client-side
```

---

## 🛡️ An Toàn Thông Tin & Bảo Mật (ATTT)
- **Chống Stored XSS**: Đã bọc hàm `escapeHtml()` cho toàn bộ dữ liệu đầu vào.
- **Thư viện an toàn**: Đã cập nhật SheetJS `v0.20.2` (vá lỗ hổng CVE) và Chart.js `v4.4.1`.
- **Bảo mật Token**: Không hardcode Personal Access Token hay mật khẩu trên mã nguồn client.

---

*Bản đóng gói phát hành chính thức — Ngày 20/09/2026.*
