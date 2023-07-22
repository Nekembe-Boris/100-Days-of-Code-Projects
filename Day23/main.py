from turtle import Screen
from cars import Cars
import random
import time


screen = Screen()
screen.setup(width=700, height=600)
screen.title("The Turtle Crossing Game")
screen.tracer(0)

car = Cars()

game_over = False

while game_over != True:
    time.sleep(0.05)
    screen.update()
    for i in range(len(car.car_list)):
        car.car_list[i].backward(10)


screen.exitonclick()