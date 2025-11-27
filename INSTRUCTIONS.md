# Student Grade Manager - Hướng dẫn sử dụng

## Mô tả
Ứng dụng quản lý điểm sinh viên với giao diện đồ họa (GUI) sử dụng Python Tkinter.

## Tính năng
1. **Load CSV**: Tải file CSV chứa dữ liệu điểm sinh viên
2. **Update Data**: Cập nhật và tính toán điểm trung bình, phân loại học lực
3. **Histogram**: Hiển thị biểu đồ phân phối điểm trung bình
4. **Pie Chart**: Hiển thị biểu đồ tròn phân phối học lực (A+, A, B, C...)
5. **3D Scatter**: Hiển thị biểu đồ 3D scatter plot của 3 môn học

## Cài đặt thư viện

Đã hoàn thành việc cài đặt:
```bash
pip install pandas matplotlib seaborn
```

## Chạy ứng dụng

```bash
python grade_manager.py
```

## Cấu trúc file CSV
File CSV cần có định dạng như sau:
```
Name,Math,Physics,English
Alice,95,88,92
Bob,78,85,80
...
```

- Cột đầu tiên: Tên sinh viên
- Các cột tiếp theo: Điểm các môn học

### 🚀 Cách sử dụng file .exe

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

## Thang điểm
```
+-------+-------------+
| GRADE | SCORE RANGE |
+-------+-------------+
| A+    |  97-100     |
| A     |   93-96     |
| A-    |   90-92     |
| B+    |   87-89     |
| B     |   83-86     |
| B-    |   80-82     |
| C+    |   77-79     |
| C     |   73-76     |
| C-    |   70-72     |
| D+    |   67-69     |
| D     |   63-66     |
| D-    |   60-62     |
| F     |    0-59     |
+-------+-------------+
```

## Ghi chú
- Ứng dụng tự động xử lý dữ liệu không hợp lệ (non-numeric)
- Hiển thị Class Average, High Score, Low Score ở thanh trạng thái
- Hỗ trợ các file CSV tiêu chuẩn với encoding UTF-8
- **Quan trọng**: File CSV phải có cột đầu tiên là tên sinh viên (Name), các cột tiếp theo là điểm số
- Biểu đồ 3D Scatter sẽ vẽ 3 môn học đầu tiên (sau cột Name)

## File demo
- `grade_manager.py`: File chương trình chính
- `students.csv`: File dữ liệu mẫu để test

## Push lên GitHub

```bash
git add .
git commit -m "Thêm ứng dụng quản lý điểm sinh viên"
git push -u origin main
```
