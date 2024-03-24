# Đặc tả use case Sao lưu hệ thống

<table>
    <tr>
        <th>Tên usecase</th>
        <th>Sao lưu hệ thống</th>
    </tr>
    <tr>
        <td>Tóm tắt</td>
        <td>Sao lưu dữ liệu, cấu hình và các thành phần khác cần sao lưu</td>
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
                <li>Sau khi quản trị viên đăng nhập vào hệ thống, có thể chọn vào danh mục sao lưu hệ thống</li>
                <li>Hệ thống chuyển sang giao diện sao luư hệ thống</li>
                <li>Quản trị viên xác định dữ liệu, cấu hình và các thành phần khác cần sao lưu</li>
                <li>Quản trị viên chọn môi trường sao lưu bằng cách chọn các phương tiện lưu trữ phù hợp và thiết lập chu kỳ sao lưu</li>
                <li>Quản trị viên ấn nút sao lưu và xác nhận sao lưu</li>
                    <b>Có thể nhảy đến:</b>
                    <ol type="A" start="A">
                        <li>
                           Hệ thông thông báo sao lưu không thành công
                        </li>
                    </ol>
                </li>
                <li>Hệ thống thông báo sao lưu thành công</li>
            </ol>
        </td>
    </tr>
    <tr>
        <td>Kịch bản thay thế</td>
        <td>
        <ol type="A">
                <li>
                    Quá trình sao lưu gặp lỗi và sao lưu không thành công</br>
                    Chuỗi A bắt đầu ở bước 5 của kịch bản thường.
                    <ol type="1" start="6">
                        <li>Quản trị viên kiểm tra nguyên nhân gây lỗi sao lưu và thực hiện lại các bước sao lưu</li>
                    </ol>
                    Trở về bước 1 của kịch bản thường.
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
        <td>Sao lưu hệ thống thành công</td>
    </tr>
</table>