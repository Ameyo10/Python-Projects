'''
Find the cubic spline for 
x   0.9     1.3     1.9     2.1     2.6     3.0     3.9     4.4     4.7     5.0     6.0     7.0     8.0     9.2     10.5    11.3     11.6    12.0   12.6    13.0    13.3
y   1.3     1.5     1.85    2.1     2.6     2.7     2.4     2.15    2.05    2.1     2.25    2.3     2.25    1.95    1.4     0.9      0.7     0.6    0.5     0.4     0.25
'''

import numpy as np
import matplotlib.pyplot as plt

# Data points
x = np.array([0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0, 9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3])
y = np.array([1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25])

# Number of intervals
n = len(x) - 1

# Step 1: Calculate h values (interval lengths)
h = np.diff(x)

# Step 2: Set up the matrix system to solve for c
A = np.zeros((n + 1, n + 1))
b = np.zeros(n + 1)

# Implementing Natural spline boundary conditions
A[0, 0] = 1
A[-1, -1] = 1

# Filling the tridiagonal system for the internal points
for i in range(1, n):
    A[i, i - 1] = h[i - 1]
    A[i, i] = 2 * (h[i - 1] + h[i])
    A[i, i + 1] = h[i]
    b[i] = 3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

# Solving for c coefficients
c = np.linalg.solve(A, b)

# Step 3: Calculating b and d coefficients
a = y[:-1]
b = (y[1:] - y[:-1]) / h - h * (2 * c[:-1] + c[1:]) / 3
d = (c[1:] - c[:-1]) / (3 * h)

# Step 4: Evaluating the spline function over each interval
x_fine = np.linspace(x[0], x[-1], 500)
y_fine = np.zeros_like(x_fine)

for i in range(n):
    xi = x[i]
    mask = (x_fine >= xi) & (x_fine <= x[i + 1])
    dx = x_fine[mask] - xi
    y_fine[mask] = a[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3

# Plotting the results
plt.plot(x, y, 'o', label="Data points")
plt.plot(x_fine, y_fine, '-', label="Cubic Spline", color="blue")
plt.xlabel('x')
plt.ylabel('S(x)')
plt.title('Cubic Spline Interpolation (without SciPy)')
plt.legend()
plt.grid(True)
plt.show()
