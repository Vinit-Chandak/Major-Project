# Import libraries
import pandas as pd
import plotly.graph_objects as go

# Read the CSV file
data = pd.read_csv("myfile.csv")

# Get the values from columns A and B
labels = data["A"]
values = data["B"]

# Create the donut chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

# Update layout for better visualization
fig.update_layout(title_text="Donut Chart from myfile.csv")

# Show the plot
fig.show()