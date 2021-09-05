import copy
import sys

T = int(sys.stdin.readline())

def solution(T):
    for x in range(0,T):
        k = int(sys.stdin.readline())
        n = int(sys.stdin.readline())
        guzoominsoo(k, n)

def guzoominsoo(k,n):
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for A1 in range(0,k):
        for B1 in range(0,n):
            list2[B1]= sum(list1[0:B1+1])
        list1=copy.deepcopy(list2)
    print(list2[n-1])
    return (list2)

solution(T)
