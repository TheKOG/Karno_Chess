#!/urs/bin/python3
import sys
from Karno_Class import *

if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk

class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.title('Karno Chess')
        self.iconbitmap('pic/karno_cyberstyle.ico')
        #self.geometry('{0}x{1}'.format(10 * 30, 10 * 30))
        self._build_maze()
        self.resizable(False,False)
    
    def _build_maze(self):
        self.geometry("{0}x{1}+400+100".format(EDGE*10,int(EDGE*8.66)))
        self.canvas = tk.Canvas(self,bg='white',
                        height=EDGE*8.66,
                        width=EDGE*10)
        self.canvas.bind("<Button -1>",self.callback)
        global bk
        bk = tk.PhotoImage(file = "pic/board.png")
        image = self.canvas.create_image(EDGE*10/2, EDGE*8.66/2, image=bk)
        #print("")
        self.canvas.pack()
    
    def callback(self,event):
        #self.turn=-self.turn
        sx=event.x
        sy=event.y
        State.React(sx,sy)
        # print(len(State.Board_to_Str()))
        # self.canvas.create_oval(sx-2,sy-2,sx+2,sy+2,fill="blue")

def Run():
    Init_Board(env)
    Init_Images()
    Init_Chess()
    while True:
        State.Show_Chess(env)
        # time.sleep(2)

if __name__=="__main__":
    # file=open("boundary.txt",mode="w")
    State=Karno()
    env=Maze()
    env.after(100, Run)
    env.mainloop()