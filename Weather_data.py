#Author:Rolande Umuhoza
#Github : Lande21
#Date : September 25, 2024

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (replace 'weather_data.csv' with your file path)
df = pd.read_csv('weather.csv')

# Use the index as a proxy for the date
df.reset_index(inplace=True)  # Resets the index to be used for plotting

# Plot MinTemp and MaxTemp
plt.figure(figsize=(10,6))
plt.plot(df.index, df['MinTemp'], label='Min Temperature', color='blue')
plt.plot(df.index, df['MaxTemp'], label='Max Temperature', color='red')

# Labels and Title
plt.xlabel('Index (as proxy for time)')
plt.ylabel('Temperature (°C)')
plt.title('Min and Max Temperatures Over Time')
plt.legend()

# Show plot
plt.show()
