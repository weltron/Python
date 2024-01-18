# This game allows a user to guess the name of the states in the US
# Each correct guess names the state based on the map provided.
# If a user exits the game using the exit keyword in the prompt box, the game produces a csv of all the state names that the user did not successfully guess

import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guess = []

while len(guess) <= 50:
    answer = screen.textinput(title=f"{len(guess)}/50 States Correct", prompt="What's another state's name").title()

    if answer == "Exit":
        missing = []
        for item in states:
            if item not in guess:
                missing.append(item)

        missing_states = pandas.DataFrame(missing)
        missing_states.to_csv("missed.csv")
        break

    if answer in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        info = data[data.state == answer]
        t.goto(int(info.x), int(info.y))
        t.write(answer)
        guess.append(answer)

