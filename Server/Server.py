#!/urs/bin/python3
import time
import socket

from Karno_Class import *
import _thread

def Run(env):
    Init_Board()
    Init_Chess()
    while True:
        State.Show_Chess(env)
        time.sleep(0.25)

def atoi(s):
    s=s[::-1]
    num=0
    for i,v in enumerate(s):
        for j in range(0,10):
            if v==str(j):
                num+=j*(10**i)
    return num

name=["NULL","NULL","NULL"]
MSG=["","",""]

def Send_Info(Socket,turn):
    global MSG
    if MSG[turn]!="":
        try:
            Socket.send(MSG[turn].encode('utf-8'))
            # print(MSG[turn])
            MSG[turn]=""
            return True
        except:
            MSG[turn]=""
            return False
    info_turn=State.turn
    if State.special_rule_king!=-1:
        info_turn=State.special_rule_king
    if State.board_info[turn]!="":
        msg=State.board_info[turn]
        msg2=name[0]+';'+name[1]+';'+name[2]+'#'
        msg=(str(info_turn)+"#"+msg2+msg)
        if game_started:
            msg+="#T"
        else:
            msg+="#F"
        msg='%'+msg
        msg=msg.encode('utf-8')
        try:
            Socket.send(msg)
        except:
            return False
    return True

def Send(Socket,turn):
    turn_info="@{0}".format(turn)
    Socket.send(turn_info.encode('utf-8'))
    # print("i like cx")
    while True:
        if Send_Info(Socket,turn)==False:
            break
        time.sleep(0.15)

def Recv(Socket,turn):
    global game_started
    global State
    while True:
        try:
            msg=Socket.recv(32)
        except:
            break
        try:
            if msg==b"":
                break
            msg=msg.decode('utf-8')
            if msg[0]=='@':
                # print("fuck pps")
                name[turn]=msg[1:]
                continue
            if msg[0]=='$' and turn==0:
                flag=True
                for i in range(3):
                    if Addr[i]==0:
                        flag=False
                if flag:
                    State.Format()
                    Init_Board()
                    Init_Chess()
                    game_started=True
            # print("asdfghjkl;")
            if State.special_rule_king==-1:
                if turn!=State.turn:
                    continue
            else:
                if turn!=State.special_rule_king:
                    continue
            # print(msg)
            sxy=msg.split(',')
            sx,sy=atoi(sxy[0]),atoi(sxy[1])
            nx,ny=State.Rotate(sx,sy,turn,-1)
            if game_started:
                State.React(nx,ny)
        except:
            pass
    if game_started:
        # print("fkpps!!!!!!!!!!!!!")
        State.fail[turn]=True
    Addr[turn]=0

Addr=[0,0,0]
player_conn=[0,0,0]

def Wait_for_Matching(conn,addr):
    Unmatched=True
    while Unmatched:
        if Send_Info(conn,0)==False:
            break
        time.sleep(0.15)
        if game_started:
            continue
        for turn in range(3):
            if Addr[turn]!=0:
                continue
            Addr[turn]=addr
            print(addr)
            print("turn={0}".format(turn))
            player_conn[turn]=conn
            _thread.start_new_thread(Recv,(conn,turn))
            _thread.start_new_thread(Send,(conn,turn))
            Unmatched=False
            break

def Server(port=3450):
    s=socket.socket()
    host=socket.gethostname()
    s.bind((host, port))
    s.listen(10)
    print("listening port:{0}".format(port))
    while True:
        conn,addr=s.accept()
        _thread.start_new_thread(Wait_for_Matching,(conn,addr,))

def Cycle():
    global game_started
    global MSG
    tag=[False,False,False]
    while True:
        try:
            if game_started==False:
                for i in range(3):
                    if Addr[i]==0:
                        name[i]="NULL"
                tag=[False,False,False]
            else:
                failed=0
                for i in range(3):
                    if State.fail[i]:
                        failed+=1
                        if tag[i]==False and player_conn[i]!=0:
                            try:
                                MSG[i]="$YOU FAIL!"
                                # player_conn[i].send("$YOU FAIL!".encode('utf-8'))
                            except:
                                pass
                            tag[i]=True
                # print("failed={0}".format(failed))
                if(failed>=2):
                    game_started=False
                    for i in range(3):
                        if State.fail[i]:
                            continue
                        if tag[i]==False and player_conn[i]!=0:
                            try:
                                MSG[i]="$YOU WIN!"
                                # print("Send WIN msg")
                            except:
                                pass
                            tag[i]=True
        except:
            pass
        time.sleep(0.15)

import sys

if __name__=="__main__":
    global State
    State=Karno()
    global game_started
    game_started=False
    env=0
    port=3450
    try:
        port=atoi(sys.argv[1])
    except:
        port=3450
    # print(sys.argv)
    _thread.start_new_thread(Server,(port,))
    _thread.start_new_thread(Cycle,())
    Run(env)