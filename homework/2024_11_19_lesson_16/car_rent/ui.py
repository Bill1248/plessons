from os import system

def printClientCarMenu() :
    print("#"*50)
    print("# 1. Show cars list")
    print("# 2. Rent a car")
    print("# 3. Return a car")
    print("# 0. Exit")
    print("#"*50)

    option = int (input(">>> "))
    return option

def printAdminCarMenu() :
    print("#"*50)
    print("# 1. Show cars list")
    print("# 2. Add a car")
    print("# 3. Update rent rate")
    print("# 4. Delete a car")
    print("# 5. Show client menu")
    print("# O. Exit")
    print("#"*50)

    option = int (input (">>> "))
    return option

def wait():
    input ("Hit enter to continue")

def clear():
    system( "clear")

def loginAdministrator():
    login = input( "admin login: " )
    passw = input ("admin password: " )
    if login == "admin" and passw == "123":
        return True
    else:
        print("Login or paasword is not valid")
        wait()
        return False

def inputCarSid():
    try:
        sid = int(input("Enter car SID:"))
        return sid
    except:
        return "Error"
    
def inputNewCar():
    print("#"*18, " Add a car ", "#"*19)
    try:
        sid = int(input("Enter car SID:"))
        brand = input("Enter car BRAND:")
        model = input("Enter car MODEL:")
        year = input("Enter car year of issue:")
        rent_rate = int(input("Enter rent rate:"))
        return [sid, brand, model, year, rent_rate]
    except:
        return None

def inputNewRate():
    print("#"*15, " New rent rate ", "#"*17)
    try:
        sid = int(input("Enter car SID:"))
        rent_rate = int(input("Enter rent rate:"))
        return [sid, rent_rate]
    except:
        return ["Error", "Error"]
    
def inputDeleteCar():
    print("#"*17, " Delete a car ", "#"*17)
    try:
        sid = int(input("Enter car SID:"))
        return sid
    except:
        return "Error"


def inputRentValues():
    try:
        sid =  int(input("Enter car SID:"))
        period = int(input("Specify the period (days):"))
        return [sid, period]
    except:
        return ["Error", "Error"]

def outputMessage(code):
    if code == 1:
        print("Successfully!!!")
    elif code == -1:
        print("Input error!!!")
    elif code == -2:
        print("Car not found.")
    else:
        print("Unknown error.")
    wait()