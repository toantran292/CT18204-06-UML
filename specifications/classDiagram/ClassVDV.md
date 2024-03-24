# Đặc tả class Vận động viên

### 1. Thuộc tính
| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước| Min | Max | Diễn giải |
|---|---|---|---|---|---|---|---|
| chieuCao | private | number | 0 | | 0 | 3 |  Đơn vị: mét |
| canNang | private | number | 0 | | 0 | 1000 | Đơn vị: kilogam |

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
    <!-- -----------------------------xemThongTinCaNhan------------------- -->
     <tr>
      <td>layThongTin</td>
      <td>public</td>
      <td colspan="4">Có 0 tham số</td>
      <td>VDV</td>
      <td>Lấy thông tin của VDV</td>
    </tr>
    <!-- --------------------------yeuCauSuaThongTin------------------- -->
    <tr>
      <td rowspan="7">yeuCauSuaThongTin</td>
      <td rowspan="7">public</td>
      <td colspan="4">Có 6 tham số</td>
      <td rowspan="7">bool</td>
      <td rowspan="7">VDV gửi yêu cầu chỉnh sửa thông tin của mình</td>
    </tr>
    <tr>
      <td>hoTen</td>
      <td>string</td>
      <td>null</td>
      <td>30</td>
    </tr>
    <tr>
      <td>gioiTinh</td>
      <td>bool</td>
      <td>null</td>
      <td></td>
    </tr>
    <tr>
      <td>ngaySinh</td>
      <td>Date</td>
      <td>null</td>
      <td></td>
    </tr>
    <tr>
      <td>sdt</td>
      <td>string</td>
      <td>null</td>
      <td>10</td>
    </tr>
    <tr>
      <td>canNang</td>
      <td>number</td>
      <td>null</td>
      <td></td>
    </tr>
    <tr>
      <td>chieuCao</td>
      <td>number</td>
      <td>null</td>
      <td></td>
    </tr>
    <!-- --------layDSVDV-------------- -->
    <tr>
      <td>layDSVDV</td>
      <td>public</td>
      <td colspan="4">Có 0 tham số</td>
      <td>List < VDV ></td>
      <td>Lấy danh sách tất cả các VDV</td>
    </tr>
    <!-- ---------------------inDSVDV--------------- -->
    <tr>
      <td rowspan="2">inDSVDV</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 0 tham số</td>
      <td rowspan="2">bool</td>
      <td rowspan="2">In danh sách tất cả vận động viên</td>
    </tr>
</table>
  