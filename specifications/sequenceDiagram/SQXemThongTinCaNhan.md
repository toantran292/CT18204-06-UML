# Sơ đồ tuần tự "Gửi yêu cầu chỉnh sửa thông tin cá nhân

### I. Người thiết kế: 
Khưu Thị Bích Ngọc - B2203514
### II. Mô tả chức năng:
Cho phép Vận động viên gửi yêu cầu chỉnh sửa thông tin cá nhân khi sai sót
### III. Điều kiện tiên quyết:
Vận động viên đã đăng nhập thành công vào hệ thống và xem thông tin cá nhân của mình
### IV. Trình tự thực hiện
1. Ở giao diện xem thông tin cá nhân, vận động viên chọn Gửi yêu cầu chỉnh sửa thông tin
2. Hệ thống hiển thị giao diện

[Loop]

3. Vận động viên tiến hành nhập thông tin cần chỉnh sửa và biểu mẫu
4. Vận động viên sau khi nhập thông tin cần sửa xong thì ấn gửi yêu cầu
5. Hệ thống tiếp nhận biểu mẫu vừa được gửi đến
6. Hệ thống tiến hành kiểm tra các thông tin của biểu mẫu có đúng ràng buộc của từng trường dữ liệu hay không
    
    [Điều kiện]
    
    a. Nếu thông tin hợp lệ
    
    7. Hệ thống lưu lại yêu cầu chờ xử lý
    8. Hệ thống gửi thông báo thành công
    9. Trình duyệt hiển thị thông báo lên màn hình

    b. Nếu thông tin không hợp lệ

    7. Thông báo thông tin đã gửi không hợp lệ
    8. Hiển thị thông báo lỗi ra màn hình và yêu cầu vận động viên nhập lại thông tin
    
    Lắp lại vòng lặp [Loop]

### V. Kết quả:
Thao tác gửi yêu cầu chỉnh sửa thông tin thành công