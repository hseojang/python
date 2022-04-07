import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


form_class = uic.loadUiType("main05.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        

    def myclick(self):
        dan = self.le.text()
        iDan = int(dan)
        rslt = ""
        
        for i in range(1, 9+1):
            rslt += "{}*{}={}\n".format(dan, i, iDan*i)
        # lineedit는 줄바꿈이 안된다
        
        self.te.setText(rslt)
             

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
        