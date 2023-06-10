from turtle import Turtle

class score(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(pos,270)
        self.count=0
        self.write(arg="{}".format(self.count),font=('Arial',20,'normal'))
        
    def rewrite(self):
        self.clear()
        self.write(arg="{}".format(self.count),font=('Arial',14,'normal'))