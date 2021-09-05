import math
A,B,C=map(int, input().split())
Y=int(1)
if C-B<=0:
    print(-1)
else :

    if math.ceil(A/(C-B)) !=0 :
        print(math.ceil(int(A/(C-B)))+1)
    else:
        print(math.ceil(int(A/(C-B)))+1)

