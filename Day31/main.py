from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
 
words_dict = data.to_dict(orient="records")
chosen_word = {}



def cards():
    """This function displays new cards when the function starts"""

    global chosen_word
    global timer
    window.after_cancel(timer)
    
    chosen_word = random.choice(words_dict)

    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=f"{chosen_word['French']}", fill="black")
    canvas.itemconfig(canvas_image, image=front_card_image)
    timer = window.after(3000, flip_card)
    

def flip_card():
    """Flips the current card and shows the word in english"""

    canvas.itemconfig(canvas_image, image= back_card_image)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=f"{chosen_word['English']}", fill="white")

def known_word():
    """Removes the current word from the csv file and creates a new csv file containing words to learn"""

    words_dict.remove(chosen_word)
    data = pandas.DataFrame(words_dict)
    data.to_csv("./data/words_to_learn.csv", index=False)
    cards()
    

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_image = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 265, image = front_card_image)
canvas_title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=cards)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=known_word)
right_button.grid(column=1, row=1)

back_card_image = PhotoImage(file="./images/card_back.png")

cards()

window.mainloop()