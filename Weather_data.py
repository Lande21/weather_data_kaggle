#Author:Rolande Umuhoza
#Github : Lande21
#Date : September 25, 2024

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (replace 'weather_data.csv' with your file path)
df = pd.read_csv('weather.csv')
# Use index as proxy for time
df.reset_index(inplace=True)

# Plot MinTemp and MaxTemp
plt.figure(figsize=(10,6))
plt.plot(df.index, df['MinTemp'], label='Min Temperature', color='blue')
plt.plot(df.index, df['MaxTemp'], label='Max Temperature', color='red')
plt.xlabel('Index (proxy for time)')
plt.ylabel('Temperature (°C)')
plt.title('Min and Max Temperatures Over Index')
plt.legend()
plt.show()


#2
plt.figure(figsize=(10,6))
plt.plot(df.index, df['Rainfall'], label='Rainfall (mm)', color='green')
plt.plot(df.index, df['Evaporation'], label='Evaporation (mm)', color='orange')
plt.xlabel('Index (proxy for time)')
plt.ylabel('Millimeters (mm)')
plt.title('Rainfall vs Evaporation Over Index')
plt.legend()
plt.show()

#3
plt.figure(figsize=(10,6))
plt.plot(df.index, df['Humidity9am'], label='Humidity at 9am (%)', color='cyan')
plt.plot(df.index, df['Humidity3pm'], label='Humidity at 3pm (%)', color='purple')
plt.xlabel('Index (proxy for time)')
plt.ylabel('Humidity (%)')
plt.title('Humidity at 9am vs 3pm Over Index')
plt.legend()
plt.show()
