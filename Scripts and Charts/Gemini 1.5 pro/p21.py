import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
data = pd.read_csv("mycarsUnique.csv")

# Group data by Name and Type, and calculate sum of Price for each group
grouped_data = data.groupby(['Name', 'Type'])['Price'].sum().unstack()

# Create stacked bar chart
grouped_data.plot(kind='bar', stacked=True)

# Customize chart
plt.xlabel("Name")
plt.ylabel("Price")
plt.title("Stacked Bar Chart of Price by Name and Type")
plt.legend(title="Type")

# Show the plot
plt.show()