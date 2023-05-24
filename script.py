# write a python script which takes city name from terminal in interactive format and prints the weather forecast using http://<domain>/weather?city=<city_name> api

import requests
from pprint import pprint
from colorama import Fore
from tabulate import tabulate
import numpy as np

# helper function to get api key from api_key.txt file
def get_api_key():
    with open("api_key.txt", "r") as f:
        api_key = f.read()
    return api_key

# helper function to get weather data from openweathermap api
def get_weather_data(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

# helper function to print the weather data
def print_weather_data(weather_info, city_name):
    #error handling
    if 'message' in weather_info:
        print(Fore.RED)
        pprint(weather_info['message'])
        return

    #parse the data 
    weather_data_parsed = []
    if ('name' in weather_info):
        weather_data_parsed.append(["City Name", weather_info['name']])
    if ('sys' in weather_info) and ('country' in weather_info['sys']):
        weather_data_parsed.append(["Country", weather_info['sys']['country']])
    if ('weather' in weather_info) and (len(weather_info['weather']) > 0) and ('main' in weather_info['weather'][0]):
        weather_data_parsed.append(["main", weather_info['weather'][0]['main']])
    if ('weather' in weather_info) and (len(weather_info['weather']) > 0) and ('description' in weather_info['weather'][0]):
        weather_data_parsed.append(["description", weather_info['weather'][0]['description']])
    if ('main' in weather_info) and ('temp_min' in weather_info['main']):
        weather_data_parsed.append(["temp_min", str(weather_info['main']['temp_min']) + " \u00b0C"])
    if ('main' in weather_info) and ('temp_max' in weather_info['main']):
        weather_data_parsed.append(["temp_max", str(weather_info['main']['temp_max']) + " \u00b0C"])
    if ('main' in weather_info) and ('temp' in weather_info['main']):
        weather_data_parsed.append(["Temp", str(weather_info['main']['temp']) + " \u00b0C"])
    if ('main' in weather_info) and ('humidity' in weather_info['main']):
        weather_data_parsed.append(["humidity", weather_info['main']['humidity']])
    if ('coord' in weather_info):
        weather_data_parsed.append(["Coordinates", weather_info['coord']])
    if ('wind' in weather_info):
        weather_data_parsed.append(["Wind", weather_info['wind']])
    
    print(Fore.YELLOW)
    print (tabulate(weather_data_parsed, tablefmt="grid"))


# take city name as input from user and print the weather forecast
def process_forecast_for_particular_city(api_key):
    print(Fore.GREEN + "Enter the city name: ")
    city_name = input(Fore.WHITE).lower()
    weather_info = get_weather_data(city_name, api_key)
    print_weather_data(weather_info, city_name)


if __name__ == "__main__":
    print(Fore.BLUE + "Welcome to the weather forecast program")

    api_key = get_api_key()
    process_forecast_for_particular_city(api_key)

    while True:
        print("\n")
        ans = input(Fore.GREEN + "Do u want to continue? (y/n): ")
        if (ans.lower() == 'y'):
            process_forecast_for_particular_city(api_key)
        else:
            pprint(Fore.GREEN + "Exiting the program")
            break
#Take interactive input from user
# Enter the city name: 
# New York 
# Do u want to continue? (y/n): 
# y
# Enter the city name:
# London 
# Do u want to continue? (y/n):
# n 
# Exiting the program
# Tell me how to achieve above 
# Hint: use while loop and break statement

#How to add an empty line in python
#Hint: use print function
# print("\n\n\n")
# Not work

#How to add color to the text in python
#Hint: use colorama module
# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)

# Tell me some colors which work in both dark and light terminal
# Hint: use colorama module
# Fore.BLACK
# Fore.RED
# Fore.GREEN
# Fore.YELLOW
# Fore.BLUE

# Use Fore.YELLOW color for printing the weather info
# pprint (f'Fore.YELLOW + {weather_info}')
# Not working 

# How to print the weather info in a pretty format using Fore.Yellow color
# Hint: use pprint module
# pprint (f'Fore.YELLOW + {weather_info}')
# Not working

#print degree celcius symbol
# weather_info['main']['temp_min'] = str(weather_info['main']['temp_min']) + " \u00b0C"
    
#showing image with scattered clouds in terminal
# print(Fore.YELLOW)

# get the image from file using weather_icon id
# print the image in terminal
# Hint: use PIL module
# from PIL import Image
# im = Image.open("bride.jpg")
# im.show()
# im.save("bride.png")
# im = Image.open("bride.png")
# im.show()

#Show image from file in terminal with string
# print(Fore.YELLOW)
# im = Image.open("bride.jpg")
# im.show()
# print("This is the image of bride")
# im = Image.open("bride.png")