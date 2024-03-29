from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 25, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.update()
        self.hideturtle()

    def add(self):
        self.score += 1
        self.clear()
        self.update()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align = ALIGN, font = FONT)

    def update(self):
        self.write(f"Score: {self.score}", align = ALIGN, font = FONT)