import math
N= input()
xyz2 =[]
M = float(0)
N = float(N)
D = float()
mi=[]
while N>M:
    xyz = list(map(int, input().split()))
    xyz2.append(xyz)
    M+=1
c= len(xyz2)
c=int(c)

# print(xyz2)

M = int(0)
N = int(1)
while c!=(M+N):
    if M + N > c:
        break
    while c!=(M+N):
        x1=xyz2[M]
        x2=xyz2[M+N]
        D=math.sqrt(((x1[0]-x2[0])**2+(x1[1]-x2[1])**2+(x1[2]-x2[2])**2))
        D2=((x1[0]-x2[0])**2+(x1[1]-x2[1])**2+(x1[2]-x2[2])**2)
        mi.append(D2)
        N=N+1
    N = M + 1
    M+=1
print(min(mi))
print(mi.count(min(mi)))