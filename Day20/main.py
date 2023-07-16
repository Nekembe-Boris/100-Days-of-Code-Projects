import turtle
import time
from snake import Snake
from food import Food
import random



screen = turtle.Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snakes = Snake()
food = Food()


screen.listen()

screen.onkey(snakes.up, "Up")
screen.onkey(snakes.down,"Down")
screen.onkey(snakes.right, "Right")
screen.onkey(snakes.left, "Left")


end_game = False

while end_game != True:
    screen.update()
    time.sleep(0.1)
    snakes.move()

    if snakes.square_list[0].distance(food) < 15:
        food.location()
