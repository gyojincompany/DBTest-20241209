import pymysql

conn = pymysql.connect(host="localhost", user="root", password="12345", db="jbedu")
# 파이썬과 mysql간의 connection 생성

# 아이디:blackDog, 비번:12345, 이름:김블랙, 이메일:black@abc.com, 나이:28
sql = "INSERT INTO membertbl(memberid, memberpw, membername, memberemail, memberage) VALUES ('blackDog','12345','김블랙','black@abc.com','28')"  # DB에 실행할 SQL문 생성

cur = conn.cursor()  # 커서 생성
resultNum = cur.execute(sql)  # SQL문 실행->성공하면 1이 반환

if resultNum == 1:
    print("회원 가입이 성공하였습니다!")
else:
    print("회원 가입이 실패하였습니다!")


cur.close()
conn.commit()  # commit 함수 호출->insert, delete, update 필수!
conn.close()