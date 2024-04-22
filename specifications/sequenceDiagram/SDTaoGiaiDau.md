# Sơ đồ tuần tự Tạo giải đấu

### I. Người thiết kế: 
Hà Ngọc Linh B2207536
### II. Mô tả chức năng:
Cho phép Trưởng ban tổ chức tạo ra giải đấu mới.
### III. Điều kiện tiên quyết:
Trưởng ban tổ chức được cấp tài khoản từ Quản trị viên và đăng nhập thành công vào hệ thống.
### IV. Trình tự thực hiện 
<ol>
    <li>Trưởng ban tổ chức sau khi đăng nhập vào hệ thống thì chọn danh mục Quản lý giải đấu.</li>
    <li>Hệ thống sẽ chuyển hướng đến giao diện Quản lý giải đấu.</li>
    <li>Trưởng ban tổ chức chọn danh mục Tạo giải đấu.</li>
    <li>Hệ thống sẽ chuyển hướng đến giao diện Tạo giải đấu.</li>
        [Loop]</br>
    <ol type="1" start="5">
        <li>Trưởng ban tổ chức điền các thông tin để tạo giải đấu mới như: tên, ngày tổ chức, cơ cấu giải thưởng,...</li>
        <li>Người dùng nhấn vào nút thoát. [Tùy chọn 1]</li>
        <li>Hệ thống chuyển hướng đến giao diện Tạo giải đấu. Thoát khỏi vòng lặp.</li> [Kết thúc tùy chọn 1]
        <li>Sau khi chỉnh sửa xong chọn Tạo giải đấu.</li>
        <li>Hệ thống gọi phương thức kiemTraThongTin() để kiểm tra tính hợp lệ của thông tin vừa nhập.</li>
        <li>Trả về kết quả kiểm tra.</li>
            [Rẽ nhánh]
        <ol type="1" start="11">
            <li>Nếu thông tin nhập không hợp lệ [ketQua == false]. Thông báo lỗi nhập liệu cụ thể cho Trưởng ban tổ chức. Trở về giao diện Tạo giải đấu, tiếp tục vòng lặp. [Rẽ nhánh 1]</li>
            <li>Ngược lại, nếu thông tin nhập hợp lệ [ketQua == true]. Hệ thống tiến hành lưu thay đổi. [Rẽ nhánh 2]</li>
            <li>Hệ thống trả về thông báo Tạo giải đấu thành công.</li>
            <li>Giao diện thông báo cho Trưởng ban tổ chức việc Tạo giải đấu đã thành công. Thoát khỏi vòng lặp.</li>
        </ol>
    </ol>
</ol>
<ol type="1" start="15">
    <li>Trở về giao diện Quản lý giải đấu.</li>
</ol>

#### Kết thúc

### V. Kết quả:
Thao tác Tạo giải đấu mới thành công.