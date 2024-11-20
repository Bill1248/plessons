def inputInt(message):
    value = input(message)
    try:
        return int(value)
    except:
        return None

def inputFloat(message):
    value = input(message)
    try:
        return float(value)
    except:
        return None

def inputBoolean(message):
    bool_dict = {
        "true": True, 
        "false": False, 
        "yes": True, 
        "no": False,
        "1": True,
        "0": False
    }
    value = input(message).lower()
    try:
        return bool_dict[value]
    except:
        return None

# Get int values
n = inputInt("Enter the first integer: ")
m = inputInt("Enter the second integer: ")

if type(n) is int and type(m) is int: 
    print( n + m )
else:
    print("Inputed illegal int value")

# Get float values
n_float = inputFloat("Enter the first float: ")
m_float = inputFloat("Enter the second float: ")

if type(n_float) is float and type(m_float) is float: 
    print( n_float + m_float )
else:
    print("Inputed illegal float value")

a = inputBoolean("Enter the first boolean: ")
b = inputBoolean("Enter the second boolean: ")

print( a, b )