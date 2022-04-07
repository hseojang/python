import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QIcon


form_class = uic.loadUiType("omok01.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.cnt = 0
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.pb_2.clicked.connect(self.myclick)
    
    def myclick(self):
        self.cnt += 1
        mymod = self.cnt%3
        
        if mymod == 0:
            self.sender().setIcon(QIcon("0.png"))
        if mymod == 1:
            self.sender().setIcon(QIcon("1.png"))
        if mymod == 2:
            self.sender().setIcon(QIcon("2.png"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
        