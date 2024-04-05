from turtle import Turtle, Screen
from player1 import Player1
from player2 import Player2
from interface import Interface
from ball import Ball
import time

screen2 = Screen()
screen1 = Screen()
screen1.tracer(0)
player1 = Player1()
player2 = Player2()

screen1.bgcolor('black')
screen1.setup(1000, 600)

screen1.listen()
screen1.onkeypress(fun = player1.bar_up, key = 'w')
screen1.onkeypress(fun = player1.bar_down, key = 's')
screen2.listen()
screen2.onkeypress(fun = player2.bar_up, key = 'Up')
screen2.onkeypress(fun = player2.bar_down, key = 'Down')



interface = Interface()
# interface.lining()

interface.scoring1()
interface.scoring2()

is_end = False
while is_end == False:
    ball = Ball()
    game_speed = 0.1
    while True:
        time.sleep(game_speed)
        screen1.update()
        ball.ball_move()

        ball.ball_bounce_wall()
        player1.bar_follow()
        player2.bar_follow()
        

        for segment1 in player1.bar:
            if ball.ball.distance(segment1) < 10:
                ball.ball.setheading((540-ball.direction)%360)
                ball.direction = ball.ball.heading()
                ball.ball.setheading(90)
                game_speed *= 0.9

        for segment2 in player2.bar:
            if ball.ball.distance(segment2) < 20:
                ball.ball.setheading((540-ball.direction)%360) 
                ball.direction = ball.ball.heading()
                ball.ball.setheading(90)
                game_speed *= 0.9


        score_p1 = 0
        score_p2 = 0
        if ball.ball.xcor() > 500:
            interface.score_p1 += 1
            interface.scoring1()
            ball.ball.hideturtle()
            break
        
        if ball.ball.xcor() <-500:
            interface.score_p2 += 1
            interface.scoring2()
            ball.ball.hideturtle()
            break
    continue
    

    # for segment2 in player2.bar:
    #     if ball.ball.distance(segment2) < 20:
    #         if ball.ball.heading() >= 270:
    #             ball.ball.setheading(540- ball.direction)
    #             ball.direction = ball.ball.heading()
    #             ball.ball.setheading(90)
    #     elif ball.ball.distance(segment2) < 20:
    #         if ball.ball.heading() >= 0:
    #             ball.ball.setheading(180- ball.direction)
    #             ball.direction = ball.ball.heading()
    #             ball.ball.setheading(90)

    
    







screen1.exitonclick()