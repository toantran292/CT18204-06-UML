# Đặc tả use case Gửi yêu cầu chỉnh sửa thông tin cá nhân

| Tên use case | Gửi yêu cầu chỉnh sửa thông tin cá nhân |
| --- | ----- |
| Tóm tắt | Cho phép Vận động viên gửi yêu cầu chỉnh sửa thông tin cá nhân của mình khi phát hiện sai sót |
| Actor | Vận động viên |
| Ngày tạo | 16/03/2024 |
| Version | 1.1 |
| Chịu trách nhiệm | Khưu Thị Bích Ngọc |
| Điều kiện tiên quyết | Vận động viên đăng nhập thành công vào hệ thống và xem thông tin cá nhân của mình|   
| Kịch bản thường | 1. Vận động viên phát hiện thông tin cá nhân không đúng và chọn vào ô gửi yêu cầu chỉnh sửa thông tin cá nhân|
| | 2. Hệ thống hiển thị giao diện biểu mẫu cho vận động viên nhập thông tin cần chỉnh sửa  | 
| | 3. Vận động viên chọn mục thông tin bị sai và gõ thông tin đúng vào  | 
| | 4.	Vận động viên ấn gửi để gửi yêu cầu chỉnh sửa thông tin | 
| | 5.	Thông tin được gửi lên hệ thống để kiểm tra | 
| | 6.	Hệ thống kiểm tra thông tin | 
| | **Có thể nhảy đến** | 
| | A1 – Khi thông tin của vận động viên gửi đi không hợp lệ | 
| | 7. Hệ thống lưu lại yêu cầu chờ phê duyệt | 
| | 8. Hệ thống gửi thông báo thành công về trình duyệt|
| | 9. Trình duyệt hiển thị kết quả | 
|Kịch bản thay thế|  **A1** – Khi thông tin của vận động viên gửi đi không hợp lệ|
| | Chuỗi A1 bắt đầu ở bước 6 của kịch bản thường. |
| | 7. Hệ thống gửi thông báo lỗi và yêu cầu Vận động viên đó nhập lại thông tin |
| | 8. Trình duyệt hiển thị thông báo lỗi và yêu cầu nhập lại thông tin |
| | Trở về bước 2 của kịch bản thường. |
| Kịch bản lỗi | |
| Kết quả | Thao tác gửi yêu cầu chỉnh sửa thông tin thành công |
