import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.relocate()

    def relocate(self):
        self.goto(random.randint(-14, 14) * 20, random.randint(-14, 12) * 20)
