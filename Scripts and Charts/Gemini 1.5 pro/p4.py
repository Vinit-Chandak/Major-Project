import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("carsMod.csv")

# Prepare data
mpg = data['mpg']
disp = data['disp']
hp = data['hp']

# Create figure and axis
fig, ax = plt.subplots()

# Plot bubble chart
ax.scatter(disp, mpg, s=hp/5, alpha=0.7)

# Customize the plot
ax.set_xlabel('Displacement (disp)')
ax.set_ylabel('Miles per Gallon (mpg)')
ax.set_title('Bubble Chart: mpg vs disp, size by hp')

# Show the plot
plt.show()