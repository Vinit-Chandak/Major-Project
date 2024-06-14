import pandas as pd
import geopandas as gpd
import folium

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('population2021.csv')

# Read the GeoJSON file into a GeoDataFrame
gdf = gpd.read_file('countries.geojson')

# Merge the DataFrame and GeoDataFrame based on the 'ADMIN' column
merged = gdf.merge(df, left_on='ADMIN', right_on='ADMIN', how='left')

# Create a Folium map object
m = folium.Map(location=[0, 0], zoom_start=2)

# Add a choropleth layer with graduated symbols
choropleth = folium.Choropleth(
    geo_data=merged,
    name='Choropleth',
    data=merged,
    columns=['ADMIN', 'Population'],
    key_on='feature.properties.ADMIN',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Population',
    highlight=True
).add_to(m)

# Save the map as an HTML file
m.save("graduated_symbol_map.html")