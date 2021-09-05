"""
날짜 : 2021/08/10
이름 : 변진하
내용 : 파이썬 3장 연습문제 77p
"""
import math
import random
#1-A
x = input("짐의 무게는 얼마입니까?")
x = int(x)
if x <10:
    print("수수료는 없습니다.")
else:
    print("수수료는 10000원 입니다.")
# 1-B
x = input("짐의 무게는 얼마입니까?")
x = int(x)
if x <10:
    print("수수료는 없습니다.")
else:
    y=x/10
    print("수수료는 %d원 입니다." % (int(y)*10000))

#2
print('>>숫자 맞추기 게임<<')
com = random.randint(1,10) #1~10사이 난수 발생
while True :
    my = int(input('예상 숫자를 입력하시오: ')) #숫자 입력
    if my==com:
        print('~~ 성공 ~~')
        break
    elif my>com:
        print('더 작은 수 입력')
    elif my<com:
        print('더 큰 수 입력')

#3
print("수열 = ", end=" ")
sum=0
for i in range (1,100):
    if i%3==0:
        if i%2!=0:
            sum+=i
            print(i , end=" ")

print("\n누적합 = ", sum)

#4
multiline= ""'안녕하세요. 파이썬 세계로 오신걸 환영합니다. 파이썬은 비단뱀 처럼 매력적인 언어입니다.'""
words = []
for word in multiline.split():
    words.append(word)
    print(word)
print('단어 개수 : ', len(words))