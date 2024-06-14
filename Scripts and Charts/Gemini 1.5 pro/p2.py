import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("myfile.csv")

# Extract the required columns
category = data["A"]
values = data["B"]

# Create the bar chart
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
plt.bar(category, values)

# Add labels and title
plt.xlabel("Category (A)")
plt.ylabel("Values (B)")
plt.title("Bar Chart of Category vs Values")

# Customize the chart further as needed (e.g., colors, grid, etc.)

# Display the chart
plt.show()