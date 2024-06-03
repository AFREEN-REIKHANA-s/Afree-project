import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
monthly_data = pd.read_csv("C:\\Users\\HP\\Downloads\\monthly_data.csv")

# Group data for the bar plot
monthly_mean_temperatures = monthly_data.groupby('MonthlySeaLevelPressure')['MonthlyDepartureFromNormalAverageTemperature'].mean()

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(16, 12))

# Bar chart
axs[0, 0].bar(monthly_mean_temperatures.index, monthly_mean_temperatures.values, color='orange')
axs[0, 0].set_xlabel('Sea Level Pressure over a Month')
axs[0, 0].set_ylabel('Average Monthly Mean Temperature (°F)')
axs[0, 0].set_title('Average Monthly Mean Temperature by Sea Level Pressure')
axs[0, 0].tick_params(axis='x', rotation=45)
axs[0, 0].grid(axis='y')

# Scatter plot of Monthly Sea Level Pressure vs Monthly Departure From Normal Average Temperature
axs[0, 1].scatter(monthly_data['MonthlySeaLevelPressure'], monthly_data['MonthlyDepartureFromNormalAverageTemperature'], alpha=0.7, color='blue')
axs[0, 1].set_xlabel('Monthly Sea Level Pressure')
axs[0, 1].set_ylabel('Monthly Departure From Normal Average Temperature (°F)')
axs[0, 1].set_title('Monthly Sea Level Pressure vs Monthly Departure From Normal Average Temperature')
axs[0, 1].grid()

# Histogram of Monthly Sea Level Pressure
axs[1, 0].hist(monthly_data['MonthlySeaLevelPressure'], bins=20, color='purple', alpha=0.7)
axs[1, 0].set_xlabel('Monthly Sea Level Pressure')
axs[1, 0].set_ylabel('Frequency')
axs[1, 0].set_title('Histogram of Monthly Sea Level Pressure')
axs[1, 0].grid(axis='y')

# Histogram of Monthly Departure From Normal Average Temperature
axs[1, 1].hist(monthly_data['MonthlyDepartureFromNormalAverageTemperature'], bins=20, color='green', alpha=0.7)
axs[1, 1].set_xlabel('Monthly Departure From Normal Average Temperature (°F)')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].set_title('Histogram of Monthly Departure From Normal Average Temperature')
axs[1, 1].grid(axis='y')

# Adjust layout
plt.tight_layout()
plt.show()