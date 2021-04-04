from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name")


def click():
    hello = "Hello " + e.get()
    label = Label(root, text=hello)
    label.pack()


button = Button(root, text='Enter yo name', command=click)
button.pack()

root.mainloop()
