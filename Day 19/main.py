import random
from turtle import Screen, Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
FINISH_LINE_X = 230

screen = Screen()
screen.setup(500, 400)

user_guess = screen.textinput("Bet", "Guess which turtle will win. Type in the color")
if user_guess:
    user_guess = user_guess.strip().lower()

racers = []
y = -100
for color in COLORS:
    racer = Turtle(shape="turtle")
    racer.color(color)
    racer.penup()
    racer.goto(-230, y)
    racers.append((racer, color))
    y += 40

if user_guess:
    winner = None
    while winner is None:
        for racer, color in racers:
            racer.forward(random.randint(0, 10))
            if racer.xcor() >= FINISH_LINE_X:
                winner = color
                break

    if winner == user_guess:
        print("You won")
    else:
        print(f"You lost, the winner is {winner}")

screen.exitonclick()
