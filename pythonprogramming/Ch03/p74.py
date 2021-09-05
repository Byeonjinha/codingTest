"""
날짜 : 2021/08/10
이름 : 변진하
내용 : 파이썬 프로그래밍 74p
"""

#구구단 출력 :RANGE() GKATN DLDYD
#(1) 바깥쪽 반복문

for i in range(2,10):
    print('~~~ {}단 ~~~'.format(i))

    # (2) 안쪽 반복문
    for j in range(1,10):
        print('%d*%d=%d'%(i,j,i*j))