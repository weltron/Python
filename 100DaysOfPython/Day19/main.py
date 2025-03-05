from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coords = [-150, -100, -50, 0, 50, 100]
turtles = []

for index in range(6):
    new_turt = Turtle(shape="turtle")
    new_turt.color(colors[index])
    new_turt.penup()
    new_turt.goto(x=-240, y=y_coords[index])
    turtles.append(new_turt)

if bet:
    race_on = True

while race_on == True:
    for turt in turtles:
        if turt.xcor() > 230:
            race_on = False
            winner = turt.pencolor()
            if winner == bet:
                print(f"You've won!. The {winner} turtle is the winner")
            else:
                print(f"You've lost!. The {winner} turtle is the winner")


        turt.fd(random.randint(0,10))

screen.exitonclick()