# Đặc tả class Đội

### 1. Thuộc tính
| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước| Min | Max | Diễn giải |
|---|---|---|---|---|---|---|---|
| idDoi | private | string | null | 8|  |  |   |
| tenDoi | private | string | null | 30|  |  |   |

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
    <!-- -----------------------------taoDoi------------------- -->
    <tr>
      <td rowspan="2">taoDoi</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2">bool</td>
      <td rowspan="2">Tạo 1 đội thi đấu mới</td>
    </tr>
    <tr>
      <td>tenDoi</td>
      <td>string</td>
      <td>null</td>
      <td>30</td>
    </tr>
    <!-- -----------------------------xoaDoi------------------- -->
     <tr>
      <td>xoaDoi</td>
      <td>public</td>
      <td colspan="4">Có 0 tham số</td>
      <td>bool</td>
      <td>Xóa 1 đội thi đấu</td>
    </tr>
    <!-- --------xemThongTinDoi-------------- -->
    <tr>
      <td>xemThongTinDoi</td>
      <td>public</td>
      <td colspan="4">Có 0 tham số</td>
      <td>Doi</td>
      <td>Xem thông tin của đội</td>
    </tr>
    <!-- --------------------------suaThongTinDoi------------------- -->
    <tr>
      <td rowspan="2">suaThongTinDoi</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2">bool</td>
      <td rowspan="2">Cập nhật thông tin của 1 đội thi đấu</td>
    </tr><tr>
      <td>tenDoi</td>
      <td>string</td>
      <td>null</td>
      <td>30</td>
    </tr>
    <!-- --------layDSDoi-------------- -->
    <tr>
      <td>layDSDoi</td>
      <td>public</td>
      <td colspan="4">Có 0 tham số</td>
      <td>List < Doi ></td>
      <td>Lấy danh sách tất cả các đội</td>
    </tr>
    <!-- --------layDSVDV-------------- -->
    <tr>
      <td>layDSVDV</td>
      <td>public</td>
      <td colspan="4">Có 0 tham số</td>
      <td>List < VDV ></td>
      <td>Lấy danh sách tất cả các VDV có trong đội</td>
    </tr>
    <!-- ---------------------themVDV--------------- -->
    <tr>
      <td rowspan="2">themVDV</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2">bool</td>
      <td rowspan="2">Thêm 1 VDV vào đội thi đấu</td>
    </tr><tr>
      <td>idVDV</td>
      <td>string</td>
      <td>null</td>
      <td>8</td>
    </tr>
    <!-- ---------------------xoaVDV--------------- -->
    <tr>
      <td rowspan="2">xoaVDV</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2">bool</td>
      <td rowspan="2">Xóa 1 VDV khỏi đội thi đấu</td>
    </tr><tr>
      <td>idVDV</td>
      <td>string</td>
      <td>null</td>
      <td>8</td>
    </tr>
    <!-- ---------------------inDSDoi--------------- -->
    <tr>
      <td rowspan="2">inDSDoi</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 0 tham số</td>
      <td rowspan="2">bool</td>
      <td rowspan="2">In danh sách tất cả đội</td>
    </tr>
</table>
  