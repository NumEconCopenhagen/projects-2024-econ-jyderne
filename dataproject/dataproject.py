import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets

# Importing csv data 
file_path = "FPI_KEY_2008_FORWARD.xlsx"
df = pd.read_excel(file_path)

# Select the columns 1 to 14
columns_1_to_18 = df.columns[1:18]

# Calculate the average for each year
average_by_year = df.groupby('Year')[columns_1_to_18].mean()

# Convert the averages into a DataFrame
average_df = pd.DataFrame(average_by_year)

# Calculate growth rates
growth_rates = average_df.pct_change().dropna()

# Get the first row
first_row = growth_rates.iloc[0]

# Get the last row
last_row = growth_rates.iloc[-1]

# Calculate the number of years
num_years = len(growth_rates)

# Calculate the average growth rate
average_growth_rate = (last_row / first_row) ** (1 / num_years) - 1

def plot_growth_rates(category):
    plt.figure(figsize=(10, 6))
    plt.plot(growth_rates.index, growth_rates[category], marker='o')
    plt.title(f'Growth Rates for {category}')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate')
    plt.grid(True)
    plt.show()

# Creating a dropdown widget
dropdown = widgets.Dropdown(options=columns_1_to_18, description='Category:')
widgets.interactive(plot_growth_rates, category=dropdown)
