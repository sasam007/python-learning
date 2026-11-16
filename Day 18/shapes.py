import random
from turtle import Screen, Turtle

tt = Turtle()
sides = 3

while sides < 11:
    tt.pencolor(random.random(), random.random(), random.random())
    for i in range(sides):
        tt.fd(100)
        tt.right(360 / sides)
    sides += 1


screen = Screen()
screen.exitonclick()
