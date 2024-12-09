import pymysql

while True:
    conn = pymysql.connect(host="localhost", user="root", password="12345", db="jbedu")

    print("************ 회원 관리 프로그램 *************")
    print("1 : 회원 가입")
    print("2 : 회원 정보 수정")
    print("3 : 회원 탈퇴")
    print("4 : 전체 회원 목록 조회")
    print("5 : 아이디로 회원 조회")
    print("0 : 프로그램 종료")
    print("******************************************")
    menuNum = input("메뉴 중 한 가지를 선택하세요(0~5) : ")

    if menuNum == "1":
        print("회원 정보를 입력하세요.")
        memberid = input("1) 가입하실 회원 아이디를 입력하세요 : ")
        memberpw = input("2) 비밀번호를 입력하세요 : ")
        membername = input("3) 가입하실 회원 이름을 입력하세요 : ")
        memberemail = input("4) 가입하실 회원 이메일을 입력하세요 : ")
        memberage = input("5) 회원님의 나이를 입력하세요 : ")

        sql = f"INSERT INTO membertbl VALUES ('{memberid}','{memberpw}','{membername}','{memberemail}','{memberage}')"

        cur = conn.cursor()
        resultNum = cur.execute(sql)
        if resultNum == 1:
            print("축하합니다! 회원 가입 성공하셨습니다.")
        else:
            print("회원 가입 실패입니다! 다시 확인하세요.")

        cur.close()
        conn.commit()  # insert->commit 필수
        conn.close()

    elif menuNum == "2":
        print("수정하실 회원 정보를 입력하세요.")
        memberid = input("1) 정보를 수정하실 회원 아이디를 입력하세요 : ")
        memberpw = input("2) 수정하실 비밀번호를 입력하세요 : ")
        membername = input("3) 수정하실 회원 이름을 입력하세요 : ")
        memberemail = input("4) 수정하실 회원 이메일을 입력하세요 : ")
        memberage = input("5) 수정하실 회원님의 나이를 입력하세요 : ")

        sql = f"UPDATE membertbl SET memberpw='{memberpw}', membername='{membername}', memberemail='{memberemail}', memberage='{memberage}' WHERE memberid='{memberid}'"

        cur = conn.cursor()
        resultNum = cur.execute(sql)
        if resultNum == 1:
            print("축하합니다! 회원 수정 성공하셨습니다.")
        else:
            print("회원 수정 실패입니다! 다시 확인하세요.")

        cur.close()
        conn.commit()  # insert->commit 필수
        conn.close()

    elif menuNum == "3":
        memberid = input("1) 탈퇴하실 회원 아이디를 입력하세요 : ")

        sql = f"DELETE FROM membertbl WHERE memberid='{memberid}'"

        cur = conn.cursor()
        resultNum = cur.execute(sql)
        if resultNum == 1:
            print("회원 탈퇴 성공하셨습니다. 안녕히 가세요.")
        else:
            print("회원 탈퇴 실패입니다! 다시 확인하세요.")

        cur.close()
        conn.commit()  # insert->commit 필수
        conn.close()

    elif menuNum == "4":

        sql = f"SELECT * FROM membertbl"

        cur = conn.cursor()
        cur.execute(sql)
        memberAllList = cur.fetchall()

        print("============ 전체 회원 리스트 =============")
        for member in memberAllList:
            print(member[0], end=" / ")  # 다음 줄 출력 내용을 한 줄로 이어주는 end 옵션 추가
            print(member[1], end=" / ")
            print(member[2], end=" / ")
            print(member[3], end=" / ")
            print(member[4])

        cur.close()
        conn.close()

    elif menuNum == "5":

        memberid = input("1) 조회하실 회원 아이디를 입력하세요 : ")

        sql = f"SELECT * FROM membertbl WHERE memberid='{memberid}'"

        cur = conn.cursor()
        cur.execute(sql)
        memberAllList = cur.fetchall()

        print("============ 회원 조회 정보 =============")
        for member in memberAllList:
            print(member[0], end=" / ")  # 다음 줄 출력 내용을 한 줄로 이어주는 end 옵션 추가
            print(member[1], end=" / ")
            print(member[2], end=" / ")
            print(member[3], end=" / ")
            print(member[4])

        cur.close()
        conn.close()


    elif menuNum == "0":
        print("프로그램을 종료합니다. 안녕히 가세요.")
        conn.close()
        break

    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
        conn.close()