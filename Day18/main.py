import colorgram

import turtle
import random


def starting_position(object, pos_x, pos_y):
    object.goto(pos_x, pos_y)

def dots(brush):
    brush.dot(25, random.choice(colors))
    brush.forward(50)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

colors = []

for i in range(0, 36):
    colors.append(random_colors())
 

turtle.colormode(255)
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()


x_pos = -250
y_start = -250


for dot in range(10):
    
    starting_position(pen, x_pos, y_start)

    for i in range(10):
        dots(pen)
        
    y_start += 50 

screen = turtle.Screen()
screen.exitonclick()
