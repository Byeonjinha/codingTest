import sys

N= int(sys.stdin.readline())
Timelist=[]


def linklist(Timelist):
    Timelist2 = []
    n=int(1)
    for x in range(1,len(Timelist)):
        if max(Timelist) ==Timelist(n):
            break
        if Timelist[i2][1]>Timelist[i2+n][0]:
            n+=1
            continue
        elif Timelist[i2][1]<=Timelist[i2+n][0]:
            Timelist2.append(Timelist[i2+n])
            linklist(Timelist[i2+n])
        return

for i in range(N):
    Time = list(map(int, sys.stdin.readline().split()))
    Timelist.append(Time)
Timelist.sort()

for i2 in range(0,len(Timelist)-1):
    linklist(Timelist[i2])


