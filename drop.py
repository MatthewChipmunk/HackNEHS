from tkinter import *

root = Tk()
root.title('e')
root.geometry('400x400')
options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

clicked = StringVar()
clicked.set(options[0])


def show():
    Label(root, text=clicked.get()).pack()


drop = OptionMenu(root, clicked, *options)
drop.pack()

b = Button(root, text='Show Selection', command=show).pack()

root.mainloop()
