import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read the CSV file
data = pd.read_csv('iowa-electricity.csv')

# Convert the 'year' column to datetime
data['year'] = pd.to_datetime(data['year'])

# Pivot the data to reshape it for plotting
pivoted_data = data.pivot(index='year', columns='source', values='net_generation')

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data as an area chart
pivoted_data.plot(kind='area', ax=ax, linewidth=2, alpha=0.8, colormap='tab10')

# Set the title and axis labels
ax.set_title('Iowa Electricity Generation by Source', fontsize=16)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Net Generation', fontsize=14)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Format the x-axis ticks as dates
date_formatter = mdates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(date_formatter)

# Add a legend
ax.legend(loc='upper left', fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()