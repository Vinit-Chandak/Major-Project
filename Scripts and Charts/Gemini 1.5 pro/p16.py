import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv("myfile.csv")

# Get the data for columns A and B
categories = data["A"]
values = data["B"]

# Create the pie chart
plt.pie(values, labels=categories)

# Add a title
plt.title("Pie chart of A vs B")

# Show the plot
plt.show()