import random
import turtle
from turtle import Screen, Turtle

turtle.colormode(255)
tt = Turtle()
tt.pensize(5)
tt.speed("fastest")

for _ in range(300):
    tt.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tt.fd(10)
    tt.right(90 * random.randint(0, 3))

screen = Screen()
screen.exitonclick()
