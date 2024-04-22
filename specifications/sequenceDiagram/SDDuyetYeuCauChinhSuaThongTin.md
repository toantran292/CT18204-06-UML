# Đặc tả sơ đồ tuần tự Duyệt yêu cầu chỉnh sửa thông tin
*Người thiết kế:* Trần Minh Trí
<br/>
Sơ đồ này đặc tả cụ thể Use case "Duyệt yêu cầu chỉnh sửa thông tin"
<br/>
***Mô tả chức năng:*** Cho phép huấn luyện viên có thể duyệt yêu cầu chỉnh sửa thông tin của vận động viên.
<br/>
***Điều kiện tiên quyết:*** Huấn luyện viên đã đăng nhập vào hệ thống.
<br/>
***Trình thực hiện:***
<ol>
    <li> Sau khi Huấn luyện viên đăng nhập vào hệ thống ,Huấn luyện viên chọn quản lý yêu cầu chỉnh sửa của các vận động viên.
    </li>
    <li>
        Hệ thống gọi layDanhSachDonChuaDuyet gán vào biến ds để lấy các đơn có trạng thái chưa duyệt.
    </li>
    <li>Trả về biến ds.</li>
    <li>
    Hệ thống chuyển hướng đến giao diện các đơn yêu cầu của vận động viên. 
    </li>
    <li> Huấn luyện viên chọn đơn yêu cầu của vận động viên.
    </li>
    <li>Hệ thống lấy thông tin của vận động viên được chọn và trả về kết quả thông tin.</li>
<li>
    Hệ thống hiển thị thông tin chi tiết đơn.
</li>

**[Lựu chọn]**
    <li>
    Huấn luyện viên nhập các thông tin được yêu cầu sửa.
    </li>
    <li>
    Huấn luyện viên chọn nút cập nhật.
    </li>
    <li>Hệ thống kiểm tra thông tin vừa nhập có hợp lệ</li>
**[Nếu hợp lệ]**
    <li>Hệ thống cập nhật trạng thái đơn thành đã duyệt.
    </li>
    <li>Hệ thống gọi luuThongTinChinhSua() để lưu thông tin chỉnh sửa của vận động viên.Đồng thời gửi thông bao cho vận đông viên qua guiThongBao().
    </li>
    <li>Thông báo cập nhật thành công.
    </li>
<li>Trở về giao diện các đơn yêu cầu của vận động viên.
    </li>

**[Nếu không hợp lệ]**
<li>
    Hệ thống thông báo thông tin không hợp lệ.
</li>
<li>Trở về giao diện các đơn yêu cầu của vận động viên.
    </li>

**[Lựu chọn]**
     <li>
    Huấn luyện viên chọn nút từ chối cập nhật. 
    </li>
    <li>Hệ thống cập nhật trạng thái đơn thành từ chối cập nhật.
    </li>
    <li>Thông báo đơn bị từ chối.
    </li>
    <li>Trở về giao diện các đơn yêu cầu của vận động viên.
    </li>
</ol>
