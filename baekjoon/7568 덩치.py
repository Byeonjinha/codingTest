import sys
N = int(sys.stdin.readline())
dungchi=[]
for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    dungchi.append([x,y])
count=1
dungsu=[]
for i in range(len(dungchi)):
    for j in range(len(dungchi)):
        if dungchi[i][0]<dungchi[j][0] and dungchi[i][1]<dungchi[j][1]:
            count+=1
    dungsu.append(count)
    count=1
for i in range(len(dungsu)-1):
    print(dungsu[i],end = " ")
print(dungsu[-1])
