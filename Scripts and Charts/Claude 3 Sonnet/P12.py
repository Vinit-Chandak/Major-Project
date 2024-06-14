import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('mycarsUnique.csv')

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Create the grouped column chart
data = data.groupby(['Name', 'Type'])['Price'].mean().reset_index()
data = data.pivot(index='Name', columns='Type', values='Price')
data.plot(kind='bar', ax=ax, rot=0)

# Set the chart title and axis labels
ax.set_title('Grouped Column Chart of Car Prices')
ax.set_xlabel('Name')
ax.set_ylabel('Average Price')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Display the chart
plt.tight_layout()
plt.show()