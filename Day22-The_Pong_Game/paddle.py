from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.penup()
        self.goto(xcor, ycor)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)