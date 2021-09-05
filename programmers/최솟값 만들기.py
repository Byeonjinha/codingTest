def solution(A,B):
    sum=0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        sum+=A[i]*B[i]

    return sum


A = [1, 4, 2]
B =	[5, 4, 4]
solution(A,B)