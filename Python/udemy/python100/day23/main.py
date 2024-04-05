import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.player_move, 'space') 


game_is_on = True
car_list = []
car = CarManager()
round = 1
  
while game_is_on:
    time.sleep(0.1)
    
    if round % 10==0:
        car.car_gen()
        screen.update()
    car.car_connect()  
    screen.update()
    
    if player.level_up():
        car.level += 1
    round+=1
    

    
    
    

    


