import turtle as t
import random

t.colormode(255)
ron = t.Turtle()
ron.speed("fastest")
ron.penup()
ron.hideturtle()

# list of colors extracted from colorgram module
colors = [(124, 180, 210), (234, 243, 238), (198, 174, 16), (29, 119, 167), (176, 14, 45), (235, 150, 76), (236, 204, 90), (217, 124, 163), (26, 144, 74), (215, 80, 123), (9, 171, 210), (212, 61, 27), (237, 77, 45), (245, 157, 187), (64, 21, 53), (12, 183, 150), (13, 31, 75), (161, 57, 106), (76, 27, 22), (129, 209, 233), (161, 192, 164), (15, 48, 132), (102, 116, 181), (250, 159, 152), (168, 24, 19), (121, 216, 209), (3, 88, 57)]

ron.setheading(225)
ron.forward(250)
ron.setheading(0)
dots = 100

for dot_count in range(1, dots + 1):
    ron.dot(20, random.choice(colors))
    ron.forward(50)

    if dot_count % 10 == 0:
        ron.setheading(90)
        ron.forward(50)
        ron.setheading(180)
        ron.forward(500)
        ron.setheading(0)


screen = t.Screen()
screen.exitonclick()
