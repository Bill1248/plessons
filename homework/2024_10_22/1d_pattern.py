# DRAW PATTERN
# * * * # #


print("\n")
star_counter = 0
lattice_counter = 0
for x in range(1,21):
    if star_counter < 3 :
        print("* ", end = "")
        star_counter += 1
    elif lattice_counter < 2 :
        print("# ", end = "")
        lattice_counter += 1
    else:
        print("* ", end = "")
        star_counter = 1
        lattice_counter = 0     
print("\n")