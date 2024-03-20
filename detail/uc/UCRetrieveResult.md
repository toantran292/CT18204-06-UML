# Đặc tả use case Xem diễn biến trận đấu

| Tên use case | Xem diễn biến trận đấu |
| --- | ----- |
| Tóm tắt | Cho phép người sử dụng xem diễn biến của trận đấu |
| Ngày tạo | 10/03/2024 |
| Version | |
| Chịu trách nhiệm | Trần Thái Toàn |
| Điều kiện tiên quyết | Không có.|   
| Kịch bản thường | 1. Người dùng truy cập vào hệ thống và chọn vào danh mục trận đấu|
| | 2. Hệ thống hiển thị danh sách trận đấu | 
| | **Có thể nhảy đến** | 
| | A1 - Người dùng chọn vào chức năng tìm kiếm trận đấu | 
| | 3. Người dùng chọn trận đấu cụ thể để xem diễn biến | 
| | 4. Hệ thống hiển thị diễn biết chi tiết của trận đấu |
| Kịch bản thay thế |  **A1** – Người dùng chọn vào chức năng tìm kiếm. |
| | Chuỗi A1 bắt đầu ở bước 2 của kịch bản thường. |
| | 3. Hệ thống hiển thị thanh tìm kiếm. |
| | 4. Người dùng nhập tên trận đấu vào thanh tìm kiếm và nhấn tìm kiếm.
| | Có thể nhảy đến:
| | A1.1 – Không tìm thấy trận đấu theo tên trận đấu người dùng cung cấp.
| | 5. Hệ thống hiển thị danh sách trận đấu theo tên trận đấu người dùng cung cấp.
| | Trở về bước 3 của kịch bản thường.
| | A1.1 – Không tìm thấy trận đấu theo tên trận đấu người dùng cung cấp.
| | Chuỗi A1.1 bắt đầu ở bước 4 của kịch bản thay thế A1.
| | 5. Hiển thị trận đấu không tìm thấy cho người dùng.
| | Trở lại bước 2 của kịch bản thường.
| Kịch bản lỗi | |
| Kết quả | Hiện thị diễn biến trận đấu |
