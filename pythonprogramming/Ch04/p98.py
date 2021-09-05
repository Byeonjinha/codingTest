"""
날짜 : 2021/08/09
이름 : 변진하
내용 : 파이썬 프로그래밍 98p
"""

# 중복 원소를 갖는 리스트
gender = ['남','여','남','여']

# 중복 원소 제거
sgender = set(gender) # list -> set
lgender = list(sgender) #set 0> list
print(lgender)
print(lgender[1])