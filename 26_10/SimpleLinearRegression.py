import matplotlib.pyplot as plt
import numpy as np

# Dữ liệu đầu vào
x = np.array([[1,2,3,4,5,6,7,8,9,10]]).T
y = np.array([[2,4,3,6,9,12,13,15,18,20]]).T

# Hàm tính b0, b1
def calculateb1b0(x, y):
    xbar = np.mean(x)
    ybar = np.mean(y)
    xybar = np.mean(x * y)
    x2bar = np.mean(x ** 2)

    # Công thức hồi quy tuyến tính
    b1 = (xybar - xbar * ybar) / (x2bar - xbar**2)
    b0 = ybar - b1 * xbar

    return b1, b0  # 🔹 Thêm dòng này để trả về giá trị

# Gọi hàm tính
b1, b0 = calculateb1b0(x, y)
print("b1 =", b1)
print("b0 =", b0)

# Tính giá trị dự đoán
y_predicted = b0 + b1 * x
print("Y predicted:\n", y_predicted)

# Hàm vẽ đồ thị
def showGraph(x, y, y_predicted, title="", xLabel="", yLabel=""):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'r-o', label="Actual values")
    plt.plot(x, y_predicted, 'b-*', label="Predicted values")

    ybar = np.mean(y)
    plt.axhline(ybar, linestyle='--', linewidth=2, color='gray', label="Mean")

    plt.xlabel(xLabel, fontsize=12)
    plt.ylabel(yLabel, fontsize=12)
    plt.title(title, fontsize=14)
    plt.legend()
    plt.show()

# Hiển thị kết quả
showGraph(x, y, y_predicted, title='Y values corresponding to X', xLabel='X values', yLabel='Y values')
