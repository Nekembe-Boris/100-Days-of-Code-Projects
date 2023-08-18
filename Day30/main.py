from tkinter import *
from tkinter import messagebox
from password_generator import p_generator
import json
import os
import pyperclip

FONT_NAME = "Courier"


def auto_gen():
    """Prints the auto generated password to the password entry placeholder"""

    auto_password = p_generator()
    password_entry.insert(END, string=f"{auto_password}")
    pyperclip.copy(auto_password)


def save_details():
    """Checks if all fields are complete, ask the user if the submitted details are correct and finally appends the details to the 'Pass_store' file"""

    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()

    new_data =  {
        website : {
            "Email" : email,
            "Password": password
        }
    }
    
    if len(website) < 1 or len(password) < 1:
        messagebox.showinfo(
            title="Error",
            message="Please ensure that there is no empty field"
            )
    else:
        confirm = messagebox.askyesno(
        message=f"Are you sure the following details are correct?\nWebsite: {website}\nEmail: {email}\nPassword: {password}",
        icon = "question",
        title="Confrim details"
            )

        if confirm == True:
            try:
                with open("Pass_store.json", "r") as file:
                    info = json.load(file)
            except FileNotFoundError:
                with open("Pass_store.json", "w") as file:
                    json.dump(new_data, file, indent=4)   
            else:
                info.update(new_data)
                with open("Pass_store.json", "w") as file:
                    json.dump(info, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

def search_data():
    
    website = website_entry.get().title()

    try:
        with open("Pass_store.json", "r") as file:
            info = json.load(file)

    except FileNotFoundError:
            messagebox.showinfo(

                title="No File",
                message="You do not have any previously store password"
            )
    else:
        for i in info:
            if i == website:
                password_entry.insert(END, string=f"{info[website]['Password']}")



window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= logo_image)
canvas.grid(column=1, row=0)


website_label = Label(text="Website: ", font=(FONT_NAME, 15, "bold"))
website_label.grid(column=0, row=1)


email_label = Label(text="Email/Username: ", font=(FONT_NAME, 15, "bold"))
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ", font=(FONT_NAME, 15, "bold"))
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
#the focus() method causes the cursor to automatically start here
website_entry.focus()
website_entry.grid(column=1, row=1)

search_button = Button(text="Search", font=(FONT_NAME, 10, "bold"), width=15, command=search_data)
search_button.grid(column=2, row=1)

email_entry = Entry(width=60)
email_entry.insert(END, string=("boris@email.com"))
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)


generate_button = Button(text="Generate Password", font=(FONT_NAME, 10, "bold"), command=auto_gen)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", font=(FONT_NAME, 10, "bold"), width=45, command=save_details)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()