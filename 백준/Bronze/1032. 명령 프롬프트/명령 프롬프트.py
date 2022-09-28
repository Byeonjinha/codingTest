import sys

N = int(sys.stdin.readline())
S = list(sys.stdin.readline())
for i in range(N-1):
    S2 = list(sys.stdin.readline())
    for i in range(len(S2)):
        if S[i] != S2[i] :
            S[i] = "?"
print(''.join(S))