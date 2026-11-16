import time
from turtle import Turtle


class Bird(Turtle):
    GRAVITY = -0.5
    JUMP_SPEED = 8

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1.2, 1.2)
        self.pu()
        self.color("yellow")
        self.velocity = 0
        self.setx(-50)

    def fall(self):
        time.sleep(1 / 240)
        self.getscreen().tracer(0)

        if -15 < self.velocity < 15:
            self.velocity += self.GRAVITY

        if -325 < self.ycor() < 335:
            self.sety(self.ycor() + self.velocity)
        elif self.ycor() >= 335:
            self.sety(334)
        else:
            self.sety(-325)
        self.getscreen().update()

    def jump(self):
        self.velocity = self.JUMP_SPEED

    def reset(self):
        self.velocity = 0
        self.goto(-50, 0)
