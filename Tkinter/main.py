import tkinter

# windows = tkinter.Tk()
# windows.title("Arjun")
# windows.minsize(width=500, height=300)
# my_label = tkinter.Label(text="This is a label", font=("Arial", 24, "italic"))
# my_label.pack(side="left")
# windows.mainloop()
windows = tkinter.Tk()
windows.title("New Text")
windows.minsize(width=500, height=500)
label = tkinter.Label(text="My Label")
label.pack()


def button_clicked():
    value = user_input.get()
    label.config(text=f"Your input is {value}")


user_input = tkinter.Entry(width=50)
user_input.pack()
button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()
windows.mainloop()
