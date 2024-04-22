# Đặc tả use case Xử lý yêu cầu chỉnh sửa thông tin vận động viên

<table>
    <tr>
        <th>Tên use case</th>
        <th>Duyệt yêu cầu chỉnh sửa thông tin</th>
    </tr>
    <tr>
        <td>Tóm tắt</td>
        <td>Duyệt yêu cầu sửa thông tin của vận động viên khi vận động viên gửi yêu cầu.</td>
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
        <td>16/3</td>
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
                Huấn luyện viên chọn đơn yêu cầu của vận động viên.
            </li>
            <li>
                Hệ thống hiển thị giao diện các đơn yêu cầu.
            </li>
                <li>Huấn luyện viên chọn đơn yêu cầu của vận động viên.
                <br/>
                    <b>Có thể nhảy đến:</b>
                    <ol type="A" start="A">
                        <li>
                            Huấn luyện viên nhấn nút không cập nhật.
                        </li>
                    </ol>
                </li>
                <li>Huấn luyện viên nhấn nút cập nhập.
                </li>
                <li>Hệ thống cập nhật thông tin mới của vận động viên.Đổi trạng thái của đơn thành đã duyệt.
                </li>
                <li>Hệ thống thông báo "Cập nhật thành công".</li>
                <li>Hệ thống trở về giao diện các đơn yêu cầu.</li>
            </ol>
        </td>
    </tr>
    <tr>
        <td>Kịch bản thay thế</td>
        <td>
            <ol type="A">
            <li>
            Huấn luyện viên nhấn nút không cập nhật. </br>
                        Chuỗi A bắt đầu ở bước 3 của kịch bản thường.
                        <ol type="1" start="4">
                        <li>
                            Đổi trạng thái của đơn thành không thành công.
                        </li>
                            <li>Hệ thống thông báo "Đơn bị từ chối".</li>
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