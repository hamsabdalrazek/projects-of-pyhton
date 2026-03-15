import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
df = pd.DataFrame({
    'time':data['daily']['time'],
    'temperature_2m_max':data['daily']['temperature_2m_max'],
    'temperature_2m_min':data['daily']['temperature_2m_min']
})
df['time'] = pd.to_datetime(df['time'])
df['average'] = (df['temperature_2m_max'] + df['temperature_2m_min']) / 2
plt.figure(figsize=(10,6))
plt.plot(df['time'],df['temperature_2m_max'],marker ='o',label='temperature_2m_max', color = 'blue')
plt.plot(df['time'],df['temperature_2m_min'],marker ='o',label='temperature_2m_min', color = 'purple')
plt.plot(df['time'],df['average'],marker ='o',label='average', color = 'green')
plt.tight_layout()
print(f"Average is {df['average'].mean():.1f}")
plt.title("Paris Temperature Last 7 Days")
plt.xlabel('time')
plt.ylabel('Temperature')
plt.legend()
plt.show()
plt.bar(df['time'],df['temperature_2m_max'],color = 'skyblue', label ='Max-TEM')
plt.xticks(rotation=45)
plt.legend()
plt.title('Max-Temperature')
plt.show()
plt.bar(df['time'],df['temperature_2m_min'],color = 'red',label ='Min-TEM')
plt.xticks(rotation=45)
plt.legend()
plt.title('Min-Temperature')
plt.show()
