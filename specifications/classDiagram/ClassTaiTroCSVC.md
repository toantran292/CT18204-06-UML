# Đặc tả class TaiTroCSVC

### 1. Thuộc tính
| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước| Min | Max | Diễn giải |
|---|---|---|---|---|---|---|---|
|tenCSVC|public|Sting|null|50|||Tên cơ sở vật chất mà nhà tài trợ tài trợ cho giải đấu.|
|soLuong|public|int|0||0||Số lượng cơ sở vật chất cụ thể mà nhà tài trợ tài trợ cho giải đấu.|

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
      <td rowspan="2">layDSCSVC()</td>
      <td rowspan="2">public</td>
      <td colspan="4">Không có tham số</td>
      <td rowspan="2">List</td>
      <td rowspan="2">Trả về danh sách các CSVC đã 
 tài trợ cho giải đấu.</td>
    </tr><tr>
      <td colspan="4"></td>
    </tr>
    <tr>
      <td rowspan="3">taoTaiTroCSVC()</td>
      <td rowspan="4">public</td>
      <td colspan="4">Có 2 tham số</td>
      <td rowspan="3">boolean</td>
      <td rowspan="3">Tạo tài trợ CSVC cho giải đấu. Trả về true nếu thành công, false nếu thất bại.</td>
    </tr><tr>
      <td>tenCSVD</td>
      <td>String</td>
      <td>null</td>
      <td>50</td>
    </tr><tr>
      <td>soLuong</td>
      <td>int</td>
      <td>0</td>
      <td></td>
    </tr>
</table>
