**Mô tả chức năng:** Cho phép người dùng có thể theo dõi diễn biến của một trận đấu loại đang được diễn ra.

**Điều kiện tiên quyết**: Không có.

**Trình tự thực hiện:**
    
1. Sau khi truy cập vào hệ thống, người dùng chọn chức năng "Xem diễn biến trận đấu"
2. Hệ thống sẽ gọi phương thức layDSTranDauLoaiDienRa để lấy danh sách trận đấu loại đang diễn ra.
3. CSDL trả về danh sách trận đấu loại đang diễn ra.
4. Giao diện hiển thị danh sách trận đấu loại đang diễn ra.
5. Người dùng chọn chức năng tìm kiếm. **[Tùy chọn 1]**
6. Giao diện hiển thị trang tìm kiếm
7. Người dùng nhập từ khóa tìm kiếm
8. Người dùng nhấn nút tìm kiếm
9. Hệ thống sẽ gọi phương thức layDSTranDauLoaiDienRa để lấy danh sách trận đấu loại đang diễn ra theo từ khóa người dùng cung cấp
10. CSDL trả về danh sách trận đấu loại đang diễn ra theo từ khóa người dùng cung cấp. **[Rẽ nhánh]**

    **[Rẽ nhánh 1]**
11. Nếu kết quả tìm thấy ít nhất một trận đấu loại đang diên ra thì giao diện hiển thị danh sách trận đấu loại đang diễn ra tìm được.
    
    **[Rẽ nhánh 2]**
12. Nếu kết quả không tìm thấy trận đấu loại đang diễn ra thì hiển thị thông báo không tìm thấy trận đấu.
13. Giao diện hiển thị danh sách trước đó.
    
    **[Kết thúc Tùy chọn 1]**
14. Người dùng chọn vào một trận đấu đang diễn ra cụ thể để xem diễn biến.
15. Hệ thống sẽ gọi phương thức layDienBien để lấy diễn biến trận đấu
16. CSDL trả về chi tiết diễn biến 
17. Giao diễn hiển thị diễn biến của trận đấu.