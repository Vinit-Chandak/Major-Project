import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("mycarsUnique.csv")

# Create the grouped bar chart
plt.figure(figsize=(10, 6))  # Adjust figure size as needed

# Group data by Name and Type
grouped_data = data.groupby(['Name', 'Type'])['Price'].sum().unstack()

# Plot the grouped bar chart
grouped_data.plot(kind='bar', stacked=False)

# Customize chart elements
plt.xlabel("Name")
plt.ylabel("Price")
plt.title("Price by Name and Type")
plt.legend(title="Type", loc='upper right')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for readability

# Show the plot
plt.show()