from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")

    def score_check(self, check):
        if check == True:
            self.score += 1
            self.clear()
            self.write(arg=f"{self.score}", move=False, align="center", font=('Arial', 60, 'normal'))

       

class Score_l(Score):
    def __init__(self):
        super().__init__()
        self.goto(x=-100, y=200)
        self.write(arg=f"{self.score}", move=False, align="center", font=('Arial', 60, 'normal'))

class Score_r(Score):
    def __init__(self):
        super().__init__()
        self.goto(x=100, y=200)
        self.write(arg=f"{self.score}", move=False, align="center", font=('Arial', 60, 'normal'))

