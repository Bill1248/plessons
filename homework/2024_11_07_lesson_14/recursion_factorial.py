def factotial(init = 1, counter = 1, number = 10):
    if counter <= number:
        value = counter * init
        print(f"{counter}! = {value}")
        factotial(value, counter + 1, number)


factotial()
#factotial(number=20)


