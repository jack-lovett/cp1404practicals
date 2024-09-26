"""
Program to calculate total price and discount for a number of items
If total price > 100 then 10% discount
"""

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
total_price = 0
for i in range(number_of_items):
    total_price += float(input("Price of item: "))
if total_price > 100:
    total_price *= 0.9 # 10% discount
print(f"Total price for {number_of_items} items: ${total_price:.2f}")
