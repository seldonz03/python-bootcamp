import tkinter
root = tkinter.Tk()
root.title("SAmple GUI Application")
root.geometry("1200x400")
label = tkinter.Label(root, text = "Hello",fg="red",bg="yellow",width = "100",height="20" ,font=("Arial", 14,"bold italic"))
label.pack()

next_label = tkinter.Label(root, text="World",fg="red",bg="yellow", width = "100",height="20",padx=10,pady=200,font=("Arial", 14,"bold italic"))
next_label.pack()

message = """Hello World
            In Multiple lines
            """

label=tkinter.Label(root, text=message)
label.pack()


root.mainloop()
