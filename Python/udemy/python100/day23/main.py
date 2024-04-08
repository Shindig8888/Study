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
screen.onkeypress(player.player_move, 'Up') 
screen.onkeypress(player.player_back, 'Down') 
scoreboard = Scoreboard()

game_is_on = True
car_list = []
car = CarManager()
round = 1
  
while game_is_on:
    time.sleep(0.1)
    
    if round % 10==0:
        car.car_gen()
    car.car_connect()  
    car.kill_car()

    for cars in car.car_list:
        if player.player.distance(cars.position()) < 20:
            game_is_on = False 
            scoreboard.gameover() 
    
    if player.level_up():
        scoreboard.del_score()
        car.level += 1
        scoreboard.update_scoreboard()

    screen.update()


    round+=1
    
screen.exitonclick()

    
    
    

    


