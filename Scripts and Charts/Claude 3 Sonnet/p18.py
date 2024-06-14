import pandas as pd
import plotly.graph_objects as go

# Read the CSV file
data = pd.read_csv('iowa-electricity.csv')

# Convert the 'year' column to datetime and sort the data by year
data['year'] = pd.to_datetime(data['year'])
data = data.sort_values(by='year')

# Get unique sources and years
sources = data['source'].unique()
years = data['year'].dt.year.unique()

# Create a list to hold the traces
traces = []

for year in years:
    # Filter the data for the current year
    year_data = data[data['year'].dt.year == year]

    # Convert the data to a long format
    long_data = pd.melt(year_data, id_vars=['source'], value_vars='net_generation', var_name='variable', value_name='value')

    # Create a trace for the current year
    trace = go.Scatterpolar(
        r=long_data['value'],
        theta=long_data['source'],
        fill='toself',
        mode='lines+markers',
        name=str(year)
    )
    traces.append(trace)

# Create the layout
layout = go.Layout(
    title='Iowa Electricity Generation by Source and Year',
    font=dict(size=14),
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, data['net_generation'].max() * 1.1]  # Adjust the radial limit to fit the data
        ),
        angularaxis=dict(
            tickvals=[i for i in range(len(sources))],  # Convert to a list
            ticktext=sources
        )
    )
)

# Create the figure and show the chart
fig = go.Figure(data=traces, layout=layout)
fig.show()