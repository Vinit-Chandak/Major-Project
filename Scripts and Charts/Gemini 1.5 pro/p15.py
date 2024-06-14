import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV
data = pd.read_csv("myfile.csv")

# Get categorical and quantitative columns
categories = data["A"]
values = data["B"]

# Define the symbol for the pictogram (e.g., *, $, O, etc.)
symbol = "*"

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate symbol repetitions based on values
symbol_repetitions = (values / values.max() * 50).astype(int)  # Adjust 50 for desired size

# Loop through categories and values to create pictograms
for i, (category, count) in enumerate(zip(categories, symbol_repetitions)):
    # Display symbols
    ax.text(i+0.5, 0.5, symbol * count, ha="center", va="center", fontsize=12)

    # Add text for category below
    ax.text(i+0.5, 0, category, ha="center", va="top", fontsize=10)

# Set labels and title
ax.set_xticks(range(len(categories)))
ax.set_xticklabels(categories)
ax.set_yticks([])
ax.set_title("Pictogram Chart")

# Remove spines and grid
ax.spines[["top", "right", "left", "bottom"]].set_visible(False)
ax.grid(False)

# Show the plot
plt.show()