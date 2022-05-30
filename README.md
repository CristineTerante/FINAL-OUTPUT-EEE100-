# FINAL-OUTPUT-EEE100
This is a Project-Based Exam for Programming
#import the required libraries
import time
from threading import Thread
from tkinter import *


#Implement a stopwatch frame widget 
class StopWatch(Frame):                                                               
    def __init__(self, parent=None, **kw):   
             
        Frame.__init__(self, parent, bg = ('#CBC3E3'))
        self.today = time.strftime("%d %b %Y %H-%M-%S", time.localtime())
        self._running = 0
        self._start = 0.0        
        self._elapsedtime = 0.0
        self.timestr = StringVar()
        self.lapstr = StringVar()
        self.e = 0
        self.listbox = 0
        self.makeWidgets()
        self.laps = []
        self.lapmod2 = 0
    
    #Display bunch of widgets
    def makeWidgets(self):                         

        lap = Label(self, text='                                                                          Lap Record', bg = ('#CBC3E3'))
        lap.pack(fill=X, expand=NO, pady=5, padx=2)

        scrollbar = Scrollbar(self, orient=VERTICAL,)
        self.listbox = Listbox(self,selectmode=EXTENDED, height = 9, bg=('violet'), yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack (side=RIGHT, fill=Y)
        self.listbox.pack(side=RIGHT, fill=BOTH, expand=1, pady=5, padx=2)

        title = Label(self, text='Stopwatch', font=('Segoe Script', 20), bg = ('#E0B0FF'))
        title.pack(fill=X, expand=NO, pady=5, padx=2)

        watch = Label(self, textvariable=self.timestr, font=('Modern No. 20', 36), bg=('VIOLET'), fg=('white'))
        self._setTime(self._elapsedtime)
        watch.pack(fill=X, expand=NO, pady=3, padx=2)

    def _update(self): 
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _setTime(self, elap):
        """ Set the time string to Hours:Minutes:Seconds.Hundredths """
        hours = int(elap/3600.0)
        minutes = int(elap/60 - hours * 60.0)
        seconds = int(elap - hours * 3600.0 - minutes * 60.0)
        hseconds = int((elap - hours * 3600.0 - minutes * 60.0 - seconds)*1000)                
        self.timestr.set('%02d:%02d:%02d.%03d' % (hours, minutes, seconds, hseconds))

    #Start the stopwatch, ignore if running
    def Start(self):                                                     
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1  

    #Set the time string to Hours:Minutes:Seconds.Hundredths 
    def _setLapTime(self, elap):
        hours = int(elap/3600.0)
        minutes = int(elap/60.0 - hours * 60.0)
        seconds = int(elap - hours * 3600.0 - minutes*60.0)
        hseconds = int((elap - hours * 3600.0 - minutes*60.0 - seconds)*1000)            
        return '%02d:%02d:%02d.%03d' % (hours, minutes, seconds, hseconds)      

    #Stop the stopwatch, ignore if stopped
    def Stop(self):                                    
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = False

    #Reset the stopwatch
    def Reset(self):                                  
        self._start = time.time() 
        self.running = False        
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)
        
        self.reset_button.config(text="Reset", command=self.reset)
        self.clock["text"] = str(self.time)

    def Lap(self):
        tempo = self._elapsedtime
        self.laps.append(self._setLapTime(tempo))
        self.listbox.insert(END, self.laps[-1])
        self.listbox.yview_moveto(1)
        self.lapmod2 = self._elapsedtime

    #Get the name of the timer and create a file to store the laps
    def storing(self):
        file = str(self.e.get()) + ' - '
        with open(file + self.today + '.txt', 'wb') as lapfile:
            for lap in self.laps:
                lapfile.write((bytes(str(lap) + '\n', 'utf-8')))
                
def main():
    ws = Tk()
    ws.wm_attributes("-topmost", 1)     
    sw = StopWatch(ws)
    sw.pack(side=TOP)

    Button(ws, text='Start', height=2, width=7, fg=('black'), bg=('violet'), command=sw.Start).pack(side=LEFT)
    Button(ws, text='Stop', height=2, width=7, fg=('black'), bg=('violet'), command=sw.Stop).pack(side=LEFT)
    Button(ws, text='Lap', height=2, width=7, fg=('black'), bg=('violet'), command=sw.Lap).pack(side=LEFT)
    Button(ws, text='Reset', height=2, width=7, fg=('black'), bg=('violet'), command=sw.Reset).pack(side=LEFT)
    

    ws.mainloop()

if __name__ == '__main__':
    main()
