example = "I am perfectly calm and everything is fine"

lower_count = 0
upper_count = 0
space_count = 0
for letter in example:
    if letter.islower():
        lower_count += 1
    elif letter.isupper():
        upper_count +=1
    elif letter.isspace():
        space_count +=1

print("Lower case count:", lower_count)
print("upper count:", upper_count)
print("space count:", space_count)








