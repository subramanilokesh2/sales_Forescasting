# -*- coding: utf-8 -*-
"""Sales Forecasting.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wjdwCKXFn2Gyl7nxYkxPLO6KBHgXpx_F
"""

import pandas as pd
from google.colab import files
uploaded = files.upload()

# Load the data into a DataFrame
df = pd.read_csv('Dataset.csv')  # replace 'orders.csv' with your file name
df.head()  # Display the first few rows of the dataset

# Check for missing values
print("Missing values in each column:\n", df.isnull().sum())

# Data types of each column
print("\nData types of each column:\n", df.dtypes)

# Convert date columns to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Drop rows with missing values (if necessary)
df = df.dropna()  # Be cautious with this; consider filling missing values instead

# Reset index
df.reset_index(drop=True, inplace=True)

# Display cleaned DataFrame
df.head()

# Summary statistics
print(df.describe())

# Sales per Region
sales_per_region = df.groupby('Region')['Sales'].sum().reset_index()

# Sales per Segment
sales_per_segment = df.groupby('Segment')['Sales'].sum().reset_index()

# Visualizing sales per region
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.barplot(data=sales_per_region, x='Region', y='Sales', palette='viridis')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# Visualizing sales per segment
plt.figure(figsize=(10, 6))
sns.barplot(data=sales_per_segment, x='Segment', y='Sales', palette='rocket')
plt.title('Sales by Segment')
plt.xlabel('Segment')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_orders.csv', index=False)

# Import the necessary module to download files
from google.colab import files

# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_orders.csv', index=False)

# Download the file to your local machine
files.download('cleaned_orders.csv')