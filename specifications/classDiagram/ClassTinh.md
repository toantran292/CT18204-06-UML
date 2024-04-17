# Đặc tả class Tỉnh

### 1. Thuộc tính
| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước| Min | Max | Diễn giải |
|---|---|---|---|---|---|---|---|
| idTinh | private | string | null | 8|  |  |   |
| tenTinh | private | string | null | 30|  |  |   |
| cap | private | string | null | 20|  |  |   |

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
    <!-- -----------------------------themTinh------------------- -->
    <!-- <tr>
      <td rowspan="2">themTinh</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2">bool</td>
      <td rowspan="2">Thêm 1 tỉnh thi đấu mới</td>
    </tr>
    <tr>
      <td>tenTinh</td>
      <td>string</td>
      <td>null</td>
      <td>30</td>
    </tr> -->
    <!-- -----------------------------xoaTinh------------------- -->
     <!-- <tr>
      <td>xoaTinh</td>
      <td>public</td>
      <td colspan="4">Có 0 tham số</td>
      <td>bool</td>
      <td>Xóa 1 tỉnh thi đấu</td>
    </tr> -->
    <!-- --------xemThongTinTinh-------------- -->
    <!-- <tr>
      <td>xemThongTinTinh</td>
      <td>public</td>
      <td colspan="4">Có 0 tham số</td>
      <td>Tinh</td>
      <td>Xem thông tin của 1 tỉnh</td>
    </tr> -->
    <!-- taiDSTinhVietNam -->
    <tr>
      <td rowspan="2">taiDSTinhVietNam</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2">bool</td>
      <td rowspan="2">Tải thông tin 63 tỉnh thành lên hệ thống, trả về kết quả tải có thành công hay không</td>
    </tr>
    <tr>
      <td>duLieu</td>
      <td>List < String > </td>
      <td>null</td>
      <td>30</td>
    </tr> 
    <!-- -----------------------------suaThongTinTinh-------------------->
     <tr>
      <td rowspan="2">suaThongTinTinh</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2">bool</td>
      <td rowspan="2">Sửa thông tin của 1 tỉnh</td>
    </tr>
    <tr>
      <td>tenTinh</td>
      <td>string</td>
      <td>null</td>
      <td>30</td>
    </tr>
    <!-- --------layDSTinh-------------- -->
    <tr>
      <td>layDSTinh</td>
      <td>public</td>
      <td colspan="4">Có 0 tham số</td>
      <td>List < Tinh ></td>
      <td>Lấy danh sách tất cả các Tỉnh</td>
    </tr>
    <!-- --------layDSTinhTheoGiaiDau-------------- -->
     <!-- <tr>
      <td rowspan="2">layDSTinhTheoGiaiDau</td>
      <td rowspan="2">public</td>
      <td colspan="4">Có 1 tham số</td>
      <td rowspan="2">List < Tinh ></td>
      <td rowspan="2">Lấy danh sách tất cả các tỉnh trong 1 giải đấu</td>
    </tr>
    <tr>
      <td>idGiaiDau</td>
      <td>string</td>
      <td>null</td>
      <td>8</td>
    </tr> -->
       <!-- --------layDSDoanTheoTinh-------------- -->
     <tr>
      <td>layDSDoan</td>
      <td>public</td>
      <td colspan="4">Có 1 tham số</td>
      <td>List < Doan ></td>
      <td>Lấy danh sách tất cả đoàn trong 1 tỉnh</td>
    </tr>
    <!-- ---------------------inDSTinh--------------- -->
    <tr>
      <td>inDSTinh</td>
      <td>public</td>
      <td colspan="4">Có 0 tham số</td>
      <td>bool</td>
      <td>In danh sách tỉnh</td>
    </tr>
</table>
  