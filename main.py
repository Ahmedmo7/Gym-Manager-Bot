from gymbot import Bot
import tkinter as gui

window = gui.Tk()

emailPrompt = gui.Label(text="Email")
emailInput = gui.Entry()
pwdPrompt = gui.Label(text="Password")
pwdInput = gui.Entry(show="*")
locPrompt = gui.Label(text="Location")
locInput = gui.Entry()
datePrompt = gui.Label(text="Date (yyyy-mm-dd)")
dateInput = gui.Entry()
timePrompt = gui.Label(text="Time (Ex. '4:00 PM'")
timeInput = gui.Entry()

emailPrompt.pack()
emailInput.pack()
pwdPrompt.pack()
pwdInput.pack()
locPrompt.pack()
locInput.pack()
datePrompt.pack()
dateInput.pack()
timePrompt.pack()
timeInput.pack()

def run_bot():
    email = emailInput.get()
    pwd = pwdInput.get()
    loc = locInput.get()
    date = dateInput.get()
    time = timeInput.get()
    bot = Bot()
    bot.login(email, pwd)
    bot.select_club(loc)
    bot.choose_date(date)
    bot.choose_time_slot(date, time)

submit = gui.Button(text="Run Bot", command=run_bot)
submit.pack()

window.mainloop()