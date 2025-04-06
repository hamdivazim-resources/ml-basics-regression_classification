""" Made for My YouTube video. Check it out! https://youtube.com/@hamdivazim """
# Generates fake stock data that follows a logarithmic trend.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

np.random.seed(42)
x = np.linspace(1, 100, 100)
y = 15 * np.log(x) + np.random.normal(scale=15, size=len(x))


def log_model(x, a, b):
    return a * np.log(x) + b

params, _ = curve_fit(log_model, x, y)
a_fit, b_fit = params
y_fit = log_model(x, a_fit, b_fit)


x_extended = np.linspace(1, 150, 150)
y_extended_fit = log_model(x_extended, a_fit, b_fit)


new_x = x_extended[100:]
new_y = log_model(new_x, a_fit, b_fit) + np.random.normal(scale=16, size=len(new_x))


plt.figure(figsize=(7, 5))
plt.fill_between(x, y, color="skyblue", alpha=0.2)
plt.scatter(x, y, s=10, color="blue")
plt.title("Stock Value over Time")
plt.xlabel("Time")
plt.ylabel("Stock Value")
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(7, 5))
plt.fill_between(x, y, color="skyblue", alpha=0.2)
plt.scatter(x, y, s=10, color="blue")
plt.title("Stock Value over Time")
plt.xlabel("Time")
plt.ylabel("Stock Value")
plt.xlim(0, 150)
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(7, 5))
plt.fill_between(x, y, color="skyblue", alpha=0.2)
plt.scatter(x, y, s=10, color="blue")
plt.plot(x, y_fit, color="red")
plt.title("Stock Value over Time with Curve of Best Fit")
plt.xlabel("Time")
plt.ylabel("Stock Value")
plt.xlim(0, 150)
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(7, 5))
plt.fill_between(x, y, color="skyblue", alpha=0.2)
plt.scatter(x, y, s=10, color="blue")
plt.plot(x_extended, y_extended_fit, color="green")
plt.title("Stock Value over Time with Extrapolated Curve of Best Fit")
plt.xlabel("Time")
plt.ylabel("Stock Value")
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(7, 5))
plt.fill_between(x, y, color="skyblue", alpha=0.25)
plt.fill_between(new_x, new_y, color="orange", alpha=0.25)
plt.scatter(x, y, s=10, color="blue")
plt.plot(x_extended, y_extended_fit, color="green")
plt.scatter(new_x, new_y, color="orange", s=10)

plt.plot([x[-1], new_x[0]], [y[-1], y_extended_fit[100]], color="green", linestyle="--")

plt.title("Stock Value over Time with Predicted Future Data")
plt.xlabel("Time")
plt.ylabel("Stock Value")
plt.grid(True)
plt.tight_layout()
plt.show()
