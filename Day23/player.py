from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        """This initializes the player class"""
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.restart()

    def move_up(self):
        self.forward(10)

    def restart(self):
        """Takes the turtle back to its starting position"""
        self.goto(x=0, y=-280)


    

class Level(Turtle):


    def __init__(self):
        """This initializes the scoreboard class"""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=270)
        self.level = 1
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=("Courier", 15, "bold"))


    def game_over(self):
        """Prints Game Over on the scren if the turtle is hit by a car"""
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=("Courier", 15, "bold"))


    def level_up(self):
            """Increases the level each time the turtle successfully crosses the road"""
            self.level += 1
            self.clear()
            self.write(arg=f"Level: {self.level}", move=False, align="center", font=("Courier", 15, "bold"))
    
    def restart(self):
        """Reinstates the scoreboard each time the player decides to try again after being hit by a car"""
        self.clear()
        self.goto(x=-280, y=270)
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=("Courier", 15, "bold"))