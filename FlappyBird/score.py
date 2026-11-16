from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(0, 300)
        with open("high_score.txt", "r") as data:
            self.highscore = int(data.read())

        self.pencolor("White")
        self.score = -1
        self.increase()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

        self.score = 0
        self.update_scoreboard()
        with open("high_score.txt", "w") as stored_highscore:
            stored_highscore.write(str(self.highscore))
        return

    def increase(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {str(self.score)} Highscore = {str(self.highscore)}", False, "center",
                   ("Arial", 20, "bold"))
