from pathlib import Path
from turtle import Screen

import pandas

from writer import Writer

BASE_DIR = Path(__file__).parent
TOTAL_STATES = 50

screen = Screen()
screen.setup(725, 491)
screen.bgpic(str(BASE_DIR / "blank_states_img.gif"))
writer = Writer()

data = pandas.read_csv(BASE_DIR / "50_states.csv")
states_list = data["state"].to_list()
guessed_states = []

while len(guessed_states) < TOTAL_STATES:
    answer = screen.textinput(f"{len(guessed_states)}/{TOTAL_STATES}", "Try to guess a state")
    if answer is None:  # window was closed or cancelled
        break

    guess = answer.strip().title()
    if guess == "Exit":
        break

    if guess in states_list and guess not in guessed_states:
        guessed_states.append(guess)
        row = data[data["state"] == guess].iloc[0]
        writer.write_state(row["state"], row["x"], row["y"])

missing_states = [state for state in states_list if state not in guessed_states]
pandas.DataFrame({"state": missing_states}).to_csv(BASE_DIR / "states_to_learn.csv", index=False)

screen.exitonclick()
