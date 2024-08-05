import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("pyqt04.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    def myclick(self):
       a = int(self.le.text())
       b = ""
       for i in range(1,9+1):
           # b += str(a)+"x"+str(i)+"="+str(a*i)+"\n"
           b += "{}x{}={}\n".format(a,i,a*i)
       self.te.setText(b)    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
