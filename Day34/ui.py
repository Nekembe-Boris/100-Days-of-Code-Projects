from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUi:
    
    def __init__(self, main_quiz:QuizBrain):
        self.quiz = main_quiz
        self.window = Tk()
        self.score = 0
        self.window.title = "GUI QUIZ TRIVIA"
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300)
        self.canvas_text = self.canvas.create_text(
            150, 
            125, 
            text= "Question", 
            font=("Arial", 20, "italic"), 
            width=290
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.false_btn = Button(image=false_img, highlightthickness=0)
        self.false_btn.grid(row=2, column=1)

        self.true_btn = Button(image=true_img, highlightthickness=0)
        self.true_btn.grid(row=2, column=0)

        self.get_next_q()


        self.window.mainloop() 

    def get_next_q(self):
        new_ques = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_text, text=new_ques)