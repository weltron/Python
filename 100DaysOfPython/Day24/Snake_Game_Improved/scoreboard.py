from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 25, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.update()
        self.hideturtle()

    def add(self):
        self.score += 1
        self.update()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("my_file.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", align = ALIGN, font = FONT)

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGN, font = FONT)
