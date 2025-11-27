import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for testing
from matplotlib.figure import Figure
from mpl_toolkits import mplot3d
import pandas as pd

# Test 3D scatter functionality
print("Testing 3D scatter plot...")

# Load data
df = pd.read_csv('students.csv')
print(f"Data loaded: {df.shape}")
print(f"Columns: {df.columns.tolist()}")

# Get score columns
all_cols = df.columns.tolist()
exclude_cols = ['Average', 'Grade']
# Thêm cột đầu tiên (Name) vào danh sách loại trừ
if len(all_cols) > 0:
    exclude_cols.append(all_cols[0])

score_cols = [col for col in all_cols if col not in exclude_cols]
print(f"Score columns: {score_cols}")

if len(score_cols) < 3:
    print("ERROR: Need at least 3 score columns!")
else:
    # Create 3D plot
    fig = Figure(figsize=(10, 8), dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    
    x_col, y_col, z_col = score_cols[0], score_cols[1], score_cols[2]
    print(f"Plotting: {x_col} vs {y_col} vs {z_col}")
    
    ax.scatter(df[x_col], df[y_col], df[z_col], 
              c='blue', marker='o', s=50, alpha=0.6)
    
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_zlabel(z_col)
    ax.set_title("3D Scatter Plot Test")
    
    # Save to file instead of showing
    fig.savefig('test_3d_scatter.png')
    print("SUCCESS: 3D scatter plot created and saved to test_3d_scatter.png")
