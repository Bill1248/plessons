# lesson of 26.09.2024
# task 1

client_name = "Bill"

line1_food_name = "Peas"
line1_food_price = 10
line1_food_quantity = 3
line1_cost = line1_food_price * line1_food_quantity

line2_food_name = "Сhicken"
line2_food_price = 15
line2_food_quantity = 2
line2_cost = line2_food_price * line2_food_quantity

line3_food_name = "Beer"
line3_food_price = 20
line3_food_quantity = 1
line3_cost = line3_food_price * line3_food_quantity

total = line1_cost + line2_cost + line3_cost
print("Ordered by : ", client_name, "\n")
print("1.", line1_food_name, "x", line1_food_quantity, "position = ", line1_cost)
print("2.", line2_food_name, "x", line2_food_quantity, "position = ", line2_cost)
print("3.", line3_food_name, "x", line3_food_quantity, "position = ", line3_cost)
print("\nTotal : ", total)