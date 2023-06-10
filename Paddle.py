from turtle import Turtle

class paddle(Turtle):
    def __init__(self,xpos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(x=xpos,y=0)
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)


    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)