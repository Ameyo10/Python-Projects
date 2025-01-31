'''
To construct a lesat square approximation of the form bx^a for the following data and find the error in the approximation and plot the approximation
x   4.0         4.2         4.5         4.7         5.1         5.5         5.9         6.3         6.8         7.1
y   102.56      113.18      130.11      142.05      167.53      195.14      224.87      256.73      299.50      326.72
'''
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Data allocation
x_data = np.array([4.0, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1])
y_data = np.array([102.56, 113.18, 130.11, 142.05, 167.53, 195.14, 224.87, 256.73, 299.50, 326.72])

# Logarithmic transformation for linearization
X = np.log(x_data)
Y = np.log(y_data)

# Number of elements
n = len(x_data)

# Calculations for least squares
X2 = np.square(X)
XY = X * Y

# Summation results
Sx = np.sum(X)
Sy = np.sum(Y)  
Sx2 = np.sum(X2)
Sxy = np.sum(XY)

# Solving for a and B
a = ((n * Sxy) - (Sx * Sy)) / ((n * Sx2) - (Sx ** 2))
B = (Sy - a * Sx) / n
b = np.exp(B)

# Defining P as a lambda function for easy evaluation
P = lambda x: b * (x ** a)

# Evaluating P for each element in x_data
y_approx = P(x_data)

# Calculating the error as the difference between y_data and y_approx
error = y_data - y_approx
error_magnitude = np.abs(error)

# Printing the errors and total error
print("Error for each data point:", error)
print("Total Error (Sum of Absolute Errors):", np.sum(error_magnitude))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, 'bo-', label='Original Data')
plt.plot(x_data, y_approx, 'r--', label='Least Squares Approximation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Squares Approximation of Form $y = bx^a$')
plt.legend()
plt.grid(True)
plt.show()
