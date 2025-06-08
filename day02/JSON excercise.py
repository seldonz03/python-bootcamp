import json

data = [
    {'Name': 'Alice','Age':30, 'Occupation':'Engineer'},
    {'Name': 'Bob','Age':20, 'Occupation':'Designer'}

]

with open('poeple.json','w') as file:
    json.dump(data, file, indent=4)