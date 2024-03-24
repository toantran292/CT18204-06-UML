# Đặc tả use case Gửi yêu cầu chỉnh sửa thông tin cá nhân

| Tên use case | Gửi yêu cầu chỉnh sửa thông tin cá nhân |
| --- | ----- |
| Tóm tắt | Cho phép Vận động viên gửi yêu cầu chỉnh sửa thông tin cá nhân của mình khi phát hiện sai sót |
| Actor | Vận động viên |
| Ngày tạo | 16/03/2024 |
| Version | 1 |
| Chịu trách nhiệm | Khưu Thị Bích Ngọc |
| Điều kiện tiên quyết | Vận động viên đăng nhập thành công vào hệ thống và xem thông tin cá nhân của mình|   
| Kịch bản thường | 1. Vận động viên phát hiện thông tin cá nhân không đúng và chọn vào ô gửi yêu cầu chỉnh sửa thông tin cá nhân|
| | 2. Vận động viên chọn mục thông tin bị sai và gõ thông tin đúng vào  | 
| | 3.	Vận động viên ấn gửi để gửi yêu cầu chỉnh sửa thông tin đến Trưởng đoàn xem xét, xử lý  | 
| | **Có thể nhảy đến** | 
| | A1 – Khi thông tin của vận động viên gửi đi không hợp lệ | 
|| 4. Hệ thống hiển thị thông báo thành công và chuyển hướng sang trang chủ |
|Kịch bản thay thế|  **A1** – Khi thông tin của vận động viên gửi đi không hợp lệ|
| | Chuỗi A1 bắt đầu ở bước 3 của kịch bản thường. |
| | 4. Hệ thống hiển thị thông báo lỗi và yêu cầu Vận động viên đó nhập lại thông tin |
| | Trở về bước 2 của kịch bản thường. |
| Kịch bản lỗi | |
| Kết quả | Thao tác gửi yêu cầu chỉnh sửa thông tin được gửi thành công |
