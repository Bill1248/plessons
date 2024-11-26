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
    print("# 3. Edit a car")
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
