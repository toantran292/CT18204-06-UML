# Đặc tả class TaiKhoan

### 1. Thuộc tính
| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước| Min | Max | Diễn giải |
|---|---|---|---|---|---|---|---|
| idTaiKhoan | protected | String | null | 8 | | | id người dùng |
| tenDangNhap | protected | String | null | 30 | | | Tên đăng nhập hệ thống |
| matKhau | protected | String | null | 30 | | | Mật khẩu đăng nhập |
| email | protected | String | null | 30 | | | Email|
| hoTen | protected | String | null | 30 | | | Họ và tên |
| gioiTinh | protected | boolean | false | | | | Giới tính(true là nam, false là nữ) |
| ngaySinh | protected | Date | toDay() | | | toDate() | Ngày sinh |
| diaChi | protected | String | null | 30 | | | Địa chỉ|
| soDienThoai | protected | String | null | 10 | | | Số điện thoại|

### 2. Phương thức

<style>
table {
  border-collapse:collapse;
}

td {
  border: 1px solid #000;
  margin: 0;
  font-weight: bold;
  padding: 0.5em;
}
</style>

<table>
    <tr>
        <th>Tên phương thức</th>
        <th>Kiểu truy cập</th>
        <th>hanh sách các tham số</th>
        <th>Kiểu hữ liệu tham số</th>
        <th>Giá trị mặc nhiên</th>
        <th>Kích thước</th>
        <th>Kiểu trả về của phương thức</th>
        <th>Diễn giải</th>
    </tr>
    <tr>
      <td rowspan="3">themTaiKhoan</td>
      <td rowspan="3">public</td>
      <td colspan="4">Có 2 tham số</td>
      <td rowspan="3">TaiKhoan</td>
      <td rowspan="3">Thêm tài khoản người dùng</td>
    </tr><tr>
      <td colspan="1">tenDangNhap</td>
      <td colspan="1">String</td>
      <td colspan="1">null</td>
      <td colspan="1"></td>
    </tr>
    <tr>
      <td colspan="1">matKhau</td>
      <td colspan="1">String</td>
      <td colspan="1">null</td>
      <td colspan="1"></td>
    </tr>
    <tr>
      <td rowspan="3">kiemTraTKHopLe</td>
      <td rowspan="3">public</td>
      <td colspan="4">Có 2 tham số</td>
      <td rowspan="3">boolean</td>
      <td rowspan="3">Trả về kết quả kiểm tra, nếu tài khoản hợp lệ là true, ngược lại là false</td>
    </tr>
    <tr>
      <td>tenDangNhap</td>
      <td>String</td>
      <td>null</td>
      <td></td>
    </tr>
    <tr>
      <td>matKhau</td>
      <td>String</td>
      <td>null</td>
      <td></td>
    </tr>
    
</table>


  