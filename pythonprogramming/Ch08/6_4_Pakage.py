"""
날짜 : 2021/08/12
이름 : 변진하
내용 : 파이썬 패키지 모듈 실습하기 교재 p175
"""
import Ch06.sub2.clac as c
from Ch06.sub2.clac import *

print('프로그램 시작1')




if __name__ == '__main__':
    print('프로그램 시작2')
    r1 = plus(1,2)
    r2 = minus(2,3)
    r3 = c.multi(3,4)
    r4 = c.div(4,2)

    print('r1:',r1)
    print('r2:',r2)
    print('r3:',r3)
    print('r4:',r4)