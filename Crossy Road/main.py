import random
import time
from turtle import Screen

from car import Car
from score import ScoreWriter
from tt import Tt

SCREEN_LEFT_EDGE = -320

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

car_list = [Car()]
tt = Tt()
score_writer = ScoreWriter()

score = 1
level_finished = False

probability_of_car_spawn = 0.01
car_speed = 5

score_writer.write_score(score)

screen.onkeypress(tt.up, "Up")
screen.onkeypress(tt.down, "Down")

while tt.not_collided(car_list):
    screen.update()
    time.sleep(0.02)

    if random.random() < probability_of_car_spawn:
        car_list.append(Car())

    for car in car_list[:]:
        car.go_left(car_speed)
        if car.xcor() < SCREEN_LEFT_EDGE:  # car left the screen: remove it
            car.hideturtle()
            car_list.remove(car)

    if not level_finished:
        if tt.check_finish():
            score += 1
            score_writer.write_score(score)
            level_finished = True
    else:
        level_finished = False
        if probability_of_car_spawn <= 0.1:
            probability_of_car_spawn += 0.03
        else:
            car_speed += 0.5
        tt.relocate()

score_writer.game_over(score)
screen.exitonclick()
