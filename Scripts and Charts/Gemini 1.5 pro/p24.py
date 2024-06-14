import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv("heatmapDataOrig.csv")

# Create a pivot table with A as index, B as columns and C as values
pivot_data = data.pivot_table(values="C", index="A", columns="B")

# Generate the heatmap using Seaborn
sns.heatmap(pivot_data, cmap="YlGnBu")
plt.xlabel("Column B (Categorical)")
plt.ylabel("Column A (Categorical)")
plt.title("Heatmap of C based on A and B")

# Show the plot
plt.show()