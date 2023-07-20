from turtle import Turtle, Screen
from player import Paddle1, Paddle2
from objects import Lines, Ball


my_screen = Screen()
my_screen.setup(height=600, width=1000)
my_screen.title("Ping Pong")
my_screen.bgcolor("black")




player_1 = Paddle1()
player_2 = Paddle2()
net = Lines()
ball = Ball()


my_screen.update()
my_screen.listen()
my_screen.onkey(player_1.move_up, "Up")
my_screen.onkey(player_1.move_down, "Down")
my_screen.onkey(player_2.move_up, "a")
my_screen.onkey(player_2.move_down, "s")
my_screen.update()

my_screen.exitonclick()