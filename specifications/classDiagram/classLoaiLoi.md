# Đặc tả class LoaiLoi

### 1. Thuộc tính
| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước| Min | Max | Diễn giải |
|---|---|---|---|---|---|---|---|
| id | public | string | null | 8 |  |  |  Loại của lỗi mà vận động viên vi phạm trong trận đấu |
| tenLoai | public | string | null | 50 |  |  | Tên của loại lỗi mà vận động viên vi phạm trong một trận đấu |


### 2. Phương thức

<table>
    <tr>
        <td>Tên phương thức</td>
        <td>Danh sách các tham số</td>
        <td>Kiểu truy cập</td>
        <td>Kiểu dữ liệu tham số</td>
        <td>Giá trị mặc nhiên</td>
        <td>Kích thước</td>
        <td>Kiểu trả về của phương thức</td>
        <td>Diễn giải</td>
    </tr>
    <tr>
      <td rowspan="2">capNhatLoaiLoi</td>
      <td rowspan="2">public</td>
      <td colspan="4">không có tham số</td>
      <td rowspan="2">Bool</td>
      <td rowspan="2">Cập nhật loại lỗi của một vận động viên trong trận đấu</td>
    </tr>
    <td colspan="4"></td>
    </tr>
      <tr>
      <td rowspan="2">thongKeLoaiLoi</td>
      <td rowspan="2">public</td>
      <td colspan="4">không có tham số</td>
      <td rowspan="2">Bool</td>
      <td rowspan="2">Thống kê loại lỗi vi phạm của vận động viên trong trận đấu</td>
    </tr>
      <td colspan="4"></td>
</table>
  