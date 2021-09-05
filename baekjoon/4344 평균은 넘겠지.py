C = int(input())
S = []
T = []
perc = float(3)
SUM=int(0)
for A in range(0,C):
    c=list(map(int,input().split()))
    for B in range(1,c[0]+1):
        SUM= c[B]+SUM
        AVG=SUM/(len(c)-1)
    for B in range(1, c[0] + 1):
        if c[B]>AVG:
            T.append(c[B])
    perc = len(T)/(len(c)-1)*100

    T.clear()
    S.append(perc)
    SUM=0
for A in range(0,C):
    print("{:.3f}%".format(S[A]))
