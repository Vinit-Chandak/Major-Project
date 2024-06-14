import pandas as pd
import plotly.graph_objects as go

# Read the CSV file
df = pd.read_csv('pyramiddata.csv')

# Create the figure
fig = go.Figure()

# Add bullet traces for Male and Female columns
fig.add_trace(go.Scatter(
    x=df['Male'],
    y=df['Age Range'],
    mode='markers',
    marker=dict(color='blue', size=10),
    name='Male',
    orientation='h'
))

fig.add_trace(go.Scatter(
    x=df['Female'],
    y=df['Age Range'],
    mode='markers',
    marker=dict(color='red', size=10),
    name='Female',
    orientation='h'
))

# Update layout
fig.update_layout(
    title='Bullet Chart',
    xaxis_title='Value',
    yaxis_title='Age Range',
    bargap=0.1,
    bargroupgap=0,
    yaxis_categoryorder='array',
    yaxis_categoryarray=df['Age Range'][::-1]
)

# Show the plot
fig.show()