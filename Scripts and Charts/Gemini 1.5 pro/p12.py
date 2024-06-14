import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv("mycarsUnique.csv")

# Create the grouped bar chart
plt.figure(figsize=(10, 6))  # Adjust figure size as needed

# Group the data by Name and Type, and calculate the mean Price for each group
grouped_data = data.groupby(["Name", "Type"])["Price"].mean().unstack()

# Plot the grouped bar chart
grouped_data.plot(kind="bar", rot=45)  # Rotate x-axis labels for readability

plt.xlabel("Name")
plt.ylabel("Average Price")
plt.title("Average Price by Car Name and Type")
plt.legend(title="Type", loc="upper right")  # Place legend in upper right

plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()