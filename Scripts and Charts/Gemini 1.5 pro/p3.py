import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("myfile.csv")

# Create the box plot
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
data.boxplot(column="B", by="A")
plt.xlabel("A (Categorical)")
plt.ylabel("B (Quantitative)")
plt.title("Box Plot of B by A")
plt.suptitle("")  # Remove the automatic suptitle

# Show the plot
plt.show()