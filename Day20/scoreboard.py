from turtle import Turtle


class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=275)
        self.write(arg="Score: 0", move=False, align="center", font=('Arial', 15, 'normal'))


    def score_check(self, eat, count):
        if eat == True:
            self.score += 1
            self.clear()
            self.write(arg=f"Score: {count}", move=False, align="center", font=('Arial', 15, 'normal'))
    