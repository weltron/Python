from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters)for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols)for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers)for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    passwd_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = web_entry.get()
    email = user_entry.get()
    password = passwd_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please do not leave any fields empty!")
    else: 
        try:      
            with open("data.json", "r") as f:
                #read json data
                data_tosave = json.load(f)
                
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)

        else:
            # update json with new data
            data_tosave.update(new_data)
            with open("data.json", "w") as f:
                # save new data to json
                json.dump(data_tosave, f, indent=4)

        finally:
            web_entry.delete(0, END)
            passwd_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def search():
    website = web_entry.get()
    try:    
        with open("data.json", "r") as file:
            data_search = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data_search:
            email = data_search[website]["email"]
            password = data_search[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

passwd_label = Label(text="Password:")
passwd_label.grid(column=0, row=3)

web_entry = Entry(width=33)
web_entry.grid(column=1, row=1)

search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1)

user_entry = Entry(width=52)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "user@example.com")

passwd_entry = Entry(width=33)
passwd_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()