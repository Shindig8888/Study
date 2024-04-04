from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.score = 0
        
    def scoreboeard(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))

    def scoreup(self):
        self.score += 1
        
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align='center', font=('Arial', 36, 'normal'))
        self.goto(0, -40)
        self.write(f"Final Score : {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))