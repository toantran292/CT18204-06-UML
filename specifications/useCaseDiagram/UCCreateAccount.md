# Đặc tả use case Tạo tài khoản người dùng

<table>
    <tr>
        <th>Tên usecase</th>
        <th>Tạo tài khoản người dùng</th>
    </tr>
    <tr>
        <td>Tóm tắt</td>
        <td>Cho phép tạo tài khoản cho ban tổ chức hoặc trưởng đoàn</td>
    </tr>
    <tr>
        <td>Actor</td>
        <td>Quản trị viên</td>
    </tr>
    <tr>
        <td>Phiên bản</td>
        <td>1.1</td>
    </tr>
    <tr>
        <td>Chịu trách nhiệm</td>
        <td>Nguyễn Tuấn Đạt</td>
    </tr>
    <tr>
        <td>Ngày tạo</td>
        <td>16/3</td>
    </tr>
    <tr>
        <td>Ngày cập nhật</td>
        <td>20/3</td>
    </tr>
    <tr>
        <td>Điều kiện tiên quyết</td>
        <td>Đã đăng nhập vào hệ thống bằng tài khoản của quản trị viên</td>
    </tr>
    <tr>
        <td>Kịch bản thường</td>
        <td>
            <ol type="1">
                <li>Sau khi quản trị viên đăng nhập vào hệ thống, có thể chọn danh mục quản lý người dùng</li>
                <li>Hệ thống chuyển đến giao diện quản lý người dùng.</li>
                <li>Quản trị viên chọn vào nút tạo tài khoản người dùng.</li>
                <li>Hệ thống chuyển sang giao diện tạo tài khoản người dùng</li>
                <li>Quản trị viên chọn vai trò cho người dùng gồm trưởng ban tổ chức hoặc trưởng đoàn và sau đó nhập đầy đủ các thông tin tài khoản người dùng</li>
                    <b>Có thể nhảy đến:</b>
                    <ol type="A" start="A">
                        <li>
                           Hệ thống thông báo thông tin nhập vào không hợp lệ
                        </li>
                    </ol>
                </li>
                <li>Hệ thống thông báo tạo tài khoản thành công và chuyển về giao diện quản lý người dùng</li>
            </ol>
        </td>
    </tr>
    <tr>
        <td>Kịch bản thay thế</td>
        <td>
        <ol type="A">
                <li>
                    Khi thông tin tài khoản nhập vào không hợp lệ</br>
                    Chuỗi A bắt đầu ở bước 5 của kịch bản thường.
                    <ol type="1" start="6">
                        <li>Hệ thống hiển thị lỗi và yêu cầu quản trị viên nhập laị thông tin tài khoản</li>
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
        <td>Tạo tài khoản người dùng thành công</td>
    </tr>
</table>