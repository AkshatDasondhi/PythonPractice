from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_text.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()
    new_data = {
        website : {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        oops = messagebox.showinfo(title="Oops", message="Please dont leave any fields empty.")
    else:
        try:
            with open("data.json", "r") as saves:
                data = json.load(saves)
        except:
            with open("data.json", "w") as saves:
                json.dump(new_data, saves, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as saves:
                json.dump(data, saves, indent=4)
        finally:
            website_text.delete(0, END)
            password_text.delete(0, END)


def find_password():
    try:
        with open("data.json") as saves:
            data = json.load(saves)
            for n in data:
                if n == website_text.get():
                    email = data[website_text.get()]["email"]
                    password = data[website_text.get()]["password"]
                    result = messagebox.showinfo(title="Result", message=f"Email : {email}\nPassword: {password}")
    except:
        error = messagebox.showinfo(title="Error", message="No such file found")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="passman.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_lable = Label(text="Website:")
website_lable.grid(column=0, row=1)

website_text = Entry(width=35)
website_text.grid(column=1, row=1)
website_text.focus()

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)

email_lable = Label(text="Email/Username:")
email_lable.grid(column=0, row=2)

email_text = Entry(width=35)
email_text.grid(column=1, row=2, columnspan=2)
email_text.insert(0, "Akay@gmail.com")

password_lable = Label(text="Password:")
password_lable.grid(column=0, row=3)

password_text = Entry(width=28)
password_text.grid(column=1, row=3)
#
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()