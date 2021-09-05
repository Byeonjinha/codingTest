"""
날짜 : 2021/08/11
이름 : 변진하
내용 : 파이썬 프로그래밍 99p
"""

#(1) dict 생성 방법1
dic= dict(key1 = 100, key2 = 200, key3 = 300)
print (dic)

#(2) dict 생성 방법2
person = {'name':'홍길동','age':35,'address':'서울시'}
print(person)
print(person['name'])
print(type(dic),type(person))

#(3)원소 수정, 삭제, 추가
#dict 원소 수정
person['age'] =45
print(person)

#dict 원소 삭제
del person['address']
print(person) # {'name': '홍길동', 'age':4 {'name':'홍길동','age':45}

#dict 원소 추가
person['pay'] =350
print(person) #{'name':'홍길동', 'pay':35 {'name':'홍길동','age':45,'pay':350}



