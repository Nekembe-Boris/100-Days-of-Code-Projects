from turtle import Turtle


class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=275)
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=('Arial', 15, 'normal'))


    def score_check(self, target):
        if target == True:
            self.score += 1
            self.refresh()
    

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.refresh()
   
    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=('Arial', 15, 'normal'))