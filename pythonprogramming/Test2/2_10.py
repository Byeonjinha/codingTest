import random


def game():
    words = ['가위', '바위', '보']
    while True:
        you_word = input('가위', '바위', '보')
        try:
            if you_word not in words:
                raise ValueError
        except ValueError:
            print('잘못 입력 하셨습니다.')
            continue
        else:
            continue

    com_word = random.choice(words)
    print('컴퓨터 결과 :', com_word)

    if com_word == '가위' and you_word == '가위':
        print('무승부')
    elif com_word == '가위' and you_word == '바위':
        print('당신의 승리!')
    elif com_word == '가위' and you_word == '보':
        print('컴퓨터의 승리!')
    elif com_word == '바위' and you_word == '가위':
        print('컴퓨터의 승리!')
    elif com_word == '바위' and you_word == '바위':
        print('무승부')
    elif com_word == '바위' and you_word == '보':
        print('당신의 승리!')
    elif com_word == '보' and you_word == '가위':
        print('당신의 승리!')
    elif com_word == '보' and you_word == '바위':
        print('컴퓨터의 승리!')
    elif com_word == '보' and you_word == '보':
        print('무승부')


while True:

    print('0:종료, 1:한번더하기')
    again = int(input('입력:'))

    if again == 0:
        break
print('게임종료...')