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


    def sql_excute(self, sql):  # sql을 입력 받아 실행해주는 함수(insert, update, delete)
        conn = pymysql.connect(host="localhost", user="root", password="12345", db="member_addr")

        cur = conn.cursor()
        resultNum = cur.execute(sql)       

        cur.close()
        conn.commit()  # insert->commit 필수
        conn.close()
        
        return resultNum  # 함수 호출시 반환값이 1이면 성공

    def sql_select_execute(self, sql):  # select 문 전용 sql 실행 함수
        conn = pymysql.connect(host="localhost", user="root", password="12345", db="member_addr")

        cur = conn.cursor()
        cur.execute(sql)
        records = cur.fetchall()  # SQL문에서 실행된 select문의 결과(record)를 반환->튜플로 반환

        cur.close()
        conn.close()

        return records  # SQL문에서 실행된 select문의 결과(record)를 함수 호출시에 반환

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
