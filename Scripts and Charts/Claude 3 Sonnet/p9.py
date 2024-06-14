import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('myfileDotPlot.csv')

# Extract the columns A and B
category = data['A']
values = data['B']

# Create the dot plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(category, values, marker='o', s=50, alpha=0.6)

# Add labels and title
ax.set_xlabel('Category (Column A)')
ax.set_ylabel('Values (Column B)')
ax.set_title('Dot Plot')

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()