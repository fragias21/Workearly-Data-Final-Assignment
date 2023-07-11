# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file into a DataFrame
df = pd.read_csv("finance_liquor_sales(2016_2019).csv")

# Group the data by zip code and calculate the total bottles sold
grouped = df.groupby('zip_code')['bottles_sold'].sum()

# Get unique zip codes and generate random colors
unique_zip_codes = grouped.index.unique()
num_colors = len(unique_zip_codes)
colors = np.random.rand(num_colors)

# Scatter plot for bottles sold by zip code
plt.scatter(grouped.index, grouped.values, c=colors)
plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')
plt.title('Bottles Sold')

# Display the plot
plt.show()

# Get the most popular item sold based on zip code
most_popular_per_zip_code = pd.DataFrame(df.groupby(by=['zip_code', 'item_description']).sum()['bottles_sold']).reset_index()

# Convert zip_code column to integer
most_popular_per_zip_code['zip_code'] = most_popular_per_zip_code['zip_code'].astype(int)

# Sort the values by Zip Code
most_popular_per_zip_code.sort_values(by=['zip_code', 'bottles_sold'], ascending=[True, False])

# Export it in csv file
most_popular_per_zip_code.to_csv('most_popular_per_zip_code.csv')