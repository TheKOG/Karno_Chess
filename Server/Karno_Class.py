#!/urs/bin/python3

from math import sqrt

EDGE=100
UP=0;DOWN=1

block=[0 for i in range(119)]
hd=[0,1,21,40,57,72,85,96,105,112,117]

Saber=0;Archer=1;Assassin=2;Priest=3;Servant=4;Magi=5;Cannon=6;King=7

Mormic=0;Finwarel=1;Hosyer=2

M1=0;M2=1;F1=2;F2=3;H1=4;H2=5;M_F=6;F_H=7;H_M=8;W=9;C=10

Type2=[[[8,1,3],[8,2,3],[8,2,2],[8,3,2],[8,3,1],[9,3,1],[9,2,1],[9,2,2],[9,1,2],[9,1,3],[10,1,2],[10,1,1],[10,2,1]],
[[7,1,5],[7,1,4],[8,1,4],[7,2,4],[6,2,4],[6,2,5],[7,2,3],[7,3,3],[6,3,3],[6,3,4],[5,3,4],[7,3,2],[7,4,2],[6,4,2],[6,4,3],[5,4,3],[8,4,1],[7,4,1],[7,5,1],[6,5,2]],
[[1,1,10],[1,2,10],[2,1,10],[1,2,9],[2,2,9],[2,1,9],[3,1,9],[3,1,8],[3,2,8],[2,2,8],[2,3,8],[1,3,8],[1,3,9]],
[[4,1,8],[4,1,7],[5,1,7],[3,2,7],[4,2,7],[4,2,6],[5,2,6],[2,3,7],[3,3,7],[3,3,6],[4,3,6],[4,3,5],[1,4,8],[1,4,7],[2,4,7],[2,4,6],[3,4,6],[3,4,5],[1,5,7],[2,5,6]],
[[1,10,1],[2,10,1],[2,9,1],[3,9,1],[3,8,1],[1,10,2],[1,9,2],[2,9,2],[2,8,2],[3,8,2],[2,8,3],[1,8,3],[1,9,3]],
[[1,7,5],[1,7,4],[1,8,4],[2,6,5],[2,6,4],[2,7,4],[2,7,3],[3,5,4],[3,6,4],[3,6,3],[3,7,3],[3,7,2],[4,5,3],[4,6,3],[4,6,2],[4,7,2],[4,7,1],[4,8,1],[5,6,2],[5,7,1]],
[[6,1,5],[6,1,6],[5,1,6],[5,2,5]],
[[1,5,6],[1,6,6],[1,6,5],[2,5,5]],
[[5,5,2],[5,6,1],[6,6,1],[6,5,1]],
[[5,3,5],[5,4,4],[5,5,3],[4,5,4],[4,4,5],[3,5,5]],
[[4,4,4]]]

Boundary=[[10,1,1],[10,1,2],[9,1,3],[8,1,4],[7,1,5],[6,1,6],[5,1,7],[4,1,8],[3,1,9],[2,1,10],[1,1,10],[1,2,10],[1,3,9],[1,4,8],[1,5,7],[1,6,6],[1,7,5],[1,8,4],
[1,9,3],[1,10,2],[1,10,1],[2,10,1],[3,9,1],[4,8,1],[5,7,1],[6,6,1],[7,5,1],[8,4,1],[9,3,1],[10,2,1]]

ID=[[[0 for z in range(12)] for y in range(12)] for x in range(12)]

move=[[[0,0,1],[0,1,0],[1,0,0]],[[0,-1,0],[0,0,-1],[-1,0,0]]]
move2=[[[1,-1,1],[1,1,-1],[-1,1,1]],[[-1,-1,1],[-1,1,-1],[1,-1,-1]]]
movescreen=[[[-0.5*EDGE,0],[0.5*EDGE,0],[0,0.866*EDGE]],[[-0.5*EDGE,0],[0.5*EDGE,0],[0,-0.866*EDGE]]]
king_in_danger=[False,False,False]
king_in_crisis=0
desperate=[False,False,False]
king_alone=[False,False,False]

