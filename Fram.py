from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to code at coding.com")
root.iconbitmap('tanks.jpg')

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="DON'T CLICK HERE")
b2 = Button(frame, text="AND HERE")
b.grid(row=1, column=1)
b2.grid(row=0, column=0)
root.mainloop()
