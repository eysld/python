import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("pyqt06.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    def myclick(self):
        a = int(self.le1.text())
        b = int(self.le2.text())
        c = int(self.le3.text())
        sum = 0
        for i in range(a, b+1):
            if(i % c == 0):
                sum += i
        self.le4.setText(str(sum))    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
