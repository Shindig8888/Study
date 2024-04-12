from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
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

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text = "Timer", fg=GREEN)
    check_label.config(text='')
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN

    if reps % 8 == 0:
        input_sec = long_break_sec
        title_label.config(fg=RED, text='Break')
    elif reps % 2 == 1:
        input_sec = work_sec
        title_label.config(fg=GREEN, text='Work')
    else:
        input_sec = short_break_sec
        title_label.config(fg=PINK, text='Break')

        
    title_label.grid(column=1,row=0)

    count_down(input_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
            
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    

    if count>0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global reps
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark+= '✔'
        check_label.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

#window
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg = YELLOW)

#canvas
canvas = Canvas(width = 200, height = 224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_image)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, 'bold'))
canvas.grid(column=1,row=1)

#label "Timer"
title_label = Label(text="Timer")
title_label.config(bg = YELLOW, fg = GREEN, highlightthickness=0,  font=(FONT_NAME, 45, "bold"))
title_label.grid(column=1,row=0)

#button "Start"
start_button = Button(text="Start", highlightthickness=0, command=start_timer, width=5, height=1)
start_button.grid(column=0, row=2)

#button "Reset"
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, width=5, height=1)
reset_button.grid(column=2, row=2)

#label "✔"
check_label = Label()
check_label.config(bg = YELLOW, fg = GREEN, highlightthickness=0, font=(FONT_NAME, 15, "bold"))
check_label.grid(column=1,row=3)

window.mainloop()



















