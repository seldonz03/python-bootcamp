import tkinter
root=tkinter.Tk()

Label2=tkinter.Label(root,text="Enter Your password:")
Label2.pack()
entry = tkinter.Entry(root)
entry.pack()
user_input=tkinter.StringVar(root, value="Enter your password and press Enter")
label=tkinter.Label(root,textvariable=user_input)
label.pack()


def display(event=None):
    if "pass123" == entry.get():
        user_input.set("Correct password")
    else:
        user_input.set("Incorrect password")

button = tkinter.Button(root, text="Submit", command = display)
button.pack()

root.bind("<Return>", display)
root.mainloop()