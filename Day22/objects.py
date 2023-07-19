from turtle import Turtle


class Lines:
    def __init__(self):
        self.create_net()

    def net(self, shift):
        line = Turtle()
        line.penup()
        line.shape("square")
        line.color("white")
        line.shapesize(0.5, 0.05)
        line.goto(x=0, y=280 - shift)

    def create_net(self):
        shift = 0
        for i in range(0, round(600/20)):
            self.net(shift)
            shift -= -20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
