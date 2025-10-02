import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("\n weather condition \n")
    city = input("\nenter the city weather\n")
    
    requests_url=f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    print(requests_url)
    weather_data = requests.get(requests_url).json()
    print(f"{weather_data["name"]} temp is {weather_data["main"]}")
    
    

get_current_weather()