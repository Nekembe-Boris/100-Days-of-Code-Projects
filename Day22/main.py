from turtle import Turtle, Screen
from player import Player1, Player2


my_screen = Screen()
my_screen.setup(height=600, width=1000)
my_screen.title("Ping Pong")
my_screen.bgcolor("black")
my_screen.tracer(0)


player_1 = Player1()
player_2 = Player2()

my_screen.update()





my_screen.exitonclick()