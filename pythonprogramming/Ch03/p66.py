"""
날짜 : 2021/08/10
이름 : 변진하
내용 : 파이썬 프로그래밍 66p
"""

#무한 루프(LOOP)
numData = [] # 빈 list
while True:
    num = int (input("숫자 입력 : "))
    if num %10 ==0: #exit 조건식
        print("프로그램 종료")
        break
    else:
        print(num)
        numData.append(num) #list 추가