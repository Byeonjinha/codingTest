import sys
N = int(sys.stdin.readline())
sangCard = {}
for i in sys.stdin.readline().split():
    sangCard[i] = 0
M = int(sys.stdin.readline())
answer = []
numCard = sys.stdin.readline().split()
for i2 in range(len(numCard)):
    if numCard[i2] in sangCard:
        answer.append(str(1))
    else:
        answer.append(str(0))
print(" ".join(answer))