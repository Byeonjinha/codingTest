"""
날짜 : 2021/08/09
이름 : 변진하
내용 : 파이썬 프로그래밍 46p
"""

#(4) format()함수 인수: format(value, "format")
print("원주율=",  format(3.14159,"8.3f"))
print("금액=", format(10000, "10d"))
print("금액=", format(125000, "3,d"))

#(5) 양식문자 인수 : print("%양식문자" %(값))
name = "홍길동"
age = 35
price = 125.456
print("이름 : %s, 나이:%d, data=%.2f" %(name,age, price))