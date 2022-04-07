import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random


form_class = uic.loadUiType("main07.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        

    def myclick(self):
        
        a = self.le1.text()
        b = self.le2.text()
        
        aa = int(a)
        bb = int(b)
        txt = ""
        
        for i in range(aa, bb+1):
            txt += self.drawStar(i)
        # aa번째부터 bb번째 줄을 합치는 for문

        self.te.setText(txt)


    def drawStar(self, cnt):
        # 입력된 개수(cnt)만큼 별을 찍어 줄바꿈을 포함한 문장으로 만드는 함수
        rt = ""
        for i in range(cnt):
            rt += "*"
            
        rt += "\n"
        return rt
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
        