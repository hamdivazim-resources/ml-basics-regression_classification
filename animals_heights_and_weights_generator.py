""" Made for My YouTube video. Check it out! https://youtube.com/@hamdivazim """
# Generates height and weight data for three types of animals, and figure with highlighted regions.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import pandas as pd

np.random.seed(42)
animals = {
    "Cat": (25, 5, 6, 3),
    "Hippo": (150, 1500, 20, 100),
    "Giraffe": (500, 800, 30, 50)
}

X, y = [], []
for animal, (h_mean, w_mean, h_var, w_var) in animals.items():
    heights = np.random.normal(h_mean, h_var, 20)
    weights = np.random.normal(w_mean, w_var, 20)
    X.extend(zip(heights, weights))
    y.extend([animal] * 20)

X = np.array(X)
y = np.array(y)

new_point = np.array([160, 1400])
new_label = "New Animal"

data = {
    "Height (cm)": X[:, 0].tolist() + [new_point[0]],
    "Weight (kg)": X[:, 1].tolist() + [new_point[1]],
    "Animal": list(y) + [new_label]
}

df = pd.DataFrame(data)

df.to_csv("animals_data.csv", index=False)

plt.figure(figsize=(10, 5))
plt.subplot(1, 1, 1)
for animal in animals.keys():
    indices = [i for i in range(len(y)) if y[i] == animal]
    plt.scatter(X[indices, 0], X[indices, 1], label=animal, marker='x')
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Animal Height vs Weight")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
for animal in animals.keys():
    indices = [i for i in range(len(y)) if y[i] == animal]
    plt.scatter(X[indices, 0], X[indices, 1], label=animal, marker='x')

plt.scatter(new_point[0], new_point[1], color='purple', label=new_label, marker='o')
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Animal Height vs Weight with New Animal?")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.scatter(X[:, 0], X[:, 1], c=["r" if label == "Cat" else "g" if label == "Hippo" else "b" for label in y], label=y, marker='x')  # Use crosses for all points
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Highlighted Animal Regions")

def draw_ellipse(ax, center, width, height, color, alpha=0.2):
    ellipse = Ellipse(center, width, height, edgecolor=color, facecolor=color, alpha=alpha, linewidth=2)
    ax.add_patch(ellipse)

ax = plt.gca()
draw_ellipse(ax, (25, 5), 20, 10, 'r')
draw_ellipse(ax, (150, 1500), 80, 600, 'g')
draw_ellipse(ax, (500, 800), 100, 200, 'b')

plt.scatter(new_point[0], new_point[1], color='purple', label=new_label, marker='o')

plt.legend(["Cats", "Hippos", "Giraffes"])

plt.tight_layout()
plt.show()
