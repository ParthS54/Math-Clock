global time
from tkinter import *
import random
import time

root = Tk()

frame1=Frame(root,height=4, bd=10, relief=SUNKEN,bg='black')
frame1.pack(fill=X, padx=5, pady=5,side= TOP)

Hour1 = Label(frame1, font=('times', 100, 'bold'), bg='black', fg='white')
Hour1.pack(side= LEFT)
Hour1.config(height=1, width=3)
Hour2 = Label(frame1, font=('times', 100, 'bold'), bg='black', fg='white')
Hour2.pack(side= LEFT)
Hour2.config(height=1, width=3)
Hour3 = Label(frame1, font=('times', 100, 'bold'), bg='black', fg='white')
Hour3.pack(side= LEFT)
Hour3.config(height=1, width=3)
Hour4 = Label(frame1, font=('times', 100, 'bold'), bg='black', fg='white')
Hour4.pack(side= LEFT)
Hour4.config(text = "h", height=1, width =2)

frame2=Frame(root,height=4, bd=10, relief=SUNKEN,bg='black')
frame2.pack(side= TOP,padx=5, pady=5,fill=X)

Min1 = Label(frame2, font=('times', 100, 'bold'), bg='black', fg='white')
Min1.pack(side= LEFT)
Min1.config(height=1, width=3)
Min2 = Label(frame2, font=('times', 100, 'bold'), bg='black', fg='white')
Min2.pack(side= LEFT)
Min2.config(height=1, width=1)
Min3 = Label(frame2, font=('times', 100, 'bold'), bg='black', fg='white')
Min3.pack(side= LEFT)
Min3.config(height=1, width=3)
Min4 = Label(frame2, font=('times', 100, 'bold'), bg='black', fg='white')
Min4.pack(side= LEFT)
Min4.config(height=1, width=1)
Min5 = Label(frame2, font=('times', 100, 'bold'), bg='black', fg='white')
Min5.pack(side= LEFT)
Min5.config(height=1, width=2)
Min6 = Label(frame2, font=('times', 100, 'bold'), bg='black', fg='white')
Min6.pack(side= LEFT)
Min6.config(text = "m", height=1, width=2)

frame3=Frame(root,height=4, width = 5, bd=10, relief=SUNKEN,bg='black')
frame3.pack(side= LEFT,padx=5, pady=5,)

Sec1 = Label(frame3, font=('times', 100, 'bold'), bg='black', fg='white')
Sec1.pack(side= LEFT)
Sec1.config(height=1, width=2)
Sec2 = Label(frame3, font=('times', 100, 'bold'), bg='black', fg='white')
Sec2.pack(side= LEFT)
Sec2.config(height=1, width=1)

TAGframe=Frame(root,height=4, width = 3, bd=10, relief=SUNKEN)
TAGframe.pack(padx=5, pady=5, side= LEFT)

clkintro = Label(TAGframe, font=('times', 50, 'bold'), bg='white')
clkintro.pack(side= LEFT)
clkintro.config(text = "TIC TOCK \n CLOCK")

frame4=Frame(root,height=4, width = 3, bd=10, relief=SUNKEN,bg='black')
frame4.pack(padx=5, pady=5, side= LEFT)

intro = Label(frame4, font=('times', 50, 'bold'), bg='black', fg='white')
intro.pack(side= LEFT)
intro.config(text = "Created by \n PARTH")

hourtime = int(time.strftime('%H'))
Hour2.config(text = hourtime)
mintime =int(time.strftime('%M'))
Min3.config(text= mintime)

def check():
    secondtime = int(time.strftime('%S'))
    Sec1.config(text = secondtime)
    Sec2.config(text = 's')
    check_hr(secondtime)
    check_minute(secondtime)
    Sec1.after(200, check)
    return;


def check_hr(secondtime):
    mysigns=['+','-','*']
    if secondtime == 0 or secondtime ==  10 or secondtime == 20 or secondtime ==  30 or secondtime == 40 or secondtime ==  50:
        hourtime = int(time.strftime('%H'))
        hrsignchoice = random.choice(mysigns)
        if hrsignchoice == "*":
            mulnum = 0
            randomno= random.randrange(2,20)
            mulnum = randomno * hourtime
            Hour1.config(text=mulnum)
            Hour2.config(text = "/")
            Hour3.config(text = randomno)
        elif hrsignchoice == "+":
            sumnum = 0
            randomno= random.randrange(24,200)
            sumnum = randomno + hourtime
            Hour1.config(text=sumnum)
            Hour2.config(text = "-")
            Hour3.config(text = randomno)
        elif hrsignchoice == "-":
            subnum = 0
            randomno= random.randrange(2,23)
            subnum = hourtime - randomno
            Hour3.config(text=subnum)
            Hour2.config(text = "+")
            Hour1.config(text = randomno)


def check_minute(secondtime):
    mysigns=['+','-','*']
    if secondtime == 0 or secondtime ==  10 or secondtime == 20 or secondtime ==  30 or secondtime == 40 or secondtime ==  50:
        mintime = int(time.strftime('%M'))
        minsignchoice = random.choice(mysigns)
        if minsignchoice == "+":
            sumnum = 0
            randomno= random.randrange(50,99)
            sumnum = randomno + mintime
            sign_choice = ['-', '*']
            sep_min_signchoice = random.choice(sign_choice)
            sep_no = seperated_min(sep_min_signchoice, randomno)
            Min1.config(text=sumnum)
            Min2.config(text = "-")
            Min3.config(text = '(' + str(sep_no))
        elif minsignchoice == "-":
            subnum = 0
            randomno= random.randrange(1,23)
            subnum = mintime - randomno
            sign_choice = ['+', '*']
            sep_min_signchoice = random.choice(sign_choice)
            sep_no = seperated_min(sep_min_signchoice, randomno)
            Min3.config(text= '(' + str(sep_no))
            Min2.config(text = "+")
            Min1.config(text = subnum)
        elif minsignchoice == "*":
            mulnum = 0
            randomno= random.randrange(10,20)
            mulnum = randomno * mintime
            sign_choice = ['-', '+']
            sep_min_signchoice = random.choice(sign_choice)
            sep_no = seperated_min(sep_min_signchoice, randomno)
            Min1.config(text=mulnum)
            Min2.config(text = "/")
            Min3.config(text = '(' + str(sep_no))

def seperated_min(sign_choice, randomno):
    if sign_choice == "+":
        sumnum = 0
        minno= random.randrange(24,50)
        sumnum = minno + randomno
        Min5.config(text= str(minno) + ')')
        Min4.config(text = "-")
        return (sumnum)
    elif sign_choice == "-":
        subnum = 0
        minno= random.randrange(1,23)
        subnum = randomno - minno
        Min5.config(text= str(minno) + ')')
        Min4.config(text = "+")
        return (subnum)
    elif sign_choice == "*":
        mulnum = 0
        minno= random.randrange(2,10)
        mulnum = randomno * minno
        Min5.config(text= str(minno) + ')')
        Min4.config(text = "/")
        return (mulnum)

check()


root.mainloop()
