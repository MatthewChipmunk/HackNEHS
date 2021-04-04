from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import sys
import random

# Variables
morale, money, employment, materials = 50, 50, 50, 50
days = 1
# Robot names & Scenarios

bots = ['Jeremy', 'Bill', 'Ashley', 'Jill', 'William', 'Amy']
Scenarios = ['Can I hack the computer system?',
             'Give me 40 bucks or else, I will take 30 materials and bucks',
             'Should we set a base at Mars?',
             'Can I invite some idiots to your company?',
             'Can we have to cancel our event because it will crash and cause a power surge']

dude = bots[random.randint(0, len(bots) - 1)]
queue = Scenarios[random.randint(0, len(Scenarios) - 1)]


# Yes & No
def yep():
    global morale, money, employment, materials, queue, game, days
    days += 1
    if queue == 'Can I hack the computer system?':
        messagebox.showinfo('', 'Because you let this act happen, you lost 10 dollars, 10 morale, 10 employment, '
                                'and 10 materials')
        money -= 10
        morale -= 10
        materials -= 10
        employment -= 10
    elif queue == 'Give me 40 bucks or else, I will take 30 materials and bucks':
        messagebox.showinfo('', 'Because you agreed, you lost 40 dollars')
        money -= 40

    elif queue == 'Should we set a base at Mars?':
        messagebox.showinfo('', 'When your went to Mars, aliens arrived and killed all of your crews, you lost 10 '
                                'morale, 15 employments, 10 dollars, and 30 materials')
        morale -= 10
        employment -= 15
        money -= 10
        materials -= 30

    elif queue == 'Can I invite some idiots to your company?':
        messagebox.showinfo('', 'Your choice led to losing 10 materials and 10 dollars but gained 10 employments')
        money -= 10
        materials -= 10
        employment += 10

    elif queue == 'Can we have to cancel our event because it will crash and cause a power surge':
        messagebox.showinfo('', 'Your choice decreased the morale by 10')
        morale -= 10

    start()


def nope():
    global morale, money, employment, materials, queue, game, days
    days += 1
    if queue == 'Can I hack the computer system?':
        messagebox.showinfo('', 'Because you prevented this act, you earned 10 dollars, 10 morale, and 10 materials')
        money += 10
        morale += 10
        materials += 10

    elif queue == 'Give me 40 bucks or else, I will take 30 materials and bucks':
        messagebox.showinfo('', 'Because you disagreed, you lost 30 dollars and 30 materials')
        money -= 30
        materials -= 30

    elif queue == 'Should we set a base at Mars?':
        messagebox.showinfo('', 'Since you rejected the offer, you never know what happened, so you lost 10 morale')
        morale -= 10

    elif queue == 'Can I invite some idiots to your company?':
        messagebox.showinfo('', 'Your choice led to a increase of 10 dollars')
        money += 10

    elif queue == 'Can we have to cancel our event because it will crash and cause a power surge':
        messagebox.showinfo('', 'Your choice decreased the morale by 15, material by 10, and money by 10')
        morale -= 15
        money -= 10
        materials -= 10
    #    game.quit()

    start()


# Main Page
root = Tk()

root.configure(bg='black')
root.geometry('500x500')
root.title('Crazy Future Business')

bigFont = Font(
    family='Times',
    size=50,
    weight='bold',
    slant='italic'
)

italy = Font(
    family='Times',
    weight='bold',
    slant='italic',
    size='15'
)

but = Font(
    family='Times',
    weight='bold',
    slant='italic',
    size='75'
)

slight = Font(
    family='Times',
    weight='bold',
    slant='italic',
    size='30'
)


def out():
    response = messagebox.askokcancel('Leave', 'Are you sure you want to leave?')
    if response:
        root.destroy()
        sys.exit()