class Block:
    def __init__(
            self,
            X,Y,Z,
            type1,
            id,
            sx,sy
    ):
        self.X=X
        self.Y=Y
        self.Z=Z
        self.type1=type1
        self.id=id
        self.sx=sx
        self.sy=sy
        self.chessid=0
        self.statepic=0
        self.color="fkpps"
        self.boundary=False
        #print("fuckpps {0} {1} {2}".format(X,Y,Z))
        ID[X][Y][Z]=id
        self.type2=0
        for type2 in range(len(Type2)):
            for v in Type2[type2]:
                if X==v[0] and Y==v[1] and Z==v[2]:
                    self.type2=type2
                    break
        for b in Boundary:
            if X==b[0] and Y==b[1] and Z==b[2]:
                self.boundary=True
                break

    
    def Move(self,direction):
        rex=self.X
        rey=self.Y
        rez=self.Z
        resx=self.sx
        resy=self.sy
        rex+=move[self.type1][direction][0]
        rey+=move[self.type1][direction][1]
        rez+=move[self.type1][direction][2]
        resx+=movescreen[self.type1][direction][0]
        resy+=movescreen[self.type1][direction][1]
        return rex,rey,rez,resx,resy
    
    def Illegal(self):
        if(self.X<1 or self.X>10):
            return True
        if(self.Y<1 or self.Y>10):
            return True
        if(self.Z<1 or self.Z>10):
            #print("fkpps{0}".format(self.Z<1|self.Z>10))
            return True
        return False
    def Debug(self):
        print("id={0},x={1},y={2},z={3}\n".format(self.id,self.X,self.Y,self.Z))

def Init_Board():
    print("fkpps")
    tot=0
    hd[1]=1
    for i in range(1,11):
        tot+=1
        if i>1:
            nx,ny,nz,nsx,nsy=block[hd[i-1]].Move(2)
            block[tot]=Block(nx,ny,nz,1,tot,nsx,nsy)
        else:
            block[tot]=Block(1,1,10,0,1,0.5*EDGE,0.433*EDGE)
        while True:
            nx,ny,nz,nsx,nsy=block[tot].Move(1)
            nblock=Block(nx,ny,nz,1-block[tot].type1,tot+1,nsx,nsy)
            if nblock.Illegal():
                ID[nx][ny][nz]=0
                break
            tot+=1
            block[tot]=nblock

Ass=[[[False for z in range(13)] for y in range(13)] for x in range(13)]

