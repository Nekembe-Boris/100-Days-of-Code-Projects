from turtle import Turtle


class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=275)
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Arial', 15, 'normal'))


    def score_check(self, target):
        if target == True:
            self.score += 1
            self.clear()
            self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Arial', 15, 'normal'))
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=('Arial', 15, 'normal'))