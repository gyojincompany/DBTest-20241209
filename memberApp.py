import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/member.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("회원 관리 프로그램 v1.0")


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
