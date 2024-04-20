# Sơ đồ tuần tự Gửi yêu cầu Đăng ký tham gia giải đấu

### I. Người thiết kế:

Nguyễn Tuấn Đạt B2203499

### II. Mô tả chức năng:

Cho phép trưởng đoàn đăng ký tham gia giả đấu

### III. Điều kiện tiên quyết:

Trưởng đoàn được cấp tài khoản từ Quản trị viên và đăng nhập thành công vào hệ thống.

### IV. Trình tự thực hiện

<ol>
    <li>Trưởng đoàn sau khi đăng nhập vào hệ thống thì chọn vào danh mục danh sách giải đấu</li>
    <li>Hệ thống gọi phương thức layDSGiaiDau để lấy ra danh sách giải đấu</li>
    <li>Cơ sở dữ liệu trả về danh sách giải đấu</li>
    <li>Giao diện hiển thị danh sách giải đấu</li>
    <li>Trưởng đoàn chọn giải đấu cần đăng ký tham gia</li>
    <li>Hệ thống gọi phương thức layGiaiDauTheoId để lấy ra thông tin chi tiết giải đấu đã chọn</li>
    <li>Cơ sơ dữ liệu trả về thông tin chi tiết giải đấu đã chọn</li>
    <li>Hệ thống hiển thị giao diện chi tiết giải đấu</li>
    <li>Trưởng đoàn chọn chức năng đăng ký tham gia giải đấu</li>
    <li>Hiển thị giao diện đăng ký tham gia giải đấu</li>
      [Loop]</br>
    <li>Trưởng đoàn không đăng ký tham gia nữa và nhấn nút thoát. [Tùy chọn]</li>  
    <li>Giao diện hiển thị chi tiết giải đấu trước đó</li>
    <li>Trưởng đoàn nhấn nút thêm hạng mục thi đấu cần đăng ký</li>
    <li>Hệ thống gọi phương thức layDSHangMuc để lấy ra danh sách hạng mục thi đấu</li>
    <li>Cơ sở dữ liệu trả về danh sách hạng mục thi đấu</li>
    <li>Giao diện hiển thị danh sách hạng mục thi đấu</li>
    <li>Trưởng đoàn nhấn chọn hạng mục thi đấu cần tham gia</li>
    <li>Trưởng đoàn nhấn vào nút thêm đội tham gia hạng mục đã chọn</li>
    <li>Hệ thống gọi phương thức layDSDoiTheoDoan để lấy danh sách đội theo đoàn mà trưởng đoàn đang quản lý</li>
    <li>Cơ sở dữ liệu trả về danh sách các đội theo đoàn mà trưởng đoàn đang quản lý</li>
    <li>Giao diện hiển thị danh sách đội</li>
    <li>Trưởng đoàn nhấn chọn các đội tham gia hạng mục đã chọn</li>
    <li>Trưởng đoàn không đăng ký thêm hạng mục thi đấu và nhấn nút đăng ký tham gia. [Tùy chọn]</li>
    <li>Hệ thống gọi phương thức DKGiaiDau để đăng ký giải đấu</li>
    <li>Hệ thống trả về kết quả đăng ký giải đấu</li>
    [Rẽ nhánh]
    <li>Nếu đăng ký thành công [kq == true]. Thông báo đăng ký tham gia giải đấu thành công cho trưởng đoàn</li>
    <li>Nếu đăng ký không thành công [kq == false]. Thông báo không thể đăng ký tham gia giải đấu cho trưởng đoàn</li>
    <li>Giao diện hiển thị chi tiết trận đấu trước đó</li>

#### Kết thúc

### V. Kết quả:

Thao tác đăng ký tham gia giải đấu thành công
