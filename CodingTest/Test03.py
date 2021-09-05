N = int(input())
ppp = input().split()
A = [1, 1]
L = [0, -1]
R = [0, 1]
U = [-1, 0]
D = [1, 0]
for Vacation in ppp:
    print(Vacation)

    if Vacation == "L":
        A[0]=A[0]+L[0]
        A[1]=A[1]+L[1]
        if A[0]==0:
            A[0]=1
        elif A[1]==0:
            A[1]=1
        elif A[0]==N+1:
            A[0]=N
        elif A[1]==N+1:
            A[1]=N

    elif Vacation == "R":
        A[0]=A[0]+R[0]
        A[1]=A[1]+R[1]
        if A[0]==0:
            A[0]=1
        elif A[1]==0:
            A[1]=1
        elif A[0]==N+1:
            A[0]=N
        elif A[1]==N+1:
            A[1]=N
    elif Vacation == "U":
        A[0]=A[0]+U[0]
        A[1]=A[1]+U[1]
        if A[0]==0:
            A[0]=1
        elif A[1]==0:
            A[1]=1
        elif A[0]==N+1:
            A[0]=N
        elif A[1]==N+1:
            A[1]=N
    elif Vacation == "D":
        A[0]=A[0]+D[0]
        A[1]=A[1]+D[1]
        if A[0]==0:
            A[0]=1
        elif A[1]==0:
            A[1]=1
        elif A[0]==(N+1) :
            A[0]=N
        elif A[1]==N+1:
            A[1]=N
    print(A)



