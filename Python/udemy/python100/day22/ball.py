from turtle import Turtle
import random
from player1 import Player1
from player2 import Player2


class Ball:
    def __init__(self):
        self.ball = self.gen_ball()
        self.direction = random.choice([15, 30, 160, 175, 195, 200, 340, 355])
        self.ball_speed = 15

    def gen_ball(self):
        ball = Turtle('square')
        ball.color('white')
        ball.pensize(10)
        ball.penup()
        return ball
    
    def ball_move(self):
        self.ball.setheading(self.direction)
        self.ball.forward(self.ball_speed)
        self.ball.setheading(90)

    def ball_bounce_wall(self):
        if self.ball.ycor() > 280 or self.ball.ycor() < -280:
            self.ball.setheading(360-self.direction)
            self.direction = self.ball.heading()
            self.ball.setheading(90)
            
 
        