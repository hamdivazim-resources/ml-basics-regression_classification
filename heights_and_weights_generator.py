""" Made for My YouTube video. Check it out! https://youtube.com/@hamdivazim """
# Generates height and weight data, and a line+curve of best fit.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

def generate_height_weight_data(n=100):
    np.random.seed(42)
    heights = np.random.normal(loc=170, scale=10, size=n)
    weights = 50 + (heights - 150) * 0.6 + np.random.normal(loc=0, scale=8, size=n)
    data = pd.DataFrame({'Height (cm)': heights, 'Weight (kg)': weights})
    return data

def plot_data(data):
    plt.figure(figsize=(8, 6))
    plt.scatter(data['Height (cm)'], data['Weight (kg)'], alpha=0.6, edgecolors='k')
    plt.xlabel("Height (cm)")
    plt.ylabel("Weight (kg)")
    plt.title("Height vs Weight Data")
    plt.show()

def join_points(data):
    plt.figure(figsize=(8, 6))
    plt.plot(data['Height (cm)'].sort_values().values, data.sort_values("Height (cm)")['Weight (kg)'].values, marker='o', linestyle='-', alpha=0.6)
    plt.xlabel("Height (cm)")
    plt.ylabel("Weight (kg)")
    plt.title("Joined Data Points")
    plt.show()

def line_of_best_fit(data):
    m, b = np.polyfit(data['Height (cm)'], data['Weight (kg)'], 1)
    plt.figure(figsize=(8, 6))
    plt.scatter(data['Height (cm)'], data['Weight (kg)'], alpha=0.6, edgecolors='k')
    plt.plot(data['Height (cm)'], m * data['Height (cm)'] + b, color='red')
    plt.xlabel("Height (cm)")
    plt.ylabel("Weight (kg)")
    plt.title("Line of Best Fit")
    plt.show()

def curve_of_best_fit(data):
    coefs = poly.Polynomial.fit(data['Height (cm)'], data['Weight (kg)'], 2).convert().coef
    x = np.linspace(min(data['Height (cm)']), max(data['Height (cm)']), 100)
    y = coefs[0] + coefs[1] * x + coefs[2] * x**2
    plt.figure(figsize=(8, 6))
    plt.scatter(data['Height (cm)'], data['Weight (kg)'], alpha=0.6, edgecolors='k')
    plt.plot(x, y, color='green')
    plt.xlabel("Height (cm)")
    plt.ylabel("Weight (kg)")
    plt.title("Curve of Best Fit")
    plt.show()

def save_data_to_csv(data, filename="height_weight_data.csv"):
    data.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

data = generate_height_weight_data(n=100)
plot_data(data)
join_points(data)
line_of_best_fit(data)
curve_of_best_fit(data)
save_data_to_csv(data)
print(data.head())
