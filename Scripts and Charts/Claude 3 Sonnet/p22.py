import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('mycarsUnique.csv')

# Create a stacked column chart
data.pivot(index='Name', columns='Type', values='Price').plot(kind='bar', stacked=True, figsize=(10, 6))

# Set the title and axis labels
plt.title('Car Prices by Type', fontsize=16)
plt.xlabel('Name', fontsize=14)
plt.ylabel('Price', fontsize=14)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Display the chart
plt.tight_layout()
plt.show()