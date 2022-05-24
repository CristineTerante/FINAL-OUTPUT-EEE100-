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
        Frame.__init__(self, parent, kw)
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
        

    def makeWidgets(self):                         
        # Make the time label.
       
        lap = Label(self, text='                         Lap Record', font=('isocteur', 10, 'bold'), height=1, fg=('blue'))
        lap.pack(fill=Y, expand=YES, pady=10, padx=10)

        scrollbar = Scrollbar(self, orient=VERTICAL)
        self.listbox = Listbox(self, selectmode=EXTENDED, height=7, bg=('black'), fg=('blue'), yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.pack(side=RIGHT, fill=BOTH, expand=1, pady=0, padx=0)

        title = Label(self, height=2, text='STOPWATCH', font=(
            'isocteur', 28, 'bold'), bg=('black'), fg=('blue'))
        title.pack(fill=Y, expand=YES, pady=10, padx=10)

        watch = Label(self, textvariable=self.timestr, font=(
            'isocteur', 23), bg=('black'), fg=('blue'))
        self._setTime(self._elapsedtime)
        watch.pack(fill=BOTH, expand=YES, pady=10, padx=10)
        
        eee = Label(self, text='EEE100 17F', font=(
            'cascadia mono light', 10), bg=('black'), fg=('blue'))
        eee.pack(fill = Y, expand = YES, pady = 10, padx = 10)
    

    def _update(self): 
        # Update the label with elapsed time. 
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _setTime(self, elap):
        # Set the time string to Hours:Minutes:Seconds.Hundredths 
        hours = int(elap/3600.0)
        minutes = int(elap/60.0)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d.%02d' % (hours, minutes, seconds, hseconds))

    def Start(self):                                                     
        # Start the stopwatch, ignore if running. 
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1  

    def _setLapTime(self, elap):
        # Set the time string to Hours:Minutes:Seconds.Hundredths 
        hours = int(elap/3600.0)
        minutes = int(elap/60.0)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)            
        return '%02d:%02d:%02d.%02d' % (hours, minutes, seconds, hseconds)      

    def Stop(self):                                    
        # Stop the stopwatch, ignore if stopped. 
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = False

    def Reset(self):                                  
        # Reset the stopwatch and clears every 1st line in the listbox per tick.            
        self._elapsedtime = 0.0 
        self._start = time.time()                   
        self.laps = []   
        self._setTime(self._elapsedtime)
        self.after_cancel(self._timer)
        self._running = False
        self.saved = []
        self.listbox.delete(0)
        
        

                 

    def Lap(self):
        tempo = self._elapsedtime
        if self._running:
            self.laps.append(self._setLapTime(tempo))
            self.listbox.insert(END, self.laps[-1])
            self.listbox.yview_moveto(1)
            self.lapmod2 = self._elapsedtime
            
    def Clear(self):
            # Clears all data inside the listbox without stopping the timer.
        self.laps = [] 
        self.laps.delete
        self.saved.destroy()

        
        


    def storing(self):
        # Get the name of the timer and create a file to store the laps.
        file = str(self.e()) + ' - '
        with open(file + self + '.txt', 'wb') as lapfile:
            for lap in self.laps:
                lapfile.write((bytes(str(lap) + '\n', 'utf-8')))
                
def main():
    root = Tk()
    root.wm_attributes("-topmost", 1)      # always on top - might do a button for it.
    sw = StopWatch(root)
    sw.pack(side=TOP)

    Button(root, text='Start', font=('isocteur'), height=1, width=7, fg=('blue'), bg=('black'), command=sw.Start).pack(side=LEFT)
    Button(root, text='Stop', font=('isocteur'), height=1, width=7, fg=('blue'), bg=('black'), command=sw.Stop).pack(side=LEFT)
    Button(root, text='Lap', font=('isocteur'), height=1, width=7, fg=('blue'), bg=('black'), command=sw.Lap).pack(side=LEFT)
    Button(root, text='Reset', font=('isocteur'), height=1, width=7, fg=('blue'), bg=('black'), command=sw.Reset).pack(side=LEFT)
    Button(root, text='Clear', font=('isocteur'), height=1, width=7, fg=('blue'), bg=('black'), command=sw.Clear).pack(side=LEFT)

    root.mainloop()

if __name__ == '__main__':
    main()