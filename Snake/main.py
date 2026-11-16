import os
import time
from turtle import Screen

from food import Food
from score import Score
from snake import Snake

# Load high_score.txt relative to the script's folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

score = Score()
snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.turn_left, "Left")
screen.onkeypress(snake.turn_right, "Right")

while True:
    while snake.in_boundaries() and snake.not_touching():
        time.sleep(0.1)
        screen.update()
        if snake.snake_head.distance(food) <= 15:
            snake.increase()
            food.relocate()
            score.increase()

        snake.move()
    snake.reset()
    score.reset()
    food.relocate()
