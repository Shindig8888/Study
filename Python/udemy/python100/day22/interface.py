from turtle import Turtle

class Interface:
    def __init__(self) -> None:
        self.score_p1 = 0
        self.score_p2 = 0
        self.line = self.lining()
        self.writer_1 = self.gen_turtle()
        self.writer_2 = self.gen_turtle()
        
        
    def gen_turtle(self):
        score_write = Turtle()
        score_write.clear
        score_write = Turtle()
        score_write.color("white")
        score_write.hideturtle()
        score_write.penup()
        score_write.goto(0, 200)
        return score_write

    def scoring1(self):
        self.writer_1.clear()
        self.writer_1.write(f"   {self.score_p1}   ", move = False, align = 'right', font = ("Courier", 50, "normal"))
    def scoring2(self):
        self.writer_2.clear()
        self.writer_2.write(f"   {self.score_p2}   ", move = False, align = 'left', font = ("Courier", 50, "normal"))

    
    
    def lining(self):
        line = Turtle()
        line.hideturtle()
        line.color('white')
        line.pensize(10)
        line.penup()
        line.goto(0,-300)
        line.setheading(90)
        while line.ycor() < 300:
            line.forward(20)
            line.penup()
            line.forward(40)
            line.pendown()
            