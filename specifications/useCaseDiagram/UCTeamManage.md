# Đặc tả use case Quản lý đội

<table>
    <tr>
        <th>Tên use case</th>
        <th>Quản lý đội.</th>
    </tr>
    <tr>
        <td>Tóm tắt</td>
        <td>Quản lý đội.</td>
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
                <li>Trưởng đoàn chọn danh mục quản lý đội.</li>
                <li>Hệ thống hiện lên giao diện quản lý đội.</li>
                <li>Trưởng phòng chọn chức năng tạo đội trong các danh mục.
                <b>Có thể nhảy đến:</b>
                    <ol type="A" start="A">
                        <li>
                            Chọn chức năng thiết lập vai trò của vận động viên.
                        </li>
                        <li>
                            Chọn chức năng lập lịch tập luyện của toàn đội.
                        </li>
                        <li>
                            Chọn chức năng thêm vận động viên vào đội.
                        </li>
                    </ol>
                </li>
                <li>Bao gồm trường hợp sử dụng của “Tạo đội”.</li>
            </ol>
        </td>
    </tr>
    <tr>
        <td>Kịch bản thay thế</td>
        <td>
        <ol type="A">
            <li>
            Chọn chức năng thiết lập vai trò của vận động viên. </br>
                        Chuỗi A bắt đầu ở bước 3 của kịch bản thường.
                        <ol type="1" start="4">
                            <li>Bao gồm những trường hợp sử dụng của “Thiết lập vai trò của vận động viên”.</li>
                        </ol>
            </li>
            <li>
            Chọn chức năng lập lịch tập luyện của toàn đội. </br>
                        Chuỗi A bắt đầu ở bước 3 của kịch bản thường.
                        <ol type="1" start="4">
                            <li>Bao gồm những trường hợp sử dụng của “Lập lịch tập luyện của toàn đội”.</li>
                        </ol>
            </li>
            <li>
            Chọn chức năng thêm vận động viên vào đội.</br>
                        Chuỗi A bắt đầu ở bước 3 của kịch bản thường.
                        <ol type="1" start="4">
                            <li>Bao gồm những trường hợp sử dụng của “Thêm vận động viên vào đội”.</li>
                        </ol>
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
        <td>Hoàn thành quản lý đội.</td>
    </tr>
</table>
