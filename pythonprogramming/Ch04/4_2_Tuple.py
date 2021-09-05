"""
날짜 : 2021/08/10
이름 : 변진하
내용 : 파이썬 자료구조 Tuple 실습하기 교재 p 92
"""

#Tuple(고정 리스트)
tuple1 = (1,2,3,4,5)
print('tuple1 type:', type(tuple1))

print('tuple1[0] :', type[0])
print('tuple1[0] :', type[2])
print('tuple1[0] :', type[3])

tuple2 = ('서울', '대전', '대구', '부산', '광주')
print('tuple2 type :',type(tuple2))
print('tuple2[0] :',tuple2[0])
print('tuple2[2] :',tuple2[2])
print('tuple2[3] :',tuple2[3])

#튜플 수정, 삭제
tuple3 = 1,2,3,4,5
tuple3[0] = 7
print('tuple3 :', tuple3)