import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.patches as patches

# Read data from CSV
data = pd.read_csv("pyramiddata.csv")

# Function to create a bullet chart
def create_bullet_chart(age_range, male_value, female_value, ax):
    # Set plot limits
    max_value = max(male_value, female_value) * 1.1  # Add 10% buffer
    
    # Male bar
    ax.barh(age_range, male_value, height=0.8, label="Male", color="#4285f4")
    
    # Female bar (ensuring correct positioning)
    ax.barh(age_range, female_value, height=0.8, left=male_value, label="Female", color="#db4437")
    
    # Target line (assuming 50% as target for each category)
    ax.axvline(max_value / 2, color="gray", linestyle="--")
    
    # Qualitative ranges (assuming equal distribution for simplicity)
    range_width = max_value / 4
    for i in range(1, 4):
        start = i * range_width
        end = start + range_width
        ax.add_patch(
            patches.Rectangle((start, 0), range_width, 1, facecolor="lightgray", alpha=0.5)
        )

    # Configure chart (explicitly set y-tick labels and order)
    ax.set_yticks(range(len(age_range)))
    ax.set_yticklabels(age_range, fontsize=8)  # Adjust fontsize as needed
    ax.set_xlabel("Population")
    ax.set_xlim(0, max_value)
    ax.legend()

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate bullet chart for each age range
for i, row in data.iterrows():
    create_bullet_chart(row["Age Range"], row["Male"], row["Female"], ax)

# Show the plot
plt.show()