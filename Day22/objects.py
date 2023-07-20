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
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.9, 0.9)

    def movement(self, turn):
        self.setheading(turn)
        self.forward(4)

    def tilt(self):
        if self.ycor() > 280:
            self.tiltangle(45)
            self.forward(4)
        elif self.ycor() < -280:
            self.tiltangle(90)
            self.forward(4)