class Chess:
    def __init__(
            self,
            group,#阵营 0,1,2
            X,Y,Z,
            ocp,#职业 0,1,2,3,4,5,6,7
            id,
            alive=True
    ):
        self.X=X
        self.Y=Y
        self.Z=Z
        self.group=group
        self.ocp=ocp
        self.id=id
        self.alive=alive
        self.pic=0
        self.choosen=False
        self.saber_special_rule=False
        self.protected=False
        self.giveup=False
        self.center_round=-3
        self.Load_Pos()
    
    def Load_Pos(self):
        block[ID[self.X][self.Y][self.Z]].chessid=self.id
        blk=block[ID[self.X][self.Y][self.Z]]
        if self.ocp==Saber and blk.boundary:
            self.saber_special_rule=True
        self.sx=blk.sx
        self.sy=blk.sy
        self.type1=blk.type1
        self.type2=blk.type2
        #print("id={0} sxy={1},{2}".format(ID[self.X][self.Y][self.Z],self.sx,self.sy))

    def Move1(self,direction):
        X=self.X+move[self.type1][direction][0]
        Y=self.Y+move[self.type1][direction][1]
        Z=self.Z+move[self.type1][direction][2]
        return X,Y,Z
    
    def Move2(self,direction):
        X=self.X+move2[self.type1][direction][0]
        Y=self.Y+move2[self.type1][direction][1]
        Z=self.Z+move2[self.type1][direction][2]
        return X,Y,Z

    def Move3(self,direction):
        dct=[[0,0],[1,1],[0,2],[2,1],[2,0],[1,2]]
        X=self.X
        Y=self.Y
        Z=self.Z
        type1=self.type1
        while True:
            nx=X+move[type1][dct[direction][type1]][0]
            ny=Y+move[type1][dct[direction][type1]][1]
            nz=Z+move[type1][dct[direction][type1]][2]
            if ID[nx][ny][nz]==0:
                break
            blk=block[ID[nx][ny][nz]]
            if blk.Illegal():
                break
            # if direction==1:
            #     print("fuckpps {0} {1} {2} id={3}".format(nx,ny,nz,blk.id))
            if blk.chessid!=0:
                chs=chess[blk.chessid]
                if chs.group==self.group or chs.protected:
                    break
                else:
                    X,Y,Z=nx,ny,nz
                    Ass[X][Y][Z]=True
                    break
            else:
                for d in range(3):
                    x,y,z=nx+move[1-type1][d][0],ny+move[1-type1][d][1],nz+move[1-type1][d][2]
                    blk_=block[ID[x][y][z]]
                    # if x==6 and y==2 and z==5:
                    #     print("ilovecx")
                    if blk_==0:
                        continue
                    chs=chess[blk_.chessid]
                    if chs==0:
                        continue
                    if (chs.group==self.group and chs.id!=self.id) or chs.protected:
                        Ass[nx][ny][nz]=True
            X,Y,Z=nx,ny,nz
            # Ass[nx][ny][nz]=True
            type1=1-type1
    
    def Move4(self,direction,dis):
        X=self.X
        Y=self.Y
        Z=self.Z
        type1=self.type1
        if direction<6:
            dct=[[0,0],[1,1],[0,2],[2,1],[2,0],[1,2]]
            for i in range(dis):
                X+=move[type1][dct[direction][type1]][0]
                Y+=move[type1][dct[direction][type1]][1]
                Z+=move[type1][dct[direction][type1]][2]
                type1=1-type1
        else:
            direction-=6
            dct=[[2,2],[2,2],[0,0],[1,1],[1,1],[0,0]]
            mv=[move,move2]
            for i in range(dis):
                X+=mv[(direction+type1)%2][type1][dct[direction][type1]][0]
                Y+=mv[(direction+type1)%2][type1][dct[direction][type1]][1]
                Z+=mv[(direction+type1)%2][type1][dct[direction][type1]][2]
                type1=1-type1
        return X,Y,Z

    def Dis(self,tx,ty,tz):
        for direction_ in range(12):
            X=self.X
            Y=self.Y
            Z=self.Z
            type1=self.type1
            direction=direction_
            if direction<6:
                dct=[[0,0],[1,1],[0,2],[2,1],[2,0],[1,2]]
                # if(direction==5):
                #     print("start")
                for i in range(1,19):
                    X+=move[type1][dct[direction][type1]][0]
                    Y+=move[type1][dct[direction][type1]][1]
                    Z+=move[type1][dct[direction][type1]][2]
                    # if(direction==5):
                    #     print("fuck pps again {0} {1} {2}".format(X,Y,Z))
                    type1=1-type1
                    if(X==tx and Y==ty and Z==tz):
                        return direction_,i
            else:
                direction-=6
                dct=[[2,2],[2,2],[0,0],[1,1],[1,1],[0,0]]
                mv=[move,move2]
                for i in range(1,19):
                    X+=mv[(direction+type1)%2][type1][dct[direction][type1]][0]
                    Y+=mv[(direction+type1)%2][type1][dct[direction][type1]][1]
                    Z+=mv[(direction+type1)%2][type1][dct[direction][type1]][2]
                    type1=1-type1
                    if(X==tx and Y==ty and Z==tz):
                        return direction_,i
        return -1,-1

    def Replace(self,X,Y,Z):
        if self.X==X and self.Y==Y and self.Z==Z:
            return
        target=block[ID[X][Y][Z]].chessid
        if target!=0:
            if chess[target].group!=self.group:
                if chess[target].ocp!=King or chess[target].giveup:
                    block[ID[self.X][self.Y][self.Z]].chessid=0
                    chess[target].alive=False
                    self.X,self.Y,self.Z=X,Y,Z
                    self.Load_Pos()
                else:
                    for chs in chess:
                        if chs==0:
                            continue
                        if chs.alive==False or chs.group!=chess[target].group or chs.ocp!=Priest:
                            continue
                        t2=[M1,F1,H1]
                        if block[chs.B_id()].type2==t2[chs.group]:
                            king_in_danger[chess[target].group]=True
                            global king_in_crisis
                            king_in_crisis=target
                    if king_in_danger[chess[target].group]==False:
                        block[ID[self.X][self.Y][self.Z]].chessid=0
                        chess[target].alive=False
                        self.X,self.Y,self.Z=X,Y,Z
                        self.Load_Pos()
            else:
                chess[target].X,chess[target].Y,chess[target].Z=self.X,self.Y,self.Z
                chess[target].Load_Pos()
                self.X,self.Y,self.Z=X,Y,Z
                self.Load_Pos()
        else:
            block[ID[self.X][self.Y][self.Z]].chessid=0
            self.X,self.Y,self.Z=X,Y,Z
            self.Load_Pos()

    def B_id(self):
        return ID[self.X][self.Y][self.Z]

    def t2(self):
        #print("fuck pps")
        return block[self.B_id()].type2

    def Protect(self):
        blk=block[self.B_id()]
        x,y,z=self.X,self.Y,self.Z
        if(blk.type1==1):
            x0,y0,z0=self.Move2(0)
            x1,y1,z1=self.Move2(1)
            x2,y2,z2=self.Move2(2)
            if self.group==Mormic:
                blk1=block[ID[x0][y0][z0]]
                blk2=block[ID[x1][y1][z1]]
                if blk1!=0 and blk1.chessid!=0:
                    if chess[blk1.chessid].group==self.group and chess[blk1.chessid].ocp!=Assassin:
                        chess[blk1.chessid].protected=True
                if blk2!=0 and blk2.chessid!=0:
                    if chess[blk2.chessid].group==self.group and chess[blk2.chessid].ocp!=Assassin:
                        chess[blk2.chessid].protected=True
            if self.group==Finwarel:
                blk1=block[ID[x1][y1][z1]]
                blk2=block[ID[x2][y2][z2]]
                if blk1!=0 and blk1.chessid!=0:
                    if chess[blk1.chessid].group==self.group and chess[blk1.chessid].ocp!=Assassin:
                        chess[blk1.chessid].protected=True
                if blk2!=0 and blk2.chessid!=0:
                    if chess[blk2.chessid].group==self.group and chess[blk2.chessid].ocp!=Assassin:
                        chess[blk2.chessid].protected=True
            if self.group==Hosyer:
                blk1=block[ID[x0][y0][z0]]
                blk2=block[ID[x2][y2][z2]]
                if blk1!=0 and blk1.chessid!=0:
                    if chess[blk1.chessid].group==self.group and chess[blk1.chessid].ocp!=Assassin:
                        chess[blk1.chessid].protected=True
                if blk2!=0 and blk2.chessid!=0:
                    if chess[blk2.chessid].group==self.group and chess[blk2.chessid].ocp!=Assassin:
                        chess[blk2.chessid].protected=True
        else:
            if self.group==Mormic:
                x1,y1,z1=x-1,y,z+2
                x2,y2,z2=x-1,y+2,z
                blk1=block[ID[x1][y1][z1]]
                blk2=block[ID[x2][y2][z2]]
                if blk1!=0 and blk1.chessid!=0:
                    if chess[blk1.chessid].group==self.group:
                        chess[blk1.chessid].protected=True
                if blk2!=0 and blk2.chessid!=0:
                    if chess[blk2.chessid].group==self.group:
                        chess[blk2.chessid].protected=True
            if self.group==Finwarel:
                x1,y1,z1=x,y+2,z-1
                x2,y2,z2=x+2,y,z-1
                blk1=block[ID[x1][y1][z1]]
                blk2=block[ID[x2][y2][z2]]
                if blk1!=0 and blk1.chessid!=0:
                    if chess[blk1.chessid].group==self.group:
                        chess[blk1.chessid].protected=True
                if blk2!=0 and blk2.chessid!=0:
                    if chess[blk2.chessid].group==self.group:
                        chess[blk2.chessid].protected=True
            if self.group==Hosyer:
                x1,y1,z1=x,y-1,z+2
                x2,y2,z2=x+2,y-1,z
                blk1=block[ID[x1][y1][z1]]
                blk2=block[ID[x2][y2][z2]]
                if blk1!=0 and blk1.chessid!=0:
                    if chess[blk1.chessid].group==self.group:
                        chess[blk1.chessid].protected=True
                if blk2!=0 and blk2.chessid!=0:
                    if chess[blk2.chessid].group==self.group:
                        chess[blk2.chessid].protected=True

    def Killable(self,target):
        if(self.ocp!=Magi or self.alive==False):
            return False
        if(target.group==self.group or target.protected or target.alive==False):
            return False
        type1=self.type1
        X,Y,Z=self.X,self.Y,self.Z
        tx,ty,tz=target.X,target.Y,target.Z
        mv=[[[-2,1,1],[1,1,-2],[1,-2,1]],[[2,-1,-1],[-1,-1,2],[-1,2,-1]]]
        for dct in range(3):
            x,y,z=X+mv[type1][dct][0],Y+mv[type1][dct][1],Z+mv[type1][dct][2]
            if x==tx and y==ty and z==tz:
                return True
        return False

    def Reachable(self,X,Y,Z):
        flag=False
        if self.ocp==Saber:
            if special_rule[0]:
                if self.X==X and self.Y==Y and self.Z==Z:
                    return True
            for dct in range(3):
                x,y,z=self.Move1(dct)
                #print("fuck {0} {1} {2}".format(x,y,z))
                if self.group==Mormic:
                    type1=block[self.B_id()].type1
                    type2=block[self.B_id()].type2
                    if type1==0 and dct==2 and (type2==M1 or type2==M2 or type2==W or type2==C):
                        #print("fuck pps {0}".format(self.B_id()))
                        continue
                    if (type2==M1 or type2==M2 or type2==M_F or type2==H_M) and type1==1 and (dct==0 or dct==1):
                        #print(type2)
                        continue
                        
                if self.group==Finwarel:
                    type1=block[self.B_id()].type1
                    type2=block[self.B_id()].type2
                    if type1==0 and dct==0 and (type2==F1 or type2==F2 or type2==W or type2==C):
                        continue
                    if (type2==F1 or type2==F2 or type2==M_F or type2==F_H) and type1==1 and (dct==0 or dct==2):
                        continue

                if self.group==Hosyer:
                    type1=block[self.B_id()].type1
                    type2=block[self.B_id()].type2
                    if type1==0 and dct==1 and (type2==H1 or type2==H2 or type2==W or type2==C):
                        continue
                    if (type2==H1 or type2==H2 or type2==F_H or type2==H_M) and type1==1 and (dct==1 or dct==2):
                        continue

                if x==X and y==Y and z==Z:
                    flag=True
                    break
            target_chs=block[ID[X][Y][Z]].chessid
            if flag and target_chs!=0:
                if chess[target_chs].group==self.group or chess[target_chs].protected:
                    flag=False

        if self.ocp==Archer:
            for dct in range(3):
                x,y,z=self.Move2(dct)
                if x==X and y==Y and z==Z:
                    flag=True
                    break
            if flag==False:
                for dct in range(3):
                    x,y,z=self.Move1(dct)
                    if x==X and y==Y and z==Z:
                        T2=block[ID[x][y][z]].type2
                        if (T2==M1 or T2==F1 or T2==H1 or T2==M_F or T2==F_H or T2==H_M):
                            flag=True
                        break
            target_chs=block[ID[X][Y][Z]].chessid
            if flag and target_chs!=0:
                target=chess[target_chs]
                if target.group==self.group or target.protected:
                    flag=False
                elif target.ocp==Cannon:
                    type1=target.type1
                    for dct in range(3):
                        if target.group==Mormic and dct==2:
                            continue
                        if target.group==Finwarel and ((type1==0 and dct==0) or (type1==1 and dct==1)):
                            continue
                        if target.group==Hosyer and ((type1==0 and dct==1) or (type1==1 and dct==0)):
                            continue
                        x,y,z=X+move[type1][dct][0],Y+move[type1][dct][1],Z+move[type1][dct][2]
                        blk=block[ID[x][y][z]]
                        if blk==0:
                            continue
                        chs=chess[blk.chessid]
                        if chs==0:
                            continue
                        if chs.alive==False:
                            continue
                        if chs.group==target.group:
                            flag=False
            if flag==False and target_chs!=0:
                target=chess[target_chs]
                if target.group==self.group or target.protected:
                    flag=False
                else:
                    for i in range(3):
                        cx,cy,cz=self.Move2(i)
                        blk=block[ID[cx][cy][cz]]
                        if blk==0:
                            continue
                        chs=chess[blk.chessid]
                        if chs==0:
                            continue
                        if chs.alive==False:
                            continue
                        if chs.group!=target.group or chs.ocp!=Cannon:
                            continue
                        type1=chs.type1
                        for dct in range(3):
                            if target.group==Mormic and dct==2:
                                continue
                            if target.group==Finwarel and ((type1==0 and dct==0) or (type1==1 and dct==1)):
                                continue
                            if target.group==Hosyer and ((type1==0 and dct==1) or (type1==1 and dct==0)):
                                continue
                            x,y,z=cx+move[type1][dct][0],cy+move[type1][dct][1],cz+move[type1][dct][2]
                            if x==X and y==Y and z==Z:
                                flag=True

        if self.ocp==Assassin:
            global Ass
            Ass=[[[False for z in range(13)] for y in range(13)] for x in range(13)]
            for dct in range(6):
                self.Move3(dct)
            flag=Ass[X][Y][Z]
        
        if self.ocp==Priest:
            for dct in range(3):
                x,y,z=self.Move1(dct)
                if x==X and y==Y and z==Z:
                    flag=True
                    break
            t1=block[self.B_id()].type2
            t2=block[ID[X][Y][Z]].type2
            target_chs=block[ID[X][Y][Z]].chessid
            if flag and target_chs!=0:
                flag=False
            if flag:
                if self.group==Mormic:
                    if t2!=M1 and t2!=M2:
                        flag=False
                    elif t1==M2 and t2==M1:
                        flag=False
                if self.group==Finwarel:
                    if t2!=F1 and t2!=F2:
                        flag=False
                    elif t1==F2 and t2==F1:
                        flag=False
                if self.group==Hosyer:
                    if t2!=H1 and t2!=H2:
                        flag=False
                    elif t1==H2 and t2==H1:
                        flag=False
        
        if self.ocp==Servant:
            for dct in range(3):
                x,y,z=self.Move1(dct)
                if x==X and y==Y and z==Z:
                    flag=True
                    break
            if flag==False:
                for dct in range(3):
                    x,y,z=self.Move2(dct)
                    if x==X and y==Y and z==Z:
                        flag=True
                        break
            target_chs=block[ID[X][Y][Z]].chessid
            if flag and target_chs!=0:
                if chess[target_chs].group==self.group and chess[target_chs].ocp==King:
                    flag=True
                elif chess[target_chs].group==self.group or chess[target_chs].protected:
                    flag=False
            if flag and desperate[self.group]==False:
                t1=block[self.B_id()].type2
                t2=block[ID[X][Y][Z]].type2
                if t1!=t2:
                    flag=False
        
        if self.ocp==Magi:
            for dct in range(3):
                x,y,z=self.Move1(dct)
                if x==X and y==Y and z==Z:
                    flag=True
                    break
            target_chs=block[ID[X][Y][Z]].chessid
            if flag and target_chs!=0:
                flag=False

        if self.ocp==Cannon:
            for dct in range(3):
                x,y,z=self.Move1(dct)
                if x==X and y==Y and z==Z:
                    flag=True
                    break
            target_chs=block[ID[X][Y][Z]].chessid
            if flag and target_chs!=0:
                flag=False
            if target_chs!=0:
                target=chess[target_chs]
                if target.group==self.group or target.protected or target.alive==False:
                    flag=False
                else:
                    tx,ty,tz=target.X,target.Y,target.Z
                    direction,dis=self.Dis(tx,ty,tz)
                    if direction==-1 or dis%2==1:
                        flag=False
                    else:
                        dis_=int(dis/2)
                        cx,cy,cz=self.Move4(direction,dis_)
                        blk=block[ID[cx][cy][cz]]
                        if(blk.chessid==0):
                            flag=False
                        else:
                            flag=True
                        if flag==True and dis_>1:
                            for dis__ in range(1,dis_):
                                cx_,cy_,cz_=self.Move4(direction,dis__)
                                blk_=block[ID[cx_][cy_][cz_]]
                                if blk_.chessid!=0:
                                    flag=False
                                    break

        if self.ocp==King:
            for dct in range(3):
                x,y,z=self.Move1(dct)
                if x==X and y==Y and z==Z:
                    flag=True
                    break
            target_chs=block[ID[X][Y][Z]].chessid
            if flag and target_chs!=0:
                if chess[target_chs].group==self.group and chess[target_chs].ocp==Servant:
                    flag=True
                elif chess[target_chs].group==self.group or chess[target_chs].protected:
                    flag=False
            if flag:
                t1=block[self.B_id()].type2
                t2=block[ID[X][Y][Z]].type2
                if t1!=t2:
                    flag=False

        return flag
    
    def Show(self,env=0):
        if(self.pic!=0):
            env.canvas.delete(self.pic)
        if(self.alive==False):
            return
        sx=self.sx
        sy=self.sy
        bias=12
        #print("fuck pps")
        if(self.type1==1):
            bias=-12

