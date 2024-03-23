# Đặc tả use case Xử lý yêu cầu chỉnh sửa thông tin viên

<table>
    <tr>
        <th>Tên use case</th>
        <th>Xử lý yêu cầu chỉnh sửa thông tin viên</th>
    </tr>
    <tr>
        <td>Tóm tắt</td>
        <td>Sửa thông tin của vận động viên khi vận động viên yêu cầu.</td>
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
        <td>Trưởng đoàn đã đăng nhập vào hệ thống.</td>
    </tr>
    <tr>
        <td>Kịch bản thường</td>
        <td>
            <ol type="1">
                <li>Trưởng đoàn nhận cái yêu cầu chỉnh sửa thông tin của vận động viên.</li>
                <li>Hệ thống hiện lên giao diện thông tin của vận động viên.</li>
                <li>Dựa vào nội dung yêu cầu sửa của vận động viên, trưởng đoàn có thể sửa, nếu có thông tin xác thực.
                </li>
                <li>Trưởng đoàn nhấn nút cập nhập.
                <br/>
                    <b>Có thể nhảy đến:</b>
                    <ol type="A" start="A">
                        <li>
                            Trưởng đoàn nhấn nút hủy.
                        </li>
                    </ol>
                </li>
                <li>Hệ thống cập nhật thông tin mới của vận động viên.
                </li>
                <li>Hệ thống thông báo "Cập nhật thành công".</li>
                <li>Hệ thống chuyển về giao diện quản lý vận động viên.</li>
            </ol>
        </td>
    </tr>
    <tr>
        <td>Kịch bản thay thế</td>
        <td>
            <ol type="A">
            <li>
            Trưởng đoàn nhấn nút hủy. </br>
                        Chuỗi A bắt đầu ở bước 4 của kịch bản thường.
                        <ol type="1" start="5">
                            <li>Hệ thống thông báo "Cập nhật thất bại".</li>
                        </ol>
                        Trở về bước 2 của kịch bản thường.
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