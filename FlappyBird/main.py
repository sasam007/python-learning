import os
import time
from turtle import Screen

from bird import Bird
from pipe import Pipes
from score import Score

# Load images and high_score.txt relative to the script's folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

screen = Screen()
screen.setup(420, 1000)
screen.bgcolor("skyblue")
screen.getcanvas().config(highlightthickness=0, border=0)
difficulty = (screen.textinput("Difficulty", "easy, medium or hard ?") or "medium").lower()

bird = Bird()
pipes = Pipes(difficulty)
score = Score()
pipes.generate_pipe_pair()

screen.listen()
screen.onkeypress(bird.jump, "space")

while True:
    # While there is no collision, the bird falls and we count the pipes passed
    while pipes.check_collision(bird):
        bird.fall()
        if pipes.passed_pipe():
            score.increase()

    time.sleep(1)
    score.reset()
    bird.reset()
    pipes.reset()
    pipes.generate_pipe_pair()