def how():
    top = Toplevel()
    top.geometry('500x400')
    top.title('How To Play')
    top.configure(bg='black')
    Label(top, text='HOW TO PLAY', font=bigFont, bg='black', fg='blue').pack()
    Label(top, text='''In this game, there are 4 different resources:
morale, money, employment, and materials.
At default, you start with 50 for each.
The goal for this game is to keep your business as long as possible.
If any of your resources dropped to 0, then the game is over.
Random robot employees will come to you make different requests.
You have to decide whether or not you should let them do it.
If you agree with the employee, click Yes button.
If you disagree with the employee, click the No button.
GOOD LUCK! ''',
          bg='black',
          fg='red',
          font=italy).pack()


game = 0


# Game Structure
def start():
    global morale, money, employment, materials, dude, queue, game
    if materials <= 0:
        messagebox.showinfo('', 'BECAUSE YOU LOST MATERIALS, YOU COMPANY CANNOT KEEP UP WITH UP TO DATE TECHNOLOGY, '
                                'SO YOUR COMPANY WENT DOWN')
        messagebox.showinfo('', 'YOUR COMPANY SURVIVED FOR '+str(days-1)+' DAYS')
        root.destroy()
        sys.exit()
    elif money <= 0:
        messagebox.showinfo('', 'BECAUSE YOU WENT BROKE, EVERYBODY GOT LAID OFF AND YOUR COMPANY IS FINISHED')
        messagebox.showinfo('', 'YOUR COMPANY SURVIVED FOR '+str(days-1)+' DAYS')
        root.destroy()
        sys.exit()
    elif morale <= 0:
        messagebox.showinfo('', 'BECAUSE YOU TREATED YOUR WORKERS CRUELLY, THEY WENT TO A DIFFERENT COMPANY')
        messagebox.showinfo('', 'YOUR COMPANY SURVIVED FOR '+str(days-1)+' DAYS')
        root.destroy()
        sys.exit()
    elif employment <= 0:
        messagebox.showinfo('', 'BECAUSE YOU LOST PEOPLE, NO ONE IS RUNNING YOUR COMPANY')
        messagebox.showinfo('', 'YOUR COMPANY SURVIVED FOR '+str(days-1)+' DAYS')
        root.destroy()
        sys.exit()
    game = Toplevel()
    dude = bots[random.randint(0, len(bots) - 1)]
    queue = Scenarios[random.randint(0, len(Scenarios) - 1)]
    game.title('Game')
    game.geometry('600x600')
    game.configure(bg='black')
    frame = LabelFrame(game, text='Resources', fg='yellow', bg='blue', padx=5, pady=5, width=1000, height=1000)
    frame.pack(padx=5, pady=5)
    Label(frame, text='Materials: ' + str(materials), bg='blue', fg='yellow').pack()
    Label(frame, text='Money: ' + str(money), bg='blue', fg='yellow').pack()
    Label(frame, text='Morale: ' + str(morale), bg='blue', fg='yellow').pack()
    Label(frame, text='Employment: ' + str(employment), bg='blue', fg='yellow').pack()
    Label(game, text=dude + ' asked ' + '"' + queue + '"', bg='black', fg='yellow').pack()
    Button(game, text='Yes', bg='black', fg='Blue', width=15, height=10, command=yep).pack()
    Button(game, text='No', bg='black', fg='Blue', width=15, height=10, command=nope).pack()
    Label(game, text='day(s): ' + str(days), bg='black', fg='yellow', font=slight).pack()
    game.mainloop()


# Main Page part 2

Button(
    root,
    text='Quit',
    command=out,
    fg='black',
    bg='red'
).grid(row=0, column=0)

Label(
    root,
    text='Crazy Future Business',
    fg='blue',
    bg='black',
    font=bigFont
).grid(row=1, column=0)
# ________________________
# How To Play Button
Button(root,
       text='How To Play',
       bg='blue',
       fg='blue',
       command=how,
       font=but).grid(row=2, column=0)
# Starting Button
Button(root,
       text='Start',
       bg='yellow',
       fg='blue',
       command=start,
       font=but).grid(row=3, column=0)
# ________________
root.mainloop()
