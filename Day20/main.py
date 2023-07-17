import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score
import random



screen = turtle.Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snakes = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkey(snakes.up, "Up")
screen.onkey(snakes.down,"Down")
screen.onkey(snakes.right, "Right")
screen.onkey(snakes.left, "Left")


end_game = False


while end_game != True:
    hit_ball = False
    screen.update()
    time.sleep(0.1)
    snakes.move()

    if snakes.square_list[0].distance(food) < 15:
        food.location()
        hit_ball = True
        score.score_check(hit_ball)
        snakes.extend_snake()

    if snakes.wall_collision() == True:
        end_game = True
        score.game_over()

    for segment in snakes.square_list[1:]:
        if snakes.square_list[0].distance(segment) < 10:
            end_game = True
            score.game_over()

screen.exitonclick()