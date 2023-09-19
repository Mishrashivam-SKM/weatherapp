import requests
import json
import os

city=input("Enter the name of the city\n")

url=f"https://api.weatherapi.com/v1/current.json?key=31d66daeac03404f830203409231809&q={city}"

r=requests.get(url)
print(r.text)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
p=wdic["current"]["condition"]["text"]
date=wdic["location"]["localtime"][:10]
time=wdic["location"]["localtime"][10:14]
region=wdic['location']['region']
os.system(f"say '{city} lies in region of {region}'")
os.system(f"say 'the current weather in {city} is {w}degrees'")
os.system(f"say '{p} in {city}'")
os.system(f"say 'today is {date} and time is {time} hours'")