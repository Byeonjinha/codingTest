def solution(storey):
    answer = 0
    down = ['0', '1', '2', '3', '4']
    five = ['5']
    up = ['9', '8', '7', '6']
    arrayStorey = list(str(storey))
    for i in range(len(arrayStorey) - 1, -1, -1):
        if i == 0:
            if arrayStorey[i] in down:
                answer += int(arrayStorey[i])
            elif arrayStorey[i] in up:
                answer += (up.index(arrayStorey[i]) + 2)
            else:
                answer += 5
        else:
            if arrayStorey[i] in down:
                answer += int(arrayStorey[i])
            elif arrayStorey[i] in up:
                answer += (up.index(arrayStorey[i]) + 1)
                arrayStorey = list(str(int(''.join(arrayStorey)) + 10 ** (len(arrayStorey) - i)))
            elif arrayStorey[i] in five:
                n = 1
                isUp = False
                if arrayStorey[i - n] in up:
                    isUp = True
                elif arrayStorey[i - n] in down or arrayStorey[i - n] in five:
                    isUp = False
                print(i - n)
                while arrayStorey[i - n] == '5':
                    if arrayStorey[i - n] in up:
                        isUp = True
                    elif arrayStorey[i - n] in down or arrayStorey[i - n] in five:
                        isUp = False
                    n += 1
                    if i - n < 1:
                        arrayStorey = arrayStorey = list(str(int(''.join(arrayStorey)) + 10 ** (len(arrayStorey) - i)))
                        break
                answer += 5
                if isUp:
                    arrayStorey = arrayStorey = list(str(int(''.join(arrayStorey)) + 10 ** (len(arrayStorey) - i)))

    return answer