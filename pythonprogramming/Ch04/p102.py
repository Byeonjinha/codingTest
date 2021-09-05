"""
날짜 : 2021/08/11
이름 : 변진하
내용 : 파이썬 프로그래밍 102p
"""

#(1) 얕은 복사 : 주소 복사(내용, 주소 동일)
import copy

name = ['홍길동', '이순신', '강감찬']
print ('name asdress = ', id(name))

name2 = name #주소 복사
print ('name asdress = ', id(name2))

print(name)
print(name2)

#원본 수정
name2[0] = "김길동" #우너본/사본 수정
print(name)
print(name2)
# (2) 깊은 복사: 내용 복사 (내용 도잉르, 주소 다름)
import copy
name3 = copy.deepcopy(name)
print(name)
print(name3)
print ('name asdress = ', id(name))
print ('name asdress = ', id(name3))

#우너본 수정
name[1] = "이순신장군"
print(name)
print(name3)
