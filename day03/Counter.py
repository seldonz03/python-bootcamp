import tkinter

root = tkinter.Tk()

count = tkinter.IntVar(root, value=0)
label = tkinter.Label(root, textvariable=count)
label.pack()

def increment():
    count.set(count.get() + 1)
button = tkinter.Button(root, text=" + ", command=increment)
button.pack(side="left")

def decrement():
    count.set(count.get() - 1)
button2 = tkinter.Button(root, text=" - ", command=decrement)
button2.pack(side="right")


root.mainloop()