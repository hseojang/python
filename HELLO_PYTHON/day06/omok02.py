import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QIcon, QSize


form_class = uic.loadUiType("omok02.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setBoard()
        self.cnt=0
        

    
    def myclick(self):
        self.cnt += 1
        mymod = self.cnt%3
        
        if mymod == 0:
            self.sender().setIcon(QIcon("0.png"))
        if mymod == 1:
            self.sender().setIcon(QIcon("1.png"))
        if mymod == 2:
            self.sender().setIcon(QIcon("2.png"))

    def setBoard(self):
        for i in range(0, 10):
            for j in range (0, 10):
                # btn = "pb" + "{}.{}".format(j, i)
                btn = QPushButton(self)
                btn.setObjectName("pb" + "{}.{}".format(j, i)) 
                btn.setGeometry(j*40,i*40,40,40)
                # setGeometry(x, y, w, h) 형식으로 사용한다. 크기와 위치를 동시에 조정할 수 있음
                btn.setIcon(QIcon("0.png"))
                btn.setIconSize(QSize(40, 40))
                btn.clicked.connect(self.myclick)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
        