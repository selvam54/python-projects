import requests
import json

city=input("enter the city :").lower()
API_key="e291de205b3ba738d8c6ef9886abbac0"

url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"

json_data=requests.get(url)

print(json.dumps(json_data.json(),indent=4))