N=int(3)
M=int(3)
A=[]
B=[]
C=[]
b=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
c=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

for K in range(0,N):
    for K2 in range(0,M):
        A.append(b[K][K2]+c[K][K2])
    print(A,"A입니다.")
    B.insert(K,A)
    print(B,"B입니다.")
