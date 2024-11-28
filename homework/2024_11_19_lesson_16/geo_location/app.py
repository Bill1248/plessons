import requests

name = input ("enter domain name or ip address: ") # mail.ru'
address = f"http://ip-api.com/json/{name}"

responce = requests.get(address)

if responce.status_code == 200:
    data = responce.json()
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
    print(f"Error request (code: {responce.status_code})")
