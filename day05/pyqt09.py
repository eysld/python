import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("pyqt09.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    def myclick(self):
        rnd = random()
        com = ""
        result = ""
        if(rnd > 0.666) :
            com = "가위"
        elif(rnd > 0.333):
            com = "바위"
        else :
            com = "보"
        self.le_com.setText(com)
        mine = self.le_mine.text()
        if(com == mine):
            result = "비김"
        elif( (mine=="가위" and com =="보") or (mine=="바위" and com =="가위") or (mine=="보" and com =="주먹")):
            result = "이김"
        else :
            result = "짐"   
        self.le_result.setText(result) 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
