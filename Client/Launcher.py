#!/urs/bin/python3
import socket
import sys
from Client import Run
from MP3Player import MP3Player
import _thread
import time
import ctypes
import tkinter as tk

EDGE=100

music=0

def atoi(s):
    s = s[::-1]
    num = 0
    for i, v in enumerate(s):
        for j in range(0, 10):
            if v == str(j):
                num += j * (10 ** i)
    return num

def Save():
    file=open("Servers",mode="w")
    name=env.name_input.get()
    file.write(name+'\n')
    for index in range(10):
        try:
            ip=env.ip_input[index].get()
            ip=ip+"\n"
            file.write(ip)
            file.flush()
        except:
            pass

def Quit():
    Save()
    try:
        env.destroy()
    except:
        pass
    # print('Quit!')
    exit(0)

picpath='pic'

class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.title('Karno Launcher')
        self.protocol("WM_DELETE_WINDOW", lambda: Quit())
        self.iconphoto(False,tk.PhotoImage(file='pic/karno_cyberstyle.png'))
        moni=ctypes.windll.user32
        global wt
        global ht
        wt=moni.GetSystemMetrics(0)
        ht=moni.GetSystemMetrics(1)
        # ht=1080
        print("height={0}".format(ht))
        if(ht<=900):
            global EDGE
            global picpath
            EDGE=75
            picpath='pic2'
        self._build_maze()
        #self.geometry('{0}x{1}'.format(10 * 30, 10 * 30))
        self.Init_Home()
        self.resizable(False,False)
        self.IP="127.0.0.1"
        self.ports=[3450 for i in range(10)]
        self.room_name=["fkpps" for i in range(10)]
        self.room_num=0
        self.s=0
        self.name="NULL"
        _thread.start_new_thread(self.Play_Music,(0,))
    
    def _build_maze(self):
        self.geometry("{0}x{1}+{2}+{3}".format(EDGE*10,int(EDGE*8.66),int((wt-EDGE*10)/2),int((ht-EDGE*8.66)/2)))
        self.canvas = tk.Canvas(self,bg='pink',
                        height=EDGE*8.66,
                        width=EDGE*10)
        global bk
        bk = tk.PhotoImage(file = picpath+"/Karno.png")
        image = self.canvas.create_image(EDGE*5, EDGE*8.66/2, image=bk)
        self.canvas.pack()
    
    def Init_Home(self):
        try:
            self._delete_rooms()
        except:
            pass
        addr = [tk.StringVar() for i in range(10)]
        name_saved=tk.StringVar()
        file=open("Servers",mode="r")
        tmp=file.readline()
        name_saved.set(tmp[:-1])
        for i in range(10):
            try:
                ip_port=file.readline()
                if ip_port[-1]=="\n":
                    ip_port=ip_port[:-1]
                addr[i].set(ip_port)
            except:
                addr[i].set("")
                break
        file.close()
        self.ip_input=[tk.Entry(self,textvariable=addr[i]) for i in range(10)]
        self.name_input=tk.Entry(self,textvariable=name_saved)
        self.ip_label=[tk.Label(self,text="IP:",bg="pink") for i in range(10)]
        self.name_label=tk.Label(self,text="NAME:",bg='pink')
        self.button=[0 for i in range(10)]
        self.button[0]=tk.Button(self,text="Connect",command=lambda: self.Connect(0))
        self.button[1]=tk.Button(self,text="Connect",command=lambda: self.Connect(1))
        self.button[2]=tk.Button(self,text="Connect",command=lambda: self.Connect(2))
        self.button[3]=tk.Button(self,text="Connect",command=lambda: self.Connect(3))
        self.button[4]=tk.Button(self,text="Connect",command=lambda: self.Connect(4))
        self.button[5]=tk.Button(self,text="Connect",command=lambda: self.Connect(5))
        self.button[6]=tk.Button(self,text="Connect",command=lambda: self.Connect(6))
        self.button[7]=tk.Button(self,text="Connect",command=lambda: self.Connect(7))
        self.button[8]=tk.Button(self,text="Connect",command=lambda: self.Connect(8))
        self.button[9]=tk.Button(self,text="Connect",command=lambda: self.Connect(9))
        self.Exit=tk.Button(self,text="Quit",command=Quit)
        self._build_home()
    
    def _build_home(self):
        # self.ip_input[0]=tk.Entry(self,show="192.168.1.107")
        # self.port_input[0]=tk.Entry(self,show="3450")
        self.Exit.pack()
        self.Exit.place(x=50,y=50,width=100)
        self.name_label.pack()
        self.name_label.place(x=10,y=100,width=40)
        self.name_input.pack()
        self.name_input.place(x=50,y=100,width=100)
        for i in range(10):
            # print("fkpps")
            self.ip_input[i].pack()
            self.ip_input[i].place(x=50,y=50*(i+3),width=200)
            self.ip_label[i].pack()
            self.ip_label[i].place(x=30,y=50*(i+3),width=20)
            self.button[i].pack()
            self.button[i].place(x=280,y=50*(i+3),width=60)
    
    def _delete_home(self):
        self.name_label.place_forget()
        self.name_input.place_forget()
        for i in range(10):
            # print("fkpps")
            self.ip_input[i].place_forget()
            self.ip_label[i].place_forget()
            self.button[i].place_forget()

    def Init_Rooms(self,ip):
        try:
            Save()
            self._delete_home()
        except:
            pass
        # print("fuckpps!!")
        self.home_button=tk.Button(self,text="Back to home",command=lambda:self.Init_Home())
        try:
            self.s=socket.socket()
            self.s.connect((ip,3450))
            msg=self.s.recv(256)
            self.s.close()
            msg=msg.decode('utf-8')
            rooms=msg.split('#')
            self.room_num=len(rooms)
            # print("fuckpps!!!"+msg)
            for i in range(len(rooms)):
                rooms[i]=rooms[i].split(";")
                self.room_name[i]=rooms[i][0]
                self.ports[i]=atoi(rooms[i][1])
            self.room_label=[tk.Label(self,text=self.room_name[i],bg="white",font=("Purisa",20,"bold")) for i in range(self.room_num)]
            self.button[0]=tk.Button(self,text="Enter",command=lambda: self.Enter(0))
            self.button[1]=tk.Button(self,text="Enter",command=lambda: self.Enter(1))
            self.button[2]=tk.Button(self,text="Enter",command=lambda: self.Enter(2))
            self.button[3]=tk.Button(self,text="Enter",command=lambda: self.Enter(3))
            self.button[4]=tk.Button(self,text="Enter",command=lambda: self.Enter(4))
            self.button[5]=tk.Button(self,text="Enter",command=lambda: self.Enter(5))
            self.button[6]=tk.Button(self,text="Enter",command=lambda: self.Enter(6))
            self.button[7]=tk.Button(self,text="Enter",command=lambda: self.Enter(7))
            self.button[8]=tk.Button(self,text="Enter",command=lambda: self.Enter(8))
            self.button[9]=tk.Button(self,text="Enter",command=lambda: self.Enter(9))
        except:
            self.room_num=0
            pass
        self._build_rooms()

    def _build_rooms(self):
        # print("fkpps!!")
        self.home_button.pack()
        self.home_button.place(x=50,y=50,width=100)
        for i in range(self.room_num):
            self.button[i].pack()
            self.button[i].place(x=300,y=50*(i+2),width=60)
            self.room_label[i].pack()
            self.room_label[i].place(x=50,y=50*(i+2),width=200)
        # print("fkpps!!!")

    def _delete_rooms(self):
        self.home_button.place_forget()
        for i in range(self.room_num):
            self.button[i].place_forget()
            self.room_label[i].place_forget()

    def Enter(self,index=0):
        port=self.ports[index]
        self.withdraw()
        try:
            global music
            music=1
            Run(self.IP,port,self.name,EDGE,picpath)
            music=0
        except:
            pass
        self.deiconify()

    def Connect(self,index=0):
        name=self.name_input.get()
        try:
            self.IP=self.ip_input[index].get()
            # print("fkpps!{0}".format(index))
            self.name=name
            self.Init_Rooms(self.IP)
            # print("fuckpps")
        except:
            pass

    def Play_Music(self,tmp):
        if tmp==0:
            msc=MP3Player("mp3/home.mp3")
        else:
            msc=MP3Player("mp3/game.mp3")
        len=msc.length
        while tmp==music:
            pos=msc.get_pos()
            if(pos==-1 or pos>=len):
                msc.set_pos(0)
            time.sleep(0.15)
        msc.stop_mp3()
        _thread.start_new_thread(self.Play_Music,(music,))

if __name__=="__main__":
    env=Maze()
    env.mainloop()
