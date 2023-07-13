import colorgram
import turtle
import random

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
pen.goto(-300, -200)

new_line = 50


for i in range(0, 10):
    for lenght in range(0, 10):

        pen.dot(25, random.choice(colors)); pen.forward(50)

        if lenght == 9:
            pen.goto(-300, -200 + new_line)
            new_line += 50


screen = turtle.Screen()
screen.exitonclick()
