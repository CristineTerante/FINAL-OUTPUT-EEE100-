from tkinter import *
import time
from threading import Thread, active_count
from tracemalloc import stop
import tkinter as tk
from tkinter.font import Font
import os
from turtle import clear



class StopWatch(Frame):  
    
    # Implements a stop watch frame widget.                                                                
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw, bg = "#ff1493")
        self.saved = []
        self._running = 0
        self._start = 0.0        
        self._elapsedtime = 0.0
        self.timestr = StringVar()
        self.lapstr = StringVar()
        self.listbox = 0
        self.makeWidgets()
        self.laps = []
        self.lapmod2 = 0
        

    # Make the time label.
    def makeWidgets(self):                         
       
        lap = Label(self, text='                          Lap Record', font=('isocteur', 10, 'bold'), height=1, bg = "#ff1493",  fg=('black'))
        lap.pack(fill=Y, expand=NO, pady=2, padx=1)

        scrollbar = Scrollbar(self, orient=VERTICAL)
        self.listbox = Listbox(self, selectmode=EXTENDED, height=7, width = 23, bg=('#c9c0bb'), fg=('black'), yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.pack(side=RIGHT, fill=BOTH, expand=1, pady=0, padx=15)

        title = Label(self, height=0, text='Hello Kitty', font=('Brush Script MT', 28, 'bold'), bg=('#ff1493'), fg=('WHITE'))
        title.pack(fill=Y, expand=NO, pady=0, padx=0)
        title = Label(self, height=0, text='STOPWATCH', font=('isocteur', 28, 'bold'), bg=('black'), fg=('white'))
        title.pack(fill=Y, expand=NO, pady=1, padx=15)

        watch = Label(self, textvariable=self.timestr, font=(
            'Modern No. 20', 30), bg=('#ffa6c9'), fg=('black'))
        self._setTime(self._elapsedtime)
        watch.pack(fill=BOTH, expand=YES, pady=30, padx=10)
        


    def _update(self): 
        # Update the label with elapsed time. 
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)


    # Set the time string to Hours:Minutes:Seconds.Hundredths 
    def _setTime(self, elap):
        hours = int(elap/3600.0)
        minutes = int(elap/60 - hours * 60.0)
        seconds = int(elap - hours * 3600.0 - minutes * 60.0)
        hseconds = int((elap - hours * 3600.0 - minutes * 60.0 - seconds)*1000)                
        self.timestr.set('%02d:%02d:%02d.%03d' % (hours, minutes, seconds, hseconds))


    # Start the stopwatch, ignore if running.
    def Start(self):                                                      
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1  


    # Set the time string to Hours:Minutes:Seconds.Hundredths 
    def _setLapTime(self, elap):
        hours = int(elap/3600.0)
        minutes = int(elap/60.0 - hours * 60.0)
        seconds = int(elap - hours * 3600.0 - minutes*60.0)
        hseconds = int((elap - hours * 3600.0 - minutes*60.0 - seconds)*1000)            
        return '%02d:%02d:%02d.%03d' % (hours, minutes, seconds, hseconds)      


    # Stop the stopwatch, ignore if stopped. 
    def Stop(self):                                    
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = False


    # Reset the stopwatch and clears every 1st line in the listbox per tick.   
    def Reset(self):                                           
        self._elapsedtime = 0.0 
        self._start = time.time()                   
        self.laps = []   
        self._setTime(self._elapsedtime)
        self.after_cancel(self._timer)
        self._running = False
                  

    def Lap(self):
        tempo = self._elapsedtime
        if self._running:
            
            self.laps.append(self._setLapTime(tempo))
            self.listbox.insert(END, self.laps[-1])
            self.listbox.yview_moveto(1)
            self.lapmod2 = self._elapsedtime
    
    
    # Clears all data inside the listbox without stopping the timer.      
    def Clear(self):
        self.saved = []
        self.listbox.delete(0)
        
    # Get the name of the timer and create a file to store the laps.
    def storing(self):
        file = str(self.e()) + ' - '
        with open(file + self + '.txt', 'wb') as lapfile:
            for lap in self.laps:
                lapfile.write((bytes(str(lap) + '\n', 'utf-8')))
     
                
def main():
    root = Tk()
    root.wm_attributes("-topmost", 1)     
    sw = StopWatch(root)
    sw.pack(side=TOP)

    Button(root, text='Start', font=('isocteur'), height=1, width=7, fg=('white'), bg=('#3b444b'), command=sw.Start).pack(side=LEFT)
    Button(root, text='Stop', font=('isocteur'), height=1, width=7, fg=('white'), bg=('#3b444b'), command=sw.Stop).pack(side=LEFT)
    Button(root, text='Reset', font=('isocteur'), height=1, width=7, fg=('white'), bg=('#3b444b'), command=sw.Reset).pack(side=LEFT)
    Button(root, text='Lap', font=('isocteur'), height=1, width=7, fg=('white'), bg=('#3b444b'), command=sw.Lap).pack(side=LEFT)
    Button(root, text='Clear', font=('isocteur'), height=1, width=7, fg=('white'), bg=('#3b444b'), command=sw.Clear).pack(side=LEFT)

    root.mainloop()

if __name__ == '__main__':
    main()