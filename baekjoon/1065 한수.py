N = int(input())
P = []
temp=int(99)
if N <= 99:
    print(N)
else :
    for A in range(100,N+1):
        for B in str(A):
            P.append(B)
        if int(P[1])-int(P[0])==int(P[2])-int(P[1]):
            temp+=1
        P.clear()
    print(temp)
