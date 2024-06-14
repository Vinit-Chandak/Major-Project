import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
data = pd.read_csv("pyramiddata.csv")

# Ensure Age Range is sorted
data.sort_values(by="Age Range", inplace=True)

# Separate male and female data
male_data = data["Male"]
female_data = -data["Female"]  # Negative for left side of chart

# Define x-axis labels and tick locations
x_labels = data["Age Range"]
tick_locations = range(len(x_labels))

# Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 7))

# Plot male and female bars
ax.barh(tick_locations, male_data, height=0.8, label="Male")
ax.barh(tick_locations, female_data, height=0.8, label="Female")

# Set axis labels and title
ax.set_xlabel("Population")
ax.set_ylabel("Age Range")
ax.set_title("Population Pyramid")

# Set x-axis ticks and labels
ax.set_xticks(tick_locations)
ax.set_xticklabels(x_labels, rotation=45, ha="right")

# Add legend and grid
ax.legend()
ax.grid(axis="x")

# Display the chart
plt.show()