
from math import cos, sin, radians
from turtle import Turtle
import random

INITIAL_SPEED = 2


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.goto(0, 0)
        self.setheading(random.randint(30, 60) + random.choice([0, 90, 180, 270]))
        self.shapesize(0.5, 0.5)
        self.move(INITIAL_SPEED)

    def move(self, speed):
        heading_angle_radians = radians(self.heading())
        x_speed = speed * cos(heading_angle_radians)
        y_speed = speed * sin(heading_angle_radians)
        self.goto(self.xcor() + x_speed, self.ycor() + y_speed)

    def wall_rebound(self):
        if self.ycor() >= 300:
            self.sety(300)
        elif self.ycor() <= -300:
            self.sety(-300)

        self.setheading(-1 * self.heading())

    def block_rebound(self, user_block, computer_block):
        if abs(self.xcor() - user_block.xcor()) < 7 and abs(self.ycor() - user_block.ycor()) < 30:
            self.setx(-440)
            self.setheading(180 - self.heading())
        elif abs(self.xcor() - computer_block.xcor()) < 7 and abs(self.ycor() - computer_block.ycor()) < 30:
            self.setx(440)
            self.setheading(180 - self.heading())
        else:
            return
