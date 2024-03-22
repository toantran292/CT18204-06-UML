# Đặc tả class NhaTaiTro

### 1. Thuộc tính
| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước| Min | Max | Diễn giải |
|---|---|---|---|---|---|---|---|
|id|public|String|null|8|||ID của nhà tài trợ.|
|tenNhaTaiTro|public|String|null|50|||Tên của nhà tài trợ.|
|logo|public|String|null|50|||Logo của nhà tài trợ.|
|diaChi|public|String|null|50|||Địa chỉ của nhà tài trợ.|
|trangWeb|public|String|null|50|||Link trang web của nhà tài trợ.|
|sdt|public|String|null|10|||Số điện thoại của nhà tài trợ.|

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
      <td rowspan="6">themNhaTaiTro()</td>
      <td rowspan="6">public</td>
      <td colspan="4">Có 5 tham số</td>
      <td rowspan="6">boolean</td>
      <td rowspan="6">Thêm Nhà tài trợ. Trả về true nếu thành công, false nếu thất bại. </td>
    </tr><tr>
      <td>tenNhaTaiTro</td>
      <td>String</td>
      <td>null</td>
      <td>50</td>
    </tr><tr>
      <td>logo</td>
      <td>String</td>
      <td>null</td>
      <td>50</td>
    </tr><tr>
      <td>diaChi</td>
      <td>String</td>
      <td>null</td>
      <td>100</td>
    </tr><tr>
      <td>trangWeb</td>
      <td>String</td>
      <td>null</td>
      <td>100</td>
    </tr><tr>
      <td>sdt</td>
      <td>String</td>
      <td>null</td>
      <td>10</td>
    </tr>
    <tr>
      <td rowspan="2">xoaNhaTaiTro()</td>
      <td rowspan="2">public</td>
      <td colspan="4">Không có tham số</td>
      <td rowspan="2">boolean</td>
      <td rowspan="2">Xóa Nhà tài trợ. Trả về true nếu thành công, false nếu thất bại.</td>
    </tr><tr>
      <td colspan="4"></td>
    </tr>
    <tr>
      <td rowspan="2">chinhSua()</td>
      <td rowspan="2">public</td>
      <td colspan="4">Không có tham số</td>
      <td rowspan="2">boolean</td>
      <td rowspan="2">Chỉnh sửa thông tin Nhà tài trợ. Trả về true nếu thành công, false nếu thất bại.</td>
    </tr><tr>
      <td colspan="4"></td>
    </tr>
</table>