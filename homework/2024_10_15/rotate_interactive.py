from os import system
from time import sleep

pos = 0
direction = 1 # right for default

def draw(position: int):
    system("clear")
    row_top    = "   "
    row_center = " * "
    row_bottom = "   "
    match position:
        case 0:
            row_top = " | "
        case 1:
            row_top = "  /"
        case 2:
            row_center = " *-"
        case 3:
            row_bottom = "  \\"
        case 4:
            row_bottom = " | "
        case 5:
            row_bottom = "/  "
        case 6:
            row_center = "-* "
        case 7:
            row_top = "\  "
        case _:
            row_top = "   "

    print("*******")
    print(f"* {row_top} *")
    print(f"* {row_center} *")
    print(f"* {row_bottom} *")
    print("*******")

draw(10)
dir = input("\nenter direction < >\n")
if dir == "<": 
    direction = -1
    
while True:
    draw(position=pos)
    sleep(1.0)
    pos += direction
    if pos == 8:
        pos = 0 
    if pos <  0:
        pos = 7 