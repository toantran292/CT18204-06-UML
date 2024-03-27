# Đặc tả class LichTapLuyen

### 1. Thuộc tính
| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước| Min | Max | Diễn giải |
|---|---|---|---|---|---|---|---|
| idLichTap | private | String | null | 8 | | | id lịch tập luyện |
| ngayTap | private | Date | Date() | |Date() | | Ngày tập luyện |
| noiDung | private | String | null | | | | Nội dung tập luyện |
| diaChi | private | String | null |  | | | Địa chỉ tập luyện|

### 2. Phương thức


<table>
    <tr>
        <th>Tên phương thức</th>
        <th>Kiểu truy cập</th>
        <th>Danh sách các tham số</th>
        <th>Kiểu hữ liệu tham số</th>
        <th>Giá trị mặc nhiên</th>
        <th>Kích thước</th>
        <th>Kiểu trả về của phương thức</th>
        <th>Diễn giải</th>
    </tr>
    <tr>
      <td rowspan="5">lapLichDoi()</td>
      <td rowspan="5">public</td>
      <td colspan="4">Có 4 tham số</td>
      <td rowspan="5">LichTapLuyen</td>
      <td rowspan="5">Lập lịch tập luyện</td>
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
      <td colspan="1">diaChi</td>
      <td colspan="1">String</td>
      <td colspan="1">null</td>
      <td colspan="1"></td>
    </tr>
    <tr>
      <td colspan="1">doi</td>
      <td colspan="1">Doi</td>
      <td colspan="1">null</td>
      <td colspan="1"></td>
    </tr>
    <tr>
      <td rowspan="2">kiemTraLichTap()</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2">boolean</td>
      <td rowspan="2">Kiểm tra ngày tập,nếu ngày hợp lệ là true, ngược lại là false</td>
    </tr>
  <tr>
      <td colspan="1">ngayTap</td>
      <td colspan="1">Date</td>
      <td colspan="1"></td>
      <td colspan="1"></td>
    </tr>
</table>


  