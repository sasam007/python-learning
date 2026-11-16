from turtle import Turtle
import random



class Pipes(Turtle):
    def __init__(self, difficulty):
        super().__init__()
        self.difficulty = difficulty
        if difficulty == "easy":
            self.DISTANCE_BETWEEN_PIPES = 70
        elif difficulty == "medium":
            self.DISTANCE_BETWEEN_PIPES = 50
        else:
            self.DISTANCE_BETWEEN_PIPES = 30



        self.getscreen().register_shape("pipe_down.png")
        self.getscreen().register_shape("pipe_up.png")
        self.pu()
        self.hideturtle()
        self.pipes_list = []
        self.setx(220)

    def generate_pipe_pair(self):
        self.getscreen().tracer(0)

        pipe_up = Pipes(self.difficulty)
        pipe_up.shape("pipe_up.png")
        pipe_up.showturtle()
        pipe_up.sety(random.randrange(-650, 50))
        self.pipes_list.append(pipe_up)

        pipe_down = Pipes(self.difficulty)
        pipe_down.shape("pipe_down.png")
        pipe_down.showturtle()
        pipe_down.sety(pipe_up.ycor() + self.DISTANCE_BETWEEN_PIPES + 590)
        self.pipes_list.append(pipe_down)

        self.getscreen().update()

        return

    def check_collision(self, bird):
        for element in reversed(self.pipes_list):
            element.setx(element.xcor() - 1.5)

            if element.xcor() <= -300:
                if self.pipes_list.index(element) % 2 == 1:
                    self.generate_pipe_pair()
                self.pipes_list.remove(element)
                element.hideturtle()
                del element
            elif abs(element.xcor() - bird.xcor()) < 38:
                if abs(element.ycor() - bird.ycor()) < 275:
                    return False
                elif self.pipes_list.index(element) % 2 == 1 and element.ycor() < bird.ycor():
                    return False
                elif self.pipes_list.index(element) % 2 == 0 and element.ycor() > bird.ycor():
                    return False

        return True

    def passed_pipe(self):
        for element in reversed(self.pipes_list):
            if abs(element.xcor() + 100) < 0.8:
                if self.pipes_list.index(element) % 2 == 1:
                    return True
        return None

    def reset(self):
        for element in self.pipes_list:
            element.hideturtle()
        self.pipes_list = []
