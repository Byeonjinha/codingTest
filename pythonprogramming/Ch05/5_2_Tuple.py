"""
날짜 : 2021/08/10
이름 : 변진하
내용 : 파이썬 함수고급 실습하기 p129
"""
#디폴트 매개변수
def hello(name='홍길동',age=21):
    print('이름:',name)
    print('나이:',age)

hello()
hello('김유신')
hello('김춘추',25)

#가변 매개변수
def total(*scores):
    tot = 0

    for score in scores:
        tot += score

    return tot

r1 = total(1, 2, 3)
r2 = total(1, 2, 3, 4, 5)
r3 = total(1, 2, 3, 4, 5, 6, 7)


print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)

#하나 이상의 리턴값
def plus_multi(num1, num2):
    y1=num1+num2
    y2=num1*num2
    return y1,y2
rs1,rs2 = plus_multi(2,3)
print('rs1:',rs1)
print('rs2:',rs2)

#변수에 저장하는 함수
def plus(x,y):
    return x+y
def minus(x,y):
    return x-y
var1=plus
var2=minus

res1 = var1(1,2)
res2 = var2(2,3)

print('res1 :',res1)
print('res2 :',res2)

#함수 리스트
funs = [plus, minus]
res3 = funs[0](3,4)
res4 = funs[1](4,5)
print('res3 :',res3)
print('res4 :',res4)