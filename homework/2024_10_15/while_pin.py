

correct_PIN = 1277
wrong = True
wrong_limit = 3

while wrong:
    user_PIN = int(input("Enter PIN :"))
    if user_PIN == correct_PIN:
        print("Yes!")
        wrong = False
    else: 
        print("Wrong!!!")
        wrong_limit -= 1
        if wrong_limit == 0: 
            print("The limit has been exhausted!!!")
            break