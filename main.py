# OpenWeatherMap One Call API endpoint
import os
import requests
from dotenv import load_dotenv

# 1. Setup your credentials and parameters
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Marathon, FL"

lat = "24.73"  # Latitude for Tokyo
lon = "-81.04"  # Longitude for Tokyo
URL = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}'



def get_weather():
    try:
        # 2. Make the API call
        response = requests.get(URL)
        
        # 3. Check if the request was successful (Status Code 200)
        response.raise_for_status()
        
        # 4. Convert the raw data into a Python Dictionary (JSON)
        data = response.json()
        
        # 5. Get Temperature and convert from Kelvin to Fahrenheit
        current_temp = data['current']['temp']
        current_feels_like = data['current']['feels_like']
        current_f_feels_like = round((current_feels_like - 273.15) * 9/5 + 32)   # Convert Kelvin to Fahrenheit
        current_f_temp = round((current_temp - 273.15) * 9/5 + 32)   # Convert Kelvin to Fahrenheit
        wind_speed = data['current']['wind_speed']
        mph_wind_speed = round(wind_speed * 2.237)  # Convert m/s to mph
        wind_deg = data['current']['wind_deg']
        
        print(f"Wind Speed: {mph_wind_speed} mph")
        print(f"Wind Direction: {wind_deg}°")

        

        print(f"Current temperature in {CITY} is {current_f_temp}F")
        print(f"Current feels like temperature in {CITY} is {current_f_feels_like}F")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    get_weather()
    

