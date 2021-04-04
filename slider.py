from tkinter import *

root = Tk()

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

label = Label(root, text=horizontal.get()).pack()


def slide():
    label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+'x'+str(vertical.get()))


btn = Button(root, text='Click Me!', command=slide).pack()

root.title('e')
root.mainloop()
