from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

 
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True

while game_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    # Detect Collison with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    # Detect collision with right paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()
    

    # Detect if right paddle misses
    if ball.xcor() > 380:
        score.l_point()
        ball.reset_pos()

    # Detect if left paddle misses
    if ball.xcor() < -380:
        score.r_point()
        ball.reset_pos()


screen.exitonclick()
