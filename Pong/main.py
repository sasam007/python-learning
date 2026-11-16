import time
from turtle import Screen

from ball import Ball
from computer_block import ComputerBlock
from score import Score
from user_block import UserBlock

screen = Screen()
screen.setup(1000, 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("PONG")
score_to_win = int(screen.numinput("SCORE TO WIN", "What should be the score to win : ") or 5)
difficulty = (screen.textinput("Difficulty", "easy, medium or hard ?") or "easy").lower()
screen.listen()

ball = Ball()
computer_block = ComputerBlock(difficulty)
user_block = UserBlock()
score = Score()

INITIAL_SPEED = 2
speed = INITIAL_SPEED

game_is_on = True
up_pressed = False
down_pressed = False


def press_up():
    global up_pressed
    up_pressed = True


def release_up():
    global up_pressed
    up_pressed = False


def press_down():
    global down_pressed
    down_pressed = True


def release_down():
    global down_pressed
    down_pressed = False


screen.onkeypress(press_up, "Up")
screen.onkeyrelease(release_up, "Up")
screen.onkeypress(press_down, "Down")
screen.onkeyrelease(release_down, "Down")

while game_is_on:
    time.sleep(0.005)
    screen.update()
    computer_block.follow_ball(ball.ycor())
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.wall_rebound()

    if ball.xcor() > 500 or ball.xcor() < -500:
        if ball.xcor() > 500:
            score.update_score("user")
        else:
            score.update_score("computer")
        game_is_on = score.check_winner(score_to_win)
        ball.hideturtle()
        ball = Ball()
        speed = INITIAL_SPEED

    ball.block_rebound(user_block, computer_block)
    if up_pressed:
        user_block.up()
    if down_pressed:
        user_block.down()

    ball.move(speed)
    speed += 0.0002

screen.exitonclick()
