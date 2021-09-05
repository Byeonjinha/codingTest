from collections import deque
def solution(left, right):
    sum=0
    for i in range(left,right+1):
        if yacksoo(i)%2==0:
            sum+=i
        else:
            sum-=i
    return sum
def yacksoo(n):
    yacksoo=deque()
    for i in range(1, n+1):
        if n % i == 0:
            yacksoo.append(i)
    return len(yacksoo)
'''
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
'''
left= 13
right= 17
solution(left, right)
