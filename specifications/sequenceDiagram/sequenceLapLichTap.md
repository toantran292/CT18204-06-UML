# Đặc tả sơ đồ tuần tự Lập lịch tập luyện
*Người thiết kế:* Trần Minh Trí
<br/>
Sơ đồ này đặc tả cụ thể Use case "Lập lịch tập luyện"
<br/>
***Mô tả chức năng:*** Cho phép trưởng đoàn có thể lập lịch tập luyện cho đội.
<br/>
***Điều kiện tiên quyết:*** Trưởng đoàn đã đăng nhập vào hệ thống.
<br/>
***Trình thực hiện:***
<ol>
    <li> Sau khi trưởng đoàn đăng nhập vào hệ thống ,trưởng đoàn chọn chức năng quản lý đội.
    </li>
    <li>
    Hệ thống chuyển hướng đến giao diện quản lý đội. 
    </li>
    <li> Trưởng đoàn chọn chức năng lập lịch tập luyện.
    </li>
    <li>
    Hệ thống chuyển hướng đến giao diện lập lịch tập luyện. 
    <br/> 
    </li>

**[Loop]**
    <li>Trưởng Đoàn nhập thời gian tập luyện mong muốn, nội dung tập luyện,của đội nào và số lượng vận động viên tham gia.
    </li>
    <li>Trưởng đoàn bấm nút "Xác nhận".
    </li>
    <li>Gọi hàm kiemTraLichTap() với tham số là ngayTap vừa nhập có hợp lệ và gán kết quả trả về vào biến KQ.
    </li>
    <li>Trả về kết quả kiểm tra.
    </li>
**[Rẽ nhánh]**
    <li>Nếu ngày nhập hợp lệ [KQ==true] thì gọi hàm lapLichDoi() với các tham số là các thông tin vừa nhập. Trở về giao diện quản lý đội, thông báo "Tạo lịch thành công". Thoát khỏi vòng lặp.Kết thúc
    </li>
    <li>Ngược lại [KQ==false] thông báo "Thời gian không hợp lệ" tiếp tục òng lặp quay về **[Loop]**</li>
**[Tùy chọn]**
    <li>Nếu trưởng đoàn chọn "Hủy" </li>
    <li>Quay về giao diện quản lý đội . Kết thúc vòng lặp.</li>
</ol>
