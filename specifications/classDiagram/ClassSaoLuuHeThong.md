# Đặc tả class SaoLuuHeThong

### 1. Thuộc tính

| Tên thuộc tính    | Kiểu truy cập | Kiểu dữ liệu   | Giá trị mặc nhiên | Kích thước | Min | Max      | Diễn giải                                              |
| ----------------- | ------------- | -------------- | ----------------- | ---------- | --- | -------- | ------------------------------------------------------ |
| idSaoLuu          | public        | String         | null              | 8          |     |          | Mã của bản sao lưu                                     |
| duongDanBanSaoLuu | public        | String         | null              | 100        |     |          | Đường dẫn nơi lưu trữ bản sao lưu hệ thống             |
| NgaySaoLuu        | public        | Date           | toDate()          |            |     | toDate() | Ngày sao lưu hệ thống                                  |
| thanhPhanSaoLuu   | public        | List< String > | null              |            |     |          | Các thành phần được sao lưu trong bản sao lưu hệ thống |

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
    <tr>
      <td rowspan="4">taoBanSaoLuu</td>
      <td rowspan="4">public</td>
      <td colspan="4">Có 3 tham số</td>
      <td rowspan="4">boolean</td>
      <td rowspan="4">Tạo ra bản sao lưu sao hệ thống. Nếu sao lưu thành công thì trả về true ngược lại thì false</td>
    </tr>
    <tr>
      <td>ngaySaoLuu</td>
      <td>Date</td>
      <td>null</td>
      <td></td>
    </tr>
    <tr>
      <td>thanhPhanSaoLuu</td>
      <td>List< String ></td>
      <td>toDate()</td>
      <td></td>
    </tr>
     <tr>
      <td>duongDanBanSaoLuu</td>
      <td>String</td>
      <td>null</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">phucHoiHeThong</td>
      <td rowspan="2">public</td>
      <td colspan="4">Không có tham số</td>
      <td rowspan="2">boolean</td>
      <td rowspan="2">Phục hồi hệ thống dựa trên các bản sao lưu trước đó. Trả về true nếu phục hồi hệ thống thành công ngược lại thì false</td>
    </tr>

</table>
