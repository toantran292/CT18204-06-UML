# Đặc tả class GiaiDau

### 1. Thuộc tính
| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước| Min | Max | Diễn giải |
|---|---|---|---|---|---|---|---|
|id|public|String|null|8|||ID của giải đấu.|
|ten|public|String|null|50|||Tên của giải đấu.|
|ngayToChuc|public|Date|Date()||||Ngày tổ chức giải đấu.|
|coCauGiaiThuong|public|String|null|1000|||Cơ cấu giải thưởng của giải đấu.|
|trangThai|public|String|null|50|||Trạng thái hiện tại của giải đấu.|

### 2. Phương thức

<table>
    <tr>
        <td>Tên phương thức</td>
        <td>Kiểu truy cập</td>
        <td>Danh sách các tham số</td>
        <td>Kiểu dữ liệu tham số</td>
        <td>Giá trị mặc nhiên</td>
        <td>Kích thước</td>
        <td>Kiểu trả về của phương thức</td>
        <td>Diễn giải</td>
    </tr>
    <tr>
      <td rowspan="5">taoGiaiDau()</td>
      <td rowspan="5">public</td>
      <td colspan="4">Có 4 tham số</td>
      <td rowspan="5">boolean</td>
      <td rowspan="5">Tạo giải đấu mới. Trả về true nếu thành công, false nếu thất bại. </td>
    </tr>
    <tr>
      <td>ten</td>
      <td>String</td>
      <td>null</td>
      <td>50</td>
    </tr>
    <tr>
      <td>ngayToChuc</td>
      <td>Date</td>
      <td>Date()</td>
      <td></td>
    </tr>
    <tr>
      <td>coCauGiaiThuong</td>
      <td>String</td>
      <td>null</td>
      <td>1000</td>
    </tr>
    <tr>
      <td>trangThai</td>
      <td>String</td>
      <td>null</td>
      <td>50</td>
    </tr>
    <tr>
      <td rowspan="5">kiemTraThongTin()</td>
      <td rowspan="5">public</td>
      <td colspan="4">Có 4 tham số</td>
      <td rowspan="5">boolean</td>
      <td rowspan="5">Kiểm tra thông tin của giải đấu. Trả về true nếu thông tin hợp lệ, false nếu không hợp lệ. </td>
    </tr>
    <tr>
      <td>ten</td>
      <td>String</td>
      <td>null</td>
      <td>50</td>
    </tr>
    <tr>
      <td>ngayToChuc</td>
      <td>Date</td>
      <td>Date()</td>
      <td></td>
    </tr>
    <tr>
      <td>coCauGiaiThuong</td>
      <td>String</td>
      <td>null</td>
      <td>1000</td>
    </tr>
    <tr>
      <td>trangThai</td>
      <td>String</td>
      <td>null</td>
      <td>50</td>
    </tr>
    <tr>
      <td rowspan="2">suaThongTin()</td>
      <td rowspan="2">public</td>
      <td colspan="4">Không có tham số</td>
      <td rowspan="2">boolean</td>
      <td rowspan="2">Sửa thông tin của giải đấu. Trả về true nếu thành công, false nếu thất bại.</td>
    </tr>
    <tr>
      <td colspan="4"></td>
    </tr>
    <tr>
      <td rowspan="2">inThongTin()</td>
      <td rowspan="2">public</td>
      <td colspan="4">Không có tham số</td>
      <td rowspan="2">boolean</td>
      <td rowspan="2">In thông tin của giải đấu. Trả về true nếu thành công, false nếu thất bại. </td>
    </tr>
    <tr>
      <td colspan="4"></td>
    </tr>
    <tr>
      <td rowspan="2">layDSGiaiDau()</td>
      <td rowspan="2">public</td>
      <td colspan="4">Không có tham số</td>
      <td rowspan="2">List</td>
      <td rowspan="2">Trả về danh sách giải đấu.</td>
    </tr>
    <tr>
      <td colspan="4"></td>
    </tr>
</table>

<!-- 

<tr>
  <td rowspan="2">phuongThucMot</td>
  <td rowspan="2">public</td>
  <td colspan="4">Có 1 tham số</td>
  <td rowspan="2">int</td>
  <td rowspan="2">diễn giải ở đây</td>
</tr><tr>
  <td>tenThamSo</td>
  <td></td>
  <td></td>
  <td></td>
</tr>

Copy đoạn trên để thêm một phương thức mới
-->
  