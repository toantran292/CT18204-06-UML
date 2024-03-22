# Đặc tả use case Tạo giải đấu

<table>
    <tr>
        <th>Tên use case</th>
        <th>Tạo giải đấu</th>
    </tr>
    <tr>
        <td>Tóm tắt</td>
        <td>Cho phép Trưởng ban tổ chức tạo một giải đấu mới.</td>
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
        <td>19/03/2024</td>
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
                <li>Trưởng ban tổ chức chọn danh mục Tạo giải đấu.</li>
                <li>Hệ thống sẽ chuyển hướng đến giao diện Tạo giải đấu.</li>
                <li>Trưởng ban tổ chức điền các thông tin để tạo giải đấu mới như: tên, ngày tổ chức, cơ cấu giải thưởng,...</li>
                    <b>Có thể nhảy đến:</b><br>
                    A1 - Trưởng ban tổ chức không nhập nữa và nhấn vào nút thoát.
                <li>Sau khi chỉnh sửa xong chọn tạo giải đấu, hệ thống sẽ kiểm tra tính hợp lệ.</li>
                    <b>Có thể nhảy đến:</b></br>
                    A2 - Thông tin không hợp lệ.
                <li>Hệ thống tiến hành lưu thay đổi.Thông báo giải đấu được tạo thành công.</li>
                <li>Trở về giao diện Quản lý giải đấu.</li>
            </ol>
        </td> 
    </tr>
    <tr>
        <td>Kịch bản thay thế</td>
        <td>
            <b>A1 - Nhấn vào nút thoát.</b></br>
            Chuỗi A1 bắt đầu ở bước 5 của kịch bản thường.
            <ol type="1" start="6">
                <li>Thông báo đã thoát giao diện tạo giải đấu.</li>
            </ol>
            Trở về bước 2 của kịch bản thường.</br>
            <b>A2 - Thông tin không hợp lệ.</b></br>
            Chuỗi A2 bắt đầu ở bước 6 của kịch bản thường.</br>
            <ol type="1" start="7">
                <li>Thông báo lỗi nhập liệu cụ thể cho Trưởng ban tổ chức.</li>
            </ol>
            Trở về bước 5 của kịch bản thường.
        </td>
    </tr>
    <tr>
        <td>Kịch bản lỗi</td>
        <td></td>
    </tr>
    <tr>
        <td>Kết quả</td>
        <td>Tạo giải đấu mới thành công.</td>
    </tr>
</table>