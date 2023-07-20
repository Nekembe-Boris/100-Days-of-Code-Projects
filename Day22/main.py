from turtle import Turtle, Screen
from player import Paddle1, Paddle2
from objects import Lines, Ball
import time


my_screen = Screen()
my_screen.setup(height=600, width=1000)
my_screen.title("Ping Pong")
my_screen.bgcolor("black")
my_screen.tracer(0)


player_1 = Paddle1()
player_2 = Paddle2()
net = Lines()
ball = Ball()


my_screen.listen()
my_screen.onkeypress(player_1.move_up, "Up")
my_screen.onkeypress(player_1.move_down, "Down")
my_screen.onkeypress(player_2.move_up, "a")
my_screen.onkeypress(player_2.move_down, "s")


end_game = False

while end_game != True:
    time.sleep(0.009)
    my_screen.update()

my_screen.mainloop()