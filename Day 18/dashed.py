from turtle import Turtle, Screen

tt = Turtle()
screen = Screen()


for i in range(10):
    tt.pd()
    tt.fd(10)
    tt.pu()
    tt.fd(10)


screen.exitonclick()