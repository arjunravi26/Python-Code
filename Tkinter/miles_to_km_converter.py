import tkinter

window = tkinter.Tk()
window.minsize(width=300, height=500)


def button_clicked():
    value = input_miles.get()
    km_value = int(value) * 1.60934
    label_km.config(text=f"{km_value}")


input_miles = tkinter.Entry(width=20)
miles = input_miles.get()
input_miles.grid(row=2, column=2)
label_miles = tkinter.Label(text='miles')
label_miles.grid(row=2, column=3)
label_is_equal = tkinter.Label(text='is equal to')
label_is_equal.grid(row=3, column=1)
label_km = tkinter.Label(text='0')
label_km.grid(row=3, column=2)
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(row=4, column=2)
label_km_label = tkinter.Label(text='km')
label_km_label.grid(row=3, column=3)

window.mainloop()
