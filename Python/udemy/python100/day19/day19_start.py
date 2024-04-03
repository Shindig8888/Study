import turtle
import random
from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def move_forwars():
#     tim.forward(10)
# def move_backwards():
#     tim.backward(10)
# def counter_clockwise():
#     tim.left(10)
# def clockwise():
#     tim.right(10)
# def clear_drawing():
#     tim.reset()



# screen.listen()
# screen.onkey(key="w", fun=move_forwars) #함수에 함수를 넣을 경우 ()를 붙이지 않음. class의 승계와 같음
# screen.onkey(key="s", fun=move_backwards) 
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clockwise) 
# screen.onkey(key="c", fun=clear_drawing) 

screen = Screen()
screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title = 'Make your bet!', prompt = 'Which turtle will win the race? Enter a color: ')
print(user_bet)

colors = ['red','yellow', 'orange', 'blue', 'green', 'purple']
all_turtles = []

is_race_on = False

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-175+turtle_index*70)
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        randnum = random.randint(0,6)
        turtles.forward(randnum)
        if turtles.xcor() > 230:
            is_race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

    
# t1 = Turtle(shape = 'turtle')
# t1.color(colors.pop())
# t2 = Turtle(shape = 'turtle')
# t2.color(colors.pop())
# t3 = Turtle(shape = 'turtle')
# t1.color(colors.pop())
# t4 = Turtle(shape = 'turtle')
# t4.color(colors.pop())
# t5 = Turtle(shape = 'turtle')
# t5.color(colors.pop())
# t6 = Turtle(shape = 'turtle')
# t6.color(colors.pop())

# for 

# t1.goto(-230,175)
# t2.goto(-230,105)
# t3.goto(-230,35)
# t4.goto(-230,-35)
# t5.goto(-230,-105)
# t6.goto(-230,-175)

screen.exitonclick()