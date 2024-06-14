import csv
import matplotlib.pyplot as plt

# Open the CSV file
with open('myfile.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Extract the data from columns A and B
categories = [row['A'] for row in data]
values = [float(row['B']) for row in data]

# Create the column chart
fig, ax = plt.subplots()
ax.bar(categories, values)

# Set chart title and axis labels
ax.set_title('Column Chart')
ax.set_xlabel('Categories')
ax.set_ylabel('Values')

# Rotate the x-axis labels for better visibility
plt.xticks(rotation=45)

# Display the chart
plt.show()