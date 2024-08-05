import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from day02.myrandom import rnd
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("pyqt10.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupUi(self)
        self.number = int(random()*99)+1
        self.pb.clicked.connect(self.myclick)
    def myclick(self):
        a = int(self.le.text())
        result = ""
        if a > self.number :
            result += str(a)+"\tDOWN"+"\n"
        elif a < self.number :
            result += str(a)+"\tUP"+"\n"
        else :
            result += str(a)+"\tANSWER"
            QMessageBox.about(self,'정답','정답입니다!')
        old = self.pte.toPlainText()
        self.pte.setPlainText(old+result) 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
