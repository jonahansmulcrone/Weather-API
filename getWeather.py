import csv
import os
import sys
from bs4 import BeautifulSoup
import requests
import datetime as dt
from datetime import datetime



"""
This is Home work 2, you are allowed to work in pairs, you can only use chatGPT or other AI model on the course discord public channel.

# Student Name 1: Jonah Mulcrone
# Student Name 2: Brian Sung

# Additional comment for this program, any bugs or creative functions?

"""

# put your code here

if len(sys.argv) < 3:
    print("This script is going to collect weather data and store in a csv file:")
    print("python "+sys.argv[0] + " \"city-name\" airquality.csv")

CITY = sys.argv[1]
file_path = sys.argv[2]

CURRENT_BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "5d608d9616a39ff9e56db80e093fa8b1"

current_url = CURRENT_BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=imperial"

current_response = requests.get(current_url).json()
print("Response:", current_response)

current_temp = round(current_response['main']['temp'], 1)
current_desc = current_response['weather'][0]['description']
current_humidity = current_response['main']['humidity']
current_wind_speed = current_response['wind']['speed']
current_wind_deg = current_response['wind']['deg']
current_visibility = current_response['visibility']
current_date = datetime.now()

formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

print(f"The current temperature in Seattle on {formatted_date} is {current_temp}F with {current_desc}. The humidity is {current_humidity}%")

FORECAST_BASE_URL = f"https://api.openweathermap.org/data/2.5/forecast?"
forecast_url = FORECAST_BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=imperial"

forecast_response = requests.get(forecast_url).json()
print("Forecast Response:", forecast_response)

forecast_temp = round(forecast_response['list'][0]['main']['temp'], 1)
forecast_desc = forecast_response['list'][0]['weather'][0]['description']
forecast_humidity = forecast_response['list'][0]['main']['humidity']
forecast_wind_speed = forecast_response['list'][0]['wind']['speed']
forecast_wind_deg = forecast_response['list'][0]['wind']['deg']
forecast_visibility = forecast_response['list'][0]['visibility']
forecast_date = forecast_response['list'][0]['dt_txt']

print(f"The temperature forecast for {forecast_date} is {forecast_temp}F with {forecast_desc}. The humidity will be {forecast_humidity}%.")

current_weather = {
    "City": CITY,
    "Time": current_date,
    "Description": str(current_desc),
    "Temperature" : int(current_temp),
    "Humidity": int(current_humidity),
    "Wind Speed": int(current_wind_speed),
    "Wind Deg": int(current_wind_deg),
    "Visibility": int(current_visibility)
}

forecast_weather = {
    "City": CITY,
    "Time": forecast_date,
    "Description": str(forecast_desc),
    "Temperature": int(forecast_temp),
    "Humidity": int(forecast_humidity),
    "Wind Speed": int(forecast_wind_speed),
    "Wind Deg": int(forecast_wind_deg),
    "Visibility": int(forecast_visibility)
}

with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Weather Element', 'Current', 'Forecast', '% Change'])
    for element in current_weather.keys():
        if (type(current_weather[element]) == int):
            writer.writerow([element, round(current_weather[element], 1), round(forecast_weather[element], 1), round((forecast_weather[element] - current_weather[element]) / current_weather[element] * 100, 5)])
        else:
            writer.writerow([element, current_weather[element], forecast_weather[element], "N/A"])
