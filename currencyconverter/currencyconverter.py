# corrency converter project 
import requests
import json

#ask input
from_currency=input("enter from currency :").upper()
to_crrency=input("enter to_currency :").upper()
amount=float(input("enter the amount :"))

#api setup
my_api="e44e97183a2ca67887386b99"
url=f"https://v6.exchangerate-api.com/v6/{my_api}/latest/{from_currency}"

#conver data
response=requests.get(url)
data=response.json()

rate=data["conversion_rates"][to_crrency]

#convert
convert=amount*rate

print("from currency=",from_currency)
print("to currency=",to_crrency)

print(f"your {to_crrency} is {convert}")

