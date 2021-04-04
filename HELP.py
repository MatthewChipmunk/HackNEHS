from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import math


# import numpy
# import cv2

def Slope():
    messagebox.showinfo(
        'Slope Formula',
        'The slope of a line is  (y₂ – y₁) /  (x₂ – x₁)for any pairs of (x₁, y₁) and (x₂, y₂)'
    )


def Midpoint():
    messagebox.showinfo(
        'Midpoint',
        'The Midpoint Formula is (x₁+x₂) / 2, (y₁+y₂) / 2 for any pairs of (x₁, y₁) and (x₂, y₂)'
        '')


def pt():
    messagebox.showinfo(
        'Pythagorean Theorem',
        'The Pythagorean Theorem is a^2 + b^2 = c^2 Where a is any leg, b is the other leg, and c is the hypotenuse '
    )


def am():
    messagebox.showinfo(
        'Arithmetic Mean',
        'The Arithmetic mean of the n numbers x_1,x_2,...,x_n is (x₁+x₂+...+x_n-1, x_n)'
    )


def gm():
    messagebox.showinfo(
        'Geometric Mean',
        'The Geometric mean of n numbers x₁, x₂,...x_n is (x₁*x₂*...x_n)^(1/n), for any number of x that is not 0'
    )


def rightTriangles1():
    messagebox.showinfo(
        'Right Triangles',
        'If the angles of a right triangle are 45, 45, and 90, then the length of the two legs are the same, and the hypotenuse is x * sqrt2. If the angles of a right triangle are 30, 60, and 90, then the longer leg is sqrt3 * the shorter leg, and the hypotenuse is 2 times the shorter leg. '
    )


def LinesIncircles():
    messagebox.showinfo(
        'Lines in Circle',
        'The diameter of a circle is the longest chord in the circle. A chord is any line in a circle that connects 2 points on the circle. The radius is the line segment from the center of the circle to the circumfrence of a circle. The radius is the half the diameter. None of these lines can be less than or equal to 0'
    )


def cc():
    messagebox.showinfo(
        'Circumference of Circle',
        '''The Circumference of a circle is πd, where π is pi, which is approximately 3.14159265358979323. d stands for diameter, which is not 0'''
    )


def ac():
    messagebox.showinfo(
        'Area of touches',
        '''The area of a circle is π*(r^2), where π is pi(approximately 3.14159265358979323). r stands for radius, which is half the diameter '''
    )


def pali():
    messagebox.showinfo(
        'Palindrome',
        '''A palindrome is a integer which reads the same forwards and backwards'''
    )


def modulo():
    messagebox.showinfo(
        'Modulo',
        '''The expression a mod b is defined as: The remainder when a is divided by b'''
    )


def basic_probability():
    messagebox.showinfo(
        'Basic Probability',
        '''The formula for probability is (wanted outcomes)/(total outcomes)'''
    )


def casework():
    messagebox.showinfo(
        'Casework', '''Casework is when you manually 
    count all the possibes cases''')


def complementary():
    messagebox.showinfo(
        'Complementary',
        '''Complementary counting is when you subtract the unwanted outcomes from the total outcomes.'''
    )


def factors():
    messagebox.showinfo('Factors',
                        '''for a number with the prime factorization p1^e1*p2^e2*...pk*ek the number of factors is (e1+1)*(e2+1)*...(en+1)''')


def Constructive():
    messagebox.showinfo('Constructive Counting',
                        'Constructive counting is counting the number of integers, lists, etc., that satisfy a certain property by "constructing" it. This strategy is useful for complicated counting or combinatorics questions, as the problem can be broken down into cases, the number of possibilities in each case can be computed, and those numbers can be summed to find the final answer.')


# Main Page
root = Tk()
root.geometry('400x600')
sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=sb.set)

root.configure(bg='black')
title = Font(family='Times', size=8, weight='bold', slant='italic')
root.title('Math Formulas and Methods Cheat Sheet')

# Label(root,
# text='MATH FORMULAS AND METHODS CHEAT SHEET',
# bg='black',
# fg='cyan',
# font=title).pack()
# Geometry
bf = LabelFrame(root, text='Geometry', bg='light green', fg='dark orange')
bf.pack(padx=10, pady=10)
Button(bf, text='Pythagorean Theorem', command=pt, height=0).pack()
Button(bf, text='Right Triangles', command=rightTriangles1, height=0).pack()
Button(bf, text='Circumference in Circles', command=cc, height=0).pack()
Button(bf, text='Lines in Circles', command=LinesIncircles, height=0).pack()
Button(bf, text='Area Of Circle', command=ac, height=0).pack()
# Algebra
algeria = LabelFrame(root, text='Algebra', bg='red', fg='green')
algeria.pack(padx=10, pady=10)
Button(algeria, text='Slope Formula', command=Slope, height=0).pack()
Button(algeria, text='Midpoint Formula', command=Midpoint, height=0).pack()
Button(algeria, text='Arithmetic Mean', command=am, height=0).pack()
Button(algeria, text='Geometry Mean', command=gm, height=0).pack()
# Number Theory
nt = LabelFrame(root, text='Number Theory', bg='orange', fg="blue")
nt.pack(padx=5, pady=5)
Button(nt, text='Palindrome', command=pali, height=0).pack()
Button(nt, text='Modulo', command=modulo, height=0).pack()
Button(nt, text='Factors', command=factors, height=0).pack()

# Counting and Probability
cp = LabelFrame(root,
                text='Counting and Probability',
                bg='light blue',
                fg='yellow')
cp.pack(padx=5, pady=5)
Button(cp, text='Casework Counting', command=casework, height=0).pack()
Button(cp, text='Complementary Counting', command=complementary, height=0).pack()
Button(cp, text='Constructive Counting', height=0, command=Constructive).pack()
Button(cp, text='Basic Probability', command=basic_probability, height=0).pack()

# Game Loop
root.mainloop()