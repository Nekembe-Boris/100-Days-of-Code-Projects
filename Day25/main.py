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
    """This function creates a new turtle, gets the name of the state and sends it to its corresponding x and y cooordinates"""
    point = turtle.Turtle()
    point.hideturtle()
    point.penup()
    point.goto(pos_x, pos_y)
    point.write(arg=f"{name}", move=False, align="center", font=("Courier", 10, "bold"))
        #alternative to the above line could be --> point.write(state.state.item())


end = False

while end != True:
    answer_state = screen.textinput(f"{score}/{total_states} Correct States", "Enter the name of a U.S. State").title()
    for state in states:
        if answer_state == state:
            #To avoid double counting of states and scores
            if state not in guessed_states:
                guessed_states.append(state)
                score += 1
            coordinates = data[data.state == answer_state]
            x_coor = int(coordinates.x)
            y_coor = int(coordinates.y)
            state_name = answer_state
            locate(answer_state, x_coor, y_coor)

    if answer_state == "Exit":
        missed_states = [state_name for state_name in data.state if state_name != guessed_states]
        end = True

learn_dict = {
    "States": missed_states
}

data_f = pandas.DataFrame(learn_dict)
data_f.to_csv("States_to_learn.csv")

screen.exitonclick()

