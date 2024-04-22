# Sơ đồ tuần tự Cập nhật diễn biến trận đấu

### I. Người thiết kế: 
Hà Ngọc Linh B2207536
### II. Mô tả chức năng:
Cho phép Trưởng ban tổ chức cập nhật liên tục các diễn biến của trận đấu đang diễn ra lên hệ thống để người hâm mộ có thể theo dõi.
### III. Điều kiện tiên quyết:
Trưởng ban tổ chức được cấp tài khoản từ Quản trị viên và đăng nhập thành công vào hệ thống.
### IV. Trình tự thực hiện 
<ol>
    <li>Trưởng ban tổ chức sau khi đăng nhập vào hệ thống thì chọn danh mục Quản lý giải đấu.</li>
    <li>Hệ thống sẽ chuyển hướng đến giao diện Quản lý giải đấu.</li>
    <li>Trưởng ban tổ chức chọn danh mục Tạo giải đấu.</li>
    <li>Hệ thống sẽ lấy danh sách giải đấu và hiển thị lên màn hình.</li>
    <li>Trưởng ban tổ chức chọn giải đấu cần cập nhật.</li>
    <li>Hệ thống sẽ lấy danh sách các trận đấu của giải đấu đó và hiển thị lên màn hình.</li>
    <li>Trưởng ban tổ chức chọn trận đấu cần cập nhật.</li>
    <li>Hệ thống sẽ lấy danh sách các đội tham gia trận đấu đó và hiển thị lên màn hình.</li>
        [Rẽ nhánh]
        <ol type="1" start="9">
            <li>Nếu trận đấu đã kết thúc [trangThai == ketThuc]. Thông báo lỗi trận đấu đã kết thúc. Trở về giao diện Quản lý trận đâu. Kết thúc tiến trình. [Rẽ nhánh 1]</li>
            <li>Nếu trận đấu đang diễn ra [trangThai == dangDienRa]. Trưởng ban tổ chức tiến hành chọn đội cần cập nhật. [Rẽ nhánh 2]</li>
            <li>Hệ thống sẽ lấy danh sách các VDV của đội đó và hiển thị lên màn hình.</li>
            <li>Trưởng ban tổ chức chọn VDV cần cập nhật.</li>
            <li>Trưởng ban tổ chức chọn mục cần cập nhật là điểm hoặc lỗi.</li>
            <ol type="1" start="14">
                <li>Trưởng ban tổ chức chọn cập nhật điểm [Tùy chọn 1]</li>
                [Loop]
                <ol type="1" start="15">
                    <li>Trưởng ban tổ chức tiến hành cập nhật thông tin của điểm.</li>
                    <li>Trưởng ban tổ chức nhấn vào nút thoát. [Tùy chọn 1.1]</li>
                    <li>Hệ thống chuyển hướng đến giao diện Quản lý trận đấu. Kết thúc tiến trình.</li>
                    [Kết thúc tùy chọn 1.1]
                    <li>Trưởng ban tổ chức xác nhận thông tin cập nhật và nhấn cập nhật điểm.</li>
                    <li>Hệ thống gọi phương thức kiemTraHopLe() để kiểm tra tính hợp lệ của thông tin vừa nhập.</li>
                    <li>Trả về kết quả kiểm tra.</li>
                        [Rẽ nhánh]
                        <ol type="1" start="21">    
                            <li>Nếu thông tin vừa nhập không hợp lệ [ketqua == false]. Thông báo lỗi nhập liệu cụ thể cho trưởng ban tổ chức. Trở về giao diện Cập nhật thông tin trận đấu, tiếp tục vòng lặp. [Rẽ nhánh 2.1]</li>
                            <li>Ngược lại, nếu thông tin nhập hợp lệ [ketQua == true]. Hệ thống đồng thời tiến hành lưu thay đổi và gửi thông báo diễn biến mới đến những người dùng có quan tâm đến trận đấu. [Rẽ nhánh 2.2]</li>
                            <li>Hệ thống trả về thông báo Cập nhật điểm thành công.</li>
                            <li>Giao diện thông báo cho Trưởng ban tổ chức việc cập nhật điểm đã thành công. Hiển thi giao diện Quản lý trận đấu. Thoát khỏi vòng lặp.</li>
                        </ol>
                </ol>
                [Kết thúc tùy chọn 1]
            </ol>
            <ol type="1" start="25">
                <li>Trưởng ban tổ chức chọn cập nhật lỗi [Tùy chọn 2]</li>
                [Loop]
                <ol type="1" start="26">
                    <li>Trưởng ban tổ chức tiến hành cập nhật thông tin của lỗi.</li>
                    <li>Trưởng ban tổ chức nhấn vào nút thoát. [Tùy chọn 2.1]</li>
                    <li>Hệ thống chuyển hướng đến giao diện Quản lý trận đấu. Kết thúc tiến trình.</li>
                    [Kết thúc tùy chọn 2.1]
                    <li>Trưởng ban tổ chức xác nhận thông tin cập nhật và nhấn cập nhật lỗi.</li>
                    <li>Hệ thống gọi phương thức kiemTraHopLe() để kiểm tra tính hợp lệ của thông tin vừa nhập.</li>
                    <li>Trả về kết quả kiểm tra.</li>
                        [Rẽ nhánh]
                        <ol type="1" start="32">    
                            <li>Nếu thông tin vừa nhập không hợp lệ [ketqua == false]. Thông báo lỗi nhập liệu cụ thể cho trưởng ban tổ chức. Trở về giao diện Cập nhật thông tin trận đấu, tiếp tục vòng lặp. [Rẽ nhánh 2.3]</li>
                            <li>Ngược lại, nếu thông tin nhập hợp lệ [ketQua == true]. Hệ thống đồng thời tiến hành lưu thay đổi và gửi thông báo diễn biến mới đến những người dùng có quan tâm đến trận đấu. [Rẽ nhánh 2.4]</li>
                            <li>Hệ thống trả về thông báo Cập nhật lỗi thành công.</li>
                            <li>Giao diện thông báo cho Trưởng ban tổ chức việc Cập nhật lỗi đã thành công. Hiển thi giao diện Quản lý trận đấu. Thoát khỏi vòng lặp.</li>
                        </ol>
                </ol>
                [Kết thúc tùy chọn 2]
            </ol>
</ol>


#### Kết thúc

### V. Kết quả:
Thao tác Cập nhật diễn biến trận đấu thành công.