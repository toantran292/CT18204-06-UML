# Sơ đồ hoạt động Tạo giải đấu

### I. Người thiết kế: 
Hà Ngọc Linh - B2207536
### II. Mô tả:
1. Trưởng ban tổ chức sau khi đã đăng nhập thành công vào hệ thống thì chọn danh mục “Quản lý trận đấu” ở giao diện chính. Hệ thống sẽ chuyển hướng đến giao diện Quản lý giải đấu.
2. Trưởng ban tổ chức chọn danh mục "Cập nhập diễn biến trận đấu" ở giao diện Quản lý giải đấu. Hệ thống sẽ lấy danh sách các giải đấu và hiển thị lên màn hình.
3. Trưởng ban tổ chức chọn giải đấu cần cập nhật. Hệ thống sẽ lấy danh sách các trận đấu của giải đấu đó và hiển thị lên màn hình.
4. Trưởng ban tổ chức chọn trận đấu cần cập nhật. Hệ thống sẽ lấy danh sách các đội tham gia trận đấu đó và hiển thị lên màn hình.
5. Nếu trận đấu đã kết thúc, báo lỗi trận đấu đã kết thúc và thoát giao diện Cập nhật diễn biến trận đấu chuyển hướng về giao diện quản lý trận đấu. Nếu không, Trưởng ban tổ chức tiến hành chọn đội cần cập nhật. Hệ thống sẽ lấy danh sách các VDV của đội đó và hiển thị lên màn hình.
6. Trưởng ban tổ chức chọn VDV cần cập nhật. Và chọn mục cần cập nhật là điểm hay lỗi.
7. Trưởng ban tổ chức tiến hành nhập các thông tin cần cập nhật.
8. Nếu Trưởng ban tổ chức không muốn Cập nhật nữa và nhấn vào nút thoát thì hệ thống sẽ thoát khỏi chức năng Cập nhật diễn biến trận đấu và chuyển hướng về giao diện Quản lý trận đấu. Nếu không thì vẫn tiếp tục nhập liệu như bình thường.
9. Sau khi đã kiểm tra lại thông tin, Trưởng ban tổ chức chọn vào nút Cập nhật điểm hoặc Cập nhật lỗi để thực hiện việc Cập nhật diễn biến trận đấu. Hệ thống sẽ kiểm tra thông tin được nhập.
10. Nếu thông tin Trưởng ban tổ chức nhập không hợp lệ thì trả về thông báo thông tin không hợp lệ và quay trở lại giao diện Cập nhật diễn biến trận đấu để Trưởng ban tổ chức tiến hành nhập lại thông tin.
11. Nếu thông tin Trưởng ban tổ chức nhập là hợp lệ thì tiến hành ghi nhận việc Cập nhật điểm hoặc Cập nhật lỗi lên hệ thống đồng gửi thông báo diễn biến mới đến những người dùng có quan tâm đến trận đấu.
12. Thông báo cho Trưởng ban tổ chức thông tin được cập nhật thành công. Hiển thị giao diện Quản lý trận đấu.

#### Kết thúc

### III. Kết quả:
Thao tác Tạo giải đấu mới thành công.