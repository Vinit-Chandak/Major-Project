import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Read the CSV and GeoJSON files
data = pd.read_csv("population2021.csv")
countries = gpd.read_file("countries.geojson")

# Merge the data and geometry based on the 'ADMIN' column
merged_data = countries.merge(data, on='ADMIN')

# Create the choropleth map
fig, ax = plt.subplots(figsize=(10, 6))
merged_data.plot(column='Population', cmap='YlOrRd', legend=True, ax=ax)
ax.set_title('Choropleth Map of Population by Region')
ax.set_axis_off()

plt.show()