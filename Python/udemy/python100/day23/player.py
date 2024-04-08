from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.player = self.gen_player()
        
    def gen_player(self):    
        player = Turtle('turtle')
        player.setheading(90)
        player.penup()
        player.color('Purple')
        player.goto(STARTING_POSITION[0], STARTING_POSITION[1])
        return player

    def player_move(self):
        self.player.setheading(90)
        self.player.forward(MOVE_DISTANCE)
    def player_back(self):
        self.player.setheading(270)
        self.player.forward(MOVE_DISTANCE)

    def level_up(self):
        if self.player.ycor() == FINISH_LINE_Y:
            self.player.goto(STARTING_POSITION[0], STARTING_POSITION[1])
            return True

    def on_hit(self):
        from car_manager import CarManager
        cars = CarManager().car_list[::]
        print(cars)
        for car in cars:
            if self.player.distance(car.position()) <20:
                return True