from tkinter import *
import random
import time
root = Tk()
frame1=Frame(root)
frame1.pack(side= TOP)
time1 = ''
Label1 = Label(frame1, font=('times', 50,'bold'), bg = 'white')
Label1.pack(expand = YES)
Label1.config(text = "Solve Equation, Know The Time")

Hour1 = Label(root, font=('times', 100, 'bold'), bg='white')
Hour1.pack(side= LEFT)
Hour1.config(height=1, width=3)
Hour2 = Label(root, font=('times', 100, 'bold'), bg='white')
Hour2.pack(side= LEFT)
Hour2.config(height=1, width=3)
Hour3 = Label(root, font=('times', 100, 'bold'), bg='white')
Hour3.pack(side= LEFT)
Hour3.config(height=1, width=3)
Hour4 = Label(root, font=('times', 100, 'bold'), bg='white')
Hour4.pack(side= LEFT)
Hour4.config(text = "h", height=1, width=3)
Hour5 = Label(root, font=('times', 100, 'bold'), bg='white')
Hour5.pack(side= LEFT)
Hour5.config(height=1, width=3)

frame2=Frame(root)
frame2.pack(side= TOP)

Min1 = Label(root, font=('times', 100, 'bold'), bg='white')
Min1.pack(side= LEFT)
Min1.config(height=1, width=3)
Min2 = Label(root, font=('times', 100, 'bold'), bg='white')
Min2.pack(side= LEFT)
Min2.config(height=1, width=3)
Min3 = Label(root, font=('times', 100, 'bold'), bg='white')
Min3.pack(side= LEFT)
Min3.config(height=1, width=3)
Min4 = Label(root, font=('times', 100, 'bold'), bg='white')
Min4.pack(side= LEFT)
Min4.config(text = "h", height=1, width=3)
Min5 = Label(root, font=('times', 100, 'bold'), bg='white')
Min5.pack(side= LEFT)
Min5.config(height=1, width=3)

def check_hour():
    global time1
    # get the current local time from the PC

    secondtime = int(time.strftime('%S'))
    Hour5.config(text = secondtime)
    #Hour1.config(text=hourtime)
    mysigns=['+','-','*']
    randomno= random.randrange(2,24)
    if secondtime == 0 or secondtime == 10 or secondtime == 20 or secondtime == 30 or secondtime == 40 or secondtime == 50:
        hourtime = int(time.strftime('%H'))
        hr1signchoice = random.choice(mysigns)
        if hr1signchoice == "*":
            mulnum = 0
            randomno= random.randrange(2,20)
            mulnum = randomno * hourtime
            Hour1.config(text=mulnum)
            Hour2.config(text = "/")
            Hour3.config(text = randomno)
        elif hr1signchoice == "+":
            sumnum = 0
            randomno= random.randrange(24,99)
            sumnum = randomno + hourtime
            Hour1.config(text=sumnum)
            Hour2.config(text = "-")
            Hour3.config(text = randomno)
        elif hr1signchoice == "-":
            subnum = 0
            randomno= random.randrange(1,23)
            subnum = hourtime - randomno
            Hour3.config(text=subnum)
            Hour2.config(text = "+")
            Hour1.config(text = randomno)
    Hour1.after(200, check_hour)

def check_minute():
    global time2
    # get the current local time from the PC

    secondtime = int(time.strftime('%S'))
    
    mysigns1=['+','-','*']
    randomno= random.randrange(2,100)
    if secondtime == 0 or secondtime == 30:
        mintime = int(time.strftime('%M'))
        minsignchoice = random.choice(mysigns1)
        if minsignchoice == "+":
            sumnum = 0
            randomno= random.randrange(24,99)
            sumnum = randomno + hourtime
            Min1.config(text=sumnum)
            Min2.config(text = "-")
            Min3.config(text = randomno)

        elif minsignchoice == "-":
            subnum = 0
            randomno= random.randrange(1,23)
            subnum = hourtime - randomno
            Min3.config(text=subnum)
            Min2.config(text = "+")
            Min1.config(text = randomno)
        elif minnsignchoice == "*":
            mulnum = 0
            randomno= random.randrange(2,20)
            mulnum = randomno * hourtime
            Hour1.config(text=mulnum)
            Hour2.config(text = "/")
            Hour3.config(text = randomno
    Hour1.after(200, check_minute)

check_hour()
root.mainloop()
