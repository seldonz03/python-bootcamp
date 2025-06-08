import json
with open('purchase.json', 'r') as file:
    purchase= json.load(file)
print(purchase)