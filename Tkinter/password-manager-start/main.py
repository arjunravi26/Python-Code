import json
import random
import string
from tkinter import Tk, Label, Entry, Button, Canvas, messagebox, END, PhotoImage

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list(string.punctuation)

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = password_letter + password_number + password_symbol
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(first=0, last=END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_clicked():
    website_name = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_dict = {website_name: {
        "username": username,
        "password": password
    }}
    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOps", message="Make sure you dont make any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website_name,
                                       message=f"username is {username} and password is {password} Is it ok to save")

        if is_ok:
            try:
                with open('password.json', 'r') as f:
                    data = json.load(f)
            except FileNotFoundError:
                with open('password.json', 'w') as f:
                    json.dump(new_dict, f, indent=4)

            else:
                data.update(new_dict)
                with open('password.json', 'w') as f:
                    json.dump(data, f, indent=4)
            finally:
                f.close()
                website_entry.delete(first=0, last=END)
                password_entry.delete(first=0, last=END)


# ---------------------------- SEARCH WEBSITE DETAILS ------------------------------- #
def search():
    website_name = website_entry.get().title()
    try:
        with open('password.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website_name in data:
            messagebox.showinfo(title=website_name,
                                message=f"Username is : {data[website_name]['username']}\nPassword is {data[website_name]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_name} exists.")


# ---------------------------- UI SETUP ------------------------------- #
image = 'Tkinter\password-manager-start\logo.png'
window = Tk()
window.title("password manager")
window.config(pady=50, padx=50)
canvas_logo = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file=image)
canvas_logo.create_image(100, 100, image=logo_img)
canvas_logo.grid(row=0, column=1)

# Label

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
label_username = Label(text="Email/Username:")
label_username.grid(row=2, column=0)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

# Entry
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(END, "@gmail.com")
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)
password_entry.focus()

# Buttons
button_search = Button(text="Search", command=search)
button_search.grid(row=1, column=2)
button_generate = Button(text="Generate", command=generate_password)
button_generate.grid(row=3, column=2)
button_ok = Button(text="Add", width=36, command=add_button_clicked)
button_ok.grid(row=4, column=1, columnspan=2)

window.mainloop()
