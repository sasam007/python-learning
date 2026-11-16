from turtle import Turtle


class ScoreWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(0, 280)
        self.pencolor("black")

    def write_score(self, score):
        self.clear()
        self.pd()
        self.write(f"Level {score}", False, "center", ("Arial", 20, "bold"))

    def game_over(self, score):
        self.clear()
        self.goto(0, 0)
        self.pd()
        self.write("GAME OVER", False, "center", ("Arial", 40, "bold"))
        self.goto(0, -100)
        self.write(f"Level reached : {score}", False, "center", ("Arial", 20, "bold"))
