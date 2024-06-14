import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv("mycarsUnique.csv")

# Create stacked column chart
data.pivot_table(values="Price", index="Name", columns="Type", aggfunc="sum").plot(kind="bar", stacked=True)

# Add labels and title
plt.xlabel("Name")
plt.ylabel("Price")
plt.title("Stacked Column Chart of Price by Name and Type")

# Display the chart
plt.show()