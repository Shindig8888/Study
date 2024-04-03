import turtle
from turtle import Turtle, Screen
import random
# import colorgram

# def rgb_fying(colorgram_v) -> tuple:
#     result_r = colorgram_v.rgb.r
#     result_g = colorgram_v.rgb.g
#     result_b = colorgram_v.rgb.b
#     return (result_r, result_g, result_b)


# def color_tuple_list(extracted_list: list) -> list:
#     return_list = []
#     for i in colors:
#         color_tuple = rgb_fying(i)
#         return_list.append(color_tuple)
#     return return_list


# colors = colorgram.extract('image.jpg', 84)

rgb_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]
print(rgb_list)

turtle.colormode(255)

timmy = turtle.Turtle()

timmy.pos()
timmy.penup()
timmy.speed('fastest')

for i in range(0,10):
    timmy.teleport(-315, -315+i*70)
    for j in range(1,11):
        ran_color = random.choice(rgb_list)
        timmy.dot(20, ran_color)
        if j != 10:
            timmy.forward(70)

timmy.hideturtle()

screen = Screen()
screen.screensize(650, 650)
screen.screensize()

screen.exitonclick()