import numpy as np
import matplotlib.pyplot as plt

# Function and its derivative
x = np.linspace(-5, 5, 100)
f_x = x**2
df_x = 2*x  # Derivative of x^2

# Plot function
plt.plot(x, f_x, label="f(x) = x²", color="blue")
plt.plot(x, df_x, label="f'(x) = 2x", color="red", linestyle="dashed")

# Highlight tangent at x=3
x_tangent = 18
y_tangent = x_tangent**2
slope = 2 * x_tangent
tangent_line = slope * (x - x_tangent) + y_tangent
plt.plot(x, tangent_line, 'green', linestyle="dotted", label="Tangent at x=3")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Function and its Derivative")
plt.grid()
plt.show()