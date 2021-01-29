from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
# Colors and font
BG_COLOR = "#351f39"
FG_COLOR = "#827397"
GREEN = "#61b15a"
WHITE = "#ffffff"
FONT_NAME = "Courier"

# Timer duration
LONG_BREAK_MIN = 20
SHORT_BREAK_MIN = 5
WORK_MIN = 25

# Checkmark constants
CHECKMARK = "✔"

# Sequence will start at index 1
TIMER_SEQ = [LONG_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, WORK_MIN]
TIMER_SEQ_TEXT = ["L. Break", "Work", "Break", "Work", "Break", "Work"]
SEQ_START = 1

# Globals variables
reps = 0
timer = None


def timer_reset():
    global reps, timer

    # If active timer, cancel timer callback
    if timer:
        window.after_cancel(timer)
        timer = None

    # Reset rep state
    reps = 0

    # Update labels
    canvas.itemconfig(timer_count_down_text, text="00:00")
    lbl_checks["text"] = ""
    lbl_timer["text"] = "Timer"

    # Set button state
    btn_start["state"] = NORMAL
    btn_reset["state"] = DISABLED


def timer_start():
    global reps, timer

    # After completing all pomodoro cycles, set reps to the sequence start so the number doesn't grow to infinity. =)
    reps = reps + 1 if reps != len(TIMER_SEQ) else SEQ_START

    # Select next rep minutes
    index = reps % len(TIMER_SEQ)
    update_timer_label(TIMER_SEQ_TEXT[index])
    minutes = TIMER_SEQ[index]

    # Set button state
    btn_start["state"] = DISABLED
    btn_reset["state"] = NORMAL

    # If timer sequence cycles is restarting, set checks label to nothing 
    if index == SEQ_START:
        lbl_checks["text"] = ""

    # Start timer count down in seconds
    timer_count_down(minutes * 60)


def timer_count_down(count):
    global reps, timer

    # Convert count to minutes and seconds
    seconds = count % 60
    minutes = count // 60
    canvas.itemconfig(timer_count_down_text, text=f"{minutes:02d}:{seconds:02d}")

    # Set callback, if count is greater than 0
    if count > 0:
        timer = window.after(1000, timer_count_down, count - 1)
    else:
        # Timer has expired
        timer = None

        # On every work rep add a checkmark
        # Work reps are odd numbers
        if reps % 2:
            update_check_mark_label()

        # Start the next timer cycle
        timer_start()


def update_check_mark_label():
    lbl_checks["text"] += CHECKMARK


def update_timer_label(text: str) -> None:
    lbl_timer["text"] = text


if __name__ == '__main__':
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=BG_COLOR)

    # Setup canvas for the tomato image
    canvas = Canvas(width=200, height=224, bg=BG_COLOR, highlightthickness=0)
    image = PhotoImage(file="tomato.png")
    canvas.create_image(100, 110, image=image)

    # Setup time text
    timer_count_down_text = canvas.create_text(103, 130, text="00:00", fill=WHITE, font=(FONT_NAME, 24, "bold"))

    # Setup labels
    lbl_timer = Label(text="Timer", bg=BG_COLOR, fg=FG_COLOR, font=(FONT_NAME, 36, "bold"))
    lbl_checks = Label(text="", bg=BG_COLOR, fg=GREEN, font=(FONT_NAME, 24, "bold"))

    # Setup buttons
    btn_start = Button(text="Start", command=timer_start, font=(FONT_NAME, 12, "bold"), highlightthickness=0)
    btn_reset = Button(text="reset", command=timer_reset,  font=(FONT_NAME, 12, "bold"), highlightthickness=0, 
                        state=DISABLED)

    # Setup GUI grid layout
    lbl_timer.grid(row=0, column=1)
    canvas.grid(row=1, column=1)
    btn_start.grid(row=2, column=0)
    btn_reset.grid(row=2, column=2)
    lbl_checks.grid(row=3, column=1)

    window.mainloop()
