# Đặc tả use case Cập nhật diễn biến trận đấu

<table>
    <tr>
        <th>Tên use case</th>
        <th>Cập nhật diễn biến trận đấu</th>
    </tr>
    <tr>
        <td>Tóm tắt</td>
        <td>Cho phép Trưởng ban tổ chức cập nhật liên tục các diễn biến của trận đấu đang diễn ra lên hệ thống để người hâm mộ có thể theo dõi.</td>
    </tr>
    <tr>
        <td>Actor</td>
        <td>Trưởng ban tổ chức.</td>
    </tr>
    <tr>
        <td>Phiên bản</td>
        <td>1.1</td>
    </tr>
    <tr>
        <td>Chịu trách nhiệm</td>
        <td>Hà Ngọc Linh</td>
    </tr>
    <tr>
        <td>Ngày tạo</td>
        <td>13/03/2024</td>
    </tr>
    <tr>
        <td>Ngày cập nhật</td>
        <td>12/03/2024</td>
    </tr>
    <tr>
        <td>Điều kiện tiên quyết</td>
        <td>Trưởng ban tổ chức được cấp tài khoản từ Quản trị viên và đăng nhập thành công vào hệ thống.</td>
    </tr>
    <tr>
        <td>Kịch bản thường</td>
        <td>
            <ol type="1">
                <li>Trưởng ban tổ chức sau khi đăng nhập vào hệ thống thì chọn danh mục Quản lý giải đấu.</li>
                <li>Hệ thống sẽ chuyển hướng đến giao diện Quản lý giải đấu.</li>
                <li>Trưởng ban tổ chức chọn vào Cập nhật diễn biến trận đấu.</li>
                    <b>Có thể nhảy đến:</b></br>
                    A1 - Trận đấu đã kết thúc.
                <li>Hệ thống sẽ chuyển hướng đến giao diện Cập nhật diễn biến trận đấu.</li>
                <li>Trưởng ban tổ chức chọn mục cần cập nhật là lỗi hay thành tích. Sau đó điền các thông tin cần cập nhật</li>
                    <b>Có thể nhảy đến:</b><br>
                    A2 - Trưởng ban tổ chức không nhập nữa và nhấn vào nút thoát.
                <li>Sau khi chỉnh sửa xong chọn lưu thay đổi, hệ thống sẽ kiểm tra tính hợp lệ.</li>
                    <b>Có thể nhảy đến:</b></br>
                    A3 - Thông tin không hợp lệ.
                <li>Hệ thống tiến hành lưu thay đổi.Thông báo thông tin được cập nhật thành công.</li>
                <li>Trở về giao diện Quản lý giải đấu.</li>
            </ol>
        </td> 
    </tr>
    <tr>
        <td>Kịch bản thay thế</td>
        <td>
            <b>A2 - Nhấn vào nút thoát.</b></br>
            Chuỗi A2 bắt đầu ở bước 5 của kịch bản thường.
            <ol type="1" start="6">
                <li>Thông báo đã thoát giao diện Cập nhật diễn biến trận đấu.</li>
            </ol>
            Trở về bước 4 của kịch bản thường.</br>
            <b>A3 - Thông tin không hợp lệ.</b></br>
            Chuỗi A3 bắt đầu ở bước 6 của kịch bản thường.</br>
            <ol type="1" start="7">
                <li>Thông báo lỗi nhập liệu cụ thể cho Trưởng ban tổ chức.</li>
            </ol>
            Trở về bước 5 của kịch bản thường.
        </td>
    </tr>
    <tr>
        <td>Kịch bản lỗi</td>
        <td>
            <b>A1 - Trận đấu đã kết thúc.</b></br>
            Chuỗi A1 bắt đầu ở bước 3 của kịch bản thường.</br>
            <ol type="1" start="4">
                <li>Báo lỗi trận đấu đã kết thúc.</li>
            </ol>
            Trở về bước 2 của kịch bản thường.
        </td>
    </tr>
    <tr>
        <td>Kết quả</td>
        <td>Cập nhật diễn biến trận đấu thành công lên hệ thống. </td>
    </tr>
</table>