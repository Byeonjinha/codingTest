from itertools import combinations
import sys



def solution(n):                    # n 이 주어지면 n 이하의 소수를 출력
    a = [True] * (n + 1)
    m = int(n**0.5)
    for i in range(2, m + 1):
        if a[i] == True:
            for j in range(i + i, n + 1, i):
                a[j] = False
    answer =([i for i in range(2, n + 1) if a[i] == True])
    return answer

def sosu(n):
    li=solution(n)
    idx = max([i for i in range(len(li)) if li[i] <=n/2])
    for i in range(idx,-1,-1):
        for j in range(i,len(li)):
            if li[i]+li[j]==n:
                return [li[i],li[j]]
for _ in range(int(input()))  :
    n=int(input())
    print(" ".join(map(str,sosu(n))))


n=10000
