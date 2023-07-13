import colorgram
import turtle
import random

color_list = [(236, 248, 243), (36, 95, 183), (236, 165, 79), (244, 223, 87), (215, 69, 105), (98, 197, 234),
              (250, 51, 22), (203, 70, 21), (240, 106, 143), (185, 47, 90), (143, 233, 216), (252, 136, 166),
              (165, 175, 233), (66, 45, 13), (72, 205, 170), (83, 187, 100), (20, 156, 51), (24, 36, 86), (252, 220, 0),
              (164, 28, 8), (105, 39, 44), (250, 152, 2), (22, 151, 229), (108, 213, 249), (254, 12, 3), (38, 48, 98),
              (98, 96, 186)
              ]

turtle.colormode(255)
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(-300, -200)

new_line = 50


for i in range(0, 10):
    for lenght in range(0, 10):

        pen.dot(25, random.choice(color_list)); pen.forward(50)

        if lenght == 9:
            pen.goto(-300, -200 + new_line)
            new_line += 50


screen = turtle.Screen()
screen.exitonclick()