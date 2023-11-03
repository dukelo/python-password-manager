from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []
    [password_list.append(random.choice(letters)) for char in range(random.randint(8, 10))]
    [password_list.append(random.choice(numbers)) for char in range(random.randint(2, 4))]
    [password_list.append(random.choice(symbols)) for char in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = "".join(password_list)
    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()

    # try:
    #     with open('data.json', mode='r') as data_file:
    #         data = json.load(data_file)
    # except FileNotFoundError:
    #     messagebox.showinfo(title='info', message='no data')
    # else:
    #     for key in data:
    #         if website == key:
    #             messagebox.showinfo(title='info', message=f"email: {data[key]['email']}\n" +
    #                                                       f"password: {data[key]['password']}")
    #         break

    try:
        with open('data.json', mode='r') as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title='info', message=f"email: {data[website]['email']}\n" +
                                                      f"password: {data[website]['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title='info', message='no data')
    except KeyError:
        messagebox.showinfo(title='info', message='no data in file')
    else:
        pass


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Don't left any empty")
    else:
        try:
            with open(file='data.json', mode='r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open(file='data.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open(file='data.json', mode='w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password-manager-start")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
password_label = Label(text='Password')
password_label.grid(column=0, row=3)

# Entries

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, sticky='w')
website_entry.focus()
email_entry = Entry(width=45)
email_entry.grid(column=1, row=2, columnspan=2, sticky='w')
email_entry.insert(0, "duke@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='w')

# Buttons
generate_password_button = Button(text='Generate Password', command=generate_password, width=15)
generate_password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='search', width=15, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
