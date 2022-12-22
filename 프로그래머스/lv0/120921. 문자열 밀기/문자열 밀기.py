def transArray(A,idx):
    B = [[] for _ in range(len(A))]
    for i in range(len(A)):
        B[i] = A[(i-idx) % len(A)]
    return ''.join(B)
def solution(A, B):
    answer = 0
    for idx in range(len(A)):
        if transArray(A,idx) == B:
            return idx
    return -1