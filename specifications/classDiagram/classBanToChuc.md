# Đặc tả class BanToChuc

### 1. Thuộc tính
| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước | Min | Max | Diễn giải |
| -------------- | ------------- | ------------ | ----------------- | ---------- | --- | --- | --------- |

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
      <td rowspan="2">taoBTC()</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2">boolean</td>
      <td rowspan="2">Thêm Ban tổ chức. Trả về true nếu thành công, false nếu thất bại.</td>
    </tr><tr>
      <td>idTruongBanToChuc</td>
      <td>String</td>
      <td>Null</td>
      <td>8</td>
    </tr>
    <tr>
      <td rowspan="2">xoaBTC()</td>
      <td rowspan="2">public</td>
      <td colspan="4">Không có tham số</td>
      <td rowspan="2">boolean</td>
      <td rowspan="2">Xóa Ban tổ chức. Trả về true nếu thành công, false nếu thất bại.</td>
    </tr><tr>
      <td colspan="4"></td>
    </tr>
    <tr>
      <td rowspan="2">layDSTruongBTC()</td>
      <td rowspan="2">public</td>
      <td colspan="4">Không có tham số</td>
      <td rowspan="2">List</td>
      <td rowspan="2">Lấy danh sách Trưởng ban tổ chức.</td>
    </tr><tr>
      <td colspan="4"></td>
    </tr>
</table>