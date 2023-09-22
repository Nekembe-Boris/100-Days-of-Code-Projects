from turtle import Turtle
import random

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
        self.x_dir = 10
        self.y_dir = 10
        self.inc_speed = 5

    def movement(self):
        positionx = self.xcor() + self.x_dir
        positiony = self.ycor() + self.y_dir
        self.goto(positionx, positiony)

    def bounce_wall(self): 
        self.y_dir *= -1

        
    def bounce_paddle(self):
        self.x_dir *= -1
        add = self.speed() * self.inc_speed
        self.speed(add)

    def start_over(self, check):
        if check == True:
            self.goto(0, 0)
            self.bounce_paddle()