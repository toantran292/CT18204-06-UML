# Đặc tả use case Tạo đội

<table>
    <tr>
        <th>Tên use case</th>
        <th>Tạo đội</th>
    </tr>
    <tr>
        <td>Tóm tắt</td>
        <td>Tạo đội tham gia giải đấu</td>
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
                <li>Trưởng đoàn chọn chức năng tạo đội trong giao diện quản lý đội.</li>
                <li>Hệ thống hiện lên giao diện tạo đội.</li>
                <li>Trưởng đoàn nhập các thông tin cho đội mới(tên ,số lượng vận động viên,...).</li>
                <li>Trưởng đoàn bấm nút xác nhận.</li>
                <li>Hệ thống kiểm tra tên đội.
                    <br/>
                    <b>Có thể nhảy đến:</b>
                    <ol type="A" start="A">
                        <li>
                            Tên đội bị trùng với tên đội đã có.
                        </li>
                    </ol>
                </li>
                <li>Hệ thống tạo ra 1 đội.</li>
                <li>Hệ thống hiển thị thông báo “Tạo đội thành công”.</li>
                <li>Hệ thống chuyển về giao diện quản lý đội.</li>
            </ol>
        </td>
    </tr>
    <tr>
        <td>Kịch bản thay thế</td>
        <td>
        <ol type="A">
                <li>
                    Tên đội bị trùng với tên đội đã có. </br>
                    Chuỗi A bắt đầu ở bước 5 của kịch bản thường.
                    <ol type="1" start="6">
                        <li>Hệ thống hiển thị thông báo”Tên đội không hợp lệ”.</li>
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
        <td>Hoàn thành tạo đội</td>
    </tr>
</table>