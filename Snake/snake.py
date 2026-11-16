from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.squares_list = []
        self.create_snake()
        self.snake_head = self.squares_list[0]

    def reset(self):
        for square in self.squares_list:
            square.hideturtle()
            square.goto(1000, 1000)
        self.squares_list.clear()
        self.create_snake()
        self.snake_head = self.squares_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_square = Turtle("square")
            new_square.pu()
            new_square.color("blue")
            new_square.goto(position)
            new_square.speed("fastest")
            self.squares_list.append(new_square)

    def move(self):
        for square_num in range(len(self.squares_list) - 1, 0, -1):
            new_x = self.squares_list[square_num - 1].xcor()
            new_y = self.squares_list[square_num - 1].ycor()
            self.squares_list[square_num].goto(new_x, new_y)
        self.snake_head.fd(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != 90 and self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 270 and self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def turn_left(self):
        if self.snake_head.heading() != 180 and self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def turn_right(self):
        if self.snake_head.heading() != 0 and self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def increase(self):
        new_square = Turtle("square")
        new_square.pu()
        new_square.color("blue")
        new_square.speed("fastest")
        new_square.goto(self.squares_list[-1].pos())
        self.squares_list.append(new_square)

    def in_boundaries(self):
        if self.snake_head.xcor() > 290 or self.snake_head.ycor() > 290 or self.snake_head.xcor() < -290 or self.snake_head.ycor() < -290:
            return False
        else:
            return True

    def not_touching(self):

        for square in self.squares_list[1:]:
            if self.snake_head.distance(square) < 10:
                return False
        return True
