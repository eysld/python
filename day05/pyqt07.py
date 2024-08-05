import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from prompt_toolkit.mouse_events import MouseEvent
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("pyqt07.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb0.clicked.connect(self.myclick)
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        
        self.pb_call.clicked.connect(self.mycall)
    def myclick(self, ):
        new = self.sender().text()
        old = self.le.text()
        self.le.setText(old + new)
    def mycall(self):
        num = self.le.text()
        QMessageBox.about(self,'calling', str(num))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
