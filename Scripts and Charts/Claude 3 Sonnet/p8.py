import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
data = pd.read_csv('myfile.csv')

# Get the categorical and quantitative columns
categories = data['A']
values = data['B']

# Create the Donut chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax.set_title('Donut Chart')

# Draw the center circle
center_circle = plt.Circle((0, 0), 0.7, fc='white')
fig.gca().add_artist(center_circle)

plt.show()