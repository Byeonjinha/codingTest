import sys
S = sys.stdin.readline().split()
chess = [1,1,2,2,2,8]
for i in range(len(S)):
    S[i] = str(chess[i] - int(S[i]))
print(' '.join(S))