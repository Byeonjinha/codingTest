"""
날짜 : 2021/08/11
이름 : 변진하
내용 : 파이썬 프로그래밍 95p
"""
#(1) 튜플 자료형 변환
lst = list(range(1,6))
t3 = tuple(lst)

print(t3)

#(2) 튜플 관련 함수
print(len(t3), type(t3))
print(t3.count(3))
print(t3.index(4))