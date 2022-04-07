import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random


form_class = uic.loadUiType("main08.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le_mine.returnPressed.connect(self.myclick)
        # le_mine 입력란에 커서가 있을 때 엔터키 입력을 myclick함수에 연결
        

    def myclick(self):
        mine = self.le_mine.text()
        com = ""
        rslt = ""
        rnd = random.random()
        
        if rnd < 1/3 :
            com = "가위"
        elif rnd < 2/3 :
            com = "바위"
        else :
            com = "보"
        
        if com==mine:
            rslt = "비김"
        elif (com=="가위" and mine=="바위")or(com=="바위" and mine=="보")or(com=="보" and mine=="가위") :
            rslt = "승리!"
        elif (com=="가위" and mine=="보")or(com=="바위" and mine=="가위")or(com=="보" and mine=="바위") :
            rslt = "패배"
        else :
            rslt = "잘못된 입력입니다."
            
        self.le_com.setText(com)
        self.le_result.setText(rslt)
             

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
        