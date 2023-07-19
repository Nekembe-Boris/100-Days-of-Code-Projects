import turtle

START1 = [(-470, 0), (-470, 30), (-470, -30)]
START2 = [(470, 0), (470, 30), (470, -30)]


class Player1:
    def __init__(self):
        self.list = []
        self.create_player()
        

    def create_player(self):
        for position in START1:
            self.blueprint(position)
   

    def blueprint(self, position):
        square = turtle.Turtle()
        square.shape("square")
        square.penup()
        square.color("white")
        square.shapesize(1.5, 0.5)
        square.goto(position)
        self.list.append(square)


class Player2(Player1):
    def __init__(self):
        super().__init__()
    
    def create_player(self):
        super().create_player()
        for position in START2:
            self.blueprint(position)

    def blueprint(self, position):
        super().blueprint(position)      
