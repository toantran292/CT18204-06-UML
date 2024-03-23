# Đặc tả class VongLoai

### 1. Thuộc tính
| Tên thuộc tính | Kiểu truy cập | Kiểu dữ liệu | Giá trị mặc nhiên | Kích thước| Min | Max | Diễn giải |
|---|---|---|---|---|---|---|---|
| idVongLoai | public | String | null | 8 | | | id vòng loại |
| tenVongLoai | public | String | null | 30 | | | tên vòng loại |

### 2. Phương thức


<table>
    <tr>
        <th>Tên phương thức</th>
        <th>Kiểu truy cập</th>
        <th>Danh sách các tham số</th>
        <th>Kiểu dữ liệu tham số</th>
        <th>Giá trị mặc nhiên</th>
        <th>Kích thước</th>
        <th>Kiểu trả về của phương thức</th>
        <th>Diễn giải</th>
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
      <td rowspan="2">bool</td>
      <td rowspan="2">Thêm trận đấu vào vòng đấu</td>
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
      <td rowspan="2">bool</td>
      <td rowspan="2">Xóa trận đấu khỏi vòng đấu</td>
    </tr>
    <tr>
      <td>idTranDauLoai</td>
      <td>String</td>
      <td>null</td>
      <td>8</td>
    </tr>
</table>


  