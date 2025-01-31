'''
To find the surface of resulution(SOR) of the function cos x + sqrt(x) in the interval 0 to 6 of x. For the step sizes h=[0.05, 0.01, 0.005, 0.001]
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function f(x)
def f(x):
    return np.cos(x) + np.sqrt(x)

# Derivative of f(x) with a condition to handle x = 0
def df_dx(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(x == 0, 0, -np.sin(x) + 0.5 / np.sqrt(x))

# Surface area calculation using the trapezoidal rule
def surface_area_SOR(a, b, h):
    x_values = np.arange(a + 1e-5, b + h, h)  # Start slightly above 0
    y_values = f(x_values)
    dy_dx_values = df_dx(x_values)
    integrand_values = 2 * np.pi * y_values * np.sqrt(1 + dy_dx_values**2)
    # Trapezoidal approximation of the integral
    surface_area = np.trapz(integrand_values, x_values)
    return surface_area

# Setting up parameters
a, b = 0, 6
step_sizes = [0.05, 0.01, 0.005, 0.001]
results = []

# Calculate and store surface area for each step size
for h in step_sizes:
    area = surface_area_SOR(a, b, h)
    results.append({"Step Size (h)": h, "Surface Area": area})

# Convert results to a DataFrame for tabulation
results_df = pd.DataFrame(results)
print(results_df)

# Plot the results
plt.plot(results_df["Step Size (h)"], results_df["Surface Area"], marker='o')
plt.xlabel("Step Size (h)")
plt.ylabel("Surface Area")
plt.title("Surface Area of SOR vs. Step Size")
plt.grid(True)
plt.show()
