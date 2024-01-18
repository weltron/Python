# Reeborg's world Hurdle problems - https://reeborg.ca/reeborg.html

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def cycle():
    turn_left()
    while wall_on_right():
        move()
    while right_is_clear(): 
        turn_right()
        move()
        turn_right()
        move()
    while front_is_clear():
        move()
    turn_left()
     
while not at_goal():
    if front_is_clear():
        move()
    else:
        cycle()