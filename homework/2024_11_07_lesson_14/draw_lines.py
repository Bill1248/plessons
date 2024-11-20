def drawLine( length, direction ):
    if direction == "h":
        print("-"*length)
    elif direction == "v":
        for i in range(0, length):
            print("|")


drawLine(5, "h")
drawLine(3, "v")