import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QIcon, QSize


form_class = uic.loadUiType("omok03.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_rst.clicked.connect(self.reset)
        self.pb2d = []
        self.arr2d = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
        ]
        
        self.setBoard()
        self.flag_wb=True
        self.flag_ing=True
        
    def myrender(self):
        for i in range(10):
            for j in range (10):
                # btnname = "pb" + "{}.{}".format(j, i)
                if self.arr2d[i][j] == 0:
                    self.pb2d[i][j].setIcon(QIcon("0.png"))
                if self.arr2d[i][j] == 1:
                    self.pb2d[i][j].setIcon(QIcon("1.png"))
                if self.arr2d[i][j] == 2:
                    self.pb2d[i][j].setIcon(QIcon("2.png"))
                
    
    def myclick(self):
        if not self.flag_ing:
            return
        str_ij = self.sender().toolTip()
        i = int(str_ij.split(",")[0])
        j = int(str_ij.split(",")[1])
        if self.arr2d[i][j] > 0:
            QMessageBox.warning(self,"!", "이미 착수한 곳에 놓을 수 없습니다.")
            return
        stone = -1
        if self.flag_wb:
            self.arr2d[i][j] = 1
            stone = 1
        else:
            self.arr2d[i][j] = 2
            stone = 2
        
        
        self.myrender()
        self.gameCnt(i,j, stone)
        self.flag_wb = not self.flag_wb

    def setBoard(self):
        for i in range(10):
            # self.pb2d.append([])
            line = []
            for j in range (10):
                mypb = QPushButton(self)
                mypb.setToolTip("{},{}".format(i, j))
                # mypb.setObjectName("pb" + "{}.{}".format(j, i)) 
                mypb.setGeometry(j*40,i*40,40,40)
                # setGeometry(x, y, w, h) 형식으로 사용한다. 크기와 위치를 동시에 조정할 수 있음
                mypb.setIcon(QIcon("0.png"))
                mypb.setIconSize(QSize(40, 40))
                mypb.clicked.connect(self.myclick)
                # self.pb2d[i].append(0)
                line.append(mypb)
            self.pb2d.append(line)
        self.myrender()
        
    def gameCnt(self, i,j, stone):
        up = self.checkUP(i,j, stone)
        dw = self.checkDW(i,j, stone)
        ri = self.checkRI(i,j, stone)
        le = self.checkLE(i,j, stone)
        ur = self.checkUR(i,j, stone)
        ul = self.checkUL(i,j, stone)
        dr = self.checkDR(i,j, stone)
        dl = self.checkDL(i,j, stone)
        print("UP:{} | DW:{} | RI:{} | LE:{}".format(up,dw,ri,le))
        print("UR:{} | UL:{} | DR:{} | DL:{}".format(ur,ul,dr,dl))
        
        d1 = up+dw+1
        d2 = ri+le+1
        d3 = ul+dr+1
        d4 = dl+ur+1
        
        if d1 >= 5 or d2 >= 5 or d3 >= 5 or d4 >= 5:
            winner = ""
            if self.flag_wb:
                winner = "백돌"
            else : 
                winner = "흑돌"
            QMessageBox.warning(self,"GAMEOVER", "{}의 승리입니다.".format(winner))
            self.flag_ing=False
            return

    def reset(self):
        for i in range(10):
            for j in range(10):
                self.arr2d[i][j]=0
        # self.arr2d = [
        #     [0,0,0,0,0, 0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0],
        #
        #     [0,0,0,0,0, 0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0],
        # ]  이거랑 어떤 차이가 있을까
        
        self.flag_wb=True
        self.flag_ing=True
        self.myrender()

    def checkUP(self, i, j, stone):
        ret = 0
        try:
            while True:
                i -= 1
                if i < 0: return ret
                if j < 0: return ret
                if self.arr2d[i][j] == stone :
                    ret += 1
                else: return ret 
        except:
            return ret
    
    def checkDW(self, i, j, stone):
        ret = 0
        try:
            while True:
                i += 1
                if i < 0: return ret
                if j < 0: return ret
                if self.arr2d[i][j] == stone :
                    ret += 1
                else: return ret 
        except:
            return ret
        
    def checkRI(self, i, j, stone):
        ret = 0
        try:
            while True:
                j += 1
                if i < 0: return ret
                if j < 0: return ret
                if self.arr2d[i][j] == stone :
                    ret += 1
                else: return ret 
        except:
            return ret
        
    def checkLE(self, i, j, stone):
        ret = 0
        try:
            while True:
                j -= 1
                if i < 0: return ret
                if j < 0: return ret
                if self.arr2d[i][j] == stone :
                    ret += 1
                else: return ret 
        except:
            return ret

    def checkUR(self, i, j, stone):
        ret = 0
        try:
            while True:
                i -= 1
                j += 1
                if i < 0: return ret
                if j < 0: return ret
                if self.arr2d[i][j] == stone :
                    ret += 1
                else: return ret 
        except:
            return ret

    def checkUL(self, i, j, stone):
        ret = 0
        try:
            while True:
                i -= 1
                j -= 1
                if i < 0: return ret
                if j < 0: return ret
                if self.arr2d[i][j] == stone :
                    ret += 1
                else: return ret 
        except:
            return ret
        
    def checkDR(self, i, j, stone):
        ret = 0
        try:
            while True:
                i += 1
                j += 1
                if i < 0: return ret
                if j < 0: return ret
                if self.arr2d[i][j] == stone :
                    ret += 1
                else: return ret 
        except:
            return ret

    def checkDL(self, i, j, stone):
        ret = 0
        try:
            while True:
                i += 1
                j -= 1
                if i < 0: return ret
                if j < 0: return ret
                if self.arr2d[i][j] == stone :
                    ret += 1
                else: return ret 
        except:
            return ret


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
        