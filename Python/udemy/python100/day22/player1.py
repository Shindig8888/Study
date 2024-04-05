from turtle import Turtle

POSITION_X = -450
SEGSIZE = 20

class Player1:
    def __init__(self) -> None:
        self.bar = self.gen_seg()
        self.bar_head = self.bar[0]
        self.bar_tail = self.bar[2]
        

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

    def bar_follow(self):
        for segment_number in range(1,len(self.bar)):
            x = self.bar[segment_number-1].xcor()
            y = self.bar[segment_number-1].ycor()
            self.bar[segment_number].goto(x, y-SEGSIZE) 


    def bar_up(self):
        if self.bar_head.ycor() <280:
            self.bar_head.setheading(90)
            self.bar_head.forward(30)
        else:
            pass
    def bar_down(self):
        if self.bar_tail.ycor() > -280:
            self.bar_head.setheading(270)
            self.bar_head.forward(30)
        else:
            pass
    
    
            

