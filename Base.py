from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to code at coding.com")


def open():
    top = Toplevel()
    top.title("YEET")
    btn2 = Button(top, text='CLOSE WINDOW', command=top.destroy).pack()


btn = Button(root, text='Open Second Window', command=open).pack()

root.mainloop()
