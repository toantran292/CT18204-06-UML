# UML nhóm 06

## 1. Cây thư mục

```bash
UML                                                                        
├── readme.md
├── report                  <- Chứa file báo cáo
├── specifications          <- Chứa file đặc tả theo từng loại diagram
│   ├── classDiagram        
│   ├── useCaseDiagram  
│   └── ... 
└── uml                     <- Chứa file UML và file hình
    ├── class
    ├── useCase
    │   └── UseCaseTongQuat.svg                           
    ├── remove.py
    └── UML.mdj 
```

## 2. Yêu cầu
Thư mục **specification** chỉ nhận duy nhất các file có định dạng .md và yêu cầu tách theo từng class, usecase, ... cụ thể không gộp cùng một file.

Vui lòng tạo bản sao của file **UML.mdj** để vẽ theo định dạng **{tên}.mdj** để vẽ diagram, ví dụ **toan.mdj**. Lý do để không phải push file đó lên **github**. Và xuất file **SVG** cho từng diagram cụ thể vào đúng thư mục (nếu chưa có thì tạo theo nguyên tắc **camelCase**)

Các phương thức lấy danh sách thì đặt theo dạng: layDS__