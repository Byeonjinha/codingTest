A,B  = input().split()
C=[]
D=[]
A2=""
B2=""
C2=[]
D2=[]
for X in A:
    C.append(X)
for X in B:
    D.append(X)
for X in range(len(A)-1,-1,-1):
    C2.append(C[X])
for X in range(len(B)-1,-1,-1):
    D2.append(D[X])

if int(A2.join(C2))>int(B2.join((D2))):
    print(A2.join(C2))
else:
    print(B2.join(D2))