from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to code at coding.com")

# r = IntVar()
# r.set("1")

pizza = StringVar()
pizza.set("Pepperoni")


def clicked(value):
    label = Label(root, text=value)
    label.pack()


MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

# Radiobutton(root, text='option 0', variable=r, value=0, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text='option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()


button = Button(root, text='clicked', command=lambda: clicked(pizza.get()))
button.pack()

root.mainloop()
