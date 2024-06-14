import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv("myfile.csv")

# Create the column chart using pandas plot
data.plot(kind="bar", x="A", y="B")

# Add labels and title
plt.xlabel("Category A")
plt.ylabel("Value B")
plt.title("Column Chart of A vs B")

# Show the plot
plt.show()