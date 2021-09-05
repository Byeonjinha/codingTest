T = int(input())
for X in range(0,T):
    R, S = input().split()
    R = int(R)
    P=[]
    K=str()
    for A in S:
        P.append(A*int(R))
    print(K.join(P))