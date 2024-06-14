import pandas as pd
import plotly.graph_objects as go
import json

# Read the CSV file
population_data = pd.read_csv('population2021.csv')

# Read the GeoJSON file
with open('countries.geojson') as f:
    geojson = json.load(f)

# Create a mapping dictionary from CSV region names to GeoJSON region names
region_mapping = {feature['properties']['ADMIN']: feature['properties']['ADMIN'] for feature in geojson['features']}

# Filter the CSV data to include only the countries present in the GeoJSON file
filtered_population_data = population_data[population_data['ADMIN'].isin(region_mapping.keys())]

# Create the Choropleth map
fig = go.Figure(data=go.Choropleth(
    geojson=geojson,
    locations=filtered_population_data['ADMIN'].map(region_mapping),
    z=filtered_population_data['Population'],
    colorscale='Viridis',
    marker_line_color='white',
    marker_line_width=0.5,
    colorbar_title='Population'
))

# Customize the layout
fig.update_layout(
    title='Population Choropleth Map',
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='natural earth'
    )
)

# Display the map
fig.show()