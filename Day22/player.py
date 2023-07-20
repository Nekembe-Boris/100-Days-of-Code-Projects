import turtle

START1 = [(-470, 20), (-470, 0), (-470, -20)]
START2 = [(470, 20), (470, 0), (470, -20)]
DISTANCE = 20

class Paddle:
    def __init__(self):
        self.list = []

            
    def blueprint(self, position):
        square = turtle.Turtle()
        square.shape("square")
        square.penup()
        square.color("white")
        square.goto(position)
        self.list.append(square)


    def move_up(self):
        for i in range(len(self.list) - 1, 0, -1):
            pos_x = self.list[i-1].xcor()
            pos_y = self.list[i-1].ycor()
            self.list[i].goto(pos_x, pos_y)
        self.list[0].forward(DISTANCE)
    

    def move_down(self):
        for i in range(0, 2, 1):
            pos_x = self.list[i+1].xcor()
            pos_y = self.list[i+1].ycor()
            self.list[i].goto(pos_x, pos_y)
        self.list[-1].forward(DISTANCE)
    


class Paddle1(Paddle):
    def __init__(self):
        super().__init__()
        self.create_player()
    
    def create_player(self):
        for position in START1:
            self.blueprint(position)
            self.list[0].setheading(90)
            self.list[-1].setheading(270)

    def blueprint(self, position):
        super().blueprint(position)      



class Paddle2(Paddle):
    def __init__(self):
        super().__init__()
        self.create_player()
    
    def create_player(self):
        for position in START2:
            self.blueprint(position)
            self.list[0].setheading(90)
            self.list[-1].setheading(270)

    def blueprint(self, position):
        super().blueprint(position)  