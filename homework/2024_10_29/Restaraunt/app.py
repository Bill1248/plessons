from func import printMenu
from os import system

while True:
    system("clear")
    data = printMenu()
    pos = int(input("choose -> ")) - 1

    if pos >= len(data) or pos < 0:
        print("Wrong position, choose 1 ...", len(data), "Press enter for continue")
        input()
        continue
    while True:
        print("How many",data[pos][0], "do you whant?")
        q = int(input())
        if q <= 0 or q > int(data[pos][2]):
            print("Wrong quantity.", "Is ready", data[pos][2], "now." )
        else:
            print("cost", q * int(data[pos][1]))
            input()
            break

    
