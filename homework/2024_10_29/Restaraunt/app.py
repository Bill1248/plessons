from func import printMenu, printOrder
from os import system

file = open('data/order.csv', "w")
while True:
    system("clear")
    data = printMenu()
    pos = int(input("choose -> ")) - 1
    if pos < 0 :
        file.close()
        break

    if pos >= len(data):
        print("Wrong position, choose 1 ...", len(data), ", press \"Enter\" for continue.")
        input()
        continue
    while True:
        q = int(input("How many " + data[pos][0] +" do you whant? "))
        if q <= 0: 
            break
        if q > int(data[pos][2]):
            print("Wrong quantity.", "Is ready", data[pos][2], "now." )
        else:
            cost = q * int(data[pos][1])
            order_line = f"{data[pos][0]:10} quantity:{q:3} cost:{cost:5}\n"
            print("\n", order_line)
            file.write(f"{data[pos][0]},{q},{cost}\n")
            input("Press \"Enter\" for  continue")
            break

printOrder()
    
