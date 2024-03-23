# Đặc tả use case Thống kê thông tin

| Tên use case | Thống kê thông tin |
| --- | ----- |
| Tóm tắt | Cho phép Vận động viên gửi yêu cầu chỉnh sửa thông tin cá nhân của mình khi phát hiện sai sót |
| Actor | Quản trị viên |
| Ngày tạo | 16/03/2024 |
| Version | 1 |
| Chịu trách nhiệm | Khưu Thị Bích Ngọc |
| Điều kiện tiên quyết | Người dùng đã đăng nhập thành công vào hệ thống và có quyền của Quản trị viên|   
| Kịch bản thường | 1. Quản trị viên có nhu cầu thống kê thông tin về hệ thống của mình và chọn chức năng Thống kê thông tin|
| | 2. Hệ thống chuyển hướng sang trang danh mục các thống kê thông tin| 
| | 3. Quản trị viên chọn thống kê theo một trong hai mục: “Thống kê số lượng truy cập” hoặc “Thống kê tỉ lệ được tổ chức của môn thể thao” và ấn chọn tiếp tục| 
| | 4. Hệ thống tiếp tục chuyển hướng sang trang chọn thông tin chi tiết của thống kê mà người Quản trị viên muốn thực hiện |
| | **Có thể nhảy đến** | 
| | A1 –Thống kê số lượng truy cập | 
| | A2 –Thống kê tỉ lệ được tổ chức của môn thể thao | 
| | 5. Sau khi hoàn thành chọn các thông tin để thực hiện thống kê, Quản trị viên thực hiện gửi yêu cầu thống kê lên hệ thống.| 
| | 6. Hệ thống chuyển hướng sang trang hiển thị các kết quả thống kê |
| | **Có thể nhảy đến** | 
| | A3 – Quản trị viên muốn tiếp tục thống kê| 
| | A4 – Quản trị viên muốn in danh sách kết quả thống kê| 
| | 7. Nếu Quản trị viên chọn thoát. Hệ thống chuyển hướng trở về trang Quản trị  viên |
| Kịch bản thay thế |  **A1** – Thống kê số lượng truy cập |
| | Chuỗi A1 bắt đầu ở bước 4 của kịch bản thường. |
| | 5. Hệ thống hiển thị giao diện cho phép Quản trị viên chọn các thống kê về số lượng truy cập trang web như: Thống kê số lượng truy cập theo ngày, theo tháng, theo năm, theo quý |
| | Trở về bước 5 của kịch bản thường. |
| |  **A2** – Thống kê tỉ lệ được tổ chức của môn thể thao |
| | Chuỗi A2 bắt đầu ở bước 4 của kịch bản thường. |
| | 5. Hệ thống hiển thị giao diện cho phép Quản trị viên chọn các thống kê về tỉ lệ được tổ chức của các môn thi đấu như: Thống kê tỉ lệ tổ chức theo môn thi đấu, theo hạng mục thi đấu, theo giới tính của vận động viên, theo quy mô của môn thể thao, theo vị trí địa lý |
| | Trở về bước 5 của kịch bản thường. |
| |  **A3** – Quản trị viên muốn tiếp tục thống kê |
| | Chuỗi A3 bắt đầu ở bước 6 của kịch bản thường. |
| | Trở về bước 2 của kịch bản thường. |
| |  **A4** – Quản trị viên muốn in danh sách kết quả thống kê |
| | Chuỗi A4 bắt đầu ở bước 6 của kịch bản thường. |
| | 7. Hệ thống thực hiện chức năng in danh sách các kết quả vừa được thống kê |
| | Trở về bước 6 của kịch bản thường. |
| Kịch bản lỗi | |
| Kết quả | Thao tác thống kê thông tin được thực hiện thành công |
