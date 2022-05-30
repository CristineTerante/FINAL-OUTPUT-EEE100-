# FINAL-OUTPUT-EEE100
EEE-EXAM
This is a Project-Based Exam for I-Programming
# using Tkinter
#importing the required libraries
import tkinter as tk
from tkinter import *

global count
count =0
class stopwatch():
    def reset(self):
        global count
        count=1
        self.t.set('00:00:00')        
    def start(self):
        global count
        count=0
        self.timer()   
    def stop(self):
        global count
        count=1
    def close(self):
        self.root.destroy()
    def timer(self):
        global count
        if(count==0):
            self.d = str(self.t.get())
            hour, minute, second = map(int,self.d.split(":")) 
            hour = int(hour)
            minute=int(minute)
            second= int(second)
            if(second<59):
                second+=1
            elif(second==59):
                second=0
                if(minute<59):
                    minute+=1
                elif(minute==59):
                    minute=0
                    hour+=1
            if(hour<10):
                hour = str(0)+str(hour)
            else:
                hour= str(hour)
            if(minute<10):
                minute = str(0)+str(minute)
            else:
                minute = str(minute)
            if(second<10):
                second=str(0)+str(second)
            else:

                second=str(second)
            self.d=hour+":"+minute+":"+second           
            self.t.set(self.d)
            if(count==0):
                self.root.after(1000,self.timer)   
                
    def __init__(self):
        self.root=Tk()
        self.root.title("Stop Watch")

        # Fixing the window size.
        self.root.minsize(width=580, height=200)
        self.t = StringVar()
        self.t.set("02:00:00")

        self.lb = Label(self.root,textvariable=self.t,font=("Pixel 50 bold"),bg="white")
        self.start = Button(self.root,text="Start",command=self.start,font=("Times 18 bold"),bg=("green"))
        self.stop = Button(self.root,text="Stop",command=self.stop,font=("Times 18 bold"),bg=("red"))
        self.reset = Button(self.root,text="Reset",command=self.reset,font=("Times 18 bold"),bg=("orange"))
        self.exit = Button(self.root, text="Exit", command=self.close,font=("Times 18 bold"),bg=("gray"))
        self.lb.pack(side="top")
        self.start.pack(side="left")
        self.stop.pack(side="left")
        self.reset.pack(side="left")
        self.exit.pack(side="left")
    
        self.label = Label(self.root,text="",font=("Pixel 40 bold",))
        self.root.configure(bg='white')
        self.root.mainloop()
a=stopwatch()    
