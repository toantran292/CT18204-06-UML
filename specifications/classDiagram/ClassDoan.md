# Đặc tả class Đoàn

### 1. Thuộc tính
| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước| Min | Max | Diễn giải |
|---|---|---|---|---|---|---|---|
| idDoan | private | string | null | 8|  |  |   |
| tenDoan | private | string | null | 30|  |  |   |

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
    <!-- -----------------------------themDoan------------------- -->
    <tr>
      <td rowspan="2">themDoan</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2">bool</td>
      <td rowspan="2">Thêm 1 đoàn thi đấu mới</td>
    </tr>
    <tr>
      <td>tenDoan</td>
      <td>string</td>
      <td>null</td>
      <td>30</td>
    </tr>
    <!-- -----------------------------xoaDoan------------------- -->
     <tr>
      <td>xoaDoan</td>
      <td>public</td>
      <td colspan="4">Có 0 tham số</td>
      <td>bool</td>
      <td>Xóa 1 đoàn thi đấu</td>
    </tr>
    <!-- -----------------------------suaThongTinDoan------------------- -->
     <tr>
      <td rowspan="2">suaThongTinDoan</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2">bool</td>
      <td rowspan="2">Sửa thông tin của 1 đoàn</td>
    </tr>
    <tr>
      <td>tenDoan</td>
      <td>string</td>
      <td>null</td>
      <td>30</td>
    </tr>
    <!-- --------xemThongTinDoan-------------- -->
    <tr>
      <td>xemThongTinDoan</td>
      <td>public</td>
      <td colspan="4">Có 0 tham số</td>
      <td>Doan</td>
      <td>Xem thông tin của 1 đoàn</td>
    </tr>
    <!-- -----------------------------themDoi------------------- -->
    <tr>
      <td rowspan="2">themDoi</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2">bool</td>
      <td rowspan="2">Thêm 1 đội thi đấu vào đoàn</td>
    </tr>
    <tr>
      <td>idDoi</td>
      <td>string</td>
      <td>null</td>
      <td>8</td>
    </tr>
    <!-- -----------------------------xoaDoi------------------- -->
     <tr>
      <td rowspan="2">xoaDoi</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2">bool</td>
      <td rowspan="2">Xóa 1 đội thi đấu khỏi đoàn</td>
    </tr>
    <tr>
      <td>idDoi</td>
      <td>string</td>
      <td>null</td>
      <td>8</td>
    </tr>
    <!-- --------layDSDoan-------------- -->
    <tr>
      <td>layDSDoan</td>
      <td>public</td>
      <td colspan="4">Có 0 tham số</td>
      <td>List < Doan ></td>
      <td>Lấy danh sách tất cả các đoàn</td>
    </tr>
    <!-- --------layDSDoanTheoTinh-------------- -->
     <tr>
      <td rowspan="2">layDSDoanTheoTinh</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2">List < Doan ></td>
      <td rowspan="2">Lấy danh sách tất cả đoàn trong 1 tỉnh</td>
    </tr>
    <tr>
      <td>idTinh</td>
      <td>string</td>
      <td>null</td>
      <td>8</td>
    </tr>
    <!-- ---------------------inDSDoan--------------- -->
    <tr>
      <td>inDSDoan</td>
      <td>public</td>
      <td colspan="4">Có 0 tham số</td>
      <td>bool</td>
      <td>In danh sách đoàn</td>
    </tr>
</table>
  