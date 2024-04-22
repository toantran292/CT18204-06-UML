# Đặc tả sơ đồ tuần tự Xếp đội hình
*Người thiết kế:* Trần Minh Trí
<br/>
Sơ đồ này đặc tả cụ thể Use case "Xếp đội hình"
<br/>
***Mô tả chức năng:*** Cho phép huấn luyện viên có thể xếp đội hình mẫu để tham gia trận đấu.
<br/>
***Điều kiện tiên quyết:*** Huấn luyện viên đã đăng nhập vào hệ thống.
<br/>
***Trình thực hiện:***
<ol>
    <li> Sau khi Huấn luyện viên đăng nhập vào hệ thống ,Huấn luyện viên chọn chức năng quản lý đội hình.
    </li>
    <li>
    Hệ thống chuyển hướng đến giao diện quản lý đội hình. 
    </li>
    <li> Huấn luyện viên chọn xếp đội hình.
    </li>

**[Loop]**
    <li>
    Hệ thống chuyển hướng đến giao diện xếp đội hình. 
    </li>
    **[Lựu chọn]**
    <li>Huấn luyện viên bấm nút thoát.
    </li>
    <li>Hệ thống chuyển về giao diện xếp đội hình và kêt thúc vòng lặp [Loop].
    </li>
    <li>Gọi hàm layDSVDV() để lấy danh sách vận động viên gán và biến dsvdv.
    </li>
    <li>Trả về biến dsvdv.
    </li>
    <li>Chọn vận động viên
    </li>
    <li>Chọn vai trò cho vận động viên</li>
    <li>Huấn luyện viên bấm nút xong.</li>
    <li>Gọi hàm thietLapVaiTro với tham số id của vận động viên và tên vai trò để thiết lập vai trò cho vận động viên.</li>
    <li>Gửi thông báo xếp đội hình thành công và tiếp tục vòng lặp quay về **[Loop]**.</li>
</ol>
