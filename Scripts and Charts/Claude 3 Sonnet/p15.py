import matplotlib.pyplot as plt
import csv

# Read data from the CSV file
data = []
with open('myfile.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append((row['A'], float(row['B'])))

# Sort the data by the quantitative value (column B)
data.sort(key=lambda x: x[1], reverse=True)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Pictogram Chart')
ax.set_xlabel('Category')
ax.set_ylabel('Quantity')

# Set up the pictogram markers
marker = '$\u25A0$'  # Unicode character for a filled square
marker_size = 100  # Size of the marker

# Plot the pictogram
categories = [category for category, _ in data]
quantities = [quantity for _, quantity in data]
y_pos = range(len(categories))

for i, quantity in enumerate(quantities):
    marker_count = int(quantity)
    markers = [marker] * marker_count
    ax.scatter([i] * marker_count, [j + 1 for j in range(marker_count)], s=marker_size, marker=marker, edgecolors='none')
    ax.annotate(str(int(quantity)), (i, marker_count + 0.5), ha='center', va='bottom')

ax.set_xticks(y_pos)
ax.set_xticklabels(categories)

# Adjust layout and display the chart
plt.tight_layout()
plt.show()