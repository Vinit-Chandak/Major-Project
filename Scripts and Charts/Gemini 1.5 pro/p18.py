import pandas as pd
import plotly.express as px

# Load data from CSV
data = pd.read_csv("iowa-electricity.csv")

# Filter data for specific columns and sort by year
data = data[["year", "source", "net_generation"]].sort_values(by="year")

# Create radar chart for each year
for year, group in data.groupby("year"):
  fig = px.line_polar(group, r="net_generation", theta="source", line_close=True,
                     title=f"Net Electricity Generation in Iowa by Source ({year})")
  fig.show()