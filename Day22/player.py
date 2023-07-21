from turtle import Turtle

START1 = (-370, 0)
START2 = (370, 0)
DISTANCE = 30
UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)

    def move_up(self):
        self.forward(DISTANCE)

    def move_down(self):
        self.backward(DISTANCE)

    
class Paddle1(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(START1)


class Paddle2(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(START2)