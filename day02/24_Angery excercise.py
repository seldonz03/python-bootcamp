paragraph = "I am perfectly calm and everything is fine"

lower_count = 0
upper_count = 0
space_count = 0

for char in paragraph:
    if paragraph.islower():
        lower_count +=1

    elif paragraph.isspace():
        space_count += 1
print("Lower case count", lower_count)
print("upper case count", upper_count)
print("space case count", space_count)
