# Đặc tả use case Đăng ký tham gia giải đấu

<table>
    <tr>
        <th>Tên usecase</th>
        <th>Đăng ký tham gia giải đấu</th>
    </tr>
    <tr>
        <td>Tóm tắt</td>
        <td>Đăng ký tham gia giải đấu</td>
    </tr>
    <tr>
        <td>Actor</td>
        <td>Trưởng đoàn</td>
    </tr>
    <tr>
        <td>Phiên bản</td>
        <td>1.1</td>
    </tr>
    <tr>
        <td>Chịu trách nhiệm</td>
        <td>Nguyễn Tuấn Đạt</td>
    </tr>
    <tr>
        <td>Ngày tạo</td>
        <td>16/3</td>
    </tr>
    <tr>
        <td>Ngày cập nhật</td>
        <td>20/3</td>
    </tr>
    <tr>
        <td>Điều kiện tiên quyết</td>
        <td>Đã đăng nhập vào hệ thống bằng tài khoản của trưởng đoàn</td>
    </tr>
    <tr>
        <td>Kịch bản thường</td>
        <td>
            <ol type="1">
                <li>Sau khi trưởng đoàn đăng nhập vào hệ thống, trưởng đoàn chọn vào danh mục danh sách giải đấu</li>
                <li>Hệ thống chuyển sang giao diện danh sách giải đấu</li>
                <li>Trưởng đoàn chọn giải đấu cần đăng ký tham gia</li>
                    <b>Có thể nhảy đến:</b></br>
                    A1 - Trưởng đoàn nhấn nút thoát
                <li>Trưởng đoàn các chọn hạng mục tham gia thi đấu và các đội thi đấu ở các hạng mục đó</li>
                <li>Trưởng đoàn nhấn vào nút xác nhận đăng ký tham gia</li>
                    <b>Có thể nhảy đến:</b></br>
                    A2 - Đăng ký tham gia không thành công
                </li>
                <li>Hệ thống thông báo đăng ký tham gia thành công</li>
            </ol>
        </td>
    </tr>
    <tr>
     <td>Kịch bản thay thế</td>
        <td>
            <b>A1 - Nhấn vào nút thoát.</b></br>
            Chuỗi A1 bắt đầu ở bước 4 của kịch bản thường.
            <ol type="1" start="5">
                <li>Hệ thống chuyển sang giao diện danh sách giải đấu trước đó</li>
            </ol>
            <b>A2 - Đăng ký tham gia giải đấu không thành công</b></br>
            Chuỗi A2 bắt đầu ở bước 5 của kịch bản thường.</br>
            <ol type="1" start="6">
                <li>Thông báo đăng ký tham gia giải đấu không thành công</li>
                  <li>Hệ thống chuyển sang giao diện danh sách giải đấu trước đó</li>
            </ol>
        </td>
    </tr>
    <tr>
        <td>Kịch bản lỗi</td>
        <td></td>
    </tr>
    <tr>
        <td>Kết quả</td>
        <td>Đăng ký tham gia giải đấu thành công</td>
    </tr>
</table>
