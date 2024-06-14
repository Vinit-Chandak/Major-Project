import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
data = pd.read_csv('myfile.csv')

# Assuming column A contains the categories and column B contains the values
categories = data['A']
values = data['B']

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(values, labels=categories, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()