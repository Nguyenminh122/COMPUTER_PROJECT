import tkinter as tk
from tkinter import ttk, filedialog, messagebox, font
import pandas as pd
from pandas.api.types import is_numeric_dtype
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits import mplot3d


class GradeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grade Manager")
        self.root.geometry("800x600")

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.btn_load = ttk.Button(button_frame, text="Load CSV", command=self.load_csv)
        self.btn_load.pack(side=tk.LEFT, padx=5)

        self.btn_update = ttk.Button(button_frame, text="Update Data", command=self.update_data)
        self.btn_update.pack(side=tk.LEFT, padx=5)

        self.btn_hist = ttk.Button(button_frame, text="Histogram", command=self.plot_histogram)
        self.btn_hist.pack(side=tk.LEFT, padx=5)

        self.btn_pie = ttk.Button(button_frame, text="Pie Chart", command=self.plot_pie_chart)
        self.btn_pie.pack(side=tk.LEFT, padx=5)

        self.btn_scatter = ttk.Button(button_frame, text="3D Scatter", command=self.plot_scatter_3d)
        self.btn_scatter.pack(side=tk.LEFT, padx=5)

        # Khung chứa bảng điểm và thang điểm
        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10)

        # Vùng hiển thị dữ liệu 
        self.data_text = tk.Text(main_frame, height=20, width=60, 
                                 font=font.Font(family="Courier New", size=10)) 
        self.data_text.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 5))

        # Vùng hiển thị thang điểm
        grade_scale_text = self.get_grade_scale()
        self.scale_text = tk.Text(main_frame, height=20, width=25, 
                                  font=font.Font(family="Courier New", size=10))
        self.scale_text.insert(tk.END, grade_scale_text)
        self.scale_text.config(state=tk.DISABLED)
        self.scale_text.pack(side=tk.RIGHT, fill=tk.Y)

        # Thanh trạng thái (hiển thị Avg, High, Low)
        self.status_label = ttk.Label(root, text="Class Avg: N/A, High: N/A, Low: N/A", 
                                      anchor=tk.W)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)
        
        # Biến để lưu trữ DataFrame
        self.df = None

    def get_grade_scale(self):
        return (
            "+-------+-------------+\n"
            "| GRADE | SCORE RANGE |\n"
            "+-------+-------------+\n"
            "| A+    |  97-100     |\n"
            "| A     |   93-96     |\n"
            "| A-    |   90-92     |\n"
            "| B+    |   87-89     |\n"
            "| B     |   83-86     |\n"
            "| B-    |   80-82     |\n"
            "| C+    |   77-79     |\n"
            "| C     |   73-76     |\n"
            "| C-    |   70-72     |\n"
            "| D+    |   67-69     |\n"
            "| D     |   63-66     |\n"
            "| D-    |   60-62     |\n"
            "| F     |    0-59     |\n"
            "+-------+-------------+"
        )

    def load_csv(self):
        try:
            file_path = filedialog.askopenfilename(
                title="Open CSV File",
                filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
            )
            if not file_path:
                return  
                
            self.df = pd.read_csv(file_path)
            self.update_data() 
            
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file: {e}")

    def update_data(self):
        if self.df is None:
            messagebox.showwarning("Warning", "Please load a CSV file first.")
            return

        try:
            # Lấy các cột điểm (ví dụ: Math, Physics, English)
            # Giả sử cột đầu tiên là tên, các cột còn lại là điểm
            score_cols = self.df.columns[1:]
            
            # Xử lý lỗi input không phải là số (như Hình 6)
            non_numeric_rows = False
            for col in score_cols:
                # Chuyển đổi sang số, nếu lỗi thì thành NaN (Not a Number)
                self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
                if self.df[col].isnull().any():
                    non_numeric_rows = True
            
            if non_numeric_rows:
                messagebox.showerror("Invalid Input", 
                                     "Some rows have non-numeric scores. They are ignored in calculation.")

            # 1. Tính điểm trung bình cho mỗi sinh viên
            self.df['Average'] = self.df[score_cols].mean(axis=1)

            # 2. Phân loại học lực (Grade Classification) 
            # Dựa trên thang điểm trong Hình 1 
            bins = [0, 59.9, 62.9, 66.9, 69.9, 72.9, 76.9, 79.9, 82.9, 86.9, 89.9, 92.9, 96.9, 100]
            labels = ['F', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']
            self.df['Grade'] = pd.cut(self.df['Average'], bins=bins, labels=labels, right=True)

            # 3. Tính toán thống kê chung (Class Average, High, Low)
            if self.df.empty or self.df['Average'].isnull().all():
                # Xử lý lỗi chia cho 0 (không có sinh viên)
                raise ZeroDivisionError("No valid student data to calculate average.")
                
            class_avg = self.df['Average'].mean()
            high_score = self.df['Average'].max()
            low_score = self.df['Average'].min()
            
            # 4. Hiển thị lên GUI
            self.data_text.config(state=tk.NORMAL)
            self.data_text.delete(1.0, tk.END)
            # Dùng to_string() với định dạng để giống trong Hình 1
            data_string = self.df.to_string(float_format="%.1f", index=False)
            self.data_text.insert(tk.END, data_string)
            self.data_text.config(state=tk.DISABLED)

            self.status_label.config(
                text=f"Class Avg: {class_avg:.2f}, High: {high_score:.2f}, Low: {low_score:.2f}"
            )

        except ZeroDivisionError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during calculation: {e}")

    def plot_histogram(self):
        if self.df is None or 'Average' not in self.df:
            messagebox.showwarning("Warning", "No data available to plot.")
            return

        # Tạo cửa sổ con (Toplevel)
        plot_window = tk.Toplevel(self.root)
        plot_window.title("Histogram of Average Scores")

        try:
            # 1. Tạo Figure của Matplotlib
            fig = Figure(figsize=(8, 6), dpi=100)
            ax = fig.add_subplot(111)

            # 2. Dùng Seaborn/Matplotlib để vẽ (như Hình 3)
            sns.histplot(self.df['Average'].dropna(), kde=True, ax=ax, bins=15)
            ax.set_title("Histogram of Average Scores", fontsize=14, fontweight='bold')
            ax.set_xlabel("Score")
            ax.set_ylabel("Count")
            ax.grid(True, alpha=0.3)

            # 3. Nhúng Figure vào Tkinter
            canvas = FigureCanvasTkAgg(fig, master=plot_window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        except Exception as e:
            plot_window.destroy()  # Hủy cửa sổ nếu có lỗi
            messagebox.showerror("Plot Error", f"Failed to plot histogram: {e}")

    def plot_pie_chart(self):
        if self.df is None or 'Grade' not in self.df:
            messagebox.showwarning("Warning", "No data available to plot.")
            return

        # Tạo cửa sổ con (Toplevel)
        plot_window = tk.Toplevel(self.root)
        plot_window.title("Pie Chart of Grade Distribution")

        try:
            # 1. Tính toán phân phối điểm
            grade_counts = self.df['Grade'].value_counts()
            
            # 2. Tạo Figure của Matplotlib
            fig = Figure(figsize=(8, 6), dpi=100)
            ax = fig.add_subplot(111)

            # 3. Vẽ biểu đồ tròn
            colors = plt.cm.Set3(range(len(grade_counts)))
            ax.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', 
                   startangle=90, colors=colors)
            ax.set_title("Grade Distribution", fontsize=14, fontweight='bold')

            # 4. Nhúng Figure vào Tkinter
            canvas = FigureCanvasTkAgg(fig, master=plot_window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        except Exception as e:
            plot_window.destroy()
            messagebox.showerror("Plot Error", f"Failed to plot pie chart: {e}")

    def plot_scatter_3d(self):
        if self.df is None:
            messagebox.showwarning("Warning", "No data available to plot.")
            return

        try:
            # Lấy các cột điểm số (loại bỏ cột Name, Average, Grade)
            # Giả sử cột đầu tiên là tên, các cột còn lại trước Average/Grade là điểm
            all_cols = self.df.columns.tolist()
            exclude_cols = ['Average', 'Grade']
            
            # Thêm cột đầu tiên (thường là Name) vào danh sách loại trừ
            if len(all_cols) > 0:
                exclude_cols.append(all_cols[0])
            
            score_cols = [col for col in all_cols if col not in exclude_cols]
            
            if len(score_cols) < 3:
                messagebox.showwarning("Warning", f"Need at least 3 score columns for 3D scatter plot.\nFound only: {score_cols}")
                return

            # Tạo cửa sổ con (Toplevel)
            plot_window = tk.Toplevel(self.root)
            plot_window.title("3D Scatter Plot")

            # 1. Tạo Figure của Matplotlib với projection 3D
            fig = Figure(figsize=(10, 8), dpi=100)
            ax = fig.add_subplot(111, projection='3d')

            # 2. Vẽ scatter 3D (dùng 3 cột điểm đầu tiên)
            x_col, y_col, z_col = score_cols[0], score_cols[1], score_cols[2]
            
            ax.scatter(self.df[x_col], self.df[y_col], self.df[z_col], 
                      c='blue', marker='o', s=50, alpha=0.6)
            
            # 3. Đặt nhãn
            ax.set_xlabel(x_col, fontsize=10, fontweight='bold')
            ax.set_ylabel(y_col, fontsize=10, fontweight='bold')
            ax.set_zlabel(z_col, fontsize=10, fontweight='bold')
            ax.set_title("3D Scatter Plot of Scores", fontsize=14, fontweight='bold')

            # 4. Nhúng Figure vào Tkinter
            canvas = FigureCanvasTkAgg(fig, master=plot_window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        except Exception as e:
            if 'plot_window' in locals():
                plot_window.destroy()
            import traceback
            error_msg = f"Failed to plot 3D scatter:\n{str(e)}\n\nTraceback:\n{traceback.format_exc()}"
            messagebox.showerror("Plot Error", error_msg)


if __name__ == "__main__":
    root = tk.Tk()
    app = GradeApp(root)
    root.mainloop()
