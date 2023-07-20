from turtle import Turtle, Screen
from player import Paddle1, Paddle2
from objects import Lines, Ball
import time


my_screen = Screen()
my_screen.setup(height=600, width=1000)
my_screen.title("Ping Pong")
my_screen.bgcolor("black")
my_screen.tracer(0)


paddle_1 = Paddle1()
paddle_2 = Paddle2()
net = Lines()
ball = Ball()

my_screen.update()

my_screen.listen()
my_screen.onkeypress(paddle_1.move_up, "w")
my_screen.onkeypress(paddle_1.move_down, "s")
my_screen.onkeypress(paddle_2.move_up, "Up")
my_screen.onkeypress(paddle_2.move_down, "Down")

end_game = False

while end_game != True:
    my_screen.update()
    time.sleep(0.05)



my_screen.mainloop()