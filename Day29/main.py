from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- Search ------------------------------- #
def search():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error Loading File", message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f" Email: {data[website]['email']}\n Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message="Website not found")       
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    rand_letters = [random.choice(letters) for _ in range(random.randint(8, 10)) ]
    rand_sym = [random.choice(symbols) for _ in range(random.randint(2, 4)) ]
    rand_num = [random.choice(numbers) for _ in range(random.randint(2, 4)) ]

    password_list = rand_letters + rand_sym + rand_num

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():

    website = website_input.get()
    user = user_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email": user,
            "password": password,
        }
    }
    if not website or not password:
        messagebox.showinfo(title="Missing Information", message="Cannot Leave Blank Entries")
        return
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4 )
        else:
            data.update(new_data)
        
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4 )
        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#Website
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = Entry(width=34)
website_input.focus()
website_input.grid(row=1, column=1)

#Email/Username
user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)
user_input = Entry(width=52)
user_input.insert(END, "austinv@email.com")
user_input.grid(row=2, column=1, columnspan=2)

#Password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_input = Entry(width=34)
password_input.grid(row=3, column=1)
password_gen = Button(text="Generate Password", command=gen_pass)
password_gen.grid(row=3, column=2)

#Add
add_button = Button(text="Add", width=44, command=save_pass)
add_button.grid(row=4, column=1, columnspan=2)

#Search
search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)


window.mainloop()
