import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random


form_class = uic.loadUiType("main04.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        

    def myclick(self):
        mine = self.leMine.text()
        com = ""
        rslt = ""
        rnd = random.random()
        
        if rnd > 0.5:
            com = "홀"
        else:
            com = "짝"
        
        if com==mine:
            rslt = "승리"
        else:
            rslt = "패배"
            
        self.leCom.setText(com)
        self.leResult.setText(rslt)
             

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
        