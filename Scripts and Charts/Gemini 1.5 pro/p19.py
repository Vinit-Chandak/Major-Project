import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV
data = pd.read_csv("myfileDotPlot2Values.csv")

# Create the range plot using Seaborn
sns.catplot(x="A", y="B", kind="violin", data=data)
plt.show()