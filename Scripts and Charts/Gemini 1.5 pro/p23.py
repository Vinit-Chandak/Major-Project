import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv("myfileDotPlot.csv")

# Get unique values from column A and their positions
unique_values = data["A"].unique()
positions = range(1, len(unique_values) + 1)

# Create a list to store data for each group
data_list = []
for value in unique_values:
    data_list.append(data[data["A"] == value]["B"])

# Create violin plot using the prepared data
plt.violinplot(data_list, positions=positions, showmeans=True)

# Add labels and title
plt.xlabel("Column A (Categorical)")
plt.ylabel("Column B (Quantitative)")
plt.xticks(positions, unique_values)  # Set x-axis ticks to the unique values
plt.title("Violin Plot of Column B vs. Column A")

# Show the plot
plt.show()