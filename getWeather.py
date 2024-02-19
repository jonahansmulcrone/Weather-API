import os
import sys
from bs4 import BeautifulSoup
import requests


"""
This is Home work 2, you are allowed to work in pairs, you can only use chatGPT or other AI model on the course discord public channel.

# Student Name 1: Jonah Mulcrone
# Student Name 2: Brian Sung
# Student Name 3: Emmanuel Obikwelu

# Additional comment for this program, any bugs or creative functions?

"""
api_key = "2a16261696fe4a80952184633241502"

if len(sys.argv)<3:
    print("This script is going to collect weather data and store in a csv file:")
    print("python "+sys.argv[0]+" \"air quality\" airquality.csv")
    sys.exit(0)

keyword = sys.argv[1]
addrOut = sys.argv[2]

# put your code here 

url = "http://api.weatherapi.com/v1"

text = requests.get(url).text