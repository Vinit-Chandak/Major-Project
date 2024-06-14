import pandas as pd
import folium
import json

# Read the airports data from the CSV file
airports = pd.read_csv('airports.csv')

# Read the GeoJSON data for the U.S. states
with open('us-states.json') as f:
    states_data = json.load(f)

# Create a Folium map object
map = folium.Map(location=[38.5, -98], zoom_start=4)

# Add the U.S. states to the map
folium.GeoJson(states_data, name='geojson').add_to(map)

# Create a feature group for the airports
airport_markers = folium.FeatureGroup(name='Airports')

# Add markers for the airports to the feature group
for index, airport in airports.iterrows():
    folium.Marker(
        location=[airport['latitude'], airport['longitude']],
        tooltip=airport['name'],
        icon=folium.Icon(color='red')
    ).add_to(airport_markers)

# Add the feature group to the map
airport_markers.add_to(map)

# Add a layer control to toggle the feature groups
folium.LayerControl().add_to(map)

# Save the map to an HTML file
map.save('locator_map.html')