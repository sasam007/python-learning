import random
from turtle import Screen, Turtle

tt = Turtle()
tt.speed("fastest")
num_of_circles = int(input("How many circles do you want in your spirograph? "))

for _ in range(num_of_circles):
    tt.color(random.random(), random.random(), random.random())
    tt.circle(100)
    tt.right(360 / num_of_circles)

screen = Screen()
screen.exitonclick()
