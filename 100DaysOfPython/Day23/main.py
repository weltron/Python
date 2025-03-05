import time
from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.title("The Turtle Crossing")
screen.tracer(0)

player = Player()
cars = Car()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    

    # Detect turtle collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_on  = False
            score.game_over()

    # Detect crossing finish line
    if player.at_finish():
        player.go_to_start()
        cars.level_up()
        score.add_level()

screen.exitonclick()
