def fibonacci(init1 = 0, init2 = 0, counter = 0, stop = 10):
    if counter <= stop:
        if counter == 0:
            value = 0
            print(f"F({counter}) = {value}")
            fibonacci(0,0,1,stop = stop)
        elif counter == 1:
            value = 1
            print(f"F({counter}) = {value}")
            fibonacci(1,0,2,stop = stop)
        else:
            prev = init1
            value = init1 + init2
            print(f"F({counter}) = {value}")
            fibonacci(
                init1 = value,
                init2 = prev,
                counter = counter + 1,
                stop = stop
            )

fibonacci()
#fibonacci(stop = 100)
