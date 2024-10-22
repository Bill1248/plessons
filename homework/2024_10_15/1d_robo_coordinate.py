from random import randint
from os import system

error_lenght = True
error_roboX = True
lenght = 80
roboX = 1
health = 102

while error_lenght:
    lenght = int(input("Enter lenght (not negative, max 80):"))
    if lenght <= 0 or lenght > 80:
        print("wrong lenght")
    else:
        error_lenght = False
while error_roboX:
    roboX = int(input("Enter robot position :"))
    if roboX < 0 or roboX > lenght:
         print("wrong robot position")
    else:
        error_roboX = False


bomb1X = randint(1, lenght)
bomb2X = randint(1, lenght)

aid_kit1X = randint(1, lenght)
aid_kit2X = randint(1, lenght)

while True:
    system("clear")
    if health == 0:
        break
    # #################### DRAWING THE MAP ###############
    #x = 1
    print("\n")
    #while x<= lenght:
    for x in range(1, lenght + 1):
        symbol = "-"
        if bomb1X == x:
            symbol = "B"
        if bomb2X == x:
            symbol = "B"
        if aid_kit1X == x:
            symbol = "A"
        if aid_kit2X == x:
            symbol = "A"
        if roboX == x:
            symbol = "R"
        print(symbol, end = "")
        #x += 1 

    print("\n")
    # ####################################################
    health -= 2
    if roboX == bomb1X:
        bomb1X = -1
        health -= 20
        print("BOOOOOOOM!!!")
    if roboX == bomb2X:
        bomb2X = -1
        health -= 20
        print("BOOOOOOOM!!!")
    if roboX == aid_kit1X:
        aid_kit1X = -1
        health += 20
        print("The robot is recharged")
    if roboX == aid_kit2X:
        aid_kit2X = -1
        health += 20
        print("The robot is recharged")
    if health < 0:
        health = 0
    print("Health :", f"{health}%")
    print("\n")
    # ################### CONTROLS #######################
    direction = input("Enter direction (a/d/x) > ")
    if direction == "a":
        roboX -= 1
        if roboX <= 0: 
            roboX = lenght
    if direction == "d":
        roboX += 1
        if roboX > lenght:
            roboX = 1
    if direction == "x":
        break
# end main loop

system("clear")
print("\n")
if health == 0:
    print("****** GAME OVER! The robot is de-energized! ******\n")
else:
    print("Thank your for plaing!!\n")
    
    