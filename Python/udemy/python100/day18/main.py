from turtle import Turtle, Screen
import random
import turtle

timmy = Turtle()
timmy.shape("turtle")
timmy.color('purple')

#///
# for i in range(15):
#     timmy.forward(10)
#     x = 20*i
#     timmy.teleport(x,0)

# for i in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#///
# pen_color = ['red', 'blue', 'orange', 'purple', 'yellow', 'green', 'wheat', 'DarkOrchid']
# for i in range(3,11):
#     n = i
#     while n > 0:
#         timmy.color(pen_color[i-3])
#         timmy.pencolor(pen_color[i-3])
#         n -= 1
#         timmy.right(180-180*(i-2)/i)
#         timmy.forward(100)
#///


# def random_color():
#     color_r = random.randint(0,255)
#     color_g = random.randint(0,255)
#     color_b = random.randint(0,255)
#     return (color_r, color_g, color_b)

# direction_angle = [0, 90, 180, 270]

# timmy.pensize(5)
# timmy.speed(150)
# turtle.colormode(255)
# for _ in range(501):
#     timmy.pencolor(random_color())
#     timmy.setheading(random.choice(direction_angle))
#     timmy.forward(20)
# ///

# def random_color():
#     color_r = random.randint(0,255)
#     color_g = random.randint(0,255)
#     color_b = random.randint(0,255)
#     return (color_r, color_g, color_b)
# timmy.speed(150)
# turtle.colormode(255)
# n = 0
# turn_angle = 5
# while n!= 360/turn_angle:
#     timmy.pencolor(random_color())
#     timmy.circle(100)
#     timmy.right(turn_angle)
#     n+=1







screen = Screen()
screen.exitonclick()

