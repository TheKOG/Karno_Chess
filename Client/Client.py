#!/urs/bin/python3
import socket

def fuckpps():
    try:
        s.close()
    except:
        pass
    env.destroy()
    # exit()

import tkinter as tk
import tkinter.messagebox

EDGE=100
picpath='pic'
import ctypes

class Maze(tk.Toplevel, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.title('Karno Chess')
        #self.geometry('{0}x{1}'.format(10 * 30, 10 * 30))
        self._build_maze()
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", lambda: fuckpps())

    def _build_maze(self):
        moni=ctypes.windll.user32
        wt=moni.GetSystemMetrics(0)
        ht=moni.GetSystemMetrics(1)
        self.geometry("{0}x{1}+{2}+{3}".format(EDGE*10,int(EDGE*8.66),int((wt-EDGE*10)/2),int((ht-EDGE*8.66)/2)))
        self.canvas = tk.Canvas(self,bg='white',
                        height=EDGE*8.66,
                        width=EDGE*10)
        self.iconphoto(False,tk.PhotoImage(file='pic/karno_cyberstyle.png'))
        self.canvas.bind("<Button -1>",self.callback)
        global bk
        bk = tk.PhotoImage(file = picpath+"/board.png")
        global image
        # print("fuck pps")
        image = self.canvas.create_image(EDGE*10/2, EDGE*8.66/2, image=bk)
        self.canvas.pack()
    
    def callback(self,event):
        #self.turn=-self.turn
        sx=event.x
        sy=event.y
        global turn
        if turn==-1:
            return
        try:
            Send(sx,sy)
        except:
            pass
        # self.canvas.create_oval(sx-2,sy-2,sx+2,sy+2,fill="blue")

def atoi(s):
    s = s[::-1]
    num = 0
    for i, v in enumerate(s):
        for j in range(0, 10):
            if v == str(j):
                num += j * (10 ** i)
    return num

def Send(sx,sy):
    # print("ilovecx")
    sx=sx*100/EDGE
    sy=sy*100/EDGE
    msg="{0},{1}".format(int(sx),int(sy))
    s.send(msg.encode('utf-8'))

class Block:
    def __init__(self,id=0,sx=0,sy=0,color=0):
        self.id=id,
        self.sx=sx,
        self.sy=sy,
        self.color=color,
        self.pic=0
    def Show(self):
        try:
            env.canvas.delete(self.pic)
        except:
            pass
        if self.color=="fkpps":
            return
        self.pic=env.canvas.create_oval(self.sx*EDGE/100-EDGE*0.3,self.sy*EDGE/100-EDGE*0.3,self.sx*EDGE/100+EDGE*0.3,self.sy*EDGE/100+EDGE*0.3,fill=self.color)

block=[Block(0,0,0,0) for i in range(119)]

img=[[0 for j in range(8)] for i in range(3)]

def Init_Images():
    for i in range(3):
        for j in range(8):
            img[i][j]=tk.PhotoImage(file=picpath+"/{0}/{1}.png".format(i,j))

class Chess:
    def __init__(self,alive=0,group=0,ocp=0,b_id=0):
        self.alive=alive,
        self.group=group,
        self.ocp=ocp,
        self.b_id=b_id,
        self.pic=0

    def Show(self,env):
        if(self.pic!=0):
            env.canvas.delete(self.pic)
        if(self.alive==0):
            return
        # print(self.b_id)
        blk=block[self.b_id]
        sx=blk.sx*EDGE/100
        sy=blk.sy*EDGE/100
        self.pic=env.canvas.create_image(sx,sy,image=img[self.group][self.ocp])

chess=[Chess(0,0,0,0) for i in range(46)]
players=["","",""]
Place=[[700,780],[80,400],[900,400]]
name_pic=[0,0,0]
pps_pic=0
start_button=0

def Client(ip,port,name):
    global s
    s=socket.socket()
    try:
        s.connect((ip, port))
    except:
        return
    while True:
        try:
            msg=s.recv(4096).decode('utf-8')
        except:
            break
        try:
            global turn
            # print(turn)
            if msg[0]=='@':
                # print("qwertyuiop")
                turn=atoi(msg[1])
                global bk
                bk = tk.PhotoImage(file = picpath+"/board{0}.png".format(turn))
                global image
                try:
                    env.canvas.delete(image)
                except:
                    pass
                image = env.canvas.create_image(EDGE*10/2, EDGE*8.66/2, image=bk)
                msg0='@'+name
                print(msg0)
                msg0=msg0.encode('utf-8')
                s.send(msg0)
                continue
            if msg[0]=='$':
                tk.messagebox.showinfo("Info",msg[1:])
                continue
            if msg[0]=='%':
                msg=msg[1:]
                info=msg.split('#')
                info_turn,info_player,info_blk,info_chs,info_start=info[0],info[1].split(';'),info[2].split(';'),info[3].split(';'),info[4]
                players[0],players[1],players[2]=info_player[0],info_player[1],info_player[2]
                fkpps=turn
                if turn==-1:
                    fkpps=0
                for t in range(3):
                    nt=(t-fkpps+3)%3
                    if(name_pic[t]!=0):
                        env.canvas.delete(name_pic[t])
                    cr="black"
                    if t==atoi(info_turn):
                        cr="red"
                    name_pic[t]=env.canvas.create_text(Place[nt][0]*EDGE/100,Place[nt][1]*EDGE/100,text="ID:"+players[t],fill=cr,font=("Purisa",int(15*(EDGE/100)),'bold'))
                global pps_pic
                if pps_pic!=0:
                    env.canvas.delete(pps_pic)
                if turn==-1:
                    pps_pic=env.canvas.create_text(100*EDGE/100,780*EDGE/100,text="正在观战",font=("Purisa",int(30*(EDGE/100)),'bold'),fill="red")
                for i in range(1,119):
                    blk_info=info_blk[i-1].split()
                    # print(blk_info)
                    # print("\n")
                    id,sx,sy,color=atoi(blk_info[0]),atoi(blk_info[1]),atoi(blk_info[2]),blk_info[3]
                    block[id].id=id
                    block[id].sx=sx
                    block[id].sy=sy
                    block[id].color=color
                    block[id].Show()
                for i in range(1,46):
                    chs_info=info_chs[i-1].split()
                    alive,group,ocp,b_id=atoi(chs_info[0]),atoi(chs_info[1]),atoi(chs_info[2]),atoi(chs_info[3])
                    chess[i].alive=alive
                    chess[i].group=group
                    chess[i].ocp=ocp
                    chess[i].b_id=b_id
                    chess[i].Show(env)
                
                if info_start=="F" and turn==0:
                    # print("i love cx")
                    global start_button
                    prepared=True
                    for i in range(3):
                        if players[i]=="NULL":
                            prepared=False
                    if prepared==False:
                        if start_button!=0:
                            try:
                                start_button.place_forget()
                            except:
                                pass
                            start_button=0
                    else:
                        if start_button==0:
                            # print("i like cx!")
                            try:
                                start_button=tk.Button(env,text="START",command=lambda:Start(s))
                                start_button.pack()
                                start_button.place(x=100*EDGE/100,y=700*EDGE/100)
                            except:
                                pass
                            # print("i love cx!!")
            env.update()
        except:
            try:
                env.update()
            except:
                pass

def Start(Socket):
    global start_button
    Socket.send("$START".encode('utf-8'))
    start_button.place_forget()
    start_button=0
    return

def Run(ip,port,name='tourist',edge=100,path='pic'):
    global turn
    global env
    global client_thread
    global EDGE
    global picpath
    EDGE=edge
    picpath=path
    turn=-1
    env=Maze()
    Init_Images()
    # client_thread=threading.Thread(target=Client,args=(ip,port,))
    # client_thread.start()
    Client(ip,port,name)
    fuckpps()
    # env.mainloop()

if __name__=="__main__":
    # file=open("boundary.txt",mode="w")
    Run("192.168.1.107",3450)