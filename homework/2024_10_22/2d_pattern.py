# 2d draw triangle

leg_lenght = 5

# 1) method
print("\n1) method\n")
y = 1
x_counter = 1
while y <= leg_lenght:
    print("* ", end="")
    x_counter += 1
    if x_counter > y :
        y += 1
        x_counter = 1
        print()
    
print("\n")

# 2) method
print("\n2) method\n")

for y in range(1,leg_lenght + 1):
    print("* " * y)
    
print("\n")

# 3) method
print("\n3) method\n")

for y in range(1,leg_lenght + 1):
    for x in range(1, y + 1):
        print("* ", end = "")
    print()


print("\n")