from tkinter import *

root = Tk()
root.title('e')
root.geometry('400x400')


def show():
    label = Label(root, text=var.get()).pack()


var = StringVar()
x = Checkbutton(root, text='Check this box, dude', variable=var, onvalue='kid', offvalue='boi')
x.deselect()
x.pack()

button = Button(root, text='show thing', command=show).pack()

root.mainloop()
