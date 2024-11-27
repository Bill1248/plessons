import json

def createCar(sid, brand, model, year, rent_rate):
    car = {}
    car["sid"]   = sid
    car["brand"] = brand
    car["model"] = model
    car["year"]  = year
    car["rented"]  = False
    car["period"]  = 0
    car["rent_rate"]  = rent_rate
    return car

def findCarBySid(cars, sid):
    car = None
    for c in cars:
        if c["sid"] == sid:
            car = c
            break
    return car

def updateRent(cars, sid, rent_rate):
    result = -2
    for i in range(len(cars)):
        if cars[i]["sid"] == sid:
            cars[i]['rent_rate'] = rent_rate
            result = 1
            break
    return result

def deleteCar(cars, sid):
    result = -2
    for i in range(len(cars)):
        if cars[i]["sid"] == sid:
            cars.pop(i)
            result = 1
            break
    return result

def rentCar(cars, sid, period):
    result = -2
    for i in range(len(cars)):
        if cars[i]["sid"] == sid:
            cars[i]['rented'] = True
            cars[i]['period'] = period
            result = 1
            break
    return result

def returnFromRent(cars, sid):
    result = -2
    for i in range(len(cars)):
        if cars[i]["sid"] == sid:
            cars[i]['rented'] = False
            cars[i]['period'] = 0
            result = 1
            break
    return result

def printCarInfo (car, is_admin):
    print("#"*50)
    if is_admin:
        print(f"# {car['sid']} {car['brand']} / {car['model']} ({car['year']}), Rent rate : {car['rent_rate']} ")
        if car["rented"]:
            sum = car['period'] * car['rent_rate']
            print(f"Rented on period {car['period']} , for the amount {sum}")
        
    else:    
        print(f"# {car['sid']} {car['brand']} / {car['model']} ({car['year']}), Rent rate : {car['rent_rate']} ")
    print("#"*50)
        
def printCarListInfo(cars, is_admin):
    for c in cars:
        if not is_admin:
            if c["rented"]:
                continue
        printCarInfo(c, is_admin)



######################## JSON #####################

def saveCarData (cars) :
    file = open("data/cars.json", "w")
    file.write(json.dumps(cars))
    file.close()

def loadCarData():
    try:
        with open('data/cars.json', 'r') as f:
            return json.load(f)
    except:
        return None
