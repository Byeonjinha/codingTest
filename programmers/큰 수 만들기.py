def solution(number, k):
    answer = []  # Stack
    for num in number:       # number 을 돌림
        if not answer:    # answer 에 값이 없으면 값을 넣음
            answer.append(num)
            continue
        if k > 0:
            # 잘라낼 숫자(k) 가 0보다 크면
            while answer[-1] < num:   #answer 의 마지막 값이 num보다 작으면
                answer.pop()          # answer 에서 pop
                k -= 1                # 잘라낼 길이 -1
                if not answer or k <= 0:  #answer 이 비거나 잘라낼 숫자가 0보다 같거나 작아지면 멈춤
                    break
        answer.append(num) #answer 에 num 을 append
    print(k)
    if k > 0 :
        answer = answer[:-k]
    print(answer)
    return ''.join(answer)

number = "4177252841"
k = 9
solution(number,k)