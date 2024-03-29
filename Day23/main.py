from turtle import Screen
from cars import Cars
from player import Player, Level
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

car_speed = 10

game_over = False

timer = 100

while game_over != True:

    time.sleep(0.15)
    screen.update()

    for i in range(len(car.car_list)):
        car.car_list[i].forward(car_speed)
    timer -= 1

    for i in range(len(car.car_list)):
        if player.distance(car.car_list[i]) < 20:
            level.game_over()
            game_over = True

    if player.ycor() >= 280:
        level.level_up()
        player.restart()
        car_speed += 5
    
    if timer == 0:
        car.create_car()
        timer += 100

    if game_over == True:
        replay = screen.textinput("PLAY AGAIN?", "Do you want to try again? 'Y' or 'N'").lower()
        if replay == 'y':
            game_over = False
            player.restart()
            car.create_car()
            level.restart()
            screen.listen()
            screen.onkeypress(player.move_up, "Up")
        else:
            screen.exitonclick()


screen.exitonclick()