from turtle import Turtle

t = Turtle()
START = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
    
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    

    def create_snake(self):
        for index in START:
            self.add_segment(index)
            
    def add_segment(self, position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for seg in range(len(self.segments)- 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
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

    def reset(self):
        for seg in self.segments:
            seg.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
