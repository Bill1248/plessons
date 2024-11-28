import http.client
import json

name = input ("enter domain name or ip address: ") 

conn = http.client.HTTPConnection("ip-api.com")
conn.request("GET", f"/json/{name}")
res = conn.getresponse()
if res.code == 200:
    response_data = res.read().decode("utf-8")
    data = json.loads(response_data)
    #print(data)
    if data['status'] == "success":
        print("*"*30)
        try: country = data["country"] 
        except: country = "None"
        try: regionName = data["regionName"] 
        except: regionName = "None"
        try: city = data["city"] 
        except: city = "None"
        try: org = data["org"] 
        except: org = "None"
        try: lat = data["lat"] 
        except: lat = "None"
        try: lon = data["lon"] 
        except: lon = "None"

        print(f"{'Country':15} : {country}")
        print(f"{'Region':15} : {regionName}")
        print(f"{'City':15} : {city}")
        print(f"{'Organization':15} : {org}")
        print(f"{'Latitude':15} : {lat}")
        print(f"{'Longitude':15} : {lon}")
        print("*"*30)
    else:
        print("Address not found.")
else:
    print(f"Error request (code: {res.code})")
