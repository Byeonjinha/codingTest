"""
날짜 : 2021/08/10
이름 : 변진하
내용 : 파이썬 프로그래밍 61p
"""

var = 10 # if블럭에서 사용될 변수
if var >= 5: #조건식
    print('var=',var)
    print('var는 5보다 크다.')
    print('조건이 참인 경우 실행')
    
print('항상 실행')


#100~85 : '우수', 84~7-: '보통', 69이하 : '저조'
score = int (input('점수 입력:'))
if score >= 85 and score <= 100:
    print('우수')
else :
    if score >= 70:
        print('보통')
    else:
        print('저조') #69이하