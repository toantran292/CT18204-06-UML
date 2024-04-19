# Đặc tả use case Xếp đội hình

<table>
    <tr>
        <th>Tên use case</th>
        <th>Xếp đội hình</th>
    </tr>
    <tr>
        <td>Tóm tắt</td>
        <td>Xếp đội hình mẫu.</td>
    </tr>
    <tr>
        <td>Actor</td>
        <td>Huấn luyện viên</td>
    </tr>
    <tr>
        <td>Phiên bản</td>
        <td>1.4.0</td>
    </tr>
    <tr>
        <td>Chịu trách nhiệm</td>
        <td>Trần Minh Trí</td>
    </tr>
    <tr>
        <td>Ngày tạo</td>
        <td>13/4</td>
    </tr>
    <tr>
        <td>Ngày cập nhật</td>
        <td>17/4</td>
    </tr>
    <tr>
        <td>Điều kiện tiên quyết</td>
        <td>Huấn luyện viên đã đăng nhập vào hệ thống.</td>
    </tr>
    <tr>
        <td>Kịch bản thường</td>
        <td>
            <ol type="1">
            <li>
                Huấn luyện viên vào giao diện quản lý đội hình.
            </li>
            <li>
                Hệ thống hiển thị giao diện quản lý đội hình.
            </li>
            <li>
                Huấn luyện viên chọn xếp đội hình.
            </li>
            <li>
                Hệ thống hiển thị giao diện xếp đội hình.
                <br/>
                    <b>Có thể nhảy đến:</b>
                    <ol type="A" start="A">
                        <li>
                            Huấn luyện viên nhấn nút thoát.
                        </li>
                    </ol>
            </li>
                <li>Huấn luyện viên chọn vận động viên từ danh sách vận động viên.
                </li>
                <li>Huấn luyện viên chọn vai trò cho vận động viên</li>
                <li>Huấn luyện viên nhấn nút xong.
                </li>
                <li>Hệ thống lưu vào đội hình mẫu.
                </li>
                <li>Hệ thống thông báo "Xếp đội hình thành công".</li>
                <li>Hệ thống hiển thị giao diện xếp đội hình.</li>
            </ol>
        </td>
    </tr>
    <tr>
        <td>Kịch bản thay thế</td>
        <td>
            <ol type="A">
            <li>
            Huấn luyện viên nhấn nút thoát. </br>
                        Chuỗi A bắt đầu ở bước 4 của kịch bản thường.
                        <ol type="1" start="5">
                            <li>Hệ thống thông báo "Các thay đổi chưa lưu".</li>
                        </ol>
                        Trở về giao diện xếp đội hình.
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
        <td>Cập nhật thành công  thông tin của vận động viên trong đội.</td>
    </tr>
</table>