
from tax import calculateTax

assignment = input("Input assignment of the amount :")
amount = 0.0
percent = 0.0
try:
    amount = float(input("Input amount :"))
    if amount < 0:
        raise ValueError("The amount must be positive")    
except:
    raise ValueError("Incorrect amount entered")

try:
    percent = float(input("Input percent :"))
    if percent < 0 or percent > 100:
        raise ValueError("The percent must be in range 0...100")    
except:
    raise ValueError("Invalid percentage input")

amount, percent, assignment_amount, tax = calculateTax(amount, percent, assignment)

print (f"{assignment:20} {amount}, percent: {percent}, tax: {tax}")