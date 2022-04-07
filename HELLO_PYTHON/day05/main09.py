import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random


form_class = uic.loadUiType("main09.ui")[0]

class MyWindow(QMainWindow, form_class):
    tel = ""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pbCall.clicked.connect(self.myclick)
        
        self.pb1.clicked.connect(self.clickbtn)
        self.pb2.clicked.connect(self.clickbtn)
        self.pb3.clicked.connect(self.clickbtn)
        self.pb4.clicked.connect(self.clickbtn)
        self.pb5.clicked.connect(self.clickbtn)
        self.pb6.clicked.connect(self.clickbtn)
        self.pb7.clicked.connect(self.clickbtn)
        self.pb8.clicked.connect(self.clickbtn)
        self.pb9.clicked.connect(self.clickbtn)
        self.pb0.clicked.connect(self.clickbtn)
        

    def myclick(self):
        msg = self.tel + " 번으로 전화할까요?"
        q = QMessageBox.question(self,'Call?', msg)
        
        if q==QMessageBox.Yes:
            pass
        else:
            self.tel = ""
            self.le.setText(self.tel)
    
    def clickbtn(self):
        self.tel += self.sender().text()
        self.le.setText(self.tel)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
        