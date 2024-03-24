# Đặc tả class TaiTroTaiChinh

### 1. Thuộc tính
| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước| Min | Max | Diễn giải |
|---|---|---|---|---|---|---|---|
|soTien|public|long|0||0||Số tiền mà nhà tài trợ tài trợ cho giải đấu.|

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
      <td rowspan="2">tinhTongTien()</td>
      <td rowspan="2">public</td>
      <td colspan="4">Không có tham số</td>
      <td rowspan="2">long</td>
      <td rowspan="2">Trả về tổng số tiền được tài trợ của giải đấu.</td>
    </tr><tr>
      <td colspan="4"></td>
    </tr>
    <tr>
      <td rowspan="2">taoTaiTroTC()</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2">boolean</td>
      <td rowspan="2">Tạo tài trợ tài chính cho giải đấu. Trả về true nếu thành công, false nếu thất bại.</td>
    </tr><tr>
      <td>soTien</td>
      <td>long</td>
      <td>0</td>
      <td></td>
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
  