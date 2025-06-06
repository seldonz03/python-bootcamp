color_input = input("Please enter a color:")


if color_input == "green":
    print("Go")
elif color_input == "yellow":
    print("Wait")
elif color_input == "red":
    print("Stop")
else:
    print("Malfunction")


#match
"""
match color_input:
    case "green":
        print("go")
    case "yellow":
        print("wait")
    case "red":
        print("stop")
    case _:
        print("Malfunction")
"""