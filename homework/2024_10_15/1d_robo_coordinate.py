
error_lenght = True
error_roboX = True
lenght = 40
roboX = 1
while error_lenght:
    lenght = int(input("Enter lenght (not negative, max 40):"))
    if lenght <= 0 or lenght > 40:
        print("wrong lenght")
    else:
        error_lenght = False
while error_roboX:
    roboX = int(input("Enter robot position :"))
    if roboX < 0 or roboX > lenght:
         print("wrong robot position")
    else:
        error_roboX = False



while True:
    # #################### DRAWING THE MAP ###############
    x = 1
    print("\n")
    while x<= lenght:
        symbol = "-"
        if roboX == x:
            symbol = "R"
        print(symbol, end = "")
        
        x += 1 

    print("\n")
    # ####################################################

    # ################### CONTROLS #######################
    direction = input("Enter direction (a/d) > ")
    if direction == "a":
        roboX -= 1
        if roboX <= 0: 
            roboX = lenght
    if direction == "d":
        roboX += 1
        if roboX > lenght:
            roboX = 1
    
    