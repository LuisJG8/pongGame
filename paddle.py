from turtle import Turtle

class T_paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.setpos(position)
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_heading = self.ycor() + 30
        self.goto(self.xcor(), y=new_heading)

    def down(self):
        new_heading = self.ycor() - 30
        self.goto(self.xcor(), y=new_heading)

