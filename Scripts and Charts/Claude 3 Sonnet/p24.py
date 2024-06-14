import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv("heatmapDataOrig.csv")

# Pivot the data to create a matrix with columns A and rows B
pivoted_data = data.pivot(index="B", columns="A", values="C")

# Create the heatmap
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(pivoted_data, annot=True, cmap="YlGnBu")

# Assign titles and labels
plt.title("XY Heatmap", fontsize=16)
plt.xlabel("Column A", fontsize=12)
plt.ylabel("Column B", fontsize=12)

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Display the heatmap
plt.show()