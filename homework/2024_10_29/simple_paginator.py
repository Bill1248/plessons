from math import ceil

from os import system

products = [
    { "name" : "Salad", "price" : 25.00 },
    { "name" : "Soup",  "price" : 15.00},
    { "name" : "Bread", "price" : 5.00},
    { "name" : "Kebab", "price" : 50.00},
    { "name" : "Pizza", "price" : 100.00},
]

item_count = len(products)
per_page = 2
page_current = 1
pages_total = int(item_count/ per_page + 0.5)
#pages_total = ceil(item_count/ per_page)
system("clear")

while True:
    start_index = (page_current - 1) * per_page
    end_index = start_index + per_page

    print()
    for i in range(len(products)):
        if i >= start_index and i < end_index:
            print(f'{i+1} > {products[i]["name"]:15} {products[i]["price"]:7.2f} MDL')

    print()
    for page in range(1, pages_total + 1):
        if page == page_current:
            print(f"[{page}] ", end = "")
        else:
            print(f"{page} ", end = "")
    print("\n")
    
    direction = input("Enter < or > for navigate, x for 'Exit' :")
    if direction == 'x':
        break
    if direction == "<" and page_current > 1: 
        page_current -= 1
    if direction == ">" and page_current < pages_total: 
        page_current += 1
    system("clear")