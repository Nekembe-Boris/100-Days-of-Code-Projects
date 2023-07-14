import turtle
import os
import random

colors = ["red", "blue", "green", "yellow", "black", "brown"]
turtle_shift = 0
turtle_list = []

def create(model):
    model.penup()
    model.shape("turtle")

for i in range(len(colors)):
    tur = turtle.Turtle()
    create(tur)
    tur.goto(x=-300, y=-200 + turtle_shift)
    turtle_shift += 70
    tur.color(colors[i])
    turtle_list.append(tur)

turtle.colormode(255)



screen = turtle.Screen()
screen.setup(height=600, width=700)


user_bet = screen.textinput("Place a Bet", "Which turtle will win the race. Enter a color: ").lower()

end_race = False

while end_race != True:

    for i in turtle_list:
        i.forward(random.randint(0, 4))
        position = round(i.xcor())


        if position > 315:
            end_race = True
            if user_bet == i.color()[0]:
                print(f"You won. The winner is the {i.color()[0]} turtle")
            else:
                print(f"You lose. The winner is the {i.color()[0]} turtle")
            


screen.exitonclick()