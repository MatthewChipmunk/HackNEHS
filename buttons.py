from tkinter import *

root = Tk()


def click():
    label = Label(root, text="I CLICKED A BUTTON")
    label.pack()


button = Button(root, text='Click me', pady=50, command=click, fg='blue', bg='red')
button.pack()

root.mainloop()
