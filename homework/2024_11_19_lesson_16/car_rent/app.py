
from car import *
from ui import *


is_admin = False
cars = [
    createCar(101, "BMW", "series 3", 2000, 50),
    createCar(102, "BMW", "series 5", 2010, 75),
    createCar(103, "BMW", "series 7", 2020, 100)
]

while True:
    clear()
    if is_admin:
        option = printAdminCarMenu()
        if option == 1: 
            printCarListInfo(cars, is_admin)
            wait()
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
            rentCar(cars, 101, 10)
        if option == 3: 
            returnFromRent(cars, 101)
        if option == 9: 
            is_admin = loginAdministrator()
        if option == 0:
            break
                 
