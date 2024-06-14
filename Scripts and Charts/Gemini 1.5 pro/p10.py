import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load data
population_data = pd.read_csv("population2021.csv")
countries_geojson = gpd.read_file("countries.geojson")

# Merge data on ADMIN column
merged_data = countries_geojson.merge(population_data, on="ADMIN", how="left")

# Calculate quantiles and create categories
quantiles = merged_data["Population"].quantile([0, 0.25, 0.5, 0.75, 1])
merged_data["population_category"] = pd.cut(merged_data["Population"], 
                                            bins=quantiles, 
                                            labels=["Low", "Medium", "High", "Very High"], # Corrected labels
                                            include_lowest=True)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot graduated symbol map using population_category
merged_data.plot(column="population_category", legend=True, ax=ax, 
                 markersize="Population", cmap="YlOrRd")

# Customize plot
ax.set_title("Population by Region - Graduated Symbol Map")
ax.axis('off')

# Show plot
plt.show()