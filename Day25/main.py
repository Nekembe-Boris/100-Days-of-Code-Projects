import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./50_states.csv")

states = data.state

total_states = len(states)
score = 0
guessed_states = []

def locate(name, pos_x, pos_y):
    point = turtle.Turtle()
    point.hideturtle()
    point.penup()
    point.goto(pos_x, pos_y)
    point.write(arg=f"{name}", move=False, align="center", font=("Courier", 10, "bold"))


end = False

while end != True:
    answer_state = screen.textinput(f"{score}/{total_states} Correct States", "Enter the name of a U.S. State").title()
    for state in states:
        if answer_state == state:
            if state not in guessed_states:
                guessed_states.append(state)
                score += 1
            coordinates = data[data.state == answer_state]
            x_coor = int(coordinates.x)
            y_coor = int(coordinates.y)
            state_name = answer_state
            locate(answer_state, x_coor, y_coor)


turtle.mainloop()
