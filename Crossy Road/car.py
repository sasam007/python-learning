import random
from turtle import Turtle, colormode


class Car(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("square")
        self.pu()
        self.setheading(180)
        self.shapesize(1, 3)
        colormode(255)
        self.color(random.randrange(0, 240), random.randrange(0, 240), random.randrange(0, 240))
        self.goto(300, random.randint(-260, 280))

    def go_left(self, speed):
        self.setx(self.xcor() - speed)
