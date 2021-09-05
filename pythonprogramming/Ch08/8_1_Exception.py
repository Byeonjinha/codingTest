"""
날짜 : 2021/08/12
이름 : 변진하
내용 : 파이썬 예외처리 실습 교재 p212
"""

# try ~ except
# try ~ except ~ finally
# try ~ except ~ else


num1, num2 = 1,0
r1= num1+num2
r2= num1-num2
r3= num1*num2
r4=0
try:
    # 예외가 발생할 가능성이 있는 로직
    r4= num1/num2
except:
    # 예외가 발생했을 때 실행되는 로직
    print('예외발생..."')

print('r1:',r1)
print('r2:',r2)
print('r3:',r3)
print('r4:',r4)
    #try ~ except ~ finally
people = ['김유신','김춘추','장보고']
try:
    #예외가 발생할 가능성이 있는 로직
    for i in range(4):
        print(people[i])
except:
    # 예외가 발생했을 때 실행되는 로직
    print('예외발생...')
finally:
    #예외 발생 상관없이 마지막에 실행되는 로직
    print('예외처리 완료...')


#try ~ except ~else


animal = ['사자','코끼리','호랑이','기린']
result = None


while True:
    try:
        #예외가 발생할 가능성이 있는 로직
        print('동물을 선택하세요.')
        print('1:사자, 2:코끼리, 3:호랑이, 4:기린, 0:종료')
        answer = int(input('선택:'))
        if answer ==0 :
            break

        result = animal[answer-1]
    except Exception as e:
        # 예외가 발생했을 때 실행되는 로직
        print('예외 내용:', e)
    else:
        #예외 발생 안했을 때 실행되는 영역
        print('선택한 동물 :', result)






print('프로그램 종료..."')