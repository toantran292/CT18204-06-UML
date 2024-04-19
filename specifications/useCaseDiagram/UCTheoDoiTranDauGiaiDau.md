# Đặc tả use case Theo dõi trận đấu, giải đấu

| Tên use case | Theo dõi trận đấu, giải đấu |
| --- | ----- |
| Tóm tắt | Cho phép Người đã đăng nhập theo dõi trận đấu, giải đấu mà mình quan tâm |
| Actor | Người đã đăng nhập |
| Ngày tạo | 17/04/2024 |
| Version | 1.0 |
| Chịu trách nhiệm | Khưu Thị Bích Ngọc |
| Điều kiện tiên quyết | Người đã đăng nhập đã đăng nhập thành công vào hệ thống và đang xem thông tin chi tiết trân đấu hoặc giải đấu nào đó|   
| Kịch bản thường | 1. Người đã đăng nhập ấn chọn nút theo dõi của trận đấu, giải đấu|
| | 2. Giao diện gửi yêu cầu kiểm tra xem người dùng đã theo dõi trận đấu, giải đấu đó hay chưa  | 
| | 3. Hệ thống tiến hành kiểm tra | 
| | 4.	Hệ thống trả về kết quả vừa kiểm tra| 
| | **Có thể nhảy đến** | 
| | A1 – Người dùng đã theo dõi | 
| | 5.	Nếu người dùng chưa theo dõi, giao diện hiển thị để người dùng chọn cấp độ theo dõi mong muốn | 
| | 6.	Người dùng chọn cấp độ theo dõi và ấn gửi | 
| | 7. Hệ thống lưu thông tin theo dõi của người dùng | 
| | **Có thể nhảy đến** | 
| | A2 – Lưu thông tin theo dõi thất bại | 
| | 8. Nếu lưu thông tin theo dõi thành công, hệ thống gửi thông báo thành công về trình duyệt|
| | 9. Trình duyệt hiển thị kết quả| 
|Kịch bản thay thế|  **A1** – Người dùng đã theo dõi|
| | Chuỗi A1 bắt đầu ở bước 4 của kịch bản thường. |
| | 5. Trình duyệt yêu cầu người dùng xác nhận tiếp tục hay dừng quá trình hủy theo dõi |
| | **Có thể nhảy đến** | 
| | A3 - Người dùng dừng quá trình hủy yêu cầu|
| | 6. Người dùng chọn tiếp tục thực hiện |
| | 7. Hệ thống hủy theo dõi trận đấu, giải đấu của người dùng đó |
| | **Có thể nhảy đến**|
| | A4 - Hủy theo dõi thất bại|
| | 8. Nếu hủy theo dõi thành công, hệ thống gửi thông báo thành công về giao diện |
| | Trở về bước 9 của kịch bản thường |
| | **A2** - Lưu thông tin theo dõi thất bại |
| | Chuỗi A2 bắt đầu ở bước 7 của kịch bản thường |
| | 8. Hệ thống gửi thông báo tạo theo dõi thất bại |
| | Trở về bước 9 của kịch bản thường |
| | **A3** - Người dùng dừng quá trình hủy yêu cầu |
| | Chuỗi A3 bắt đầu ở bước 5 của kịch bản thay thế |
| | 6. Trở về giao diện ban đầu và kết thúc kịch bản |
| | **A4** - Hủy theo dõi thất bại |
| | Chuỗi A4 bắt đầu ở bước 7 của kịch bản thay thế |
| | 8. Hệ thống gửi thông báo hủy theo dõi thất bại về giao diện |
| | Trở về bước 9 của kịch bản thường |
| Kết quả | Thao tác theo dõi/hủy theo dõi trận đấu, giải đấu thành công|
