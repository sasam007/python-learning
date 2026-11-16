import random
from turtle import Screen, Turtle

import colorgram

colors = colorgram.extract("hirst.jpg", 25)
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
# Remove the first 4 extracted colors (often the background of the image)
del rgb_colors[0:4]

screen = Screen()
screen.colormode(255)

tt = Turtle()
tt.speed("fastest")
tt.hideturtle()
tt.penup()
tt.teleport(-200, -200)

y = -170
size = random.randint(3, 20)
for _ in range(size):
    for _ in range(size):
        tt.forward(30)
        tt.dot(15, random.choice(rgb_colors))
    tt.teleport(-200, y)
    y += 30

screen.exitonclick()
