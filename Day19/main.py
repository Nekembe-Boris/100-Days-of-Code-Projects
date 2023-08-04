import turtle
import random

colors = ["red", "blue", "green", "yellow", "black", "brown"]
racer_list = []

y_pos = -200

for object in range(len(colors)):
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.penup()
    racer.color(colors[object])
    racer.goto(-350, y_pos)
    racer_list.append(racer)
    y_pos += 70

#This turtle prints the race winner on the screen
declare_winner = turtle.Turtle()
declare_winner.hideturtle()
declare_winner.penup()

screen = turtle.Screen()
screen.screensize(canvwidth=600, canvheight=600)

user_bet = screen.textinput("Place a Bet", "Which turtle will win the race. Enter a color: ").lower()

end_race = False

while end_race != True:

    for object in racer_list:

        object.forward(random.randint(1, 4))

        position = round(object.xcor())

        if position > 355:
            end_race = True
            if user_bet == object.color()[0]:
                declare_winner.write(arg=f"You WON the bet. The {object.color()[0]} turtle won", move=True, align = 'center', font = ('Courier', 15, 'bold'))
            else:
                declare_winner.write(arg=f"You LOST the bet. The {object.color()[0]} turtle won", move=True, align = 'center', font = ('Courier', 15, 'bold'))
            


screen.exitonclick()