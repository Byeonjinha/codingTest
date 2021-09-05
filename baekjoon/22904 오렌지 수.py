
n = input()
n = int(n)
if (n%9==0) or ((n-1)%9==0):
    N = int(n)**2
    sum = int(0)
    ssum = int(0)
    n = str(n)
    for a in n:
        a= int(a)
        sum = sum+a
    N = str(N)
    for b in N:
        b=int(b)
        ssum = ssum+b
    if int(sum)==int(ssum) and int(n)%10!=0 :
        print(n,N,sum)
else:
    print("-1")