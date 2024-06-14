import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('myfile.csv')

# Create a box plot
plt.figure(figsize=(8, 6))
data.boxplot(column='B', by='A')
plt.xticks(rotation=45)
plt.xlabel('Category (Column A)')
plt.ylabel('Values (Column B)')
plt.title('Box Plot')

# Display the plot
plt.show()