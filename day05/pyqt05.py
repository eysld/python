import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("pyqt05.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    def myclick(self):
        arr = list(range(1,45+1))
        for i in range(999):
            rnd = int(random()*45)
            a = arr[0]
            arr[0] = arr[rnd]
            arr[rnd] = a
        # print(arr[0])
        self.lcd1.display(arr[0])
        self.lcd2.display(arr[1])
        self.lcd3.display(arr[2])
        self.lcd4.display(arr[3])
        self.lcd5.display(arr[4])
        self.lcd6.display(arr[5])
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
