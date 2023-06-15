1-- Copy this code and head over to Reeborg World (https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)

2-- Select the Maze challenge to see how this code directs the robot to the flag regardless of its starting position and the direction it may be facing.


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while at_goal() == False:
    if front_is_clear():
        move()
    if wall_on_right():
        turn_left()
    if front_is_clear():
        move()
    if right_is_clear():
        turn_right()