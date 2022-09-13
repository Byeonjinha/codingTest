
K=input()
K=int(K)
n1=int(0)
n2=int(0)
n3=int(0)
if K%9==0:
    n1=K/9
    n2=n1-4
    n3=n1-3
    n1=int(n1)
    n2=int(n2)
    n3=int(n3)
    print("9"*n1)
    print("1","9"*(n2),"8999",sep="")
    print("1","9"*(n3),"899",sep="")
elif (K-1)%9==0:
    n1 = K / 9
    n2 = n1 - 4
    n3 = n1 - 3
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    print("1","9" * n1,sep="")
    print("2", "9" * (n2), "8999", sep="")
    print("2", "9" * (n3), "899", sep="")
else:
    print("-1")