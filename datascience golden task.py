import pandas as pd
import matplotlib.pyplot as plt

# Function for distribution graphs
def plot_distribution(df):
    for column in df.select_dtypes(include=['number']).columns:
        df[column].hist(bins=20, edgecolor='black')
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

# Function for scatter and density plots
def plot_scatter_matrix(df):
    pd.plotting.scatter_matrix(df, alpha=0.75, figsize=(10, 10), diagonal='kde')
    plt.suptitle('Scatter Matrix with Density Plots')
    plt.show()

# Read data
df = pd.read_csv("C:\\Users\\HP\\Downloads\\store transaction\\portfolio_data.csv")

# Display basic info
print(f'Data shape: {df.shape}')
print(df.head())

# Visualizations
plot_distribution(df)
plot_scatter_matrix(df)