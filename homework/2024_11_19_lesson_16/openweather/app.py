import http.client
import json
from ui import *

# weather
key = "2c6552d9aec7e8bdd612e500d4c4d219"
domain = "api.openweathermap.org"
connection = http.client.HTTPConnection(domain)
while True:
    clear()
    place = input("Enter city or place, 0 for exit:")
    try: 
        if int(place) == 0:
            break
    except:
        pass
    
    endpoint_current = f"/data/2.5/weather?q={place}&appid={key}&units=metric&lang=en"
    connection. request("GET", endpoint_current )
    response = connection. getresponse ()
    if response.status == 200:
        data = json.loads(response.read().decode("utf-8"))
    
        if data['cod'] == 200:
            #print(data)
            weather = dict()
            try: weather["name"] = data["name"] 
            except: weather["name"] = "None"
            try: weather["country"] = data["sys"]["country"] 
            except: weather["country"] = "None"
            try: weather["dt"] = data["dt"] 
            except: weather["dt"] = 0
            try: weather["main"] = data["weather"][0]["main"] 
            except: weather["main"] = "None"
            try: weather["temp"] = str(int(data["main"]["temp"] + 0.5)) + "°C"
            except: weather["temp"] = "None"
            try: weather["temp_min"] = str(int(data["main"]["temp_min"] + 0.5)) + "°C"
            except: weather["temp_min"] = "None"
            try: weather["temp_max"] = str(int(data["main"]["temp_max"] + 0.5)) + "°C"
            except: weather["temp_max"] = "None"
            try: weather["pressure"] = str(data["main"]["pressure"]) + " Pa"
            except: weather["pressure"] = "None"
            try: weather["wind"] = str(data["wind"]["speed"]) + " km/h"
            except: weather["wind"] = "None"

            printData(weather)
        else:
            print("Place not found.")
    else:
        print(f"Error request (code: {response.status})")
    wait()

connection.close