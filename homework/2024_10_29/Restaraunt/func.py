def printMenu():
    file = open('homework/2024_10_29/Restaraunt/data/food.csv', "r")
    content = file.read()

    print("================== MENU =================")
    lines = content.split("\n")
    pos = 0
    data = []
    for line in lines:
        pos += 1
        food_name, food_price, food_avail = line.split(",")
        data.append([food_name, food_price, food_avail])
        print(f"{pos:2}) {food_name:>20} {food_price:10}")

    return data