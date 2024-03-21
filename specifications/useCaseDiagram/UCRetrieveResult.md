# Đặc tả use case Xem diễn biến trận đấu

| Tên use case |  |
| --- | ----- | 
| Kịch bản thường | 1. Người dùng truy cập vào hệ thống và chọn vào danh mục trận đấu|
| | 2.  | 
| | **Có thể nhảy đến** | 
| | A1 - Người dùng chọn vào chức năng tìm kiếm trận đấu | 
| | 3.  | 
| | 4. Hệ thống hiển thị diễn biết chi tiết của trận đấu |
| Kịch bản thay thế |  **A1** – Người dùng chọn vào chức năng tìm kiếm. |
| | Chuỗi A1 bắt đầu ở bước 2 của kịch bản thường. |
| | 3. Hệ thống hiển thị thanh tìm kiếm. |
| | 4. Người dùng nhập tên trận đấu vào thanh tìm kiếm và nhấn tìm kiếm.
| | Có thể nhảy đến:
| | A1.1 – Không tìm thấy trận đấu theo tên trận đấu người dùng cung cấp.
| | 5. Hệ thống hiển thị danh sách trận đấu theo tên trận đấu người dùng cung cấp.
| | Trở về bước 3 của kịch bản thường.
| | A1.1 – Không tìm thấy trận đấu theo tên trận đấu người dùng cung cấp.
| | Chuỗi A1.1 bắt đầu ở bước 4 của kịch bản thay thế A1.
| | 5. Hiển thị trận đấu không tìm thấy cho người dùng.
| | Trở lại bước 2 của kịch bản thường.

<table>
    <tr>
        <th>Tên use case</th>
        <th>Xem diễn biến trận đấu</th>
    </tr>
    <tr>
        <td>Tóm tắt</td>
        <td>Cho phép người sử dụng xem diễn biến của trận đấu</td>
    </tr>
    <tr>
        <td>Actor</td>
        <td></td>
    </tr>
    <tr>
        <td>Phiên bản</td>
        <td>1.0</td>
    </tr>
    <tr>
        <td>Chịu trách nhiệm</td>
        <td>Trần Thái Toàn</td>
    </tr>
    <tr>
        <td>Ngày tạo</td>
        <td>10/03/2024</td>
    </tr>
    <tr>
        <td>Ngày cập nhật</td>
        <td>21/03/2024</td>
    </tr>
    <tr>
        <td>Điều kiện tiên quyết</td>
        <td>Không có.</td>
    </tr>
    <tr>
        <td>Kịch bản thường</td>
        <td>
            <ol type="1">
                <li>Người dùng truy cập vào hệ thống và chọn vào danh mục trận đấu</li>
                <li>
                    Hệ thống hiển thị danh sách trận đấu </br>
                    <b>Có thể nhảy đến: </b>
                    <ol type="A">
                        <li>Người dùng nhập sai tên đăng nhập, mật khẩu.</li>
                    </ol>
                </li>
                <li>Người dùng chọn trận đấu cụ thể để xem diễn biến</li>
                <li>Hệ thống hiển thị diễn biết chi tiết của trận đấu</li>
            </ol>
        </td> 
    </tr>
    <tr>
        <td>Kịch bản thay thế</td>
        <td></td>
    </tr>
    <tr>
        <td>Kịch bản lỗi</td>
        <td></td>
    </tr>
    <tr>
        <td>Kết quả</td>
        <td>Hiện thị diễn biến trận đấu</td>
    </tr>
</table>