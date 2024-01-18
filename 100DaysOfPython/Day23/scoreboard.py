from turtle import Turtle

FONT = ("Courier", 24, "normal")
    
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}" , align = "left", font = FONT)

    def add_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align = "center", font = FONT)
