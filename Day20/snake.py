import turtle

START = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

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
        if self.square_list[0].heading() != LEFT:
            self.square_list[0].setheading(RIGHT)

    def up(self):
        if self.square_list[0].heading() != DOWN:
            self.square_list[0].setheading(UP)

    def left(self):
        if self.square_list[0].heading() != RIGHT:
            self.square_list[0].setheading(LEFT)

    def down(self):
        if self.square_list[0].heading() != UP:
            self.square_list[0].setheading(DOWN)
