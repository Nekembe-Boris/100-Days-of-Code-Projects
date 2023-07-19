from turtle import Turtle, Screen
from player import Paddle1, Paddle2
from objects import Lines


my_screen = Screen()
my_screen.setup(height=600, width=1000)
my_screen.title("Ping Pong")
my_screen.bgcolor("black")
my_screen.tracer(0)


player_1 = Paddle1()
player_2 = Paddle2()
net = Lines()


my_screen.update()





my_screen.exitonclick()