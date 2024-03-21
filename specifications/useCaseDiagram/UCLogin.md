# Đặc tả use case Đăng nhập

| Tên use case | Đăng nhập |
| --- | ----- |
| Tóm tắt | Cho phép người dùng đã được cấp tài khoản đăng nhập vào hệ thống|
| Ngày tạo | 10/03/2024 |
| Version | 1.1|
| Chịu trách nhiệm | Trần Thái Toàn |
| Điều kiện tiên quyết | Người dùng đã được cấp tài khoản trên hệ thống | 
| Kịch bản thường | 1. Người dùng chọn vào đăng nhập.|
| | 2. Hệ thống hiển thị giao diện đăng nhập với biểu mẫu đăng nhập bao gồm nhập tên đăng nhập, mật khẩu.|
| | 3. Người dùng nhập tên đăng nhập, mật khẩu và nhấn đăng nhập.|
| | 4. Hệ thống kiểm tra thông tin đăng nhập. |
| | **Có thể nhảy đến:** |
| | **A1** - Người dùng nhập sai tên đăng nhập, mật khẩu |
| | 5. Hệ thống hiển thị thông báo đăng nhập thành công |
| | 6. Hệ thống chuyển hướng người dùng tới trang chủ với các chức năng hiển thị theo quyền hạn của tài khoản |
| Kịch bản thay thế | **A1** - Người dùng nhập sai tên đăng nhập, mật khẩu |  
| | Chuỗi A1 bắt đầu ở bước 4 của kịch bản thường |
| | 5. Hệ thống hiển thị thông báo đăng nhập thất bại do sai thông tin đăng nhập |
| | Trở về bước 3 của kịch bản thường.
| Kịch bản lỗi | | 
| Kết quả | Đăng nhập thành công và cho phép người dùng sử dụng các chức năng theo quyền hạn của tài khoản | 
