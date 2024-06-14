import pandas as pd
import plotly.express as px

# Read the airports data
airports_df = pd.read_csv("airports.csv")

# Create the scatter mapbox plot
fig = px.scatter_mapbox(airports_df, lat="latitude", lon="longitude", hover_name="name",
                        hover_data=["city", "state"], zoom=3, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_traces(marker={"size": 8})

fig.show()