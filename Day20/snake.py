import turtle

START = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20

class Snake:

    def __init__(self):
        self.square_list = []
        self.snake_blueprint()


    def snake_blueprint(self):   
        for i in range(3):
            square = turtle.Turtle(shape=("square"))
            square.penup()
            square.color("white")
            square.goto(START[i])
            self.square_list.append(square)

    def move(self):
        for i in range(len(self.square_list) - 1, 0, -1):
            positionx = self.square_list[i-1].xcor()
            positiony = self.square_list[i-1].ycor()
            self.square_list[i].goto(positionx, positiony)  
        self.square_list[0].forward(DISTANCE)


    def right(self):
        self.square_list[0].setheading(0)

    def up(self):
        self.square_list[0].setheading(90)

    def left(self):
        self.square_list[0].setheading(180)

    def down(self):
        self.square_list[0].setheading(270)
