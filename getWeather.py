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
# Student Name 3: Emmanuel Obikwelu

# Additional comment for this program, any bugs or creative functions?

"""

# put your code here

if len(sys.argv) < 2:
    print("This script is going to collect weather data and store in a csv file:")
    print("python "+sys.argv[0] + " \"city-name\" airquality.csv")

file_path = sys.argv[1]

CURRENT_BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "5d608d9616a39ff9e56db80e093fa8b1"

cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte",
    "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington",
    "Boston", "El Paso", "Nashville", "Detroit", "Oklahoma City",
    "Portland", "Las Vegas", "Memphis", "Louisville", "Baltimore",
    "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Mesa",
    "Sacramento", "Atlanta", "Kansas City", "Colorado Springs", "Miami",
    "Raleigh", "Omaha", "Long Beach", "Virginia Beach", "Oakland",
    "Minneapolis", "Tampa", "Tulsa", "Arlington"
]

for i in range(len(cities)):

    current_url = CURRENT_BASE_URL + "q=" + cities[i] + "&appid=" + API_KEY + "&units=imperial"
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

    print(f"The current temperature in {cities[i]} on {formatted_date} is {current_temp}F with {current_desc}. The humidity is {current_humidity}%")

    current_weather = {
        "City": cities[i],
        "Time": current_date,
        "Temperature" : int(current_temp),
        "Humidity": int(current_humidity),
        "Wind Speed": int(current_wind_speed),
        "Wind Deg": int(current_wind_deg),
        "Visibility": int(current_visibility)
    }


    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        if i < 1:
            writer.writerow(['City', 'Time', 'Temperature', 'Humidity', 'Wind Speed', 'Wing Deg', 'Visibility'])
        else:
            writer.writerow([current_weather["City"], current_weather["Time"], current_weather["Temperature"], current_weather["Humidity"], current_weather["Wind Speed"], current_weather['Wind Deg'], current_weather["Visibility"]])




