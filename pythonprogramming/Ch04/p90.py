"""
날짜 : 2021/08/11
이름 : 변진하
내용 : 파이썬 프로그래밍 90p
"""
import p89

result = p89.result
print(result) # [1,2,3,4,1,2,3,4]
result.sort() # 오름차순
print(result) # [1,1,2,3,3,4,4]
result.sort(reverse = True) #내림차순 정렬
print(result) # [4,4,3,3,2,2,1,1]

#(2) 리스ㅡ 요소 검사
import random
r= [] #빈 list
for i in range(5) :
    r.append(random.randint(1,5))

print(r)
if 4 in r :
    print('있음')
else :
    print('없음')