import time 
from graphics import *
#Make a text object for each digit so that it doesn't look like an insane person. 
#timer need to be fixed. 

#Global crap
DISPLAY_HEIGHT = 4.5
DISPLAY_WIDTH = 7
WINDOW_WIDTH = 133*DISPLAY_WIDTH
WINDOW_HEIGHT = 133*DISPLAY_HEIGHT
SPACING = WINDOW_WIDTH/5

class Timer(object):
    def __init__(self, hun_sec, sec, minu, hour):
        self.hun_sec = hun_sec
        self.sec = sec
        self.minu = minu
        self.hour = hour

        self._window = GraphWin("Dashboard", WINDOW_WIDTH, WINDOW_HEIGHT)

        background = Rectangle(Point(0,0),Point(WINDOW_WIDTH,WINDOW_HEIGHT))
        background.setFill('salmon')
        background.draw(self._window)
        self._background = background

        t = Text(Point(SPACING*(3+1),WINDOW_HEIGHT/2+10),str(self.hun_sec))
        t.setSize(36)
        s = Text(Point(SPACING*(2+1),WINDOW_HEIGHT/2+10),str(self.sec)+':')
        s.setSize(36)
        r = Text(Point(SPACING*(1+1),WINDOW_HEIGHT/2+10),str(self.minu)+':')
        r.setSize(36)
        q = Text(Point(SPACING*(0+1),WINDOW_HEIGHT/2+10),str(self.hour)+':')
        q.setSize(36)
        t.setTextColor('black')
        t.draw(self._window)
        s.setTextColor('black')
        s.draw(self._window)
        r.setTextColor('black')
        r.draw(self._window)
        q.setTextColor('black')
        q.draw(self._window)

        self.hun_sec_obj = t
        self.sec_obj = s
        self.minu_obj = r
        self.hour_obj = q


    def print_time(self):
        st = ""
        st = str(self.hour) + ":" + str(self.minu) + ":" + str(self.sec) + ":" + str(self.hun_sec)
        return st

    def update_time(self, time):
        #time[0] is hours, time[1] is min, time[2] is sec, time[3] is hou sec
        if time[0] != self.hour:
            self.hour = time[0]
            self.hour_obj.setText(self.hour+':')
        if time[1] != self.minu:
            self.minu = time[1]
            self.minu_obj.setText(self.minu+':')
        if time[2] != self.sec:
            self.sec = time[2]
            self.sec_obj.setText(self.sec+':')
        if time[3] != self.hun_sec:
            self.hun_sec = time[3]
            self.hun_sec_obj.setText(self.hun_sec)


   

def main():
    timer = Timer('00','00','00','00')
    
    while True:
        new_time = raw_input("Time(00 00 00 00)")
        nt = new_time.split()
        timer.update_time([nt[0],nt[1],nt[2],nt[3]])

            



if __name__ == "__main__":
    main()