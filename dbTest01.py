# pip install pymysql

import pymysql  # MySql과 python을 연동시켜주는 라이브러리


# 파이썬과 mysql 서버간의 커넥션 생성
# 1) url : localhost, 192.168.0.100
# 2) 계정 : root
# 3) 비밀번호 : 12345
# 4) 스키마(DB) 이름 : ex) jbedu

conn = pymysql.connect(host="localhost", user="root", password="12345", db="jbedu")
# 파이썬과 mysql간의 connection 생성

sql = "SELECT * FROM membertbl"  # DB에 실행할 SQL문 생성

cur = conn.cursor()  # 커서 생성
cur.execute(sql)  # SQL문 실행

records = cur.fetchall()  # SQL문에서 실행된 select문의 결과(record)를 반환->튜플로 반환

print(records)  # 모든 레코드
print(records[0])  # 첫번째 레코드
print(records[1][0])  # 두번째 레코드의 아이디 출력

for member in records:
    print(member)  # 레코드 단위로 출력
    print(member[0])  # 아이디만 출력

# 커넥션의 사용이 종료된 후에는 반드시 닫아줄 것(순서:cur->conn)
cur.close()
conn.close()