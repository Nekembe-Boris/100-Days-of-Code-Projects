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
        self.create_snake()


    def create_snake(self):
        for position in (START):
            self.snake_blueprint(position)


    def snake_blueprint(self, position):   
        square = turtle.Turtle(shape=("square"))
        square.penup()
        square.color("white")
        square.goto(position)
        self.square_list.append(square)


    def extend_snake(self):
        self.snake_blueprint(self.square_list[-1].position())

    def move(self):
        for i in range(len(self.square_list) - 1, 0, -1):
            positionx = self.square_list[i-1].xcor()
            positiony = self.square_list[i-1].ycor()
            self.square_list[i].goto(positionx, positiony)  
        self.square_list[0].forward(DISTANCE)


    def restart_snake(self):
        for i in range(len(self.square_list)):
            self.square_list[i].goto(1000, 1000)
        self.square_list.clear()
        self.create_snake()


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

    def wall_collision(self):
        positionx = self.square_list[0].xcor()
        positiony = self.square_list[0].ycor()
        if positionx < -295 or positionx > 295:
            return True
        elif positiony < -295 or positiony > 295:
            return True