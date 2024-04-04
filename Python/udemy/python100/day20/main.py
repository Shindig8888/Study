import turtle
from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# turtles = []

# for i in range(0,3):
#     new_turtle = Turtle(shape = 'square')
#     new_turtle.penup()
#     new_turtle.color('white')
#     new_turtle.setpos(0-20*i, 0)
#     turtles.append(new_turtle)

snake = Snake()
# screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")










screen.exitonclick()