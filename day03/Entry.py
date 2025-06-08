import tkinter

root=tkinter.Tk()
entry=tkinter.Entry(root)
entry.pack()

def print_left(event):
    print("Left pressed")

root.bind("<Left>",print_left)


root.mainloop()