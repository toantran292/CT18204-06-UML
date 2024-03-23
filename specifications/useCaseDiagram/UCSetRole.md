# Đặc tả use case Thiết lập vai trò của vận động viên

<table>
    <tr>
        <th>Tên use case</th>
        <th>Thiết lập vai trò của vận động viên</th>
    </tr>
    <tr>
        <td>Tóm tắt</td>
        <td>Thiết lập vai trò cho mỗi vận động viên</td>
    </tr>
    <tr>
        <td>Actor</td>
        <td>Trưởng Đoàn</td>
    </tr>
    <tr>
        <td>Phiên bản</td>
        <td>1.3.0</td>
    </tr>
    <tr>
        <td>Chịu trách nhiệm</td>
        <td>Trần Minh Trí</td>
    </tr>
    <tr>
        <td>Ngày tạo</td>
        <td>16/3</td>
    </tr>
    <tr>
        <td>Ngày cập nhật</td>
        <td>21/3</td>
    </tr>
    <tr>
        <td>Điều kiện tiên quyết</td>
        <td>Trưởng đoàn đã đăng nhập vào hệ thống. Trưởng đoàn chọn chức năng quản lý đội.</td>
    </tr>
    <tr>
        <td>Kịch bản thường</td>
        <td>
            <ol type="1">
                <li>Trưởng đoàn chọn chức năng thiết lập vai trò của vận động viên trong giao diện quản lý đội.</li>
                <li>Hệ thống hiện lên giao diện vai trò của toàn đội.</li>
                <li>Trưởng đoàn thêm vai trò của vận động viên bất kì.
                <br/>
                    <b>Có thể nhảy đến:</b>
                    <ol type="A" start="A">
                        <li>
                            Trưởng đoàn nhấn nút hủy.
                        </li>
                    </ol>
                </li>
                <li>Trưởng đoàn bấm nút xác nhận.</li>
                <li>Hệ thống thêm vai trò của vận động viên trong đội.
                </li>
                <li>Hệ thống hiển thị thông báo “Thêm vai trò thành công”.</li>
                <li>Hệ thống chuyển về giao diện quản lý đội.</li>
            </ol>
        </td>
    </tr>
    <tr>
        <td>Kịch bản thay thế</td>
        <td>
        Trưởng đoàn nhấn nút hủy. </br>
                    Chuỗi A bắt đầu ở bước 3 của kịch bản thường.
                    <ol type="1" start="4">
                        <li>Hệ thống thông báo "Cập nhật thất bại".</li>
                    </ol>
                    Trở về bước 2 của kịch bản thường.
        </td>
    </tr>
    <tr>
        <td>Kịch bản lỗi</td>
        <td></td>
    </tr>
    <tr>
        <td>Kết quả</td>
        <td>Hoàn thành thêm vai trò của vận động viên.</td>
    </tr>
</table>