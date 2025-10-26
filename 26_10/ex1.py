# Import libraries
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import math

# Input data
x1 = [0.76, 4.25, 5.71, 3.58, 0.45, 0.13, 1, 0.76, 7.56, 0.76,
      0.42, 2.93, 5.64, 3.93, 0.5, 0.2, 1.09, 1.95, 3.81, 5.41]
x2 = [7.01, 14.45, 42.28, 11.13, 3, 63.46, 48.25, 24.8, 13.85, 50.46,
      3.1, 11.21, 18.11, 21.56, 11.2, 7.62, 22.54, 44.38, 5.5, 11.73]
x3 = [0.94, 0.84, 0.83, 0.24, 0.48, 0.18, 0.35, 0.34, 0.55, 0.43,
      0.94, 0.53, 0.09, 0.43, 0.79, 0.33, 0.94, 0.9, 0.61, 0.29]
y  = [33.52, 42.89, 12.04, 6.91, 6.57, 2.07, 4.18, 58.45, 29.64, 48.87,
      33.75, 0.04, 16.75, 4.63, 61.69, 24.55, 32.9, 9.23, 11.4, 27.64]


X = np.column_stack((x1, x2, x3))
y = np.array(y)

model = LinearRegression()
model.fit(X, y)


y_pred = model.predict(X)

mse = mean_squared_error(y, y_pred)
rmse = math.sqrt(mse)

print("=============== Multiple Linear Regression Results ==========================")
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")

# Compare actual vs predicted
print("\nActual vs Predicted:")
for actual, predicted in zip(y, y_pred):
    print(f"Actual: {actual:6.2f} | Predicted: {predicted:6.2f}")
