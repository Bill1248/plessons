from os import system
from random import randint


gm = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

ry = randint(0, 9)
rx = randint(0, 9)
gm[ry][rx] = 1

while True:
    system("clear")
    print("*"*19)

    for y in range(0, 10):
        for x in range(0, 10):
            if gm[y][x] == 1:
                print("R", end = " ")
            elif gm[y][x] == 2:
                print("X", end = " ")
            else:
                print(".", end = " ")
        print()
    print("*"*19)
    option = input(">>>")
    gm[ry][rx] = 0
    if option == "d" and rx < 9:
        rx += 1
    if option == "a" and rx > 0:
        rx -= 1
    if option == "s" and ry < 9:
        ry += 1
    if option == "w" and ry > 0:
        ry -= 1
    if gm[ry][rx] == 2:
        system("clear")
        input("Bomb!!! Press enter for continue.")
    gm[ry][rx] = 1

    