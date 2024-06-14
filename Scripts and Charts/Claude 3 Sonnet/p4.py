import pandas as pd
import plotly.express as px

# Read the CSV file
cars_data = pd.read_csv('carsMod.csv')

# Create the Bubble chart
fig = px.scatter(cars_data, x='mpg', y='disp', size='hp', hover_name='cyl',
                 color='am', size_max=60, title='Bubble Chart for Cars Data')

# Customize the axis labels and title
fig.update_layout(
    xaxis_title='Miles per Gallon (mpg)',
    yaxis_title='Displacement (disp)',
    title_x=0.5,  # Center the title
)

# Display the chart
fig.show()