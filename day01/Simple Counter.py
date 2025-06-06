count = 0
stop_program = False
"""
while not stop_program:
    choice = input("Provide a command:")
    if choice == "add":
        count += 1
        print(count)
    elif choice == "minus":
        count -= 1
        print(count)
    elif choice == "exit":
        stop_program = True """

while not stop_program:
    choice = input("Provide a command:")
    match choice:
        case "add":
            count += 1
            print(count)
        case "minus":
            count -= 1
            print(count)
        case "exit":
            stop_program = True

