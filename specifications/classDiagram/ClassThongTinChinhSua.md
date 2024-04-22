# Đặc tả class ThongTinChinhSua

### 1. Thuộc tính
| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước| Min | Max | Diễn giải |
|---|---|---|---|---|---|---|---|
| idDon | public | String | null | 8 | | | id đơn thông tin chỉnh sửa |
| noiDung | public | VanDongVien | null | 100 | | | nội dung của thông tin cần chỉnh sửa |

### 2. Phương thức


<table>
    <tr>
        <th>Tên phương thức</th>
        <th>Kiểu truy cập</th>
        <th>Danh sách các tham số</th>
        <th>Kiểu dữ liệu tham số</th>
        <th>Giá trị mặc nhiên</th>
        <th>Kích thước</th>
        <th>Kiểu trả về của phương thức</th>
        <th>Diễn giải</th>
    </tr>
    <tr>
      <td rowspan="2">layDSDonThongTin</td>
      <td rowspan="2">public</td>
      <td colspan="4">Không có tham số</td>
      <td rowspan="2">List < ThongTinChinhSua ></td>
      <td rowspan="2">Lấy danh sách các đơn yêu cầu chỉnh sửa</td>
    </tr><tr>
      <td colspan="4"></td>
    </tr>
    <tr>
      <td rowspan="3">luuThongTinChinhSua</td>
      <td rowspan="3">public</td>
      <td colspan="4">Có 2 tham số</td>
      <td rowspan="3">bool</td>
      <td rowspan="3">Lưu thông tin chỉnh sửa</td>
    </tr>
    <tr>
      <td>idVanDongVien</td>
      <td>String</td>
      <td>null</td>
      <td>8</td>
    </tr>
    <tr>
      <td>noiDung</td>
      <td>String</td>
      <td>null</td>
      <td>100</td>
    </tr>
</table>


  