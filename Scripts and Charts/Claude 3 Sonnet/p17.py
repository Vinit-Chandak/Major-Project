import matplotlib.pyplot as plt
import pandas as pd

def generate_pyramid_chart(csv_file):
    # Read the data from the CSV file
    data = pd.read_csv(csv_file)

    # Ensure the required columns exist
    required_columns = ['Age Range', 'Male', 'Female']
    if not all(col in data.columns for col in required_columns):
        print("Error: The CSV file does not contain the required columns.")
        return

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))

    # Sort the data by 'Age Range'
    data = data.sort_values(by='Age Range')

    # Get the age ranges
    age_ranges = data['Age Range'].tolist()

    # Plot the bars for females
    ax.barh(age_ranges, data['Female'], color='pink', label='Female')

    # Plot the bars for males
    ax.barh(-data['Male'], age_ranges, color='skyblue', label='Male')

    # Set the axis labels and title
    ax.set_xlabel('Population')
    ax.set_ylabel('Age Range')
    ax.set_title('Population Pyramid')

    # Adjust the x-axis limits
    max_population = max(data['Male'].max(), data['Female'].max())
    ax.set_xlim(-max_population * 1.1, max_population * 1.1)

    # Add a legend
    ax.legend()

    # Adjust the spacing between subplots
    plt.tight_layout()

    # Display the chart
    plt.show()

# Replace 'pyramiddata.csv' with the actual name of your CSV file
generate_pyramid_chart('pyramiddata.csv')