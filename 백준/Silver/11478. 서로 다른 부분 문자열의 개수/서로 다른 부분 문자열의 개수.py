import sys
input = sys.stdin.readline
t = input()
indexList = [i for i in range(len(t))]
answer = []
for i in range(0,len(t)):
   for j in range(i, len(t)):
       answer.append(t[i:j])
print(len(set(answer))-1)