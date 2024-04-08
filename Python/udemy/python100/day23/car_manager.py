from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

car_list = []


class CarManager:
    def __init__(self):
        self.car_list = []
        self.level = 1
        
        

    def car_gen(self):
        car_color = random.choice(COLORS)
        car_position = random.randint(-250,250)
        new_car = Turtle("square")
        new_car.penup()
        new_car.pensize(20)
        new_car.color(f'{car_color}')
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.setpos(350, car_position)
        new_car.setheading(180)

        self.car_list.append(new_car)
            

    def car_connect(self):
        for i in range(0, len(self.car_list)-1):
            self.car_list[i].forward(STARTING_MOVE_DISTANCE+(self.level-1)*MOVE_INCREMENT)
            
    
    def kill_car(self):
        for car in self.car_list:
            if car.xcor() <= -300:
                car.hideturtle()
   




            
