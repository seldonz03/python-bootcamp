import json
import tkinter

root = tkinter.Tk()

label= tkinter.Label(root, text ="Name")
label.pack()
entry1 = tkinter.Entry(root)
entry1.pack()


label2 = tkinter.Label(root, text ="Age" )
label2.pack()
entry2 = tkinter.Entry(root)
entry2.pack()

label3 = tkinter.Label(root, text ="Preferred Theme" )
label3.pack()
radio_var = tkinter.StringVar(value="Light")
radio1 = tkinter.Radiobutton(
    root, text="Light", variable=radio_var, value="Light")
radio2 = tkinter.Radiobutton(
    root, text="Dark", variable=radio_var, value="Dark")
radio1.pack()
radio2.pack()


#Checkbox

check_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(
root,
text="Subscribe to newsletter",
variable=check_value
)
checkbox.pack()

#slide

slider_value = tkinter.IntVar(value=0)
slider = tkinter.Scale(
    root,
    from_= 0,
    to = 5,
    orient="horizontal",
    variable=slider_value


)

slider.pack()
label3 = tkinter.Label(root, text ="Rate us" )
label3.pack()





def display():
    user_info = {
        "Name": entry1.get(),
        "Age": entry2.get(),
        "Theme":radio_var.get(),
        "Subscribe":check_value.get(),
        "Rating": slider_value.get()
    }
    with open('user.json', 'w') as file:
        json.dump(user_info, file, indent=4)

button = tkinter.Button(root, text="Submit", command= display)
button.pack()








root.mainloop()