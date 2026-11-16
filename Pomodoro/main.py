import tkinter as tk
from pathlib import Path

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = "✓"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
IMAGE_PATH = Path(__file__).parent / "tomato.png"

# ---------------------------- STATE ------------------------------- #
reps = 0
work_sessions = 0
timer_id = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, work_sessions, timer_id
    if timer_id is not None:
        window.after_cancel(timer_id)
        timer_id = None
    reps = 0
    work_sessions = 0
    canvas.itemconfig(timer_text, text=f"{WORK_MIN:02d}:00")
    title_label.config(text="Timer", fg=GREEN)
    checks_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, work_sessions
    if timer_id is not None:  # a countdown is already running
        return

    reps += 1
    if reps % 8 == 0:
        title, color, minutes = "Long Break", RED, LONG_BREAK_MIN
    elif reps % 2 == 1:
        title, color, minutes = "Work", GREEN, WORK_MIN
        work_sessions += 1
        checks_label.config(
            text=(CHECKMARK * 5 + "\n") * (work_sessions // 5) + CHECKMARK * (work_sessions % 5)
        )
    else:
        title, color, minutes = "Break", PINK, SHORT_BREAK_MIN

    title_label.config(text=title, fg=color)
    count_down(minutes * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    global timer_id
    minutes, secs = divmod(seconds, 60)
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{secs:02d}")
    if seconds > 0:
        timer_id = window.after(1000, count_down, seconds - 1)
    else:
        timer_id = None


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "normal"))
title_label.grid(row=0, column=1)

tomato_img = tk.PhotoImage(file=IMAGE_PATH)
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text=f"{WORK_MIN:02d}:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = tk.Button(text="Start", command=start_timer, width=10, fg=PINK, highlightthickness=0,
                         borderwidth=0, highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", command=reset_timer, width=10, fg=PINK, highlightthickness=0,
                         borderwidth=0, highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)

checks_label = tk.Label(highlightthickness=0, bg=YELLOW)
checks_label.grid(row=2, column=1)

window.mainloop()
