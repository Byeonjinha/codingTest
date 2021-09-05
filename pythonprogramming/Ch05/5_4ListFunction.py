"""
날짜 : 2021/08/11
이름 : 변진하
내용 : 파이썬 리스트 함수 실습하기 교재 p88
"""
import math

dataset = [1, 4, 3]
print('1-dataset :', dataset)

# 데이터 추가
dataset.append(2)
dataset.append(5)
print('2-dataset :', dataset)

# 데이터 정렬
dataset.sort()
print('3-dataset :', dataset) # 오름차순

dataset.sort(reverse=True)
print('4-dataset :', dataset) # 내림차순

# 데이터 뒤집기
dataset.reverse()
print('5-dataset :', dataset)

# 데이터 삽입
dataset.insert(2, 6)
print('6-dataset :', dataset)

# 데이터 삭제
dataset.remove(6)
print('7-dataset :', dataset)

# map함수 : 리스트의 데이터를 지정된 함수에 일괄 처리해주는 함수
def plus10(n):
    return n+10


list1 = [1, 2, 3, 4, 5]
r1 = map(plus10, list1)
print('r1 :', list(r1))

list2 = [0.1, 1.2, 2.6, 3.4, 4.9]
r2 = map(math.ceil, list2)
print('r2 :', list(r2))

list3 = ['1', '2', '3', '4', '5']
r3 = map(int, list3)
print('r3 :', list(r3))