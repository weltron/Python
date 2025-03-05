from turtle import Turtle

t = Turtle()
X_CORDS = [-40, -20, 0]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
    
class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    

    def create_snake(self):
        for index in range(3):
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.setposition(X_CORDS[index], 0)
            self.snake.append(tim)

    
    def move(self):
        for seg in range(len(self.snake)- 1, 0, -1):
            new_x = self.snake[seg - 1].xcor()
            new_y = self.snake[seg - 1].ycor()
            self.snake[seg].goto(new_x, new_y)
        self.head.forward(MOVE)
    

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    
    def down(self): 
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    
    def left(self): 
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
         
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)