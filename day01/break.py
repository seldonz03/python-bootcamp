counter = 0
for item in range(100):
    user_input = input("Stop?(y/n):")
     if user_input == "y":
        counter +=1
     else:
        break

    print(item)
