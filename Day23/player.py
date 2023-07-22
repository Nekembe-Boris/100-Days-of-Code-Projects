from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(x=0, y=-280)

    def move_up(self):
        self.forward(10)

    def restart(self, check):
        if check == True:
            self.goto(x=0, y=-280)

    



class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=270)
        self.level = 1
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=("Courier", 15, "bold"))

    def game_over(self):
        self.color("black")
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=("Courier", 15, "bold"))

    def level_up(self, check):
        if check == True:
            self.level += 1
            self.clear()
            self.write(arg=f"Level: {self.level}", move=False, align="center", font=("Courier", 15, "bold"))