chess=[0 for i in range(46)]

pos=[[6,2,5],[6,3,4],[6,4,3],[6,5,2],[6,2,4],[6,4,2],[7,2,4],[7,4,2],[8,1,3],[8,3,1],[9,1,2],[9,2,1],[7,3,3],[9,2,2],[10,1,1]]
ocp=[0,0,0,0,1,1,2,2,3,3,4,4,5,6,7]

def Init_Chess():
    tot=0
    for gp in range(3):
        for ele in range(15):
            tot+=1
            if gp==Mormic:
                chess[tot]=Chess(gp,pos[ele][0],pos[ele][1],pos[ele][2],ocp[ele],tot)
            if gp==Finwarel:
                chess[tot]=Chess(gp,pos[ele][1],pos[ele][2],pos[ele][0],ocp[ele],tot)
            if gp==Hosyer:
                chess[tot]=Chess(gp,pos[ele][2],pos[ele][0],pos[ele][1],ocp[ele],tot)
    #chess[tot].Show(env)

special_rule=[False for i in range(8)]

class Karno:
    def __init__(self):
        self.choose=0
        self.turn=0
        self.round=1
        self.fail=[False,False,False]
        self.board_info=["","",""]
        self.special_rule_king=-1

    def Format(self):
        self.choose=0
        self.turn=0
        self.round=1
        self.fail=[False,False,False]
        self.board_info=["","",""]
        self.special_rule_king=-1

    def Show_Choosen(self):
        debug=False
        if(self.choose==0 or debug):
            return
        #print("fuck pps id={0}".format(self.choose))
        blk=block[chess[self.choose].B_id()]
        blk.color="blue"

    def Show_Reachable_Block(self):
        for blk in block:
            if blk==0:
                continue
            if self.choose==0:
                continue
            if self.Reachable(self.choose,blk.id):
                blk.color="green"

    def Show_Protection(self):
        for chs in chess:
            if(chs==0):
                continue
            if(chs.alive==False or chs.protected==False):
                continue
            # print("fuck pps")
            blk=block[chs.B_id()]
            blk.color="gold"
        return

    def Show_Killable(self):
        if self.choose==0:
            return
        magi=chess[self.choose]
        if magi.ocp!=Magi:
            return
        for target in chess:
            if target==0:
                continue
            if(self.Killable(self.choose,target.id)==False):
                continue
            blk=block[target.B_id()]
            blk.color="red"

    
    def Clear(self,env):
        for blk in block:
            if blk==0:
                continue
            blk.color="fkpps"
            if env==0:
                continue
            try:
                env.canvas.delete(blk.statepic)
            except:
                pass

    def Check(self):
        flag=[True,True,True]
        for chs in chess:
            if chs==0:
                continue
            if chs.ocp==King and chs.alive==False:
                self.fail[chs.group]=True
            elif chs.alive==True:
                if chs.ocp!=King and chs.ocp!=Servant and chs.ocp!=Priest:
                    flag[chs.group]=False
        
        for gp in range(3):
            desperate[gp]=desperate[gp] or flag[gp]
        
        global king_alone
        king_alone=[True,True,True]
        for chs in chess:
            if chs==0:
                continue
            if chs.alive==False or chs.ocp==King:
                continue
            t2=[M1,F1,H1]
            # print(chs.B_id())
            if chs.t2()==t2[chs.group]:
                king_alone[chs.group]=False

        for chs in chess:
            if chs==0:
                continue
            if chs.alive==False:
                continue
            for gp in range(3):
                if gp==chs.group:
                    continue
                elif king_alone[gp]:
                    self.fail[gp]=True

        for chs in chess:
            if chs==0:
                continue
            if self.fail[chs.group]:
                self.Kill(chs.id)
            elif desperate[chs.group]:
                if chs.ocp==Priest:
                    chs.ocp=Magi
        
        # if self.choose!=0 and special_rule[0]:
        #     if self.round<chess[self.choose].center_round+3:
        #         special_rule[0]=False
        
                
    def Show_King_in_Crisis(self):
        king=chess[king_in_crisis]
        blk=block[king.B_id()]
        blk.color="red"
        
    def Show_Swapable(self):
        king=chess[king_in_crisis]
        t2=[M1,F1,H1]
        gp=king.group
        for chs in chess:
            if chs==0:
                continue
            if chs.alive==False or chs.group!=gp or chs.ocp!=Priest or block[chs.B_id()].type2!=t2[gp]:
                continue
            blk=block[chs.B_id()]
            blk.color="purple"
        return

    def Show_Block_Color(self,env=0):
        for blk in block:
            if blk==0:
                continue
            bias=12
            if(blk.type1==1):
                bias=-12
            sx=blk.sx
            sy=blk.sy
            try:
                env.canvas.delete(blk.statepic)
            except:
                pass
            if blk.color!="fkpps":
                blk.statepic=env.canvas.create_oval(sx-30,sy+bias-30,sx+30,sy+bias+30,fill=blk.color)
            
    def Show_Chess(self,env=0):
        self.Check()
        while self.fail[self.turn]:
            self.turn=(self.turn+1)%3
            self.round+=1
        self.Set_Protection()
        self.Clear(env)
        self.Show_Protection()
        if king_in_crisis==0:
            self.special_rule_king=-1
            self.Show_Killable()
            self.Show_Choosen()
            self.Show_Reachable_Block()
        else:
            self.special_rule_king=chess[king_in_crisis].group
            self.Show_King_in_Crisis()
            self.Show_Swapable()
        if(env!=0):
            self.Show_Block_Color(env)
        for i in range(3):
            self.board_info[i]=self.Board_to_Str(i)
        if env!=0:
            for chs in chess:
                if(chs!=0):
                    chs.Show(env)
            env.update()

    def Find_Chess(self,sx,sy):
        r=EDGE/(2*sqrt(3))
        re=0
        for i in range(1,46):
            chs=chess[i]
            if(chs.alive==False):
                continue
            bias=12
            if(chs.type1==1):
                bias=-12
            nsx=chs.sx
            nsy=chs.sy+bias
            dis=(nsx-sx)*(nsx-sx)+(nsy-sy)*(nsy-sy)
            if dis<r*r:
                re=i
        return re

    def Find_Block(self,sx,sy):
        r=EDGE/(2*sqrt(3))
        re=0
        for i in range(1,119):
            blk=block[i]
            bias=12
            if(blk.type1==1):
                bias=-12
            nsx=blk.sx
            nsy=blk.sy+bias
            dis=(nsx-sx)*(nsx-sx)+(nsy-sy)*(nsy-sy)
            if dis<r*r:
                re=i
        return re

    def Set_Protection(self):
        for chs in chess:
            if chs==0:
                continue
            if chs.alive==False:
                continue
            chs.protected=False
        for chs in chess:
            if chs==0:
                continue
            if chs.alive==False:
                continue
            if chs.ocp==Priest:
                chs.Protect()
            if chs.center_round==-3 and chs.t2()==C:
                chs.center_round=self.round
            elif self.round<chs.center_round+2:
                chs.protected=True

    def Reachable(self,chs_id,blk_id):
        return chess[chs_id].Reachable(block[blk_id].X,block[blk_id].Y,block[blk_id].Z)

    def Replace(self,chs_id,blk_id):
        if special_rule[0]==False:
            if chess[chs_id].ocp==Saber and (block[chess[chs_id].B_id()].type2==W or block[chess[chs_id].B_id()].type2==C):
                special_rule[0]=True
                if block[blk_id].type2==C and chess[chs_id].center_round==-3:
                    special_rule[0]=False
        elif special_rule[0]:
            special_rule[0]=False
        chess[chs_id].Replace(block[blk_id].X,block[blk_id].Y,block[blk_id].Z)

    def Killable(self,magi_id,target_id):
        return chess[magi_id].Killable(chess[target_id])

    def Kill(self,target_id):
        if chess[target_id].alive==False:
            return
        if chess[target_id].ocp!=King or chess[target_id].giveup:
            block[chess[target_id].B_id()].chessid=0
            chess[target_id].alive=False
        else:
            for chs in chess:
                if chs==0:
                    continue
                if chs.alive==False or chs.group!=chess[target_id].group or chs.ocp!=Priest:
                    continue
                t2=[M1,F1,H1]
                if block[chs.B_id()].type2==t2[chs.group]:
                    king_in_danger[chess[target_id].group]=True
                    global king_in_crisis
                    king_in_crisis=target_id
            if king_in_danger[chess[target_id].group]==False:
                block[chess[target_id].B_id()].chessid=0
                chess[target_id].alive=False

    def React(self,sx,sy,file=0):
        chs_id=self.Find_Chess(sx,sy)
        blk_id=self.Find_Block(sx,sy)
        if file!=0:
            if blk_id!=0:
                str="[{0},{1},{2}],".format(block[blk_id].X,block[blk_id].Y,block[blk_id].Z)
                print(str)
                file.write(str)
                file.flush()
        for gp in range(3):
            if king_in_danger[gp]:
                global king_in_crisis
                king=king_in_crisis
                t2=[M1,F1,H1]
                if chs_id!=0:
                    if chess[chs_id].group==gp and chess[chs_id].ocp==Priest and block[chess[chs_id].B_id()].type2==t2[gp] and chess[chs_id].alive:
                        self.Replace(king,chess[chs_id].B_id())
                        if chess[self.choose].ocp==Magi:
                            self.Kill(chs_id)
                        else:
                            self.Replace(self.choose,chess[chs_id].B_id())
                        king_in_crisis=0
                        king_in_danger[gp]=False
                        self.turn=(self.turn+1)%3
                        self.round+=1
                        self.choose=0
                        chess[king].giveup=True
                    elif chs_id==king:
                        chess[king].giveup=True
                        if chess[self.choose].ocp==Magi:
                            self.Kill(chs_id)
                        else:
                            self.Replace(self.choose,chess[chs_id].B_id())
                        king_in_crisis=0
                        king_in_danger[gp]=False
                        self.turn=(self.turn+1)%3
                        self.round+=1
                        self.choose=0
                return
        if self.choose!=0 and blk_id!=0:
            if self.Reachable(self.choose,blk_id):
                self.Replace(self.choose,blk_id)
                if special_rule[0]:
                    return
                if king_in_crisis==0:
                    self.turn=(self.turn+1)%3
                    self.round+=1
                    self.choose=0
                return
            elif chs_id!=0:
                if self.Killable(self.choose,chs_id):
                    self.Kill(chs_id)
                    if king_in_crisis==0:
                        self.turn=(self.turn+1)%3
                        self.round+=1
                        self.choose=0
                    return
        if(chs_id!=0 and special_rule[0]==False):
            if chess[chs_id].group==self.turn:
                chess[chs_id].choosen=True
                self.choose=chs_id
    
    def Rotate(self,sx,sy,turn,direction=1):
        cx,cy=5*EDGE,11*EDGE*sqrt(3)/6
        dx,dy=sx-cx,sy-cy
        for i in range(turn):
            dx_,dy_=-0.5*dx+direction*sqrt(3)*dy/2,-direction*sqrt(3)*dx/2-0.5*dy
            dx,dy=dx_,dy_
        nx,ny=cx+dx,cy+dy
        return nx,ny

    def Board_to_Str(self,turn=0):
        str=""
        for i in range(1,119):
            blk=block[i]
            bias=12
            if(blk.type1==1):
                bias=-12
            sx=blk.sx
            sy=blk.sy+bias
            nx,ny=self.Rotate(sx,sy,turn)
            blk_str="{0} {1} {2} ".format(blk.id,int(nx),int(ny))+blk.color
            str+=blk_str
            if(i!=118):
                str+=';'
        str+='#'
        for i in range(1,46):
            chs=chess[i]
            fk=0
            if chs.alive:
                fk=1
            chs_str="{0} {1} {2} {3}".format(fk,chs.group,chs.ocp,chs.B_id())
            str+=chs_str
            if(i!=45):
                str+=';'
        return str