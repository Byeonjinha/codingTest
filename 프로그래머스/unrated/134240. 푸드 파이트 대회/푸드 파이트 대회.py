def solution(food):
    answer = '0'
    for i in range(len(food)-1,0,-1):
        count =  food[i] // 2
        answer = str(i) * count + answer + str(i) * count
    print(answer)
    return answer