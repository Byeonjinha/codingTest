"""
날짜 : 2021/08/09
이름 : 변진하
내용 : 파이썬 프로그래밍 96p
"""

#(1) 중복 불가
s= {1,3,5,3,1}
print(len(s))
print(s)

#(2) 요소 반복
for d in s:
    print(d,end=' ') # 135
print()

#(3) 집합관련 함수
s2 = {3,6}
print(s.union(s2)) #합집합
print(s.difference(s2)) #차집합
print(s.intersection(s2)) #교집합

# (4) 추가, 삭제 함수
s3 = {1,3,5}
print(s3)

s3.add(7) #원소 추가
print(s3) #

s3.discard(3) # 원소 삭제
print(s3)