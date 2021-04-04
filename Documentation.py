from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.iconbitmap('tanks.jpg')
username = ''
password = ''
root.configure(bg='black')


def generate():
    global username, password
    word = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length_of_username = random.randint(5, 10)
    length_password = random.randint(5, 10)
    for i in range(length_of_username):
        username += word[random.randint(0, len(word)-1)]
    for i in range(length_password):
        password += word[random.randint(0, len(word)-1)]
    
    messagebox.showinfo('', 'Your username is ' + username + ' and your password is ' + password)


root.title('Random Username and Password generator')
Label(root, text='Generate your username and password', bg='black', fg='red').pack()
Button(root, text='generate', command=generate, bg='black').pack()

root.mainloop()
