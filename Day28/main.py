from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def reset_timer():
    """This function resets the timer label, the timer and checkmarks to their default values"""
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(current_time, text="00:00")
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
    check_button.config(text="", bg=YELLOW, fg=GREEN)

    reps = 0


def start():
    """Starts the timer and automatically detects if it is working time or a long or short break"""
    global reps
    reps += 1

    working_seg = WORK_MIN * 60
    short_break_seg = SHORT_BREAK_MIN * 60
    long_break_seg = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_seg)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seg)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(working_seg)
        timer_label.config(text="CODE UP", fg=GREEN)


def count_down(count):
    """This function calculate the minutes and seconds, prints it on the screen, and adds a check mark after 2 reps"""
    global reps
    global timer

    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(current_time, text =f"{count_min} : {count_sec}")
    if count > 0:
       timer = window.after(1000, count_down, count - 1)
    else:
        start()
        check_marks = ""
        for _ in range(math.floor(reps/2)):
            check_marks += "✓"
            check_button.config(text=check_marks)



window = Tk()
window.title("The Pomodoro Timer")
window.config(padx=150, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(103, 113, image=tomato_image)
current_time = canvas.create_text(100, 125, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

check_button = Label(text="", bg=YELLOW, fg=GREEN)
check_button.grid(column=1, row=3)

window.mainloop()