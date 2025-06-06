name_message = "your name is {}."
number_message = "Your favorite number is {}."
color_message = "your favorite color {}."

name = input("What is your name:")
number = input("Your Favorite number:")
color = input("Your Favorite color: ")

format_name = name_message.format(name)
format_number = number_message.format(number)
format_color = color_message.format(color)

print(format_name)
print(format_number)
print(format_color)
