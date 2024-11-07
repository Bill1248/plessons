def printMenu():
    file = open('data/food.csv', "r")
    content = file.read()

    print("================== MENU =================")
    lines = content.split("\n")
    pos = 0
    data = []
    for line in lines:
        pos += 1
        food_name, food_price, food_avail = line.split(",")
        data.append([food_name, food_price, food_avail])
        print(f"{pos:2}) {food_name:<10} {food_price:10}")

    return data

def printOrder():
    file = open('data/order.csv', "r")
    if file.__sizeof__ == 0:
        return
    content = file.read()

    print("\n============== YOUR ORDER ============")
    lines = content.split("\n")
    
    pos = 0
    total = 0
    for line in lines:
        if len(line) == 0:
            break
        pos += 1
        food_name, food_quantity, food_cost = line.split(",")
        total += int(food_cost) 
        order_line = f"{pos:2}) {food_name:10} quantity: {food_quantity:3} cost: {food_cost:5}"
        print(order_line)

    print("--------------------------------------")
    print(f"                           Total:{total:5}\n")
    return