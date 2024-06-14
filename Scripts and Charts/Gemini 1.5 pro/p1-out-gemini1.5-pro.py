import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv("iowa-electricity.csv")

# Convert 'year' column to datetime format
data['year'] = pd.to_datetime(data['year'])

# Set 'year' as the index
data = data.set_index('year')

# Create pivot table to group net generation by source and year
pivot_data = data.pivot_table(values='net_generation', index='year', columns='source', aggfunc='sum')

# Plot the area chart
pivot_data.plot(kind='area', stacked=False)

# Customize the plot
plt.title("Iowa Electricity Net Generation by Source")
plt.xlabel("Year")
plt.ylabel("Net Generation (MWh)")
plt.legend(title="Source")

# Show the plot
plt.show()