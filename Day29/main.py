from tkinter import *
from tkinter import messagebox

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    confirm = messagebox.askyesno(
        message=f"Are you sure you want to save this password?\nWebsite: {website}\nEmail: {email}\nPassword: {password}",
        icon = "question",
        title="Confim password"
    )

    if confirm == True:
        with open("Pass_store.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
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

website_entry = Entry(width=60)
#the focus() method causes the cursor to automatically start here
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=60)
email_entry.insert(END, string=("nekembeb@gmail.com"))
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)


generate_button = Button(text="Generate Password", font=(FONT_NAME, 10, "bold"))
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", font=(FONT_NAME, 10, "bold"), width=45, command=save_details)
add_button.grid(column=1, row=4, columnspan=2)







window.mainloop()