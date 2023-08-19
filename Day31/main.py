from tkinter import *
import pandas


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 265, image = card_image)
canvas.grid(column=0, row=0, columnspan=2)

language_label = Label(text="French", font=("Arial", 35, "italic"), background="white")
language_label.place(x=325, y=100)

word_label = Label(text="word", font=("Century Gothic", 20, "normal"), background="white")
word_label.place(x=355, y=350)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=1, row=1)


window.mainloop()