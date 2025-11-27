# Hướng dẫn tạo file .exe cho Grade Manager

## ✅ Đã hoàn thành

File **GradeManager.exe** đã được tạo thành công!
- **Vị trí**: `dist\GradeManager.exe`
- **Kích thước**: ~47.4 MB
- **Ngày tạo**: 20/11/2025

## 📝 Các bước đã thực hiện

### 1. Cài đặt PyInstaller
```bash
pip install pyinstaller
```

### 2. Tạo file .exe
```bash
pyinstaller --onefile --windowed --name "GradeManager" grade_manager.py
```

**Giải thích các tham số:**
- `--onefile`: Tạo 1 file .exe duy nhất (thay vì nhiều file)
- `--windowed`: Ẩn cửa sổ console khi chạy (chỉ hiển thị GUI)
- `--name "GradeManager"`: Đặt tên cho file .exe

### 3. Kết quả

PyInstaller tạo ra các thư mục:
```
DEMO_COMPUTER/
├── build/              # Thư mục tạm (có thể xóa)
├── dist/               # Chứa file .exe đã build
│   └── GradeManager.exe  ⭐ FILE CHÍNH
├── GradeManager.spec   # File cấu hình (có thể tùy chỉnh)
└── grade_manager.py    # File nguồn
```

## 🚀 Cách sử dụng file .exe

### Chạy ứng dụng
1. Vào thư mục `dist/`
2. Double-click vào `GradeManager.exe`
3. Ứng dụng sẽ mở ra mà không cần cài Python!

### Chia sẻ cho người khác
Bạn có thể gửi file `GradeManager.exe` cho bất kỳ ai có Windows. Họ chỉ cần:
1. Copy file .exe
2. Chuẩn bị file CSV (ví dụ: `students.csv`)
3. Chạy .exe và load file CSV

**Lưu ý**: File .exe này chỉ chạy trên Windows!

## 📦 Nếu muốn build lại

### Xóa các file cũ (tùy chọn)
```bash
# PowerShell
Remove-Item -Recurse -Force build, dist
Remove-Item GradeManager.spec
```

### Build lại với tùy chọn nâng cao
```bash
# Thêm icon tùy chỉnh (cần file .ico)
pyinstaller --onefile --windowed --icon=icon.ico --name "GradeManager" grade_manager.py

# Thêm dữ liệu (như file CSV mẫu)
pyinstaller --onefile --windowed --add-data "students.csv;." --name "GradeManager" grade_manager.py
```

## ⚠️ Xử lý lỗi thường gặp

### 1. "Module not found"
Đảm bảo đã cài đặt tất cả thư viện:
```bash
pip install pandas matplotlib seaborn
```

### 2. File .exe quá lớn
Đây là bình thường vì PyInstaller đóng gói toàn bộ Python runtime và thư viện.
Nếu muốn giảm kích thước:
```bash
# Dùng UPX để nén (cần cài UPX)
pyinstaller --onefile --windowed --upx-dir=<path-to-upx> grade_manager.py
```

### 3. Antivirus cảnh báo
Một số antivirus có thể cảnh báo file .exe mới. Đây là false positive.
Giải pháp: Thêm exception trong antivirus hoặc ký code (code signing).

## 📊 Thống kê build

- **Thời gian build**: ~57 giây
- **Số file dependencies**: 1736 entries
- **Backend matplotlib**: TkAgg (automatic)
- **Bootloader**: Windows-64bit-intel

## 🔧 Tùy chỉnh nâng cao

### Chỉnh sửa file .spec
File `GradeManager.spec` được tạo tự động. Bạn có thể chỉnh sửa và build lại:
```bash
pyinstaller GradeManager.spec
```

### Ví dụ tùy chỉnh trong .spec:
- Thêm hidden imports
- Loại bỏ các module không cần thiết
- Thêm resources (images, fonts...)

## 📚 Tài liệu tham khảo

- [PyInstaller Documentation](https://pyinstaller.org/)
- [PyInstaller Options](https://pyinstaller.org/en/stable/usage.html)

## ✨ Hoàn thành!

File `GradeManager.exe` có thể chạy độc lập, không cần cài Python hay bất kỳ thư viện nào!
