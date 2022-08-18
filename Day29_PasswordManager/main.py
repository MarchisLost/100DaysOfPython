from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 5))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 5))]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char
    # Instead of the code above we can do it like this
    password = ''.join(password_list)

    # Place the password on the entry
    passwordEntry.insert(0, password)

    # Copies the password to the paperclip
    pyperclip.copy(password)
    messagebox.showinfo(message='The password has been copied to ur clipboard')

# ---------------------------- SAVE PASSWORD ------------------------------- #


def saveData(websiteEntry, mailEntry, passwordEntry):
    if (not websiteEntry.get() or not mailEntry.get() or not passwordEntry.get()):
        messagebox.showerror(message='At least one of the variables is empty')
    else:
        is_ok = messagebox.askokcancel(title=websiteEntry.get(), message='U sure u wanna save it?')
        if is_ok:
            with open("Day29_PasswordManager/data.txt", "a") as f:
                f.write(f"{websiteEntry.get()} - {mailEntry.get()} - {passwordEntry.get()}\n")

            # Clear data on entries
            websiteEntry.delete(0, END)
            passwordEntry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="Day29_PasswordManager/logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Labels
websiteLabel = Label(text='Website:')
websiteLabel.grid(column=0, row=1)

mailLabel = Label(text='Email/Password:')
mailLabel.grid(column=0, row=2)

passwordLabel = Label(text='Password:')
passwordLabel.grid(column=0, row=3)

# Entries
websiteEntry = Entry(width=52)
websiteEntry.grid(column=1, row=1, columnspan=2)
websiteEntry.focus()

mailEntry = Entry(width=52)
mailEntry.grid(column=1, row=2, columnspan=2)
mailEntry.insert(0, 'davidpinto15@gmail.com')

passwordEntry = Entry(width=33, show='*')
passwordEntry.grid(column=1, row=3)

# Buttons
generateButton = Button(text='Generate Password', command=generatePassword)
generateButton.grid(column=2, row=3)

addButton = Button(text='Add', width=44, command=lambda: saveData(websiteEntry, mailEntry, passwordEntry))
addButton.grid(column=1, row=4, columnspan=2)

window.mainloop()
