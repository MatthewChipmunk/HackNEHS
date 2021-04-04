from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Learn to code at coding.com")


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    '''response = messagebox.askyesno("YEET", 'hi amigos')
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text='OK, INITIATING').pack()
    else:
        Label(root, text='OK, DEACTIVATE').pack()'''
    '''response = messagebox.askquestion("YEET", 'hi amigos')
    if response == 'yes':
        Label(root, text='yay').pack()
    else:
        Label(root, text='NOPE').pack()'''
    response = messagebox.showinfo("THIS IS DANGEROUS", "HA AMIGOS")
    Label(root, text=response).pack()


Button(root, text='yeet', command=popup).pack()

root.mainloop()
