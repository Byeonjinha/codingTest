def solution(n):
    answer =[]
    for i in range(1,n+1):
        sum=0
        for j in range(i,n+1):
            sum+=j
            if sum == n:
                answer.append(1)
                break
            elif sum > n :
                break

    return len(answer)


n=15
solution(n)