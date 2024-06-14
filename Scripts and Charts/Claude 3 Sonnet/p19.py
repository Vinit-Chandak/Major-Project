import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('myfileDotPlot2Values.csv')

# Create the range plot
fig, ax = plt.subplots()
data.boxplot(column='B', by='A', ax=ax, showmeans=True)

# Set the title and axis labels
ax.set_title('Range Plot')
ax.set_xlabel('Category (Column A)')
ax.set_ylabel('Value (Column B)')

# Show the plot
plt.show()