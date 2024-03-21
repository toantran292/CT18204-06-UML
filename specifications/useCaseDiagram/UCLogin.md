# Đặc tả use case Đăng nhập

<table>
    <tr>
        <th>Tên use case</th>
        <th>Đăng nhập</th>
    </tr>
    <tr>
        <td>Tóm tắt</td>
        <td>Cho phép người dùng đã được cấp tài khoản đăng nhập vào hệ thống.</td>
    </tr>
    <tr>
        <td>Actor</td>
        <td></td>
    </tr>
    <tr>
        <td>Phiên bản</td>
        <td>1.0</td>
    </tr>
    <tr>
        <td>Chịu trách nhiệm</td>
        <td>Trần Thái Toàn</td>
    </tr>
    <tr>
        <td>Ngày tạo</td>
        <td>10/03/2024</td>
    </tr>
    <tr>
        <td>Ngày cập nhật</td>
        <td>21/02/2024</td>
    </tr>
    <tr>
        <td>Điều kiện tiên quyết</td>
        <td>Người dùng đã được cấp tài khoản trên hệ thống.</td>
    </tr>
    <tr>
        <td>Kịch bản thường</td>
        <td>
            <ol type="1">
                <li>Người dùng chọn vào đăng nhập.</li>
                <li>Hệ thống hiển thị giao diện đăng nhập với biểu mẫu đăng nhập bao gồm nhập tên đăng nhập, mật khẩu.</li>
                <li>Người dùng nhập tên đăng nhập, mật khẩu và nhấn đăng nhập.</li>
                <li>
                    Hệ thống kiểm tra thông tin đăng nhập. </br>
                    <b>Có thể nhảy đến: </b> </br>
                    A. Người dùng nhập sai tên đăng nhập, mật khẩu.
                </li>
                <li>Hệ thống hiển thị thông báo đăng nhập thành công</li>
                <li>Hệ thống chuyển hướng người dùng tới trang chủ với các chức năng hiển thị theo quyền hạn của tài khoản</li>
            </ol> 
        </td>
    </tr>
    <tr>
        <td>Kịch bản thay thế</td>
        <td>
            <ol type="A">
                <li>
                    Người dùng nhập sai tên đăng nhập, mật khẩu. </br>
                    Chuỗi A bắt đầu ở bước 4 của kịch bản thường.
                    <ol type="1" start="5">
                        <li>Hệ thống hiển thị thông báo đăng nhập thất bại do sai thông tin đăng nhập.</li>
                    </ol>
                    Trở về bước 3 của kịch bản thường.
                </li>
            </ol>
        </td>
    </tr>
    <tr>
        <td>Kịch bản lỗi</td>
        <td></td>
    </tr>
    <tr>
        <td>Kết quả</td>
        <td>Đăng nhập thành công và cho phép người dùng sử dụng các chức năng theo quyền hạn của tài khoản</td>
    </tr>
</table>