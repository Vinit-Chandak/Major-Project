import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("mycarsUnique.csv")

# Create a pivot table with "Name" as rows, "Type" as columns, and "Price" as values
pivot_table = pd.pivot_table(df, values="Price", index=["Name"], columns=["Type"], aggfunc="sum", fill_value=0)

# Create a stacked bar chart
pivot_table.plot(kind="bar", stacked=True, figsize=(10, 6))

# Add labels and title
plt.xlabel("Name", fontsize=12)
plt.ylabel("Price", fontsize=12)
plt.title("Stacked Bar Chart of Car Prices by Type", fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha="right")

# Add a legend
plt.legend(title="Type", loc="upper left", bbox_to_anchor=(1.01, 1))

# Adjust spacing between subplots
plt.subplots_adjust(right=0.7)

# Display the chart
plt.show()