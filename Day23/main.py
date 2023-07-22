from turtle import Screen
from cars import Cars
from player import Player, Level
import random
import time


screen = Screen()
screen.setup(width=700, height=600)
screen.title("The Turtle Crossing Game")
screen.tracer(0)

car = Cars()
player = Player()
level = Level()

screen.listen()
screen.onkeypress(player.move_up, "Up")

speed = 0.15

game_over = False

timer = 180

while game_over != True:


    time.sleep(speed)
    screen.update()
    check = False

    for i in range(len(car.car_list)):
        car.car_list[i].forward(10)
    timer -= 1

    print(timer)

    for i in range(len(car.car_list)):
        if player.distance(car.car_list[i]) < 15:
            level.game_over()
            game_over = True

    if player.ycor() >= 280:
        check = True
        level.level_up(check)
        player.restart(check)
        car.restart(check)
        speed -= 0.05
    
    if timer == 0:
        print("yep")
        check = True
        car.restart(check)
        timer += 180


screen.exitonclick()