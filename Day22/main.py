from turtle import Turtle, Screen
from player import Paddle1, Paddle2
from objects import Lines, Ball
from scoreboard import Score_l, Score_r
import time


my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.title("Ping Pong")
my_screen.bgcolor("black")
my_screen.tracer(0)


paddle_l = Paddle1()
paddle_r = Paddle2()
net = Lines()
ball = Ball()
score_right = Score_l()
score_left = Score_r()

my_screen.update()

my_screen.listen()
my_screen.onkeypress(paddle_l.move_up, "w")
my_screen.onkeypress(paddle_l.move_down, "s")
my_screen.onkeypress(paddle_r.move_up, "Up")
my_screen.onkeypress(paddle_r.move_down, "Down")

end_game = False

while end_game != True:

    time.sleep(0.1)
    my_screen.update()
    ball.movement()
    check = False

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 350 or ball.distance(paddle_l) < 50 and ball.xcor() < -350:
        ball.bounce_rpaddle()

    if ball.xcor() > 400:
        check = True
        score_right.score_check(check)
        ball.start_over(check)
    elif ball.xcor() < -400:
        check = True
        score_left.score_check(check)
        ball.start_over(check)

my_screen.exitonclick()