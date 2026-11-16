from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.pencolor("white")
        self.hideturtle()
        self.user_score = 0
        self.computer_score = 0
        self.show_score()

    def draw_dotted_line(self):
        self.goto(0, -290)
        self.setheading(90)
        for _ in range(20):
            self.pd()
            self.fd(10)
            self.pu()
            self.fd(20)

    def show_score(self):
        self.clear()
        self.draw_dotted_line()
        self.goto(0, 250)
        self.write(f"{self.user_score}      {self.computer_score}", True, "center", ("Arial", 20, "bold"))

    def update_score(self, player):
        if player == "user":
            self.user_score += 1
        elif player == "computer":
            self.computer_score += 1
        self.show_score()

    def check_winner(self, score_to_win):
        if self.user_score == score_to_win:
            self.clear()
            self.goto(0, 0)
            self.write("User Won", True, "center", ("Arial", 40, "bold"))
            return False

        elif self.computer_score == score_to_win:
            self.clear()
            self.goto(0, 0)
            self.write("Computer Won", True, "center", ("Arial", 40, "bold"))
            return False

        return True
