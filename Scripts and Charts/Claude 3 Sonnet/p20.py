import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
cars_data = pd.read_csv('carsMod.csv')

# Extract the relevant columns
mpg = cars_data['mpg']
disp = cars_data['disp']

# Create a scatter plot
plt.scatter(disp, mpg)

# Add labels and title
plt.xlabel('Displacement (disp)')
plt.ylabel('Miles per Gallon (mpg)')
plt.title('Scatter Plot: mpg vs. disp')

# Show the plot
plt.show()