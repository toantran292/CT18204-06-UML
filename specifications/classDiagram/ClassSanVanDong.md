# Đặc tả class SanVanDong

### 1. Thuộc tính

| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước | Min | Max | Diễn giải            |
| -------------- | ------------- | ------------ | ----------------- | ---------- | --- | --- | -------------------- |
| idSVD          | public        | String       | null              | 8          |     |     | id sân vận động      |
| tenSVD         | public        | String       | null              | 100        |     |     | Tên của sân vận động |

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
      <td rowspan="2">LayDSSVD</td>
      <td rowspan="2">public</td>
      <td colspan="4">không có tham số</td>
      <td rowspan="2">boolean</td>
      <td rowspan="2">Trả về danh sách sân vận động</td>
    </tr>
    <td colspan="4"></td>
     <tr>
      <td rowspan="2">capNhatSVD</td>
      <td rowspan="2">public</td>
      <td colspan="4">có 1 tham số</td>
      <td rowspan="2">Bool</td>
      <td rowspan="2">Cập nhật thông tin sân vận động</td>
    </tr>
     <tr>
      <td>sanVanDong</td>
      <td>SanVanDong</td>
      <td></td>
      <td></td>
    </tr>
     <tr>
      <td rowspan="2">taoSVD</td>
      <td rowspan="2">public</td>
      <td colspan="4">có 1 tham số</td>
      <td rowspan="2">Bool</td>
      <td rowspan="2">Tạo sân vận động</td>
    </tr>
     <tr>
      <td>sanVanDong</td>
      <td>SanVanDong</td>
      <td></td>
      <td></td>
    </tr>

</table>
