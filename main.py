import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
# PINK = "#e2979c"
# RED = "#e7305b"
# GREEN = "#9bdeac"
YELLOW = "#FFB000"
FONT_NAME = "Courier"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
reps = 0
tick = 0
tmr = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_tmr():
    global tick, reps
    w.after_cancel(tmr)
    canvas.itemconfig(timer_txt, text=f"00:00")
    lbl2.config(text=f"")
    tick = 0
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_tmr():
    global reps
    print(reps)
    reps += 1
    s = 60
    WORK_MIN = 25
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 20
    if reps % 8 == 0:
        reps = 0
        lbl.config(text=f"rest{LONG_BREAK_MIN}", fg="blue")
        count_down(LONG_BREAK_MIN, s)
    elif reps % 2 == 0:
        lbl.config(text="Break", fg="red")
        count_down(SHORT_BREAK_MIN, s)
    else:
        lbl.config(text="Work", fg="green")
        count_down(WORK_MIN, s)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(m, s):
    count_min = m
    count_sec = s
    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count_sec > 0:
        global tmr
        tmr = w.after(1000, count_down, m, s - 1)
    elif count_sec == 0:
        if m != 0:
            m -= 1
            s = 60
            count_down(m, s)
        elif m == 0:
            canvas.itemconfig(timer_txt, text=f"00:00")
            if reps % 2 == 0:
                global tick
                tick += 1
                lbl2.config(text=f"{'✔' * tick}")
            start_tmr()


# ---------------------------- UI SETUP ------------------------------- #
w = tkinter.Tk()
w.title("Pomodoro Technique !!!")
w.minsize(width=400, height=400)
w.config(bg=YELLOW)

lbl = tkinter.Label(text="Timer", font=(FONT_NAME, 30, "bold"), foreground="Green", bg=YELLOW)
lbl.place(x=150, y=12)

canvas = tkinter.Canvas(width=210, height=224, background=YELLOW, highlightthickness=0)
tomato_ing = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_ing)
timer_txt = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.place(x=100, y=50)

start_btn = tkinter.Button(text="Start", width=4, height=1, background="white", command=start_tmr)
start_btn.place(x=100, y=300)

lbl2 = tkinter.Label(foreground="Green", bg=YELLOW)
lbl2.place(x=200, y=300)

reset_btn = tkinter.Button(text="reset", width=4, height=1, background="white", command=reset_tmr)
reset_btn.place(x=250, y=300)

w.mainloop()
