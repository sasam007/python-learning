from turtle import Turtle


class Tt(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.pu()
        self.setheading(90)
        self.goto(0, -280)

    def up(self):
        self.setheading(90)
        self.sety(self.ycor() + 20)

    def down(self):
        self.setheading(270)
        self.sety(self.ycor() - 20)

    def relocate(self):

        self.goto(0, -280)

    def not_collided(self, car_list):
        for car in car_list:
            car_x = car.xcor()
            car_y = car.ycor()
            if abs(self.ycor() - car_y) <= 20:
                if abs(self.xcor() - car_x) <= 30:
                    return False
        return True

    def check_finish(self):
        if self.ycor() >= 300:
            self.goto(0, -280)
            return True
        else:
            return False
