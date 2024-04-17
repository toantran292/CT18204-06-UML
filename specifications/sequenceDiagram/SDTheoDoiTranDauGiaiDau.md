# Sơ đồ tuần tự "Theo dõi trận đấu, giải đấu"

### I. Người thiết kế: 
Khưu Thị Bích Ngọc - B2203514
### II. Mô tả chức năng:
Cho phép Người đã đăng nhập theo dõi trận đấu, giải đấu mà mình quan tâm
### III. Điều kiện tiên quyết:
Người đã đăng nhập đã đăng nhập thành công vào hệ thống và đang xem thông tin chi tiết trân đấu hoặc giải đấu nào đó
### IV. Trình tự thực hiện
1. Người đã đăng nhập ấn chọn nút theo dõi của trận đấu, giải đấu
2. Giao diện gửi yêu cầu kiểm tra xem người dùng đã theo dõi trận đấu, giải đấu đó hay chưa
3. Hệ thống tiến hành kiểm tra
4. Hệ thống trả về kết quả vừa kiểm tra

**[Rẽ nhánh 1]**

a. Người dùng chưa theo dõi

5. Giao diện hiển thị để người dùng chọn cấp độ theo dõi mong muốn
6. Người dùng chọn cấp độ theo dõi và ấn gửi
7. Hệ thống lưu thông tin theo dõi của người dùng

    **[Rẽ nhánh 2]**

    a. Lưu thông tin theo dõi thành công

        8. Hệ thống gửi thông báo thành công về trình duyệt

    b. Lưu thông tin theo dõi thất bại

        8. Hệ thống gửi thông báo tạo theo dõi thất bại

b. Người dùng đã theo dõi

5. Trình duyệt yêu cầu người dùng xác nhận tiếp tục hay dừng quá trình hủy theo dõi

    **[Tùy chọn]**

    a. Tiếp tục thực hiện
   
    6. Hệ thống hủy theo dõi trận đấu, giải đấu của người dùng đó

        **[Rẽ nhánh 3]**

        a. Hủy theo dõi thành công

            7. Hệ thống gửi thông báo hủy theo dõi thành công về giao diện

        b. Hủy theo dõi thất bại

            7. Hệ thống gửi thông báo hủy theo dõi thất bại về giao diện

    b. Dừng quá trình hủy yêu cầu

    6. Trở về giao diện ban đầu và kết thúc kịch bản

9. Trình duyệt hiển thị kết quả