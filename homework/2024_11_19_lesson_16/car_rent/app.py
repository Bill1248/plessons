
from car import *
from ui import *
from validate import *

is_admin = False
cars = [
    createCar(101, "BMW", "series 3", 2000, 50),
    createCar(102, "BMW", "series 5", 2010, 75),
    createCar(103, "BMW", "series 7", 2020, 100)
]

jsonData =  loadCarData()
if jsonData:
    cars = jsonData
else:
    saveCarData(cars)

while True:
    clear()
    if is_admin:
        option = printAdminCarMenu()
        if option == 1: 
            printCarListInfo(cars, is_admin)
            wait()

        if option == 2:
            car = inputNewCar()
            if car:
                new_car = createCar(
                    sid = car[0],
                    brand = car[1],
                    model = car[2],
                    year = car[3],
                    rent_rate = car[4]
                )
                cars.append(new_car)
                saveCarData(cars)
                outputMessage(1)
            else:
                outputMessage(-1)

        if option == 3:
            sid, new_rate = inputNewRate()
            if validate_int_type(sid) and validate_int_type(new_rate):
                outputMessage(updateRent(cars, sid, new_rate))
                saveCarData(cars)
            else:
                outputMessage(-1)

        if option == 4:
            sid = inputDeleteCar()
            if validate_int_type(sid):
                outputMessage(deleteCar(cars, sid))
                saveCarData(cars)
            else:
                outputMessage(-1)
        if option == 5:
            is_admin = False
        if option == 0:
            break
    else:
        option = printClientCarMenu()
        if option == 1: 
            printCarListInfo(cars, is_admin)
            wait()
        if option == 2: 
            sid, period = inputRentValues()
            if validate_int_type(sid) and validate_int_type(period):
                outputMessage(rentCar(cars, sid, period))
                saveCarData(cars)
            else:
                outputMessage(-1)
        if option == 3: 
            sid = inputCarSid()
            if validate_int_type(sid):
                outputMessage(returnFromRent(cars, sid))
                saveCarData(cars)
            else:
                outputMessage(-1)
        if option == 9: 
            is_admin = loginAdministrator()
        if option == 0:
            break
                 
