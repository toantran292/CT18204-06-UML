# Đặc tả class VongLoai

### 1. Thuộc tính
| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước| Min | Max | Diễn giải |
|---|---|---|---|---|---|---|---|
| idVongLoai | public | String | null | 8 | | | tên vòng loại |
| tenVongLoai | public | String | null | 30 | | | tên vòng loại |

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
      <td rowspan="2">layDSTranDau</td>
      <td rowspan="2">public</td>
      <td colspan="4">Không có tham số</td>
      <td rowspan="2">List< TranDauLoai ></td>
      <td rowspan="2">Lấy danh sách trận đấu của vòng loại đang xét</td>
    </tr><tr>
      <td colspan="4"></td>
    </tr>
    <tr>
      <td rowspan="2">themTranDauLoai</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2"></td>
      <td rowspan="2">Thêm đội thi đấu vào trận đấu</td>
    </tr>
    <tr>
      <td>idTranDauLoai</td>
      <td>String</td>
      <td>null</td>
      <td>8</td>
    </tr>
    <tr>
      <td rowspan="2">xoaTranDauLoai</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2"></td>
      <td rowspan="2">Xóa đội thi đấu khỏi trận đấu</td>
    </tr>
    <tr>
      <td>idTranDauLoai</td>
      <td>String</td>
      <td>null</td>
      <td>8</td>
    </tr>
</table>


  