
products = [
    { "name" : "Salad", "price" : 25.00 },
    { "name" : "Soup",  "price" : 15.00},
    { "name" : "Bread", "price" : 5.00},
    { "name" : "Kebab", "price" : 50.00},
    { "name" : "Pizza", "price" : 100.00},
    
]

# Find max
max_i = 0
for i in range(len(products)) :
    if products[i]["price"] > products[max_i]["price"]:
        max_i = i

print(f'{max_i} > {products[max_i]["name"]:15} {products[max_i]["price"]:7.2f} MDL')

# Find by name
search_str = input("Enter full name for search : ")
finding_i = None
for i in range(len(products)) :
    if products[i]["name"].upper() == search_str.upper():
        finding_i = i
        break

if finding_i == None :
    print("Not found")
else:
    print(f'Result : {finding_i} > {products[finding_i]["name"]:15} {products[finding_i]["price"]:7.2f} MDL')


# Find by substring
text = input("Enter text for search : ").upper()
finding = []
for i in range(len(products)) :
    if text in products[i]["name"].upper() :
        finding.append(products[i])

if len(finding) == 0 :
    print("Not found")
else:
    print("Result : ")
    for i in range(len(finding)) :
        print(f'{i} > {finding[i]["name"]:15} {finding[i]["price"]:7.2f} MDL')

