N = int(input())
N2 = (N+1)*60*60
COUNT3 = []
TIME=[]
H=int(0)
M=int(0)
S=int(0)
n=int(0)
for A in range(0,N2):
    S+=1
    if S==60:
        S=0
        M+=1
        if M==60:
            M=0
            H+=1
    TIME.append(str(H)+str(M)+str(S))


for B in TIME:
    if B.find('3')>-1:
        n+=1
print(n)


