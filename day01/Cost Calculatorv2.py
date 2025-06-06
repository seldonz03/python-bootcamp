total = 0
count = 0
item_count = int(input("Enter number of items:"))

for item in range(item_count):
    item_price = int(input("Enter item price:"))
    number_pax = int(input("Enter number of pax:"))
    count += number_pax
    total += item_price
    result = count * total
print("Total Cost:",result)





