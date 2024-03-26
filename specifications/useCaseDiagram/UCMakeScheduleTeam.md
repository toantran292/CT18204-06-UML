# Đặc tả use case Lập lịch tập luyện

<table>
    <tr>
        <th>Tên use case</th>
        <th>Lập lịch tập luyện.</th>
    </tr>
    <tr>
        <td>Tóm tắt</td>
        <td>Lập lịch tập luyện cho đội.</td>
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
                <li>Trưởng đoàn chọn chức năng lập lịch tập luyện trong giao diện quản lý đội.</li>
                <li>Hệ thống hiện lên giao diện lập luyện của đội.</li>
                <li>Trưởng đoàn nhập thời gian tập luyện mong muốn, nội dung tập luyện,của đội nào và số lượng vận động viên tham gia.</li>
                <li>Trưởng đoàn bấm nút xác nhận.</li>
                <li>Hệ thống kiểm tra thời gian có hợp lệ.
                    <br/>
                    <b>Có thể nhảy đến:</b>
                    <ol type="A" start="A">
                        <li>
                            Thời gian không hợp lệ.
                        </li>
                    </ol>
                </li>
                <li>Hệ thống tạo lịch tập luyện.</li>
                <li>Hệ thống hiển thị thông báo “Tạo lịch tập luyện thành công”.</li>
                <li>Hệ thống chuyển về giao diện quản lý đội.</li>
            </ol>
        </td>
    </tr>
    <tr>
        <td>Kịch bản thay thế</td>
        <td>
        <ol type="A">
                <li>
                     Thời gian không hợp lệ. </br>
                    Chuỗi A bắt đầu ở bước 5 của kịch bản thường.
                    <ol type="1" start="6">
                        <li>Hệ thống hiển thị thông báo ”Thời gian không hợp lệ do trùng lịch tập hoặc chọn thời 
                        gian tập sai”.
                         <br/>
                        <b>Có thể nhảy đến:</b>
                        <ol type="A" start="A">
                            <li>
                                Trưởng đoàn chọn hủy.
                            </li>
                        </ol>
                        </li>
                    </ol>
                    Trở về bước 3 của kịch bản thường.
                </li>
            </ol>
            <ol type="a">
                <li>
                     Trưởng đoàn chọn hủy. </br>
                    Chuỗi a bắt đầu ở bước 6 của kịch bản thay thế A.<br/>
                    Trở về bước 8 của kịch bản thường.
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
        <td>Hoàn thành lập lịch tập luyện</td>
    </tr>
</table>