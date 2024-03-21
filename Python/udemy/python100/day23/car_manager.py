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
        car_position = random.randint(-250,280)
        for i in range(0,4):
            new_car = Turtle("square")
            new_car.penup()
            new_car.pensize(20)
            new_car.color(f'{car_color}')
            new_car.setpos(350+20*i, car_position)
            new_car.setheading(180)

            self.car_list.append(new_car)
            

    def car_connect(self):
        for i in range(0, len(self.car_list)-1, 4):
            self.car_list[i].forward(STARTING_MOVE_DISTANCE+(self.level-1)*MOVE_INCREMENT)
       
        for i in range (3, len(self.car_list)-1, 4):
            y = self.car_list[i].ycor()
            self.car_list[i-2].goto(self.car_list[i-3].xcor()+20, y)
            self.car_list[i-1].goto(self.car_list[i-2].xcor()+20, y)
            self.car_list[i].goto(self.car_list[i-1].xcor()+20, y)
            
    
    def kill_car(self):
        for car in self.car_list:
            if car.xcor() <= -300:
                car.hideturtle()
   




            
