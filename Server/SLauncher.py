#!/urs/bin/python3
import os
import socket
import _thread

def atoi(s):
    s=s[::-1]
    num=0
    for i,v in enumerate(s):
        for j in range(0,10):
            if v==str(j):
                num+=j*(10**i)
    return num

names=[]
ports=[]
num=0

def Server(port=3450):
    s=socket.socket()
    host=socket.gethostname()
    s.bind((host, port))
    s.listen(10)
    print("listening port:{0}".format(port))
    while True:
        conn,addr=s.accept()
        print(addr)
        msg=""
        for i in range(num):
            msg+=names[i]+";"+ports[i]
            if i!=num-1:
                msg+='#'
        try:
            # print(msg)
            conn.send(msg.encode('utf-8'))
            print("Send Successfully")
            conn.close()
        except:
            pass

if __name__=="__main__":
    file=open("Rooms",mode="r",encoding='utf-8')
    for i in range(10):
        try:
            info=file.readline()
            # print(info)
            if info[-1]=='\n':
                info=info[:-1]
            info=info.split(':')
            names.append(info[0])
            ports.append(info[1])
            num+=1
            _thread.start_new_thread(os.system,("python Server.py "+info[1],))
        except:
            break
    # print(names)
    # print(ports)
    Server()