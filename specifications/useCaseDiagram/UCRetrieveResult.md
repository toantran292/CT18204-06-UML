# Đặc tả use case Xem diễn biến trận đấu loại

<table>
    <tr>
        <th>Tên use case</th>
        <th>Xem diễn biến trận đấu loại</th>
    </tr>
    <tr>
        <td>Tóm tắt</td>
        <td>Cho phép người sử dụng xem diễn biến của trận đấu loại</td>
    </tr>
    <tr>
        <td>Actor</td>
        <td></td>
    </tr>
    <tr>
        <td>Phiên bản</td>
        <td>1.4</td>
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
        <td>26/03/2024</td>
    </tr>
    <tr>
        <td>Điều kiện tiên quyết</td>
        <td>Không có.</td>
    </tr>
    <tr>
        <td>Kịch bản thường</td>
        <td>
            <ol type="1">
                <li>Người dùng truy cập vào hệ thống và chọn vào danh mục trận đấu loại</li>
                <li>
                    Hệ thống hiển thị danh sách trận đấu </br>
                    <b>Có thể nhảy đến: </b> </br>
                    A. Người dùng chọn vào chức năng tìm kiếm trận đấu
                </li>
                <li>Người dùng chọn trận đấu cụ thể để xem diễn biến</li>
                <li>Hệ thống hiển thị diễn biết chi tiết của trận đấu</li>
            </ol>
        </td> 
    </tr>
    <tr>
        <td>Kịch bản thay thế</td>
        <td>
            <ol type="A">
                <li>
                    Người dùng chọn vào chức năng tìm kiếm. </br>
                    Chuỗi A bắt đầu ở bước 2 của kịch bản thường.
                    <ol type="1" start="3">
                        <li>Hệ thống hiển thị thanh tìm kiếm.</li>
                        <li>
                            Người dùng nhập tên trận đấu vào thanh tìm kiếm và nhấn tìm kiếm. </br>
                            <b>Có thể nhảy đến:</b> </br>
                            I. Không tìm thấy trận đấu theo tên trận đấu người dùng cung cấp.
                        </li>
                        <li>Hệ thống hiển thị danh sách trận đấu theo tên trận đấu người dùng cung cấp.</li>
                    </ol>
                    Trở về bước 3 của kịch bản thường.
                </li>
            </ol>
            <ol type="I">
                <li>
                    Không tìm thấy trận đấu theo tên trận đấu người dùng cung cấp. </br>
                    Chuỗi I bắt đầu ở bước 4 của kịch bản thay thế A.
                    <ol type="1" start="5">
                        <li>Hiển thị trận đấu không tìm thấy cho người dùng.</li>
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
        <td>Hiện thị diễn biến trận đấu</td>
    </tr>
</table>