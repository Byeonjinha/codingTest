from sys import stdin

N= input()
xyz2 =[]
xyz3 =[]
N = int(N)
M = int(1)
K=  int(1)
xyzz = list(map(int, stdin.readline().split()))
shortest_distance=int(10000)
for A in range(M,N):
    temp = M
    for B in range(M,N):
        if N>K:
            xyz = list(map(int, stdin.readline().split()))
            K += 1
            xyz2.append(xyz)
        p=xyzz
        q=xyz
        temp_xyz2 = sum((px - qx) ** 2.0 for px, qx in zip(p, q))
        if  shortest_distance>=temp_xyz2:
            shortest_distance=temp_xyz2
            xyz3.append(shortest_distance)

        M+=1
    M = temp
    xyzz=xyz2[M-1]
    M+=1
print(shortest_distance)
print(xyz3.count(shortest_distance))