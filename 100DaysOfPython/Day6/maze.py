#Lost in MAZE problem on Reeborg's world - https://reeborg.ca/reeborg.html

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
     
while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
    
   