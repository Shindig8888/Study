from turtle import Turtle
from car_manager import CarManager


FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.score = 1
        self.score_writer = Turtle()
        self.score_writer.hideturtle()
        self.score_writer = self.scoring()


    def scoring(self):
        self.del_score()
        score_writer = Turtle()
        score_writer.penup()
        score_writer.hideturtle()
        score_writer.goto(-270, 250)
        score_writer.write(f"LEVEL {self.score}", False, "left", FONT)
        return score_writer
    
    def del_score(self):
        self.score_writer.clear()

    def gameover(self):
        self.score_writer.goto(0,0)
        self.score_writer.write("GAMEOVER", False, "center", FONT)
        self.score_writer.goto(0,-30)
        self.score_writer.write(f"Your final socre(level) is :{self.score}", False, "center", ("Courier", 16, "normal"))
        
