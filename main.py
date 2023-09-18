from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

FONT_NAME = "Ariel"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 and len(password) == 0:
        messagebox.showinfo(title="OOPS!!", message="Can't leave this fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: Email: {email}\n"
                                                              f"password: {password} \n is it okay to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
# labels
website_label = Label(text="website:")
website_label.grid(column=0, row=1)
#
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
#
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# entry's
web_entry = Entry(width=38)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

# buttons
generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text='add', width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
