import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv("myfileDotPlot.csv")

# Get categorical and quantitative columns
categorical_column = data["A"]
quantitative_column = data["B"]

# Create figure and axes
fig, ax = plt.subplots()

# Generate dot plot
for category in categorical_column.unique():
    category_data = quantitative_column[categorical_column == category]
    x = [category] * len(category_data)
    ax.scatter(x, category_data, s=20)

# Set labels and title
ax.set_xlabel("Category (Column A)")
ax.set_ylabel("Value (Column B)")
ax.set_title("Dot Plot of Column B vs. Column A")

# Show the plot
plt.show()