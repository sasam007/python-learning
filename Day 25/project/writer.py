from turtle import Turtle


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("black")
        self.pu()

    def write_state(self, state_name, xcor, ycor):
        self.goto(xcor, ycor)
        self.pd()
        self.write(state_name, False, "center", ("Arial", 15, "bold"))
        self.pu()