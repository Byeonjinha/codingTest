"""
날짜 : 2021/08/09
이름 : 변진하
내용 : 파이썬 2장 연습문제 56p
"""

#1
su = 5
dan = 800
print('su 주소 : ' , id(su))
print('dan 주소 : ', id(dan))
print('금액 :' , su*dan)

#2
x=2
y=2.5*x**2+3.3*x+6
print('2차 방정식 결과 =' ,y )

#3
a = input('지방의 그램을 입력하세요 : ')
b = input('지방의 그램을 입력하세요 : ')
c = input('지방의 그램을 입력하세요 : ')
a = int(a)
b = int(b)
c = int(c)
print('총칼로리 : ',a*9+b*4+c*4,'cal')

#4
word1 = input('첫번째 단어 : ')
word2 = input('두번째 단어 : ')
word3 = input('세번째 단어 : ')
print('='*20)
print('약자 : ' ,word1[0:1]+word2[0:1]+word3[0:1])

