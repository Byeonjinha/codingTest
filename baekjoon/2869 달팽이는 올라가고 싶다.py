import math
A,B,V = input().split()

A=int(A)
B=int(B)
V=int(V)

if (V-B)/(A-B) == int ((V-B)/(A-B)):
    print( int ((V-B)/(A-B))  )
else :
    print( int(math.ceil((V-A)/(A-B)))+1)