# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv("carsMod.csv")

# Extract desired columns
mpg = data["mpg"]
disp = data["disp"]

# Create scatterplot
plt.figure(figsize=(8,6))  # Adjust figure size as needed
plt.scatter(disp, mpg, s=50)  # s: marker size

# Add labels and title
plt.xlabel("Displacement (disp)", fontsize=12)
plt.ylabel("Miles per Gallon (mpg)", fontsize=12)
plt.title("Scatterplot of Displacement vs. MPG", fontsize=14)

# Show the plot
plt.grid(True)  # Add grid for better visualization
plt.show()