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