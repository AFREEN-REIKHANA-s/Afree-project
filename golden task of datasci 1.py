import pandas as pd
import matplotlib.pyplot as plt

# Reading the data files
working_data = pd.read_csv("C:\\Users\\HP\\Downloads\\store transaction\\Hackathon_Working_Data.csv")
validation_data = pd.read_csv("C:\\Users\\HP\\Downloads\\store transaction\\Hackathon_Validation_Data.csv")
ideal_data = pd.read_csv("C:\\Users\\HP\\Downloads\\store transaction\\Hackathon_Ideal_Data.csv")
mapping_file = pd.read_csv("C:\\Users\\HP\\Downloads\\store transaction\\Hackathon_Mapping_File.csv")

# Displaying the first few rows of each dataset
print("Working Data:")
print(working_data.head())
print("\nValidation Data:")
print(validation_data.head())
print("\nIdeal Data:")
print(ideal_data.head())
print("\nMapping File:")
print(mapping_file.head())

# Visualizing data
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Histogram for PRICE column in Hackathon_Working_Data
if 'PRICE' in working_data.columns:
    axes[0, 0].hist(working_data['PRICE'], bins=20, color='skyblue', edgecolor='black')
    axes[0, 0].set_title('Histogram of PRICE')
    axes[0, 0].set_xlabel('Price')
    axes[0, 0].set_ylabel('Frequency')

# Scatter plot for MONTH vs GRP in Hackathon_Validation_Data
if 'MONTH' in validation_data.columns and 'GRP' in validation_data.columns:
    axes[0, 1].scatter(validation_data['MONTH'], validation_data['GRP'], alpha=0.6, color='green')
    axes[0, 1].set_title('MONTH vs GRP Scatter Plot')
    axes[0, 1].set_xlabel('Month')
    axes[0, 1].set_ylabel('Group')

# Bar plot for CMP vs VALUE in Hackathon_Ideal_Data
if 'CMP' in ideal_data.columns and 'VALUE' in ideal_data.columns:
    axes[1, 0].bar(ideal_data['CMP'], ideal_data['VALUE'], color='salmon', edgecolor='black')
    axes[1, 0].set_title('CMP vs VALUE Bar Plot')
    axes[1, 0].set_xlabel('Category (CMP)')
    axes[1, 0].set_ylabel('Value')

# Line plot for a hypothetical trend in Hackathon_Working_Data
if 'DATE' in working_data.columns and 'SALES' in working_data.columns:
    working_data['DATE'] = pd.to_datetime(working_data['DATE'])
    axes[1, 1].plot(working_data['DATE'], working_data['SALES'], color='purple')
    axes[1, 1].set_title('Sales Over Time')
    axes[1, 1].set_xlabel('Date')
    axes[1, 1].set_ylabel('Sales')

plt.tight_layout()
plt.show()