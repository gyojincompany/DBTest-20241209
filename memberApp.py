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

        # 회원 가입 탭
        self.join_btn.clicked.connect(self.member_join)  # 회원가입 버튼이 클릭되면 member_join 함수 호출
        self.idcheck_btn.clicked.connect(self.id_check)  # 아이디 체크 버튼이 클릭되면 id_check 함수 호출
        self.join_reset_btn.clicked.connect(self.join_reset)  # 회원가입 탭 초기화 버튼이 클릭되면 join_reset 함수 호출

        # 로그인 탭
        self.login_btn.clicked.connect(self.login_check)  # 로그인 탭 로그인 버튼 클릭되면 login_check 함수 호출
        self.login_reset_btn.clicked.connect(self.login_reset)  # 로그인 탭 로그인 정보 삭제 login_reset 함수 호출


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
    
    def id_check(self):  # 아이디의 존재여부 확인 함수
        memberid = self.joinid_input.text()  # user가 입력한 회원아이디 텍스트 가져오기

        if memberid == "":
            QMessageBox.warning(self, "정보 입력 오류!", "아이디는 필수 입력사항 입니다.")
        else:
            sql = f"SELECT count(*) FROM membertbl WHERE memberid='{memberid}'"  # 조건에 맞는 레코드의 개수를 반환
            result = self.sql_select_execute(sql)
            # print(result) -> ((0,),) or ((1,),)
            if result[0][0] == 1:
                QMessageBox.warning(self, "회원 가입 불가!", "이미 가입된 아이디 입니다.\n다른 아이디를 입력하세요.")
            else:
                QMessageBox.information(self, "회원 가입 가능!", "회원 가입 가능한 아이디 입니다.")

        return result[0][0]  # 1 or 0

    def member_join(self):  # 새로운 회원 가입 insert 함수
        memberid = self.joinid_input.text()  # user가 입력한 회원아이디 텍스트 가져오기
        memberpw = self.joinpw_input.text()  # user가 입력한 회원비밀번호 텍스트 가져오기
        membername = self.joinname_input.text()  # user가 입력한 회원이름 텍스트 가져오기
        memberemail = self.joinemail_input.text()  # user가 입력한 회원이메일 텍스트 가져오기
        memberaddress = self.joinaddress_input.text()  # user가 입력한 회원주소 텍스트 가져오기
        memberphone = self.joinphone_input.text()  # user가 입력한 회원전화번호 텍스트 가져오기

        # sql문이 만들어지기 전 유효성 체크(validation)
        if memberid == "" or memberpw == "" or membername == "" or memberemail == "" or memberaddress == "" or memberphone == "":
            QMessageBox.warning(self, "정보 입력 오류!","가입시 모든 회원 정보란을 입력하여야 합니다.")
        # 아이디를 4자 이상 10자 이하만 허용
        elif len(memberid) < 4 or len(memberid) > 10:
            QMessageBox.warning(self, "아이디 입력 오류!", "아이디는 4자 이상 10자 이하이어야 합니다.")
        elif len(memberpw) < 4 or len(memberpw) > 10:
            QMessageBox.warning(self, "비밀번호 입력 오류!", "비밀번호는 4자 이상 10자 이하이어야 합니다.")
        elif len(memberphone) < 10 or len(memberpw) > 11:
            QMessageBox.warning(self, "전화번호 입력 오류!", "전화번호는 -를 제외한 숫자만 넣어주세요.")
        else:
            sql = f"INSERT INTO membertbl VALUES ('{memberid}','{memberpw}','{membername}','{memberemail}','{memberaddress}','{memberphone}')"
            checkFlag = self.id_check()  # 경고창 발생->가입가능 0, 가입불가 1 반환
            if checkFlag == 0:
                resultNum = self.sql_excute(sql)  # sql을 실행하는 함수->성공하면 1을 반환

                if resultNum == 1:
                    QMessageBox.information(self, "회원 가입 성공!", "회원 가입을 축하드립니다.")
                    self.join_reset()  # 입력 내용 초기화
                else:
                    QMessageBox.warning(self, "회원 가입 실패!", "회원 가입이 실패하였습니다.\n다시 확인해 주세요.")

    def join_reset(self):  # 회원 가입 탭 입력 정보 삭제(초기화)
        self.joinid_input.clear()  # user가 입력한 회원아이디 텍스트 지우기
        self.joinpw_input.clear()  # user가 입력한 회원비밀번호 텍스트 지우기
        self.joinname_input.clear()  # user가 입력한 회원이름 텍스트 지우기
        self.joinemail_input.clear()  # user가 입력한 회원이메일 텍스트 지우기
        self.joinaddress_input.clear()  # user가 입력한 회원주소 텍스트 지우기
        self.joinphone_input.clear()  # user가 입력한 회원전화번호 텍스트 지우기

    def login_check(self):  # 로그인 확인 함수
        loginid = self.loginid_input.text()  # user가 입력한 로그인 아이디 텍스트 가져오기
        loginpw = self.loginpw_input.text()  # user가 입력한 로그인 비밀번호 텍스트 가져오기

        if loginid == "" or loginpw == "":
            QMessageBox.warning(self, "로그인 오류!","아이디와 비밀번호는 필수 입력사항 입니다.")
        else:
            sql = f"SELECT count(*) FROM membertbl WHERE memberid='{loginid}' AND memberpw='{loginpw}'"
            # 로그인 여부 SQL -> 1이 반환되면 로그인 성공, 0이 반환되면 로그인 실패
            result = self.sql_select_execute(sql)
            if result[0][0] == 1:
                QMessageBox.information(self, "로그인 성공!", "로그인 성공하였습니다.")
                self.login_reset()  # 로그인 성공 후 입력 내용 제거
                self.login_label.setText(f"{loginid}님 로그인 중")
            else:
                QMessageBox.warning(self, "로그인 실패!", "로그인 실패하였습니다.\n아이디 또는 비밀번호가 잘못 되었습니다.")

        return result[0][0]  # 1 or 0

    def login_reset(self):  # 로그인 탭 입력창 초기화
        self.loginid_input.clear()
        self.loginpw_input.clear()


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
