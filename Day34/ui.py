from tkinter import *
from quiz_brain import QuizBrain
import time

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

        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.respond_false)
        self.false_btn.grid(row=2, column=1)

        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.respond_true)
        self.true_btn.grid(row=2, column=0)

        self.get_next_q()


        self.window.mainloop() 

    def get_next_q(self):
        self.canvas.config(bg="white")
        new_ques = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_text, text=new_ques)

        if self.quiz.questions_left() == False:
            self.canvas.itemconfig(self.canvas_text, text=f"End of Quiz\nFinal score is {self.score}/{len(self.quiz.question_list)}")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")


    def respond_true(self):
        answer = self.quiz.check_answer("True", self.quiz.question.answer)
        self.feedback(answer)


    def respond_false(self):
        answer = self.quiz.check_answer("False", self.quiz.question.answer)
        self.feedback(answer)
        

    def feedback(self, response):
        if response ==True:
            self.canvas.config(bg="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_q)
