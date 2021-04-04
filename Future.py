from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import sys
import random

run = True
morale = 50
money = 50
employment = 50
resources = 50
root = Tk()
root.title('Crazy Future Business')
root.geometry('500x500')
root.configure(bg='black')
robots = ['Jeremy', 'Anna', 'Bob', 'Sophia', 'William', 'Liam']
Scenarios = ['Can I hack the computer system?', 'Sir, we have to cancel the deal because it\'s a scam']


def nex():
    while True:
        global morale, money, employment, resources, Scenarios, q
        top = Toplevel()
        break


def ding():
    global q, morale, money, employment, resources
    if q == 'Can I hack the computer system?':
        messagebox.showinfo('Your Choice',
                            "Because you let " + q + " hack your company's computer system, your profit got decreased by 10, so you lost 10 employees, 10 morality, 10 resources, and 10 coins")
        morale = morale - 10
        money = money - 10
        employment = employment - 10
        resources = resources - 10


def errnn():
    global q, morale, money, employment, resources
    if q == 'Can I hack the computer system?':
        messagebox.showinfo('Your Choice',
                            "Because you prevented " + q + " hack your company's computer system, your profit got increased by 10, so you earned 10 employees, 10 morality, 10 resources, and 10 coins")
        morale = morale + 10
        money = money + 10
        employment = employment + 10
        resources = resources + 10
        nex()


small = Font(
    family='Times',
    size=15,
    weight='bold',
    slant='italic'
)

bigF = Font(
    family='Times',
    size=70,
    weight='bold',
    slant='italic'
)

qf = Font(
    family='Helvetica',
    slant='italic'
)

bigFont = Font(
    family='Times',
    size=45,
    weight='bold',
    slant='italic'
)


def yep():
    global morale, money, employment, resources, Scenarios, q
    top = Toplevel()
    top.configure(bg='blue')
    top.geometry('450x450')
    frame = LabelFrame(top, text="Resources", padx=5, pady=5)
    frame.pack(padx=10, pady=10)
    questions = Label(frame, text='morale: ' + str(morale))
    questions.pack()
    cash = Label(frame, text='money: ' + str(morale))
    cash.pack()
    employ = Label(frame, text='workers: ' + str(employment))
    employ.pack()
    materials = Label(frame, text='resources: ' + str(resources))
    materials.pack()
    Label(top, text='Scenario:').pack()
    Label(top, text=dude + ' asked ' + '"' + q + '"').pack()
    Button(top, text='Yes', fg='black', bg='green', font=bigF, command=ding).pack(padx=5, pady=5)
    Button(top, text='No', fg='black', bg='green', font=bigF, command=errnn).pack(padx=5, pady=10)


q = Scenarios[random.randint(0, len(Scenarios) - 1)]
dude = robots[random.randint(0, len(robots) - 1)]


def ins():
    top = Toplevel()
    top.title('Instructions')
    top.geometry('500x300')
    top.configure(bg='white')
    Label(top,
          text='HOW TO PLAY',
          font=bigF
          ).grid(row=0, column=0)


Label(top,
      text='''
In this game, there are 4 different parts:
morale, money, employment, and resources.
At default, you start with 50 for each.
The goal for this game is to keep your business as long as possible.
If any of your resources dropped to 0, then the game is over.
Random robot employees will come to you make different requests.
You have to decide whether or not you should let them do it.
If you agree with the employee, click Yes button.
If you disagree with the employee, click the No button.
GOOD LUCK!
''',
      font=small
      ).grid(row=5, column=0)


def out():
    response = messagebox.askokcancel('Leave', 'Are you sure you want to leave?')
    if response == True:
        root.destroy()
        sys.exit()


Button(
    root,
    text='How to Play',
    bg='red',
    fg='green',
    command=ins,
    padx=50,
    pady=50,
    font=bigF
).grid(row=10, column=1)

out = Button(
    root,
    text='Quit',
    command=out,
    fg='black',
    bg='red',
    font=qf
).grid(row=0, column=0)

Button(
    root,
    text='Start',
    padx=50,
    pady=50,
    font=bigF,
    command=yep
).grid(row=11, column=1)

Label(
    root,
    text='Crazy Future Business',
    fg='blue',
    bg='black',
    font=bigFont
).grid(row=1, column=1)

root.mainloop()

