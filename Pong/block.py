from turtle import Turtle

SPEED = 3


class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.7, 3)
        self.color("white")
        self.pu()
        self.setheading(90)

    def up(self):
        if self.ycor() < 300:
            self.forward(SPEED)

    def down(self):
        if self.ycor() > -300:
            self.backward(SPEED)
