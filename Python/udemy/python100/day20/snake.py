from turtle import Turtle, Screen
PART_LENGTH = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self) -> None:
        self.turtles = []
        for i in range(0,3):
            new_turtle = Turtle(shape = 'square')
            new_turtle.penup()
            new_turtle.color('white')
            new_turtle.setpos(0-PART_LENGTH*i, 0)
            self.turtles.append(new_turtle)
        self.head = self.turtles[0]
        self.screen = Screen()
        
    def move(self):
        for seg_num in range(len(self.turtles)-1, 0, -1):
            self.turtles[seg_num].goto(self.turtles[seg_num-1].pos())
        self.head.forward(PART_LENGTH)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
