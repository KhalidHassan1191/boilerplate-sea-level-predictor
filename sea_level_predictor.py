import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(df['Year'].min(), 2051)
    sea_level_extended = intercept + slope * years_extended
    plt.plot(years_extended, sea_level_extended, color='red', label='Fit All Data')

    # Create second line of best fit
    recent_data = df[df['Year'] >= 2000]
    recent_slope, recent_intercept, recent_r_value, recent_p_value, recent_std_err = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    recent_years_extended = np.arange(2000, 2051)
    recent_sea_level_extended = recent_intercept + recent_slope * recent_years_extended
    plt.plot(recent_years_extended, recent_sea_level_extended, color='green', label='Fit 2000+ Data')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Call the function to generate the plot
draw_plot()
