<body>
    <h2>Sơ đồ tuần tự tạo tài khoản người dùng</h2>
    <p><strong>Mô tả chức năng:</strong> Cho phép quản trị viên tạo tài khoản cho trưởng ban tổ chức hoặc trưởng đoàn</p>
    <p><strong>Điều kiện tiên quyết:</strong> Đăng nhập vào hệ thống với tài khoản của quản trị viên</p>
    <p><strong>Trình tự thực hiện:</strong></p>
    <ol>
        <li>Quản trị viên chọn danh mục quản lý người dùng</li>
        <li>Hệ thống chuyển hướng đến giao diện quản lý người dùng</li>
        <li>Quản trị viên nhấn chọn vào chức năng tạo tài khoản người dùng </li>
        <li>Hệ thống hiển thị giao diện tạo tài khoản người dùng <strong>[Loop]</strong></li>
        <li>Quản trị viên nhấn chọn vai trò tài khoản bao gồm trưởng ban tổ chức hoặc trưởng đoàn và sau đó nhập các thông tin cho tài khoản bao gồm: Họ và tên, email, mật khẩu, giới tính, ngày sinh, số điện thoại</li>
        <li>Nếu quản trị viên chọn nút thoát thì quá trình tạo tài khoản sẽ kết thúc và hệ thống chuyển hướng giao diện sang quản lý người dùng và nếu không quá trình tạo sẽ tiếp tục diễn ra.</li>
        <li>Gọi phương thức kiểm tra hợp lệ với tham số là thông tin tài khoản<strong>[Rẽ nhánh]</strong></li>
        <li>Nếu kết quả kiểm tra hợp lệ là false: thông báo cho quản trị viên tạo tài khoản không thành công và yêu cầu nhập lại. Quay trở về bước 5.</li>
        <li>Ngược lại kết quả kiểm tra hợp lệ là true: gọi phương thức tạo tài khoản với tham số là thông tin tài khoản. Thông báo cho quản trị viên tạo tài khoản thành công</li>
        <li>Hệ thống trở về giao diện quản lý người dùng</li>
        <p><strong>Kết quả:</strong> thêm tài khoản học viên thành công.</p>
        </li>
    </ol>
</body>
