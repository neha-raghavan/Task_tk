from tkinter import *
import tkinter.messagebox
import random

top = tkinter.Tk()
top.geometry("600x300")  
score = 0
def fun():
    global score
    num = random.randint(1,6)
    score=score+num
    if score%7==0:
        score=0
    if score==100:
        tkinter.messagebox.showinfo( "Task", "Congratulations")
    print(num)
    print(score)
    label1 = Label(top, text= str(score))
    label2 = Label(top, text= str(num))
    label1.pack()
    label2.pack()
    

B = tkinter.Button(top, text ="Roll the dice", command = fun)

B.pack()
top.mainloop()