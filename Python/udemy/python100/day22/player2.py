from turtle import Turtle
from player1 import Player1

POSITION_X = 450
SEGSIZE = 20

class Player2(Player1):
    def __init__(self) -> None:
        super().__init__()

    def gen_seg(self):
        bar_list = []
        for i in range(0,5):
            new_segment = Turtle('square')
            new_segment.penup()
            new_segment.color('white')
            new_segment.goto(POSITION_X, 20-SEGSIZE*i)
            new_segment.left(90)
            new_segment.speed('fastest')
            bar_list.append(new_segment)
        return bar_list
    
            

