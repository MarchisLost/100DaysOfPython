from tkinter import *
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
count_id = None

# ---------------------------- TIMER RESET ------------------------------- #


def resetClock():
    global count_id
    global reps
    if count_id:
        window.after_cancel(count_id)
        canvas.itemconfig(timerText, text='00:00')
        labelCheck.config(text='')
        label1.config(text='Timer', fg=GREEN)
        reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def startClock():
    global reps
    reps += 1

    if reps % 2 != 0:
        printTime(WORK_MIN * 60)
        label1.config(text='Work', fg=GREEN)
    elif reps == 8:
        printTime(LONG_BREAK_MIN * 60)
        label1.config(text='Break', fg=RED)
    elif reps % 2 == 0 and reps != 8:
        printTime(SHORT_BREAK_MIN * 60)
        label1.config(text='Break', fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def printTime(count):
    global count_id
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count > 0:
        canvas.itemconfig(timerText, text=f'{count_min}:{count_sec}')
        count_id = window.after(1000, printTime, count - 1)
    else:
        startClock()
        marks = ''
        for _ in range(math.floor(reps/2)):
            marks += '✔'
        labelCheck.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

label1 = Label(text='Timer', bg=YELLOW, highlightthickness=0, fg=GREEN, font=(FONT_NAME, 50, 'bold'))
label1.grid(column=1, row=0)

canvas = Canvas(width=200 , height=224, bg=YELLOW, highlightthickness=0)
tomatoImg = PhotoImage(file="Day28_PomodoroApp/tomato.png")
canvas.create_image(100, 112, image=tomatoImg)
timerText = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

buttonStart = Button(text='Start', command=startClock)
buttonStart.grid(column=0, row=2)

buttonReset = Button(text='Reset', command=resetClock)
buttonReset.grid(column=2, row=2)

labelCheck = Label(text='', bg=YELLOW, highlightthickness=0, fg=GREEN, font=('bold'))
labelCheck.grid(column=1, row=3)

window.mainloop()
