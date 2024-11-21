from os import system
def menu():
    system("clear")
    print("MENU")
    print("###############")
    print("1. save name")
    print("2. load name")
    print("0. exit")

    option = int(input(">>>"))
    return option

def save():
    file = open("name.txt", 'w')
    name = input("Enter your name:")
    file.write(name)
    file.close()
    input()

def load():
    file = open("name.txt", 'r')
    name = file.read()
    print("Reading name:", name)
    file.close()
    input()

def exit():
    quit()

actions = [
    exit,
    save,
    load
]
#############################
while True:
    option = menu()
    if option >= 0 and option < len(actions):
        actions[option]()
    else:
        print("Wrong option!!!")
        input()
    