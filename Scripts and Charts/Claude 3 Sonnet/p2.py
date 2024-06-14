import csv
import matplotlib.pyplot as plt

# Open the CSV file
with open('myfile.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Extract the category labels and values from the data
categories = [row['A'] for row in data]
values = [float(row['B']) for row in data]

# Create the bar chart
fig, ax = plt.subplots()
ax.bar(categories, values)

# Set the chart title and axis labels
ax.set_title('Bar Chart')
ax.set_xlabel('Category')
ax.set_ylabel('Value')

# Rotate the x-axis labels for better visibility
plt.xticks(rotation=45)

# Show the chart
plt.tight_layout()
plt.show()