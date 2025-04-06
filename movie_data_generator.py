""" Made for My YouTube video. Check it out! https://youtube.com/@hamdivazim """
# Generates data points for varied film ratings and highlights regions for each rating.

import numpy as np
import matplotlib.pyplot as plt
import random

np.random.seed(42)

n_samples = 150
budget_range = (5e6, 200e6)
revenue_range = (1e7, 500e6)
rating_range = (1, 5)

budgets = []
revenues = []
ratings = []

for _ in range(n_samples):
    rating = random.choice([1, 2, 3, 4, 5])
    
    if rating == 1:
        budget = np.random.uniform(5e6, 30e6)
        revenue = budget + np.random.uniform(-budget * 0.3, budget * 0.3)
    elif rating == 2:
        budget = np.random.uniform(20e6, 50e6)
        revenue = budget + np.random.uniform(-budget * 0.2, budget * 0.2)
    elif rating == 3:
        budget = np.random.uniform(40e6, 80e6)
        revenue = budget + np.random.uniform(-budget * 0.15, budget * 0.15)
    elif rating == 4:
        budget = np.random.uniform(70e6, 120e6)
        revenue = budget + np.random.uniform(0, budget * 0.1)
    elif rating == 5:
        budget = np.random.uniform(100e6, 200e6)
        revenue = budget + np.random.uniform(0, budget * 0.15)
    
    if random.random() < 0.05:
        budget = np.random.uniform(5e6, 200e6)
        revenue = np.random.uniform(1e7, 500e6)
    
    budgets.append(budget)
    revenues.append(revenue)
    ratings.append(rating)

budgets = np.array(budgets)
revenues = np.array(revenues)
ratings = np.array(ratings)

colors = ['blue', 'green', 'yellow', 'orange', 'red']
markers = ['o', 's', '^', 'D', 'p']

plt.figure(figsize=(10, 6))
for i, rating in enumerate([1, 2, 3, 4, 5]):
    rating_mask = ratings == rating
    plt.scatter(budgets[rating_mask], revenues[rating_mask], 
                color=colors[i], marker=markers[i], 
                label=f"Rating {rating}", alpha=0.7)

plt.title("Movie Data - Budget vs Box Office Revenue")
plt.xlabel("Budget (in millions)")
plt.ylabel("Box Office Revenue (in millions)")
plt.legend(title="Rating")
plt.grid(True)

plt.figure(figsize=(10, 6))
for i, rating in enumerate([1, 2, 3, 4, 5]):
    rating_mask = ratings == rating
    plt.scatter(budgets[rating_mask], revenues[rating_mask], 
                color=colors[i], marker=markers[i], 
                alpha=0.7)

    x_min, x_max = np.min(budgets[rating_mask]), np.max(budgets[rating_mask])
    y_min, y_max = np.min(revenues[rating_mask]), np.max(revenues[rating_mask])
    
    plt.fill_betweenx([y_min, y_max], x_min, x_max, color=colors[i], alpha=0.2)

for i, rating in enumerate([1, 2, 3, 4, 5]):
    plt.fill_betweenx([0, 0], 0, 0, color=colors[i], alpha=0.2, label=f"Rating {rating} Region")

plt.title("Movie Data with Highlighted Rating Regions")
plt.xlabel("Budget (in millions)")
plt.ylabel("Box Office Revenue (in millions)")
plt.legend(title="Rating")
plt.grid(True)

plt.tight_layout()
plt.show()
