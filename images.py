from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to code at coding.com")
root.iconbitmap('tanks.jpg')

img = ImageTk.PhotoImage(Image.open('abrams.png'))
label = Label(imgae=img)
label.pack()
button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()
