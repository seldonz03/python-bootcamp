"""def m(n):
    p = []
    for q in n:
        if q not in p:
            p.append(q)
    return p
r = [1, 2, 3, 3, 4, 5, 5]
s = m(r)
print(s)
"""
from copyreg import remove_extension


def remove_duplicate(numbers):
    new_list=[]
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
    return  new_list

List = [1, 2, 3, 3, 4, 5, 5]
result = remove_duplicate(List)
print(result)


