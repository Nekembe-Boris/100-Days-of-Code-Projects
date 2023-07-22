import turtle
import random

turtle.colormode(255)


color_list = []
position = []

for i in range(0, 50):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color_list.append((red,green,blue))

    x = random.randint(300, 2000)
    y = random.randint(-230, 250)
    position.append((x, y))



class Cars():
    def __init__(self):
        self.car_list = []
        self.create_car()
        
    def car_model(self):
        car = turtle.Turtle()
        car.shape("square")
        car.penup()
        car.color(random.choice(color_list))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        car.goto(random.choice(position))
        self.car_list.append(car)

    def create_car(self):
        for i in range(len(color_list)):
            self.car_model()
