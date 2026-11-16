from turtle import Screen, Turtle

tt = Turtle()
tt.shape("turtle")
tt.color("blue")


def square():
    for _ in range(4):
        tt.forward(100)
        tt.right(90)


square()

screen = Screen()
screen.exitonclick()
