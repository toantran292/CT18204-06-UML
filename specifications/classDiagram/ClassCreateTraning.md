# Đặc tả class LichTapLuyen

### 1. Thuộc tính
| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước| Min | Max | Diễn giải |
|---|---|---|---|---|---|---|---|
| idLichTap | private | String | null | 8 | | | id lịch tập luyện |
| ngayTap | private | Date | Date() | |Date() | | Ngày tập luyện |
| noiDung | private | String | null | | | | Nội dung tập luyện |
| soLuong | private | int | 0 |  | | Count(List<DsVDV>) | Số lượng người tham gia|

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
      <td rowspan="4">lapLich()</td>
      <td rowspan="4">public</td>
      <td colspan="4">Có 3 tham số</td>
      <td rowspan="4">LichTapLuyen</td>
      <td rowspan="4">Lập lịch tập luyện</td>
    </tr><tr>
      <td colspan="1">ngayTap</td>
      <td colspan="1">Date</td>
      <td colspan="1">Date()</td>
      <td colspan="1"></td>
    </tr>
    <tr>
      <td colspan="1">noiDung</td>
      <td colspan="1">String</td>
      <td colspan="1">null</td>
      <td colspan="1"></td>
    </tr>
    <tr>
      <td colspan="1">soLuong</td>
      <td colspan="1">int</td>
      <td colspan="1">null</td>
      <td colspan="1"></td>
    </tr>
    
</table>


  