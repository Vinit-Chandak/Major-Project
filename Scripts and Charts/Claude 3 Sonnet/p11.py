import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('mycarsUnique.csv')

# Create a grouped bar chart
grouped = data.groupby(['Name', 'Type'])['Price'].mean().reset_index()
grouped = grouped.pivot('Name', 'Type', 'Price')

fig, ax = plt.subplots(figsize=(10, 6))
grouped.plot(kind='bar', ax=ax)

ax.set_xlabel('Name')
ax.set_ylabel('Average Price')
ax.set_title('Average Price by Name and Type')
ax.legend(title='Type', loc='best')

plt.tight_layout()
plt.show()