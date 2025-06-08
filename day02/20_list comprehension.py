"""list=[number + 1 for number in range(11)]
print(list)

list=[]
for number in range(11):
    list.append(number+1)
print(list)
"""
number_count = int(input("How many to generate?:"))

squares = [0,1,24,9,16,25,36,49,64,81,100]

squares =[number ** 2 for number in range(number_count)]

print(squares)

