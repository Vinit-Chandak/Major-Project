import pandas as pd
from matplotlib import pyplot as plt

# Load data from CSV file
data = pd.read_csv("iowa-electricity.csv")

# Create the line chart
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
for source in data["source"].unique():
    source_data = data[data["source"] == source]
    plt.plot(source_data["year"], source_data["net_generation"], label=source)

# Add labels and title
plt.xlabel("Year")
plt.ylabel("Net Generation")
plt.title("Net Electricity Generation in Iowa by Source")
plt.legend()

# Show the plot
plt.show()