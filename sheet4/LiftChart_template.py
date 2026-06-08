import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)

# --------------------------------------------------
# Data generation
# --------------------------------------------------

n_true = 200
n_false = 800
n_total = n_true + n_false

sell_win = 100
return_costs = -25



true_scores = np.random.beta(a=4, b=2, size=n_true)
false_scores = np.random.beta(a=2, b=5, size=n_false)

# Labels
y_true = np.concatenate([
    np.ones(n_true,dtype=bool),
    np.zeros(n_false, dtype=np.bool)
])

# Scores
scores = np.concatenate([
    true_scores,
    false_scores
])

x = np.arange(1, n_total + 1) / n_total
# --------------------------------------------------
# YOUR WORK HERE
# --------------------------------------------------

# 1. Sort the labels (y_true) based on the model's scores in descending order
# argsort sorts ascending, so we use [::-1] to reverse it to descending
sorted_indices = np.argsort(scores)[::-1]
sorted_y_true = y_true[sorted_indices]

# 2. Calculate y_values: The cumulative sum of working devices found
# Since working devices are True (1) and broken are False (0), cumsum works perfectly.
y_values = np.cumsum(sorted_y_true)

# 3. Calculate cumulative profit
# Total devices checked at each step is simply the index + 1
devices_checked = np.arange(1, n_total + 1)
broken_devices_found = devices_checked - y_values

# Profit = (working * 100) + (broken * -25)
profit = (y_values * sell_win) + (broken_devices_found * return_costs)

# 4. Find the threshold (the x-value where profit is highest)
best_index = np.argmax(profit)
threshold = x[best_index]

print("Profit maximum on x=", threshold)

# Random classifier
baseline = x*n_true

# --------------------------------------------------
# Plot (no need to modify)
# --------------------------------------------------

fig, ax = plt.subplots(1,figsize=(4, 3))

ax.plot(x, y_values, label="Model")
ax.plot(x, baseline, linestyle="--", label="Random")

ax.set_xlabel("Sample size")
ax.set_ylabel("# of working devices")
ax.set_title("Lift Chart")
ax_profit = ax.twinx()
ax_profit.plot(x, profit, label = "Profit", ls=":", c="green")
ax_profit.set_ylabel("profit")
ax.axvline(x=threshold, ls="--", c="red", lw="1")
fig.legend()
ax.grid(True)
fig.tight_layout()
plt.show()