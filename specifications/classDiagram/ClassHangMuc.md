# Đặc tả class HangMuc

### 1. Thuộc tính
| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước| Min | Max | Diễn giải |
|---|---|---|---|---|---|---|---|
| idHangMuc | protected | String | null | 8 | | | id hạng mục thi đấu |
| tenHangMuc | public | String | null | | | | Tên hạng mục thi đấu |
| gioiTinh | public | boolean | false | | | | Giới tính thi đấu của hạng mục |

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
      <td rowspan="3">taoHangMuc</td>
      <td rowspan="3">public</td>
      <td colspan="4">Có 2 tham số</td>
      <td rowspan="3">boolean</td>
      <td rowspan="3">Trả về  kết quả nếu tạo được là true, ngược lại là false</td>
    </tr>
    <tr>
      <td>tenHangMuc</td>
      <td>String</td>
      <td>null</td>
      <td></td>
    </tr>
    <tr>
      <td>gioiTinh</td>
      <td>boolean</td>
      <td>false</td>
      <td></td>
    </tr>
</table>


  